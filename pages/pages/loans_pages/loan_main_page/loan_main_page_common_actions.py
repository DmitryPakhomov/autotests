from typing import NoReturn


from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.loans_pages_blocks.loans_common_page_blocks import LoansCommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import LoansHistory
from autotests.pages.settings import Settings
from autotests.pages.utils import click_btn, click_toggle


class LoansMainPageCommonActions(LoansCommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loans_main_locators = LoansHistory.Locators

    @click_btn('Angle right')
    def click_btn_angle_right(self) -> NoReturn:
        self.click_element(self.loans_main_locators.B_ARROW)
        self.waiting_for_page_loaded()

    @click_btn('sms consent')
    def click_sms_consent(self) -> NoReturn:
        self.click_element(self.loans_main_locators.B_SMS_CONSENT)

    def change_tab_note_mail(self, value: str) -> NoReturn:
        with allure.step(f'Change tab on {value}.'):
            self.click_elem_by_text('a', value)

    @click_btn('Financial Profile')
    def click_btn_financial_profile(self) -> NoReturn:
        self.click_elem_by_text('a', 'Financial Profile')
        self.waiting_for_page_loaded()

    @click_btn('Send')
    def click_btn_send_financial_profile(self) -> NoReturn:
        self.click_element(self.loans_main_locators.B_SEND_IN_FINANCIAL_PROFILE)

    @click_btn('Click here')
    def click_btn_click_here_fp(self) -> NoReturn:
        self.click_elem_by_text('a', 'Click here')

    @click_btn('Email')
    def click_email_button(self) -> NoReturn:
        self.click_element(self.loans_main_locators.B_EMAIL_PAGE)

    def fill_email_attachments(self) -> NoReturn:
        with allure.step('Add email attachments'):
            document_path = f'{Settings.DOWNLOAD_PATH}/file_example.jpg'
            self.find_element(
                self.loans_main_locators.B_UPLOAD_DOCUMENT_EMAIL).send_keys(document_path)

    @click_btn('Do Not Contact')
    def click_btn_do_not_contact(self) -> NoReturn:
        self.click_elem_by_text('a', 'Do Not Contact')

    @click_toggle('Toggle SMS to')
    def click_toggle_sms_to(self) -> NoReturn:
        self.click_elem_by_text('label', 'SMS to')
