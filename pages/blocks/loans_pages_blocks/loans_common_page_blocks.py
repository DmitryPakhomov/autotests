import time
from typing import NoReturn

import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.data.main_data import Configs
from autotests.pages.data.test_data import TestData
from autotests.pages.pages.loans_pages.loans_common_page.loans_common_page import LoansCommonPage
from autotests.pages.utils import step, get_last_id_from_lead_json, get_value


class LoansCommonPageBlocks(LoansCommonPage):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.cfg = cfg

    def reassigning(
            self,
            opener: str = None,
            sales_rep: str = None,
            sales_manager: str = None,
            c9_loan_consultant: str = None
    ) -> NoReturn:
        with allure.step('Reassign client.'):
            self.refresh_page_with_closed_all_hints()
            self.click_btn_reassign()
            if sales_rep:
                self.choose_sales_rep(sales_rep=sales_rep)
            if opener:
                pass
            if sales_manager:
                pass
            if c9_loan_consultant:
                self.choose_c9_loan_consultant(loan_consultant=c9_loan_consultant)
            self.click_btn_reassign_save()
            self.success_or_error_check()

    def choose_sales_rep(self, sales_rep: str) -> NoReturn:
        with allure.step(step.choose('Sales Rep')):
            self.click_dl_reassign_sales_rep()
            self.fill_field_reassign(user=sales_rep)

    def crb_and_loanpro_off(self):
        with allure.step(step.choose('Turn of crb and loanpro')):
            self.click_crb_toggle_to_off()
            self.click_loan_pro_toggle_to_off()

    def choose_c9_loan_consultant(self, loan_consultant: str) -> NoReturn:
        with allure.step(step.choose('C9 loan consultant')):
            user = self.cfg.auth[loan_consultant]['username']
            self.click_dl_reassign_c9_loan_consultant()
            self.fill_field_reassign(user=user)

    def check_validation_error_in_tab(self) -> NoReturn:
        with allure.step('Checking validation errors in tab.'):
            title = self.get_validation_error_title()
            if title:
                reason = self.get_validation_error_reason()
                error = f'{title} {reason}'
                raise Exception(
                    self.error_handler(
                        action='Checking validation errors in tab.',
                        error=error
                    )
                )

    def sending_docs(self, sending_type: str) -> NoReturn:
        with allure.step('Send Docs.'):
            self.close_all_hints()
            self.click_btn_send_docs()
            self.click_btn_sending_type(sending_type=sending_type)
            self.success_or_error_check()
            self.confirmation()
            self.success_or_error_check()
            self.waiting_for_page_loaded()
            self.highlight_and_make_screenshot()
            self.refresh_page()

    def read_id_and_check_history(self):
        with allure.step('Go to page Enrollments profile and check what Lead transfer to Deal.'):
            deal_id = get_last_id_from_lead_json(file_name='lead_to_deal')
            self.open_page(page='EnrollmentsMain', client_id=deal_id)
            self.check_js_errors()
        return deal_id

    def reassigning_enrollments(
            self,
            sales_rep: str = TestData.sales_rep(),
            underwriter: str = TestData.sales_rep(),
            loc: str = TestData.sales_rep()
    ) -> NoReturn:
        with allure.step('Reassign deal.'):
            self.reassign_deal(sales_rep=sales_rep, underwriter=underwriter, loc=loc)

    def check_exception_loan(self) -> NoReturn:
        with allure.step('Click to button'):
            self.waiting_for_page_loaded()
            self.click_elem_by_text('a', 'Override: Exception Loan')
            time.sleep(1)
            self.confirmation()

    def click_override_qualify(self) -> NoReturn:
        with allure.step('Click "Override Qualify".'):
            self.click_elem_by_text('a', 'Override Qualify')
            time.sleep(2)
            self.confirmation()
            self.success_or_error_check()
            time.sleep(2)

    def click_send_documents(self):
        with allure.step('Select Send E-docs for LOC.'):
            self.click_elem_by_text('button', 'eDocs')
            self.click_elem_by_text('a', 'Send E-docs for LOC')
            time.sleep(2)
            self.confirmation()
            self.success_or_error_check()

    def click_loan_send_documents(self, doc_type: str):
        with allure.step('Select Send E-docs.'):
            self.click_elem_by_text('button', 'eDocs')
            self.click_elem_by_text('a', doc_type)
            time.sleep(2)
            self.confirmation()
            self.success_or_error_check()

    def signing_docs(self) -> NoReturn:
        with allure.step('Get link for signing.'):
            link = self.get_link_for_signing()
        with allure.step('Open docs and sign.'):
            signing = self.sign_docs(link)
        with allure.step('Docs signed:', signing):
            self.highlight_and_make_screenshot(file_name='deal_docs_sign')

    def click_underwriting(self):
        with allure.step('Press underwriting.'):
            self.click_elem_by_text('a', 'To Underwriting')
            self.confirmation()
            self.waiting_for_page_loaded()
            self.success_or_error_check()

    @get_value('link for signing')
    def get_link_for_signing(self) -> str:
        self.find_element(self.loan_common_locators.B_ARROW).click()
        self.waiting_for_page_loaded()
        self.switch_to_iframe(0)
        link_for_signing = self.get_text(self.loan_common_locators.T_SIGN_DOCS_LINK)
        return link_for_signing

    def change_enrollment_status(self):
        with allure.step('Go to page deal history and change status to active.'):
            self.select_active()
            self.click_elem_by_text('span', 'Active')
            self.waiting_for_page_loaded()
            self.success_or_error_check()

    def click_approved(self):
        with allure.step('Click Approve'):
            self.waiting_for_page_loaded()
            self.saving()
            time.sleep(1)
            self.confirmation()
            self.success_or_error_check()

    def send_pre_load_docs(self):
        with allure.step('Send pre-load documents'):
            self.click_elem_by_text('button', 'Send Pre-Loan Docs')
            self.click_elem_by_text('a', 'Line of Credit Draw Request Form')
            time.sleep(1)
            self.confirmation()
            self.success_or_error_check()
            self.highlight_and_make_screenshot(file_name='pre_final_docs_sent')

    def send_final_load_docs(self):
        with allure.step('Send final documents'):
            self.click_elem_by_text('button', 'Send Final Loan Docs')
            self.click_elem_by_text('a', 'Line of Credit Draw Request Form')
            time.sleep(1)
            self.confirmation()
            self.success_or_error_check()
            self.waiting_for_page_loaded()
            self.highlight_and_make_screenshot(file_name='final_docs_sent')

    def check_docusign_agreements_deal(self, url: str) -> NoReturn:
        login = self.cfg.auth['email_account']['username']
        password = self.cfg.auth['email_account']['password']
        with allure.step('Check docusign agreements.'):
            self.refresh_page()
            self.get_elem_by_text('span', 'Loan Docs Sent')
            self.get_page(url=url)
            self.login_to_email_service(login, password)
            self.click_elem_by_text('div', 'Dmitry Drigo via DocuSign', 65)
            self.switch_to_iframe(0)
            self.get_elem_by_text('span', 'REVIEW DOCUMENTS')
            self.get_elem_by_text('div', 'dmitry.drigo@americor.com')
            self.switch_out_iframe()
            self.delete_last_email()
            self.highlight_and_make_screenshot(file_name='lead_docs_sign')

    def click_ready_for_funding(self):
        with allure.step('Go to page deal history.'):
            self.select_pre_funded()
            self.click_elem_by_text('span', 'Ready for Funding')
            self.waiting_for_page_loaded()
            self.success_or_error_check()

    def reassign_deal(self, sales_rep: str = None, underwriter: str = None, loc: str = None):
        with allure.step('Reassign deal.'):
            self.click_btn_reassign()
            if sales_rep:
                self.choose_sales_rep(sales_rep=sales_rep)
            if underwriter:
                self.choose_underwriter(underwriter=underwriter)
            if loc:
                self.choose_loc_processor(loc=loc)
            self.click_btn_reassign_save()
            self.waiting_for_page_loaded()
            self.success_or_error_check()
