import time

import allure
from typing import NoReturn
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common import StaleElementReferenceException, ElementClickInterceptedException
from autotests.pages import pages_details
from autotests.pages.data.enrollments_data import enrollments_pages
from autotests.pages.data.leads_data import leads_pages
from autotests.pages.data.loans_data import loans_pages
from autotests.pages.data.main_data import Configs
from autotests.pages.pages.common_pages.common_page import CommonPage
from autotests.pages.utils import step


class CommonPageBlocks(CommonPage):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver)
        self.cfg = cfg
        self.base_url = cfg.common['url']
        self.url_api = cfg.common['url_api']

    def open_page(
            self,
            page: str,
            client_id: str = '',
            title: bool = False
    ) -> str:
        url = self.base_url + getattr(pages_details, page).ENDPOINT + client_id
        with allure.step(f'Open page: {url}.'):
            self.get_page(url)
            self.highlight_and_make_screenshot()
            if title:
                excepted_title = getattr(pages_details, page).TITLE
                with allure.step(f'Checking {page} page title.'):
                    current_title = self.check_page_title(title=excepted_title)
                with allure.step(f'{page} page title is correct: {current_title}'):
                    return current_title

    def check_page_internal_title(self, title: str) -> NoReturn:
        with allure.step(f'Checking {title} page internal title.'):
            current_title = self.get_internal_page_title()
            assert current_title == title, AssertionError(
                self.error_handler(
                    action='Check internal page title.',
                    error='Incorrect internal page',
                    as_is=current_title,
                    to_be=title
                )
            )
        with allure.step(f'{title} page internal title is correct: {title}'):
            pass

    def check_page_error(self, action: str = 'Check page errors.') -> NoReturn:
        with allure.step('Check page errors.'):
            error_icon = self.element_is_present(self.common_page_locators.EE_ICON)
            if error_icon:
                error_text = self.find_element(self.common_page_locators.ET)
                assert not error_icon, AssertionError(self.error_handler(action=action, error=error_text.text))

    def check_page_console_log_errors(
            self, pages: list[str], broker: bool = False, client_id: str = '') -> NoReturn:
        with allure.step('Check page console log errors.'):
            errors = {}
            page_without_client = [
                leads_pages.leads, enrollments_pages.enrollments, loans_pages.loans
            ]

            for page in pages:
                if page in page_without_client:
                    self.open_page(page=page, broker=broker)
                else:
                    self.open_page(page=page, broker=broker, client_id=client_id)

                with allure.step(f'Check {page} page errors.'):
                    page_errors = self.check_js_errors(return_errors=True)
                    if page_errors:
                        errors[page] = page_errors

            if errors:
                raise Exception(
                    self.error_handler(
                        page_url=False,
                        action='Checking the logs of the page for errors.',
                        error=errors
                    )
                )

    def validation_check(self, locator: tuple | list, err_text: str | list) -> NoReturn:
        with allure.step('Checking validation of form fields.'):
            if isinstance(locator, list):
                elem = all(map(self.element_is_present, locator, [2, 2]))
            else:
                elem = self.element_is_present(locator=locator, t=2)

            assert elem, AssertionError(
                self.error_handler(
                    action='Checking validation of form fields.',
                    error='No validation error.',
                    to_be=err_text
                )
            )

    def choose_tab(self, tab: str) -> NoReturn:
        with allure.step(f'Click on the tab: {tab}.'):
            self.close_all_hints()
            self.scroll_up()
            self.click_elem_by_text('a[@class="nav-link"]', tab)
            self.refresh_page()

    def choose_enrollments_tabs(self, tab: str) -> NoReturn:
        with allure.step(f'Click on the tab: {tab}.'):
            self.close_all_hints()
            self.click_elem_by_text('a[@class="nav-link"]', tab)
            self.waiting_for_page_loaded()

    def confirmation(self, confirm: bool = True) -> NoReturn:
        with allure.step('Confirmation in pop-up.'):
            time.sleep(6)
            if confirm:
                self.click_btn_confirm()
            if not confirm:
                self.click_btn_cancel()
            self.waiting_for_page_loaded()

    def confirmation_in_popup(self, confirm: bool = True) -> NoReturn:
        with allure.step('Confirmation in pop-up.'):
            time.sleep(2)
            if confirm:
                self.click_checkbox_acknowledge()
                self.click_btn_continue()
            if not confirm:
                self.click_btn_cancel()
            self.waiting_for_page_loaded()

    def confirmation_upfront(self) -> NoReturn:
        with allure.step('Confirmation upfront send in pop-up.'):
            time.sleep(2)
            self.click_elem_by_text('button', 'Confirm & Send documents')
            self.waiting_for_page_loaded()

    def logout(self) -> NoReturn:
        with allure.step(step.click_btn('Logout')):
            self.click_dl_avatar()
            self.click_btn_logout()

    def success_or_error_text(self, t: int = 10) -> str:
        with allure.step('Check error notifications.'):
            success = self.common_page_locators.T_SUCCESS
            error = self.common_page_locators.ET_ERROR
            if self.element_is_present(locator=error, t=t):
                error_text = self.get_text(error)
                with allure.step(f'Get error notification: {error_text}.'):
                    return error_text
            if self.element_is_present(locator=success, t=t):
                success_text = self.get_text(success)
                with allure.step(f'Get success notification: {success_text}.'):
                    return success_text

    def check_loader(self):
        with allure.step('Check loader'):
            a = self.element_is_present(locator=self.common_page_locators.B_UPLOAD_SPINNER)
            start = time.monotonic()
            while a:
                a = self.element_is_present(locator=self.common_page_locators.B_UPLOAD_SPINNER)
                end = time.monotonic()
                if end - start > 30:
                    raise Exception(
                        self.error_handler(error='Loading time more then 30 sec'))

    def success_or_error_check(self, timeout: int = 30) -> str:
        with allure.step('Check error notifications.'):
            notif_error_words = ['error']
            notif_locator = self.common_page_locators.E_SUCCESS_OR_ERROR
            notif = self.element_is_present(locator=notif_locator)
            start = time.monotonic()
            while not notif:
                notif = self.element_is_present(locator=notif_locator)
                end = time.monotonic()
                if end - start > timeout:
                    raise Exception(
                        self.error_handler(error='Success or error message not present.'))
            notif_text = self.get_text(locator=notif_locator, lower=True)
            for notif_word in notif_error_words:
                assert notif_word not in notif_text, AssertionError(
                    self.error_handler(error=notif_text)
                )
            return notif_text

    def saving(self) -> NoReturn:
        with allure.step('Saving.'):
            self.click_btn_save()

    def saving_income(self) -> NoReturn:
        self.scroll_up()
        self.click_elem_by_text('button', 'Save')
        time.sleep(2)

    def close_all_hints(self) -> NoReturn:
        with allure.step('Find and close all toasts.'):
            if self.element_is_present(self.get_locator_by_text('a', ' Close')):
                self.double_click_elem_by_text('a', ' Close')
                self.waiting_for_page_loaded(sleep_time=2)

    def refresh_page_with_closed_all_hints(self) -> NoReturn:
        self.driver.refresh()
        self.waiting_for_page_loaded()
        self.close_all_hints()

    def sign_docs(self, url: str) -> str:
        with allure.step('Open docs and sign.'):
            self.get_page(url)
            self.waiting_for_page_loaded(sleep_time=6)
            self.click_btn_go_next_signature()
            while self.element_is_present(self.common_page_locators.B_CLICK_HERE_TO_SIGN, t=5):
                try:
                    self.click_btn_click_here_to_sign()
                except StaleElementReferenceException:
                    self.waiting_for_page_loaded()
                except ElementClickInterceptedException:
                    self.waiting_for_page_loaded()
            if self.get_signing_success() in ['Success!', 'Congratulations!']:
                return self.get_client_signed()

    def check_docusign_agreements(self, lead_id: str, url: str) -> NoReturn:
        with allure.step('Transition to docusign documents'):
            login = self.cfg.auth['email_account']['username']
            password = self.cfg.auth['email_account']['password']
            self.open_page(page='LeadsProfile', client_id=lead_id)
            self.check_locked_status()
            self.get_page(url=url)
            self.login_to_email_service(login, password)
            self.click_by_mail()
            time.sleep(2)
            self.switch_to_iframe(0)
            self.get_elem_by_text_review_document()
            self.get_elem_by_text_mail_text()
            self.switch_out_iframe()
            self.delete_last_email()
            self.highlight_and_make_screenshot(file_name='lead_docs_sign')

    def click_btn_confirm_and_sign_docs(self) -> NoReturn:
        with allure.step(step.click_btn('Sign Docs')):
            self.wait_until_element_not_visible(self.common_page_locators.B_SIGN_DOCS)
            self.click_elem_by_text('button', 'Confirm & Send documents')
            time.sleep(1)

    def click_active_day(self) -> NoReturn:
        with allure.step('Choose active day on data picker.'):
            self.find_element(self.common_page_locators.E_ACTIVE_DAY).click()

    def check_locked_status(self) -> NoReturn:
        with allure.step('Check change status.'):
            actual_locked_status = self.get_locked_status()
            excepted_locked_status = 'locked'
            assert actual_locked_status == excepted_locked_status, AssertionError(
                self.error_handler(
                    action='Check locked status.',
                    error='Incorrect locked status.',
                    as_is=actual_locked_status,
                    to_be=excepted_locked_status
                )
            )
            self.refresh_page()

    def check_docs_send_status(self) -> NoReturn:
        with allure.step('Check change status.'):
            self.find_element(self.common_page_locators.DOCS_SEND_STATUS)
            actual_doc_send_status = self.get_doc_send_status()
            excepted_doc_send_status = 'docs sent'
            assert actual_doc_send_status == excepted_doc_send_status, AssertionError(
                self.error_handler(
                    action='Check doc send status.',
                    error='Incorrect doc send status.',
                    as_is=actual_doc_send_status,
                    to_be=excepted_doc_send_status
                )
            )
            self.refresh_page()

    def login_to_email_service(self, login: str, password: str) -> NoReturn:
        with allure.step('Login to https://mail.tm/'):
            self.find_element(self.common_page_locators.B_ACCOUNT_EMAIL).click()
            self.find_element(self.common_page_locators.B_LOGIN_EMAIL).click()
            self.find_element(self.common_page_locators.B_EMAIL_LOGIN).send_keys(login)
            self.send_keys(locator=self.common_page_locators.B_EMAIL_PASSWORD, keys=[password, Keys.ENTER])

    def click_by_mail(self) -> NoReturn:
        with allure.step('Click by text "Dmitry Drigo via DocuSign"'):
            self.click_elem_by_text('div', 'Dmitry Drigo via DocuSign', 65)

    def get_elem_by_text_review_document(self):
        with allure.step('Check what text is visible "REVIEW DOCUMENTS"'):
            self.get_elem_by_text('span', 'REVIEW DOCUMENTS')

    def get_elem_by_text_mail_text(self):
        with allure.step('Check what text is visible "dmitry.drigo@americor.com"'):
            self.get_elem_by_text('div', 'dmitry.drigo@americor.com')

    def delete_last_email(self) -> NoReturn:
        with allure.step('Delete last email'):
            self.find_element(self.common_page_locators.B_DELETE_EMAIL).click()

    def check_notification(self, name: str, last_name: str, lead_id: str):
        self.click_btn_bell()
        actual_notif_text = self.get_first_notif_text()
        excepted_notif_text = f'{name} {last_name} ({lead_id}) has been assigned to you'
        assert actual_notif_text == excepted_notif_text, AssertionError(
            self.error_handler(
                action='Check notification text.',
                error='Incorrect notification.',
                as_is=actual_notif_text,
                to_be=excepted_notif_text
            )
        )

    def sign_docusign_docs(self, url: str) -> NoReturn:
        with allure.step('Sign docusign Docs.'):
            self.get_page(url)
            time.sleep(2)
            self.click_cb_docusign_term_of_service()
            self.click_btn_docusign_next()
            self.click_btn_docusign_start()

            # Первый раз подписываем в pop up
            self.click_btn_docusign_sign_arrow()
            time.sleep(2)
            self.click_btn_docusign_sign_acceptance()
            time.sleep(2)

            self.click_btn_docusign_start()
            self.click_btn_go_next_signature()
            while self.element_is_present(self.common_page_locators.B_CLICK_HERE_TO_SIGN):
                try:
                    self.click_btn_click_here_to_sign()
                except StaleElementReferenceException:
                    self.waiting_for_page_loaded()
                except ElementClickInterceptedException:
                    self.waiting_for_page_loaded()
            time.sleep(10)
            # пока заполняем вручную так как docusign нестабильно работает

            self.click_btn_docusign_sign_final()
            self.click_btn_docusign_submit()

    def search_applicant(self, search_text: str, many: bool = False) -> str | list:
        with allure.step('Search and get searching result.'):
            self.click_btn_search()
            self.fill_field_search(search_text=search_text)
            return self.get_search_result(many=many)

    def check_search_result(self, actual_result: str, expected_result: str) -> NoReturn:
        with allure.step('Checking search result.'):
            if isinstance(actual_result, str):
                assert expected_result in actual_result, AssertionError(
                    self.error_handler(
                        action='Checking main search result.',
                        error='Excepted search result data not equal actual data.',
                        as_is=actual_result,
                        to_be=expected_result
                    )
                )
            if isinstance(actual_result, list):
                flag = False
                for i in actual_result:
                    if expected_result in i:
                        flag = True
                if not flag:
                    raise AssertionError(
                        self.error_handler(
                            action='Checking main search result in list.',
                            error='Excepted search result data not equal actual data.',
                            as_is=actual_result,
                            to_be=expected_result
                        )
                    )

    def check_customer_id_and_name(self, customer_id: str, name: str) -> NoReturn:
        with allure.step('Click by result.'):
            self.click_by_found_user()
            self.waiting_for_page_loaded()
            expected_title = f"{name} ({customer_id})".lower()
            actual_title = self.get_internal_page_title().lower()
            assert expected_title.lower() == actual_title, AssertionError(
                self.error_handler(
                    action='Checking the compliance of the search data with the data in the profile',
                    error='Excepted search result data not equal profile data.',
                    as_is=actual_title,
                    to_be=expected_title
                )
            )

    def check_valid_link(self, customer_id: str) -> NoReturn:
        url = self.get_current_page_url()
        assert customer_id in url, AssertionError(
            self.error_handler(
                action='Checking valid link from main search.',
                error='Incorrect customer id in url.',
                as_is=url,
                to_be=customer_id
            )
        )


