import time
import traceback
from typing import Any, NoReturn, Union

from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.settings import Settings


class WebPage:
    """
    Web page abstraction in the Page Object Model concept.

    docs:
    https://selenium-python.readthedocs.io/page-objects.html
    """

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def get_page(self, url: str) -> NoReturn:
        """
        A method for retrieving a web page at a given url.

        :param url: url request.
        """
        self.driver.get(url)
        self.waiting_for_page_loaded()

    def get_page_in_new_tab(self, url: str) -> NoReturn:
        """
        Method of opening a link in a new tab.

        :param url: URL request.
        """
        self.driver.execute_script(
            '''var url = arguments[0]; window.open(url,"_blank");''', url)
        self.waiting_for_page_loaded()

    def refresh_page(self) -> NoReturn:
        """
        Page reload method.
        """
        self.driver.refresh()
        self.waiting_for_page_loaded()

    def go_back(self) -> NoReturn:
        """
        Method to return to the previous page.
        """
        self.driver.back()
        self.waiting_for_page_loaded()

    def get_page_title(self) -> str:
        """
        Method for retrieving text from the title of the current page.

        :return: Title Text.
        """
        return self.driver.title

    def get_current_page_url(self) -> str:
        """
        Method for obtaining the current URL of the page.

        :return: The url string of the current page.
        """
        return self.driver.current_url

    def scroll_down(self, offset: int = 0) -> NoReturn:
        """
        Method for scrolling to the end of the page.

        :param offset: Scroll coordinates.
        """
        if offset:
            self.driver.execute_script(f'window.scrollTo(0, {offset});')
        else:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset: int = 0) -> NoReturn:
        """
        Method for scrolling to the top of the page.

        :param offset: Scroll coordinates.
        """
        if offset:
            self.driver.execute_script(f'window.scrollTo(0, -{offset});')
        else:
            self.driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    def switch_to_iframe(self, iframe: Union[str, int]) -> NoReturn:
        """
        Method for switching to iFrame.

        :param iframe: Locator for iframe.
        """
        self.driver.switch_to.frame(iframe)

    def switch_to_windows(self, window: int, new: bool = False) -> NoReturn:
        """
        Method for switching to tabs.

        :param window: Tab locator.
        :param new: Locator for a new window.
        """
        if new:
            self.driver.execute_script('window.open();')
        self.driver.switch_to.window(self.driver.window_handles[window])

    def switch_out_iframe(self) -> NoReturn:
        """
        Method for switching to a page from iFrame.
        """
        self.driver.switch_to.default_content()

    def get_page_source(self) -> str:
        """
        Method to get the source code of the current page.

        :return: Page source code.
        """
        source = ''
        # noinspection PyBroadException
        try:
            source = self.driver.page_source
        except Exception:
            err = traceback.format_exc()
            self.error_handler(
                action='Getting the source code of the page.',
                error='The page source code has not been received.',
                reason=err
            )

        return source

    def check_page_title(self, title: str, action: str = 'Page title check.') -> NoReturn:
        """
        Method for checking the title of the current page.

        :param title: Correct page title.
        :param action: Action taken.
        """
        current_title = self.get_page_title()
        assert current_title == title, \
            AssertionError(
                self.error_handler(
                    action=action,
                    error='Incorrect title.',
                    as_is=self.get_page_title(),
                    to_be=title
                )
            )
        return current_title

    def check_js_errors(self, return_errors: bool = False) -> NoReturn:
        """
        Method for checking the current page logs for errors.
        """
        ignore_list = Settings.JS_LOG_IGNORE_LIST
        error_logs = []
        logs = self.driver.get_log('browser')

        if logs:
            for log in logs:
                # if log['level'] != 'WARNING' \
                #         and log['message'].split('/')[2] not in ignore_list:
                if log['level'] != 'WARNING':
                    for error in ignore_list:
                        if error not in log['message']:
                            error_logs.append(log)

        if error_logs:
            if return_errors:
                return error_logs
            raise Exception(
                self.error_handler(
                    action='Checking the logs of the current page for errors.',
                    error=error_logs
                )
            )

    def error_handler(
            self,
            page_url: bool = True,
            action: str = None,
            error: Any = None,
            as_is: Any = None,
            to_be: Any = None,
            reason: Any = None
    ) -> dict[str, Any]:
        """
        Method for handling error text.

        :param page_url: Retrieving the current page.
        :param action: Actions performed.
        :param error: Error text.
        :param as_is: As is.
        :param to_be: As it should be.
        :param reason: The reason for the error.
        :return: Dictionary with error text.
        """
        error_data = {
            'Action': action,
            'Error': error
        }

        if page_url:
            error_data['Page'] = self.get_current_page_url()
        if as_is is not None:
            error_data['As is'] = as_is
        if to_be is not None:
            error_data['To be'] = to_be
        if reason is not None:
            error_data['Reason'] = reason

        return error_data

    def waiting_for_page_loaded(
            self,
            timeout: int = 60,
            double_check: bool = False,
            sleep_time: int = 0.5
    ) -> NoReturn:
        """
        Method to check if the current page is loaded.

        :param timeout: The final time to wait for the page to load.
        :param double_check: Checking for successful page loading on the second round.
        :param sleep_time: Initial time to wait for page loading.
        """

        page_loaded = False
        page_load_time = 0

        # Waiting for page load:
        while not page_loaded:
            time.sleep(sleep_time)
            page_load_time += sleep_time

            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            page_loaded = self.driver.execute_script("return document.readyState == 'complete';")

            assert page_load_time < timeout, f'Page loading took more than {timeout} с.'

            # Checking for successful page loading on the second round:
            if page_loaded and double_check:
                page_loaded = False
                double_check = False

        # Scroll to the top of the page:
        self.driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
