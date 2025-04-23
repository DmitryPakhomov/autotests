import json
import os
import time
from typing import NoReturn, Any

import allure
import pytest
import urllib3
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from urllib3 import exceptions


from autotests.pages.api.api_utils import API
from autotests.pages.api.settings import ENDPOINTS_MAPPING, API_USERS_TOKEN_MAPPING
from autotests.pages.blocks.loans_pages_blocks.loan_ach_page_blocks import LoanAchPageBlocks
from autotests.pages.blocks.loans_pages_blocks.loan_budget_page_blocks import LoanBudgetPageBlocks
from autotests.pages.blocks.loans_pages_blocks.loan_creditors_page_blocks import \
    LoanCreditorsPageBlocks
from autotests.pages.blocks.loans_pages_blocks.loan_history_page_blocks import LoanHistoryPageBlocks
from autotests.pages.blocks.loans_pages_blocks.loan_income_page_blocks import LoanIncomePageBlocks
from autotests.pages.blocks.loans_pages_blocks.loan_profile_page_blocks import LoanProfilePageBlocks
from autotests.pages.blocks.login_pages_blocks import LoginPageBlocks
from autotests.pages.data.api_data import api_users
from autotests.pages.data.main_data import Configs, ApiData, URL, UIData
from autotests.pages.settings import Settings
from autotests.pages.utils import compress_image
from autotests.pages.utils import slack_post_msg

class TestResults:
    def __init__(self):
        self.start_time = time.time()
        self.total = 0
        self.passed = 0
        self.failed = 0
        self.skipped = 0

