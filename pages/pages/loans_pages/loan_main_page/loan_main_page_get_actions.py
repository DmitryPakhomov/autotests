from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.loans_pages_blocks.loans_common_page_blocks import LoansCommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import LoansHistory
from autotests.pages.utils import get_value


class LoansMainPageGetActions(LoansCommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loans_main_locators = LoansHistory.Locators

    @get_value('History element note')
    def get_history_note_text(self) -> str:
        return self.get_text(self.loans_main_locators.T_HISTORY_NOTE_TEXT, lower=True)

    @get_value('History element email subject')
    def get_history_email_subject(self) -> str:
        return self.get_text(self.loans_main_locators.T_HISTORY_EMAIL_SUBJECT, lower=True)

    @get_value('History event subject')
    def get_history_event_subject(self) -> str:
        return self.get_text(
            self.loans_main_locators.T_HISTORY_EVENT_SUBJECT_2, many=True, lower=True)

    @get_value('History event content')
    def get_history_event_content(self) -> str:
        return self.get_text(
            self.loans_main_locators.T_HISTORY_EVENT_CONTENT, many=True, lower=True)

    @get_value('History element email text in CHOICE case')
    def get_history_email_text_financial_profile(self) -> str:
        return self.get_text(
            self.loans_main_locators.T_HISTORY_EMAIL_IFRAME_TEXT_CHOICE, lower=True)

    @get_value('History element email text in CHOICE case')
    def get_history_email_text(self) -> str:
        return self.get_text(
            self.loans_main_locators.T_HISTORY_EMAIL_IFRAME_TEXT_CHOICE, lower=True)

    @get_value('History element email text')
    def get_history_iframe_email_text(self) -> str:
        return self.get_text(self.loans_main_locators.T_HISTORY_EMAIL_IFRAME_TEXT, lower=True)

    @get_value('History element attachments')
    def get_attachments_iframe_email_text(self, attachments: str) -> tuple:
        return self.get_locator_by_text('a', attachments)

    @get_value('History element task title')
    def get_history_task_title(self) -> str:
        return self.get_text(self.loans_main_locators.T_HISTORY_TASK_TITLE, lower=True)

    @get_value('History element creditor')
    def get_history_task_creditor(self) -> str:
        return self.get_text(self.loans_main_locators.T_HISTORY_TASK_CREDITOR, lower=True)

    @get_value('History element sales rep')
    def get_history_sales_rep(self) -> str:
        return self.get_text(self.loans_main_locators.T_HISTORY_SALES_REP, lower=True)
