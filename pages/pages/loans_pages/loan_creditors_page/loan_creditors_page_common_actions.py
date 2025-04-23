from typing import NoReturn

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.loans_pages_blocks.loans_common_page_blocks import LoansCommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import LoansCreditors, LeadsBudget
from autotests.pages.settings import Settings
from autotests.pages.utils import click_btn, click_dl, choose_elem, get_value, \
    check_visibility_elem, choose, click_radio_btn


class LoansCreditorsPageCommonActions(LoansCommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loan_creditors_page_locators = LoansCreditors.Locators

    @click_btn('Create new')
    def click_btn_create_new(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.B_CREATE_NEW)

    @click_btn('Create new creditor')
    def click_btn_create_new_creditor(self) -> NoReturn:
        self.wait_until_element_to_be_clickable(
            self.loan_creditors_page_locators.B_ADD_NEW_CREDITORS).click()

    @click_btn('Tab Acct. Information')
    def click_tab_acct_information_creditor(self) -> NoReturn:
        self.click_elem_by_text('a', 'Acct. Information')
        self.wait_until_element_visible(
            self.loan_creditors_page_locators.F_INPUT_CURRENT_CREDITOR_COMPANY)

    @click_dl('Creditor')
    def click_current_creditor_field(self) -> NoReturn:
        self.click_element(
            self.loan_creditors_page_locators.F_INPUT_CURRENT_CREDITOR_COMPANY)

    @choose_elem('Creditor')
    def choose_current_creditor_value(self, creditor: str) -> NoReturn:
        self.click_elem_by_text('strong', creditor)

    @click_dl('Account')
    def click_current_creditors_account(self) -> NoReturn:
        self.click_elem_by_text('label', 'Account #')

    @choose_elem('Account')
    def choose_current_creditors_account(self, account: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CURRENT_CREDITOR_ACCOUNT,
            keys=[account]
        )

    @click_btn('Document tab')
    def click_documents_tab(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.E_TAB_DOCUMENTS_CREDITOR)

    @click_btn('Document tab')
    def click_documents_tab_settlemet_offer(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.E_TAB_DOCUMENTS_SETTLEMENT_OFFER)

    @click_btn('Settlement offers tab')
    def click_tab_settlement_offers_creditor(self) -> NoReturn:
        self.click_elem_by_text('a', 'Settlement Offers')
        self.wait_until_element_visible(
            self.loan_creditors_page_locators.B_CREATE_NEW_OFFER)

    @click_btn('Creditor payments tab')
    def click_tab_payments_creditor(self) -> NoReturn:
        self.click_elem_by_text('a', 'Payments')

    @click_btn('Create new offer')
    def click_create_new_settlement_offer_item(self) -> NoReturn:
        self.wait_until_element_to_be_clickable(
            self.loan_creditors_page_locators.B_CREATE_NEW_OFFER)
        self.click_elem_by_text('a', 'Create New Offer')
        self.wait_until_element_to_be_clickable(
            self.loan_creditors_page_locators.E_TAB_SETTLEMENT_OFFER)

    @click_btn('Save')
    def click_btn_save_creditors(self) -> NoReturn:
        self.scroll_to_elem(self.find_element(
            self.loan_creditors_page_locators.B_CREDITORS_SAVE))
        self.click_element(self.loan_creditors_page_locators.B_CREDITORS_SAVE)

    @click_btn('Sort')
    def click_on_button_sort(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.B_SORT)

    @click_btn('Sort minus')
    def click_on_button_sort_minus(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.B_SORT_MINUS)

    @click_btn('Offer')
    def click_on_offer(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.T_ROW_OFFER)

    @click_btn('Click change offer status')
    def click_dl_status_creditor_offer(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.DL_STATUSES)

    @get_value('Check status offer')
    def check_not_clickable_dl_status_settlement_offer(self):
        aria_disabled_value = self.get_attribute(
            self.loan_creditors_page_locators.DL_RESULT_SEARCH, 'aria-disabled')
        return aria_disabled_value

    @click_btn('Save offer')
    def click_btn_save_settlement_offer(self) -> NoReturn:
        self.scroll_to_elem(
            self.find_element(
                self.loan_creditors_page_locators.B_CREDITOR_SETTLEMENT_OFFER_SAVE
            )
        )
        self.wait_until_element_to_be_clickable(
            self.loan_creditors_page_locators.B_CREDITOR_SETTLEMENT_OFFER_SAVE).click()

    @click_btn('Override save and add payments')
    def click_btn_override_save_and_add_payments_settlement_offer(self) -> NoReturn:
        self.scroll_to_elem(
            self.find_element(
                self.loan_creditors_page_locators.
                B_CREDITORS_SETTLEMENT_OFFER_OVERRIDE_SAVE_ADD_PAYMENTS
            ))
        self.wait_until_element_to_be_clickable(
            self.loan_creditors_page_locators.
            B_CREDITORS_SETTLEMENT_OFFER_OVERRIDE_SAVE_ADD_PAYMENTS,
            20
        ).click()

    @click_btn('Cancel')
    def click_btn_cancel_settlement_offer(self) -> NoReturn:
        self.scroll_to_elem(self.find_element(
            self.loan_creditors_page_locators.B_CANCEL_MODAL_OFFER))
        self.wait_until_element_to_be_clickable(
            self.loan_creditors_page_locators.B_CANCEL_MODAL_OFFER, 10).click()

    @click_btn('Upload document')
    def upload_documents(self) -> NoReturn:
        document_path = f'{Settings.DOWNLOAD_PATH}/example.pdf'
        self.find_element(
            self.loan_creditors_page_locators.B_UPLOAD_DOCUMENT_FILE).send_keys(document_path)

    @click_btn('Upload document to Settlement Offer')
    def upload_documents_to_settlement_offer(self) -> NoReturn:
        document_path = f'{Settings.DOWNLOAD_PATH}/example.pdf'
        self.find_element(
            self.loan_creditors_page_locators.B_UPLOAD_DOCUMENT_FILE_SETTLEMENT_OFFER
        ).send_keys(document_path)

    @click_btn('Type of document file')
    def select_type(self, doc_type: str) -> NoReturn:
        self.wait_until_element_to_be_clickable(
            self.loan_creditors_page_locators.S_TYPE_OF_FILE_CREDITORS).click()
        self.send_keys(
            self.loan_creditors_page_locators.F_TYPE_OF_FILE_FIELD,
            keys=[doc_type, Keys.ENTER]
        )

    @click_btn('Type of document file')
    def select_type_of_file_settlement_offer(self, doc_type: str) -> NoReturn:
        self.wait_until_element_to_be_clickable(
            self.loan_creditors_page_locators.S_TYPE_OF_FILE_SETTLEMENT_OFFER).click()
        self.send_keys(
            self.loan_creditors_page_locators.F_TYPE_OF_FILE_FIELD,
            keys=[doc_type, Keys.ENTER]
        )

    @click_btn('Upload document')
    def click_btn_upload(self) -> NoReturn:
        self.click_elem_by_text('button', 'Upload Document')
        self.wait_until_element_to_be_clickable(
            self.loan_creditors_page_locators.B_UPLOAD_DOCUMENT_IN_FORM, 20)

    @click_btn('Delete settlement offer')
    def click_delete_offer(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.B_DELETE_OFFER)

    @check_visibility_elem('Button delete')
    def check_btn_delete_not_present(self):
        self.element_is_present(self.loan_creditors_page_locators.B_DELETE_OFFER)

    @click_btn('Click on current offer')
    def click_acceptance_toggle(self) -> NoReturn:
        self.wait_until_element_not_visible(self.loan_creditors_page_locators.T_ROW_OFFER)
        self.click_element(self.loan_creditors_page_locators.TG_ACCEPTED_XPATH)

    @click_btn('Waiting for loaded')
    def wait_after_saving_creditor(self) -> NoReturn:
        self.wait_until_element_not_visible(self.loan_creditors_page_locators.T_ROW_CREDITOR)

    @click_btn('Delete')
    def click_on_deleted(self) -> NoReturn:
        self.wait_until_element_not_visible(
            self.loan_creditors_page_locators.B_DELETE).click()

    @click_btn('Verified')
    def click_verified(self) -> NoReturn:
        self.click_elem_by_text('button', 'I verified the information')

    @click_btn('Upload Document')
    def click_elem_by_text_upload_document(self):
        self.click_elem_by_text('button', 'Upload Document')

    @click_btn('Verification Block')
    def click_elem_by_text_verification_block(self):
        self.click_elem_by_text('a', 'Verification Block')

    @click_btn('Send Pre-Loan Docs')
    def click_send_preload_docs(self):
        self.click_elem_by_text('button', 'Send Pre-Loan Docs')

    @click_btn('Line of Credit Draw Request Form')
    def click_line_of_credit_draw_request_form(self):
        self.click_elem_by_text('a', 'Line of Credit Draw Request Form')

    @click_btn('Send Final-Loan Docs')
    def click_elem_by_text_send_final_loan_docs(self):
        self.click_elem_by_text('button', 'Send Final Loan Docs')

    @click_btn('Line of Credit Draw Request Form')
    def click_elem_by_text_line_of_credit_draw(self):
        self.click_elem_by_text('a', 'Line of Credit Draw Request Form')

    @get_value('Send loan docs')
    def get_elem_by_text_loan_docs_send(self):
        self.click_elem_by_text('span', 'Loan Docs Sent')

    @click_btn('Override Qualify')
    def click_elem_by_text_override_qualify(self):
        self.click_elem_by_text('a', 'Override Qualify')

    @click_btn('Override: Exception Loan')
    def click_elem_by_text_override_exception_loan(self):
        self.click_elem_by_text('span', 'Override: Exception Loan')

    @click_btn('eDocs')
    def click_elem_by_text_edocs(self):
        self.click_elem_by_text('button', 'eDocs')

    @click_btn('Send E-docs for LOC')
    def click_elem_by_text_send_edocs_for_loc(self):
        self.click_elem_by_text('a', 'Send E-docs for LOC')

    @click_btn('Ready for Funding')
    def click_elem_by_text_ready_for_funding(self):
        self.click_elem_by_text('span', 'Ready for Funding')

    @click_btn('Ready for Active')
    def click_elem_by_text_active(self):
        self.click_elem_by_text('span', 'Active')

    @choose('Hardship Reason')
    def select_hardship_reason_budget(self, hardship_reason_text: str) -> NoReturn:
        self.select_element(
            locator=LeadsBudget.Locators.S_HARDSHIP_REASON, text=hardship_reason_text)

    @click_radio_btn('Applicant')
    def fill_account_holder_applicant(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.RB_ACCOUNT_HOLDER_CHECK_APPLICANT)

    @click_radio_btn('Co-Applicant')
    def fill_account_holder_coapplicant(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.RB_ACCOUNT_HOLDER_CHECK_CO_APPLICANT)
