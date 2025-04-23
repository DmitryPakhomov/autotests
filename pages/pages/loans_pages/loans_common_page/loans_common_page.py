from typing import NoReturn

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.common_pages_blocks.common_page_blocks import CommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import Loans
from autotests.pages.settings import Settings
from autotests.pages.utils import click_btn, fill_field, choose_elem, choose, click_elem, \
    str_to_bool


class LoansCommonPage(CommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loan_common_locators = Loans.Locators

    @click_btn('Create Note')
    def click_btn_create_note(self) -> NoReturn:
        self.click_element(self.loan_common_locators.B_CREATE_NOTE)

    @click_btn('Fill Note')
    def fill_note_field(self, note_text: str) -> NoReturn:
        self.send_keys(self.loan_common_locators.F_NOTE_MODAL_EDITOR, keys=[note_text], t=0)

    @click_btn('Tab Note')
    def click_note_tab_form(self) -> NoReturn:
        self.click_element(self.loan_common_locators.E_NOTE_TAB)

    @fill_field('Fill Note tab')
    def fill_note_tab_form_field(self, note_text: str) -> NoReturn:
        self.send_keys(self.loan_common_locators.F_NOTE_TAB_EDITOR, keys=[note_text], t=0)

    @click_btn('Create Email')
    def click_btn_create_email(self) -> NoReturn:
        self.click_element(self.loan_common_locators.B_CREATE_EMAIL)

    @click_btn('Email Tab')
    def click_email_tab_form(self) -> NoReturn:
        self.click_element(self.loan_common_locators.E_EMAIL_TAB)

    @click_btn('Sales Rep')
    def click_dl_reassign_sales_rep(self) -> NoReturn:
        self.click_element(self.loan_common_locators.DL_REASSIGN_SALES_REP)

    @fill_field('Email Subject')
    def fill_email_field_subject(self, email_subject: str) -> NoReturn:
        self.send_keys(self.loan_common_locators.F_EMAIL_MODAL_SUBJECT, keys=[email_subject], t=0)

    @click_btn('Email Body')
    def fill_email_field_body(self, email_text: str) -> NoReturn:
        self.send_keys(self.loan_common_locators.F_EMAIL_MODAL_BODY, keys=[email_text], t=0)

    @click_btn('Email Subject')
    def fill_email_tab_form_subject(self, email_subject: str) -> NoReturn:
        self.send_keys(
            self.loan_common_locators.F_EMAIL_TAB_EDITOR_SUBJECT, keys=[email_subject], t=0)

    @click_btn('Email Body')
    def fill_email_tab_form_body(self, email_text: str) -> NoReturn:
        self.send_keys(self.loan_common_locators.F_EMAIL_TAB_EDITOR, keys=[email_text], t=0)

    @click_btn('Create Task')
    def click_btn_create_task(self) -> NoReturn:
        self.click_element(self.loan_common_locators.B_CREATE_TASK)

    @click_btn('Task title')
    def fill_task_field_title(self, title_text: str) -> NoReturn:
        self.send_keys(self.loan_common_locators.F_TASK_MODAL_TITLE, keys=[title_text], t=0)

    @click_btn('Task Description')
    def fill_task_field_description(self, description_text: str) -> NoReturn:
        self.send_keys(
            self.loan_common_locators.F_TASK_MODAL_DESCRIPTION, keys=[description_text], t=0)

    @click_btn('Creditor')
    def click_task_dl_creditor(self) -> NoReturn:
        self.click_element(self.loan_common_locators.DL_TASK_MODAL_CREDITOR)

    @click_btn('1st creditor')
    def choose_task_modal_creditor(self) -> NoReturn:
        self.click_element(self.loan_common_locators.DL_TASK_MODAL_CREDITOR_LIST)

    @choose_elem('Pre funded')
    def select_pre_funded(self) -> NoReturn:
        self.click_element(self.loan_common_locators.B_CLICK_PRE_FUNDED_STATUS)

    @click_btn('Upload file')
    def upload_documents(self) -> NoReturn:
        document_path = f'{Settings.DOWNLOAD_PATH}/example.pdf'
        self.find_element(self.loan_common_locators.B_UPLOAD_DOCUMENT).send_keys(document_path)

    @click_btn('Upload file')
    def upload_documents_in_tabs(self) -> NoReturn:
        document_path = f'{Settings.DOWNLOAD_PATH}/example.pdf'
        self.find_element(
            self.loan_common_locators.B_UPLOAD_DOCUMENT_IN_TAB).send_keys(document_path)

    @choose('Reassign uderwriter')
    def choose_underwriter(self, underwriter: str) -> NoReturn:
        self.click_element(self.loan_common_locators.DL_REASSIGN_UNDERWRITER)
        self.send_keys(
            self.loan_common_locators.F_REASSIGN_SALES_REP_INPUT, keys=[underwriter, Keys.ENTER])

    @choose('Reassign loc')
    def choose_loc_processor(self, loc: str) -> NoReturn:
        self.click_element(self.loan_common_locators.DL_REASSIGN_LOC)
        self.send_keys(self.loan_common_locators.F_REASSIGN_INPUT, keys=[loc, Keys.ENTER])

    @choose_elem('Status')
    def select_active(self) -> NoReturn:
        self.click_element(self.loan_common_locators.B_CLICK_STATUS)

    @click_elem('Documents')
    def click_document_in_popup(self) -> NoReturn:
        self.click_element(self.loan_common_locators.B_CLICK_DOCUMENTS)

    @choose_elem('Type of document file')
    def select_type(self, file_type: str) -> NoReturn:
        self.click_element(self.loan_common_locators.S_TYPE_OF_FILE)
        self.send_keys(self.loan_common_locators.S_TYPE_OF_FILE_FIELD, keys=[file_type, Keys.ENTER])

    @choose('Type of document file')
    def select_type_in_tabs(self, file_type: str) -> NoReturn:
        self.click_element(self.loan_common_locators.S_TYPE_OF_FILE_IN_TABS)
        self.send_keys(
            self.loan_common_locators.S_TYPE_OF_FILE_FIELD_IN_TABS, keys=[file_type, Keys.ENTER])

    @click_btn('CRB')
    def click_crb_toggle_to_off(self) -> NoReturn:
        status = self.get_property(
            self.loan_common_locators.TG_CRB_STATUS, property_name='data-switchery', lower=True)
        if not str_to_bool(status):
            self.click_element(self.loan_common_locators.TG_CRB)

    @click_btn('Loan Pro')
    def click_loan_pro_toggle_to_off(self) -> NoReturn:
        status = self.get_property(
            self.loan_common_locators.TG_LOAN_PRO_STATUS,
            property_name='data-switchery',
            lower=True
        )
        if not str_to_bool(status):
            self.click_element(self.loan_common_locators.TG_LOAN_PRO)