def pytest_configure(config):
    config.test_results = TestResults()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        item.session.config.test_results.total += 1
        if report.passed:
            item.session.config.test_results.passed += 1
        elif report.failed:
            item.session.config.test_results.failed += 1
        elif report.skipped:
            item.session.config.test_results.skipped += 1


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Отправка результатов в Slack после всех тестов"""
    if not config.getoption("--slack-report"):
        return
    results = config.test_results
    duration = time.time() - results.start_time

    # Получаем данные из terminalreporter для перепроверки
    stats = terminalreporter.stats
    passed = len(stats.get('passed', []))
    failed = len(stats.get('failed', []))
    skipped = len(stats.get('skipped', []))
    total = passed + failed + skipped

    # Формируем сообщение (используем оба источника данных для надежности)
    message = (
        f"• **Total Tests**: {total} (hook counted: {results.total})\n"
        f"• **Passed**: {passed} ✅\n"
        f"• **Failed**: {failed} ❌\n"
        f"• **Skipped**: {skipped} ⏸\n"
        f"• **Duration**: {duration:.2f}s\n"
        f"• **Test Scope**: {config.option.file_or_dir or 'All tests'}"
    )

    if os.getenv('PERFORMANCE_BOT_TOKEN'):
        try:
            slack_post_msg(
                token=os.environ['PERFORMANCE_BOT_TOKEN'],
                channel=os.environ.get('TEST_PATH_TALKS_RESULT_CHANNEL', '#qa_test_api_pathtalks_results'),
                text=message,
                icon_emoji=":robot_face:",
                username="Selenium"
            )
        except Exception as e:
            terminalreporter.write_line(
                f"\n⚠️ Failed to send Slack report: {str(e)}",
                red=True
            )


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    """Дополнительная проверка результатов"""
    if not hasattr(session.config, 'test_results'):
        session.config.warn("NO_RESULTS", "Test results were not collected properly")


def pytest_addoption(parser: Parser) -> None:
    """
    Get parameters of CLI.
    """
    parser.addoption("--env", action="store", default='test', help=(
        "Environment for running tests. Options: test, test2, prod Default: test"))
    parser.addoption('--ver', action='store', default='off', help=(
        'Running GUI tests in verbose mode. Options: on, off, Default: off'))
    parser.addoption('--scope', action='store', default='function', help=(
        'Key for changing the scope of fixtures. '
        'Options: module, function, session, class. Default: function'))
    parser.addoption('--res', action='store', default='', help=(
        'Key for changing browser window resolution. Options: local. Default: local'))
    parser.addoption("--ssh", action="store_true", default=False, help=(
        'Use SSH tunnel to connect to database'))
    parser.addoption("--slack-report", action="store_true", default=False, help=(
        'Send test results to Slack'))


def get_scope(fixture_name: str, config: Config) -> Any:
    """
    Fixture for getting the value of the --scope parameter CLI.
    """
    return config.getoption('--scope')


@pytest.fixture(scope='session')
def environ(request: FixtureRequest) -> str:
    """
    Fixture for getting the value of the --env parameter CLI.
    """
    return request.config.getoption('--env')


@pytest.fixture(scope='module', autouse=True)
def config(environ: str) -> Configs:
    """
    Fixture for getting the data from the config file.

    :param environ: CLI argument, environment variable in which tests are run.

    :return: Returns data from the config file.
    """
    directory = f'{Settings.CONFIGS_PATH}/{environ}_cfg/'

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if 'common' in filepath:
            with open(filepath) as common_data:
                common = json.load(common_data)
        if 'auth' in filepath:
            with open(filepath) as auth_data:
                auth = json.load(auth_data)
        if 'ui_data' in filepath:
            with open(filepath) as ui_data:
                ui_d = json.load(ui_data)
        if 'api' in filepath:
            with open(filepath) as api_data:
                api_d = json.load(api_data)
        if 'path_talks' in filepath:
            with open(filepath) as path_talks_data:
                path_talks_d = json.load(path_talks_data)

    return Configs(
        common=common,
        auth=auth,
        ui_data=ui_d,
        path_talks_data=path_talks_d
    )


@pytest.fixture
def api_data(config: Configs, request) -> ApiData:
    method = request.param[0]
    case = request.param[1]
    data = config.api_data[method][case]
    return ApiData(data=data, method=method, case=case)


@pytest.fixture
def ui_data(config: Configs, request) -> UIData:
    test = request.param[0]
    case = request.param[1]
    data = config.ui_data[test][case]
    return UIData(data=data, test=test, case=case)


@pytest.fixture
def urls(config: Configs) -> URL:
    return URL(
        url=config.common['url'],
        url_api=config.common['url_api'],
        url_api_path_talks=config.common['url_api_path_talks']
    )


@pytest.fixture(scope=get_scope)
def browser(request: FixtureRequest) -> WebDriver:
    """
    Fixture for obtaining Selenium Webdriver.

    docs:
    https://selenium-python.com/
    https://www.seleniumhq.org/
    https://selenium-python.readthedocs.io/api.html
    """
    chrome_options = Options()

    if request.config.getoption('--ver') != 'on':
        chrome_options.add_argument('--headless')  # запуск хрома в фоновом режиме

    if request.config.getoption('--res') == 'local':
        chrome_options.add_argument('--start-maximized') # запуск окна хрома в максимальном размере размере
    else:
        chrome_options.add_argument(
            '--window-size=1980,1080')  # запуск окна хрома в указанном размере
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--incognito')  # запуск хрома в режиме инкогнито
    chrome_options.add_argument(
        '--disable-notifications')  # отключение всплывающих уведомлений в окне хрома
    chrome_options.add_argument('--disable-cache')  # отключение кэша
    chrome_options.add_argument('--disable-extensions')  # отключение расширений
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': Settings.DOWNLOAD_PATH,
        'download.prompt_for_download': False,
        'download.directory_upgrade': True,
        'safebrowsing_for_trusted_sources_enabled': False,
        'safebrowsing.enabled': False
    })

    driver = webdriver.Chrome(options=chrome_options)
    failed_before = request.session.testsfailed

    yield driver
    if request.session.testsfailed != failed_before:
        with allure.step('Screen of error.'):
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                compress_image(screenshot), name='error_screen', attachment_type=AttachmentType.JPG)
    with allure.step('Closing the browser.'):
        driver.quit()


@pytest.fixture
def login_page(browser, config):
    return LoginPageBlocks(browser, config)


@pytest.fixture
def login(login_page):
    login_page.login_with_cookies()


# loans
@pytest.fixture
def loan_profile_page(browser, config):
    return LoanProfilePageBlocks(browser, config)


@pytest.fixture
def loan_income_page(browser, config):
    return LoanIncomePageBlocks(browser, config)


@pytest.fixture
def loan_creditors_page(browser, config):
    return LoanCreditorsPageBlocks(browser, config)


@pytest.fixture
def loan_history_page(browser, config):
    return LoanHistoryPageBlocks(browser, config)


@pytest.fixture
def loan_ach_page(browser, config):
    return LoanAchPageBlocks(browser, config)


@pytest.fixture
def loan_budget_page(browser, config):
    return LoanBudgetPageBlocks(browser, config)


# api
api = API()


@pytest.fixture
def get_token(config: Configs, request) -> str:
    method = 'authentication'
    url = config.common['url_api'] + ENDPOINTS_MAPPING[method]
    username = request.param
    body = {'username': username, 'publicKey': API_USERS_TOKEN_MAPPING[username]}
    res = api.make_request(method_type='POST', url=url, method=method, body=body)
    return res.json()['token']


@pytest.fixture
def get_token_leads(config: Configs) -> str:
    method = 'authentication'
    url = config.common['url_api'] + ENDPOINTS_MAPPING[method]
    username = api_users.leads
    body = {'username': username, 'publicKey': API_USERS_TOKEN_MAPPING[username]}
    res = api.make_request(method_type='POST', url=url, method=method, body=body)
    return res.json()['token']


@pytest.fixture(scope='session', autouse=True)
def disable_request_warnings() -> None:
    """
    Disables warnings from urllib3 for requests to work over the https protocol.

    docs: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
    """
    urllib3.disable_warnings(exceptions.InsecureRequestWarning)


# @pytest.fixture(scope="session", autouse=True)
# def ssh_tunnel():
#     """Глобальный SSH-туннель для всех тестов"""
#     port = start_tunnel()
#     yield port  # Возвращаем локальный порт
#     stop_tunnel()  # Останавливаем туннель после завершения всех тестов


@pytest.fixture(scope="session", autouse=True)
def manage_ssh_tunnel(request):
    """Фикстура для управления SSH-туннелем в зависимости от параметра."""
    use_tunnel = request.config.getoption("--ssh")
    if use_tunnel:
        from ssh_tunnel_manager import start_tunnel, stop_tunnel
        start_tunnel()  # Функция запуска туннеля
        yield
        stop_tunnel()  # Остановка туннеля
    else:
        yield


def get_test_case_docstring(item) -> str:
    """
    Function to get the string from a test case and edit it,
    to display this string instead of the standard test case name in reports.
    """
    full_name = ''

    if item.obj.__doc__:
        # Удаление лишние пробелы:
        name = str(item.obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Генерация списка из параметров кейсов:
        if hasattr(item, 'callspec'):
            params = item.callspec.params
            res_keys = sorted([k for k in params])
            res = [f'{k}: "{params[k]}"' for k in res_keys]
            # Добавление всех параметров к назавнию кейса:
            full_name += ' Parameters: (' + str(', '.join(res)) + ')'

    return full_name


def pytest_itemcollected(item) -> NoReturn:
    """
    Function for changing the names of cases while running tests.
    """
    if item.obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session) -> NoReturn:
    """
    Function for changing case names when using the --collect-only parameter.
    """
    if session.config.option.collectonly is True:
        for item in session.items:
            if item.obj.__doc__:
                get_test_case_docstring(item)
        pytest.exit('Done!')