class CommonBrokersPageBlocks(CommonPage):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver)
        self.cfg = cfg
        self.base_url = cfg.common['url']
        self.url_api = cfg.common['url_api']
        self.url_broker = cfg.common['url_brokers']

    def success_or_error_check(self, action: str = None, t: int = 3) -> str:
        with allure.step('Check error notifications.'):
            success = self.common_page_locators.T_SUCCESS
            error = self.common_page_locators.ET_ERROR

            if self.element_is_present(locator=error, t=t):
                raise Exception(self.error_handler(action=action, error=self.get_text(error)))
            if self.element_is_present(locator=success, t=t):
                success_text = self.get_text(success)
                with allure.step(f'Get success notification: {success_text}.'):
                    return success_text

    def open_page(
            self,
            page: str,
            client_id: str = '',
            title: bool = False,
            internal_title: bool = False,
    ) -> str:
        url = self.url_broker + getattr(pages_details, page).ENDPOINT_BROKER + client_id
        with allure.step(f'Open page: {url}.'):
            self.get_page(url)
            self.highlight_and_make_screenshot()
            if not page == 'Password':
                self.close_all_hints()
            if internal_title:
                excepted_title = getattr(pages_details, page).TITLE
                self.check_page_internal_title(title=excepted_title)
            if title:
                excepted_title = getattr(pages_details, page).TITLE
                with allure.step(f'Checking {page} page title.'):
                    current_title = self.check_page_title(title=excepted_title)
                with allure.step(f'{page} page title is correct: {current_title}'):
                    return current_title

    def check_page_console_log_errors(
            self, pages: list[str], client_id: str = '') -> NoReturn:
        with allure.step('Check page console log errors.'):
            errors = {}
            page_without_client = [
                leads_pages.leads, enrollments_pages.enrollments, loans_pages.loans
            ]

            for page in pages:
                if page in page_without_client:
                    self.open_page(page=page)
                else:
                    self.open_page(page=page, client_id=client_id)

                with allure.step(f'Check {page} page errors.'):
                    page_errors = self.check_js_errors(return_errors=True)
                    if page_errors:
                        errors[page] = page_errors

            if errors:
                raise Exception(
                    self.error_handler(
                        page_url=False,
                        action='Checking the logs of the page for errors.',
                        error=errors
                    )
                )

    def close_all_hints(self) -> NoReturn:
        with allure.step('Find and close all toasts.'):
            if self.element_is_present(self.get_locator_by_text('a', ' Close')):
                self.double_click_elem_by_text('a', ' Close')
                self.waiting_for_page_loaded(sleep_time=1)

    def check_page_internal_title(self, title: str) -> NoReturn:
        with allure.step(f'Checking {title} page internal title.'):
            current_title = self.get_internal_page_title()
            assert current_title == title, AssertionError(
                self.error_handler(
                    action='Check internal page title.',
                    error='Incorrect internal page',
                    as_is=current_title,
                    to_be=title
                )
            )
        with allure.step(f'{title} page internal title is correct: {title}'):
            pass

    def confirmation(self, confirm: bool = True) -> NoReturn:
        with allure.step('Confirmation in pop-up.'):
            time.sleep(2)
            if confirm:
                self.click_btn_confirm()
            if not confirm:
                self.click_btn_cancel()
            self.waiting_for_page_loaded()

    def saving(self) -> NoReturn:
        with allure.step('Saving.'):
            self.click_btn_save()
            self.success_or_error_check()
