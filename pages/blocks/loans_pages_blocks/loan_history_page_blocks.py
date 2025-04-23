from typing import NoReturn

import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.data.main_data import Configs
from autotests.pages.pages.loans_pages.loan_main_page.loan_main_page_common_actions import \
    LoansMainPageCommonActions
from autotests.pages.pages.loans_pages.loan_main_page.loan_main_page_fill_actions import \
    LoansMainPageFillActions
from autotests.pages.pages.loans_pages.loan_main_page.loan_main_page_get_actions import \
    LoansMainPageGetActions


class LoanHistoryPageBlocks(
    LoansMainPageCommonActions, LoansMainPageFillActions, LoansMainPageGetActions
):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.common_action = LoansMainPageCommonActions(self.driver, self.cfg)
        self.fill_action = LoansMainPageFillActions(self.driver, self.cfg)
        self.get_action = LoansMainPageGetActions(self.driver, self.cfg)

    def check_history_event_create_email(
            self,
            email_text: str,
            subject_text: str,
            attachments: str,
            body_text: bool = False
    ) -> NoReturn:
        with allure.step('Checking of the email in history'):
            self.click_btn_angle_right()
            history_email_subject = self.get_history_email_subject()
            if body_text:
                self.switch_to_iframe(0)
                history_email_text = self.get_history_email_text()
                self.switch_out_iframe()
            if not body_text:
                self.switch_to_iframe(0)
                history_email_text = self.get_history_iframe_email_text()
                self.switch_out_iframe()
                email_attachments = self.get_attachments_iframe_email_text(attachments=attachments)
            assert subject_text == history_email_subject, AssertionError(
                self.error_handler(
                    action='Checking of the note text in history',
                    error='Incorrect note text in history',
                    as_is=subject_text,
                    to_be=history_email_subject
                )
            )
            assert email_text in history_email_text, AssertionError(
                self.error_handler(
                    action='Checking of the note text in history',
                    error='Incorrect note text in history',
                    as_is=history_email_text,
                    to_be=email_text
                )
            )
            if attachments:
                assert email_attachments is not None, AssertionError(
                    self.error_handler(
                        action='Checking attachments in email',
                        error='Incorrect attachments in history',
                        as_is=email_attachments,
                        to_be=attachments
                    )
                )
        self.highlight_and_make_screenshot()

    def sending_email(self, email_text: str, subject_text: str, attachments: bool) -> NoReturn:
        with allure.step('Creating New Email.'):
            self.click_btn_create_email()
            self.fill_email_field_subject(subject_text)
            self.fill_email_field_body(email_text)
            if attachments:
                self.fill_email_attachments()
            self.click_btn_save_modal()
            self.success_or_error_check()

    def check_history_event_download_document(self, text: str, subject_text: str) -> NoReturn:
        with allure.step('Checking of the message in history'):
            self.click_btn_angle_right()
            history_message_subject = self.get_history_event_subject()
            get_history_event_content = self.get_history_event_content()
            assert subject_text in history_message_subject, AssertionError(
                self.error_handler(
                    action='Checking of the subject text in history',
                    error='Incorrect note text in history',
                    as_is=history_message_subject,
                    to_be=subject_text
                )
            )
            for text in get_history_event_content:
                assert text in get_history_event_content, AssertionError(
                    self.error_handler(
                        action='Checking of the note text in history',
                        error='Incorrect note text in history',
                        as_is=get_history_event_content,
                        to_be=text
                    )
                )
        self.highlight_and_make_screenshot()

    def fill_do_not_contact_sms_loan(self) -> NoReturn:
        with allure.step('SMS to toggle on'):
            self.click_btn_do_not_contact()
            self.click_toggle_sms_to()
            self.click_btn_reassign_save()
            self.waiting_for_page_loaded(10)

    def check_sms_button_disable_loan(self) -> NoReturn:
        with allure.step('SMS button disable check'):
            enabled_value = self.find_element(self.loans_main_locators.B_SMS_DISABLED).is_enabled()
            assert enabled_value, AssertionError(
                self.error_handler(
                    action='Checking button SMS',
                    error='Button SMS is enabled',
                    as_is=enabled_value,
                    to_be=False
                )
            )
