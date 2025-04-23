from typing import NoReturn
import allure


from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.elements import Element
from autotests.pages.pages_details.common_pages_details import Common
from autotests.pages.utils import get_number_from_text, click_btn, get_value, click_toggle, \
    fill_field, click_elem, click_dl, click_cb


class CommonPage(Element):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.common_page_locators = Common.Locators

    @click_dl('Drop-down on avatar')
    def click_dl_avatar(self) -> NoReturn:
        self.click_element(self.common_page_locators.DL_AVATAR)

    @click_dl('Settings')
    def click_btn_settings(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_SETTINGS, t=16)

    @click_btn('Send a SMS')
    def click_btn_sms_filtering_list(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_SMS_FILTERING_LIST)

    # main search
    @click_btn('Main search')
    def click_btn_search(self) -> NoReturn:
        self.click_element(self.common_page_locators.E_MAIN_SEARCH)

    @fill_field('Main search')
    def fill_field_search(self, search_text) -> NoReturn:
        self.wait_until_element_visible(self.common_page_locators.F_INPUT_MAIN_SEARCH)
        self.send_keys(self.common_page_locators.F_INPUT_MAIN_SEARCH, keys=[search_text, Keys.ENTER])

    @get_value('Search result')
    def get_search_result(self, many: bool = False) -> str:
        self.wait_until_element_visible(self.common_page_locators.F_SEARCH_RESULT)
        return self.get_text(self.common_page_locators.F_SEARCH_RESULT, many=many, lower=True)

    @click_elem('Found user')
    def click_by_found_user(self) -> NoReturn:
        self.wait_until_element_visible(self.common_page_locators.F_SEARCH_RESULT)
        self.click_element(self.common_page_locators.F_SEARCH_RESULT)

    @click_btn('Bell')
    def click_btn_bell(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_BELL)
        self.waiting_for_page_loaded()

    @get_value('First notification')
    def get_first_notif_text(self) -> str:
        return self.get_text(self.common_page_locators.T_FIRST_NOTIFICATION).lower()

    @get_value('Locked status')
    def get_locked_status(self) -> str:
        return self.get_attribute(self.common_page_locators.E_LOCKED_STATUS, attr_name='title').lower()

    @get_value('Doc send status')
    def get_doc_send_status(self) -> str:
        return self.get_attribute(self.common_page_locators.DOCS_SEND_STATUS, attr_name='title').lower()

    @click_toggle('Logout')
    def click_btn_logout(self) -> NoReturn:
        self.click_elem_by_text('button', 'Logout')

    @click_btn('Go next signature')
    def click_btn_go_next_signature(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_GO_TO_NEXT_SIGNATURE)

    @click_btn('Click here to sign')
    def click_btn_click_here_to_sign(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_CLICK_HERE_TO_SIGN)
        self.waiting_for_page_loaded()

    @get_value('Client id')
    def get_client_id(self) -> str:
        return get_number_from_text(self.get_text(self.common_page_locators.T_CLIENT_ID))

    @click_btn('Confirm')
    def click_btn_confirm(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_CONFIRM)

    @click_btn('Continue')
    def click_checkbox_acknowledge(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_CONFIRM_CONTINUE_CHECKBOX)

    @click_btn('Continue')
    def click_btn_continue(self) -> NoReturn:
        self.click_elem_by_text('button', 'Continue')

    @click_btn('Cancel')
    def click_btn_cancel(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_CANCEL)

    @click_btn('Save')
    def click_btn_save(self) -> NoReturn:
        self.click_via_js(self.find_element(self.common_page_locators.B_SAVE))
        self.waiting_for_page_loaded()

    @click_btn('Save')
    def click_btn_save_negative(self) -> NoReturn:
        elem = self.find_element(self.common_page_locators.B_SAVE)
        self.click_via_js(elem)
        self.waiting_for_page_loaded()

    @click_btn('Save')
    def click_btn_save_modal(self) -> NoReturn:
        self.click_via_js(self.find_element(self.common_page_locators.B_SAVE_MODAL))
        self.waiting_for_page_loaded()

    @click_btn('Save')
    def click_btn_save_modal_financial_profile(self) -> NoReturn:
        self.wait_until_element_to_be_clickable(self.common_page_locators.B_SAVE_MODAL_FINANCIAL_PROFILE)
        self.click_via_js(self.find_element(self.common_page_locators.B_SAVE_MODAL_FINANCIAL_PROFILE))
        self.waiting_for_page_loaded()

    @click_btn('Save')
    def click_btn_send_email(self) -> NoReturn:
        self.click_via_js(self.find_element(self.common_page_locators.B_SEND_EMAIL))
        self.waiting_for_page_loaded()

    @click_btn('Save')
    def click_btn_tab_send_email(self) -> NoReturn:
        self.click_elem_by_text(tag='button', text='Send Email')

    @get_value('Internal page title')
    def get_internal_page_title(self) -> str:
        return self.get_text(self.common_page_locators.T_INTERNAL_PAGE_TITLE)

    @get_value('Error text list')
    def get_error_text_list(self) -> list[str]:
        return self.get_text(self.common_page_locators.ET_FIELDS_ERRORS, many=True)

    @get_value('Error text list')
    def get_brokers_error_text_list(self) -> list[str]:
        return self.get_text(self.common_page_locators.ET_BROKERS_FIELDS_ERRORS, many=True)

    def click_main_tabs(self, tab: str) -> NoReturn:
        with allure.step(f'Click on the tab: {tab}.'):
            self.click_elem_by_text('span[@class="site-menu-title"]', tab)
            self.waiting_for_page_loaded()

    @click_btn('Reassign')
    def click_btn_reassign(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_REASSIGN)
        self.wait_until_element_to_be_clickable(self.common_page_locators.B_SAVE, t=15)

    @click_btn('Reassign to me')
    def click_btn_reassign_to_me(self) -> NoReturn:
        self.click_elem_by_text('a', 'Assign to me')

    @click_dl('C9 Loan consultant')
    def click_dl_reassign_c9_loan_consultant(self) -> NoReturn:
        self.click_element(self.common_page_locators.DL_REASSIGN_C9_LOAN_CONSULTANT)

    @fill_field('Reassigning')
    def fill_field_reassign(self, user: str) -> NoReturn:
        self.send_keys(self.common_page_locators.F_REASSIGN_INPUT, keys=[user, Keys.ENTER])

    @click_dl('Save & Close')
    def click_btn_reassign_save(self) -> NoReturn:
        self.click_elem_by_text('button', 'Save & Close')

    @get_value('Validation error title')
    def get_validation_error_title(self) -> str | bool:
        if self.element_is_present(self.common_page_locators.T_VALIDATION_ERROR_TITLE):
            return self.get_text(self.common_page_locators.T_VALIDATION_ERROR_TITLE)
        return False

    @get_value('Validation error reason')
    def get_validation_error_reason(self) -> str:
        return ' '.join(
            self.get_text(self.common_page_locators.T_VALIDATION_ERROR_REASON, many=True))

    def click_btn_sending_type(self, sending_type: str) -> NoReturn:
        with allure.step(f'Click on the button "{sending_type}".'):
            self.click_elem_by_text('a', sending_type)

    @get_value('Signing success')
    def get_signing_success(self) -> str:
        return self.get_text(self.common_page_locators.T_SIGNING_SUCCESS)

    @get_value('Name of client')
    def get_client_signed(self) -> str:
        return self.get_text(self.common_page_locators.T_CLIENT_SIGNED)

    @click_toggle('Upfront Lending Candidate')
    def click_tg_upfront(self) -> NoReturn:
        self.click_elem_by_text('label', 'Upfront Lending Candidate')

    @click_btn('Underwrite')
    def click_btn_underwrite_file(self) -> NoReturn:
        self.scroll_up()
        self.click_elem_by_text('a', 'Underwrite file')

    @click_toggle('LoanPro')
    def click_tg_loan_pro(self) -> NoReturn:
        self.click_element(self.common_page_locators.TG_LOAN_PRO)

    @click_btn('Create loan')
    def click_btn_create_loan(self) -> NoReturn:
        self.click_via_js_new(self.find_element(self.common_page_locators.TG_LOAN_PRO_CREATE))

    @click_btn('Send docs')
    def click_btn_send_docs(self) -> NoReturn:
        self.wait_until_element_not_visible(self.common_page_locators.B_SEND_DOCS, t=20).click()

    @click_btn('Send docs')
    def click_btn_enroll(self) -> NoReturn:
        #self.wait_until_element_not_visible(self.common_page_locators.B_ENROLL, t=20).click()
        self.click_elem_by_text('a', 'Enroll')

    @click_btn('Agreement only')
    def click_btn_agreement_only(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_AGREEMENT_ONLY)

    @click_btn('Upfront final loans')
    def click_upfront_final_loans(self) -> NoReturn:
        self.click_elem_by_text('a', 'Upfront Final Loan')

    @fill_field('Pre-Enrollment reason')
    def fill_reason_send_docs(self, text: str) -> NoReturn:
        self.send_keys(self.common_page_locators.F_SEND_PRE_ENROLLMENT, keys=[text, Keys.ENTER])

    # docusign
    @click_cb("Docusign term of service")
    def click_cb_docusign_term_of_service(self) -> NoReturn:
        self.click_element(self.common_page_locators.CB_DOCUSIGN_TERM_OF_SERVICE)

    @click_btn('Docusign next')
    def click_btn_docusign_next(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_DOCUSIGN_ACTION_NEXT)

    @click_btn('Docusign start')
    def click_btn_docusign_start(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_DOCUSIGN_ACTION_START)

    @click_btn('Docusign sign arrow')
    def click_btn_docusign_sign_arrow(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_DOCUSIGN_SIGN_ARROW)

    @click_btn('Docusign sign acceptance')
    def click_btn_docusign_sign_acceptance(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_DOCUSIGN_SIGN_ACCEPTANCE)

    @click_btn('Docusign sign final')
    def click_btn_docusign_sign_final(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_DOCUSIGN_SIGN_FINAL)
        self.waiting_for_page_loaded()

    @click_btn('Docusign submit')
    def click_btn_docusign_submit(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_FINAL_CHECK_BUTTON_SUBMIT)

    @click_btn('Send')
    def click_btn_send_a_sms(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_SEND_SMS)

    @click_btn('Send a SMS')
    def click_btn_send_a_sms_tab(self) -> NoReturn:
        self.click_element(self.common_page_locators.B_SEND_A_SMS_TAB)

    @fill_field('Fill forbidden word')
    def fill_filtering_field(self, forbidden_text: str) -> NoReturn:
        self.send_keys(self.common_page_locators.F_SMS_FILTERING_LIST, keys=[forbidden_text])