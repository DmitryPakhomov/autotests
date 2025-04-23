import os
import sys

import allure
from typing import NoReturn
from selenium.webdriver.chrome.webdriver import WebDriver
from autotests.pages.data.leads_data import leads_pages
from autotests.pages.data.main_data import main_tabs, roles
from autotests.pages.pages.login_pages.login_page import LoginPage
from autotests.pages.pages_details.login_pages_details import Password
from autotests.pages.utils import get_cookies_by_user_id
from autotests.pages.data.main_data import Configs


class LoginPageBlocks(LoginPage):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.cfg = cfg

    def login_with_cookies(
            self, role: str = roles.admin, page: str = leads_pages.leads, client_id: str = ''
    ) -> NoReturn:
        with allure.step('Login with cookies by admin.'):
            self.open_page(page='Login', broker=False)
            user = self.cfg.auth[role]['cookies']
            self.driver.add_cookie(
                {
                    'name': user['name'],
                    'value': user['value'],
                    'domain': user['domain']
                }
            )
            self.open_page(page=page, client_id=client_id, broker=False)

    def login_with_cookies_hmac(self, role: str) -> dict[str, str]:
        user_id = self.cfg.auth[role]['user_id']
        data = get_cookies_by_user_id(user_id=user_id, url=self.cfg.common['url'])
        cookies = {
            'name': data['name'],
            'value': data['value'],
            'domain': self.cfg.common['url'].split('//')[-1]
        }
        self.open_page(page='Login', broker=False)
        self.driver.add_cookie(cookies)
        self.open_page(page='Acknowledge', broker=False)
        self.click_btn_acknowledge()
        self.waiting_for_page_loaded()
        self.highlight_and_make_screenshot()
        return cookies


    def login_by_email(
            self,
            broker: bool = False,
            title: bool = True,
            main_tab: str | None = main_tabs.leads
    ) -> NoReturn:
        with allure.step(f'Login by email: {os.environ["EMAIL"]}.'):
            self.open_page(page='Login', title=title, broker=broker)
            self.click_btn_sign_in_via_google()
            if '--ver=on' in sys.argv:
                self.fill_email(email=os.environ['EMAIL'])
                self.click_btn_further()
                self.fill_email_password(password=os.environ['EMAIL_PASS'])
                self.click_btn_further()
            else:
                self.fill_email_headless(email=os.environ['EMAIL'])
                self.click_btn_further_after_email()
                self.fill_email_password_headless(password=os.environ['EMAIL_PASS'])
                self.click_btn_further_after_pass()
            self.click_btn_acknowledge()
            self.waiting_for_page_loaded()
            if main_tab:
                if self.get_internal_page_title() != main_tab:
                    self.click_main_tabs(tab=main_tab)
            self.highlight_and_make_screenshot()

    def login_field_validation_check(self, credentials: list[str]) -> NoReturn:
        with allure.step('Checking the correctness of the entered data.'):
            error_locator = Password.Locators.ET_LOGIN
            try:
                error = self.wait_until_element_not_visible(error_locator)
            except Exception:
                return

            assert not error, AssertionError(
                self.error_handler(
                    action='Checking validation of authorization form fields.',
                    error=error.text,
                    reason=f'{error.text} - {credentials}'
                )
            )

    def login_field_validation_check_negative(self, case: str) -> NoReturn:
        with allure.step('Checking the correctness of the entered data.'):
            locator_username = Password.Locators.ET_USERNAME
            locator_password = Password.Locators.ET_PASSWORD
            locator_common = Password.Locators.ET_LOGIN
            err_text_username = Password.Errors.ET_USERNAME
            err_text_password = Password.Errors.ET_PASSWORD
            err_text_common = Password.Errors.ET_LOGIN

            if case == 'empty_fields':
                self.validation_check(
                    [locator_username, locator_password], [err_text_username, err_text_password]
                )
            elif case in ['empty_username', 'spaces_username']:
                self.validation_check(locator_username, err_text_username)
            elif case == 'empty_password':
                self.validation_check(locator_password, err_text_password)
            else:
                self.validation_check(locator_common, err_text_common)
            self.highlight_and_make_screenshot(file_name='validation_login_page')


    def login_by_token(
            self,
            title: bool = True
    ) -> NoReturn:
        with allure.step(f'Login by token: {os.environ["PATH_TALKS_TOKEN"]}.'):
            self.open_page(page='Login', title=title)
            if '--ver=on' in sys.argv:
                self.fill_token(email=os.environ['PATH_TALKS_TOKEN'])
                self.click_btn_login()
            else:
                self.fill_token_headless(email=os.environ['PATH_TALKS_TOKEN'])
                self.click_btn_login()

            try:
                self.wait_until_element_visible(Password.Locators.ET_USERNAME, 2)
                raise ValueError("Autorisation error. 'Unauthorized'.")
            except TimeoutException:
                # Если попап не появился, продолжаем выполнение
                pass
            self.highlight_and_make_screenshot()