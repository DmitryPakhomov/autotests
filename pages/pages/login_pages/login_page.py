from typing import NoReturn


from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.common_pages_blocks.common_page_blocks import CommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details.login_pages_details import Login, Password
from autotests.pages.utils import click_btn, fill_field


class LoginPage(CommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.login_locators = Login.Locators
        self.login_password_locators = Password.Locators

    @click_btn('Sign In via Google')
    def click_btn_sign_in_via_google(self) -> NoReturn:
        self.click_element(self.login_locators.B_SIGN_VIA_GOOGLE)

    @fill_field('Email')
    def fill_email(self, email: str) -> NoReturn:
        self.send_keys(self.login_locators.F_EMAIL, keys=[email])

    @fill_field('Token')
    def fill_token(self, token: str) -> NoReturn:
        self.send_keys(self.login_locators.F_TOKEN, keys=[token])

    @fill_field('Password')
    def fill_email_password(self, password: str) -> NoReturn:
        self.send_keys(self.login_locators.F_EMAIL_PASS, keys=[password])

    @click_btn('Further')
    def click_btn_further(self) -> NoReturn:
        self.click_elem_by_text('span', 'Далее')

    @click_btn('Further')
    def click_btn_login(self) -> NoReturn:
        self.click_elem_by_text('span', 'Login')

    @fill_field('Email')
    def fill_email_headless(self, email: str) -> NoReturn:
        self.send_keys(self.login_locators.F_EMAIL_HEADLESS, keys=[email])

    @fill_field('Token')
    def fill_token_headless(self, token: str) -> NoReturn:
        self.send_keys(self.login_locators.F_TOKEN_HEADLESS, keys=[token])

    @fill_field('Password')
    def fill_email_password_headless(self, password: str) -> NoReturn:
        self.send_keys(self.login_locators.F_EMAIL_PASS_HEADLESS, keys=[password])

    @click_btn('Further')
    def click_btn_further_after_email(self) -> NoReturn:
        self.click_element(self.login_locators.B_FURTHER_AFTER_EMAIL)

    @click_btn('Further')
    def click_btn_further_after_pass(self) -> NoReturn:
        self.click_element(self.login_locators.B_FURTHER_AFTER_PASS)

    @click_btn('Sign In by Password')
    def click_btn_sign_in_by_password(self) -> NoReturn:
        self.click_element(self.login_locators.B_SIGN_BY_PASS)

    @fill_field('Username')
    def fill_username(self, username: str) -> NoReturn:
        self.send_keys(self.login_password_locators.F_USERNAME, keys=[username])

    @fill_field('Password')
    def fill_password(self, password: str) -> NoReturn:
        self.send_keys(self.login_password_locators.F_PASSWORD, keys=[password])

    @click_btn('Log In')
    def click_btn_login(self) -> NoReturn:
        self.click_element(self.login_password_locators.B_LOGIN)

