from typing import NoReturn


from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.data.loans_data import LoansCreditorsSettlementOfferData, \
    loans_settlement_offer_statuses, loans_creditor_statuses, LoansCreditorsAllData, \
    loans_creditor_debt_type, loans_creditor_status, loans_creditor_priority, \
    loans_creditor_disposition, loans_creditor_admin_disposition, LoansCreditorsMainData, \
    loans_creditor_poa_send, LoansCreditorsOriginalCreditorData, LoansCreditorsCurrentCreditorData, \
    LoansCreditorsOverrideAddressData
from autotests.pages.data.main_data import Configs
from autotests.pages.data.test_data import TestData
from autotests.pages.pages.loans_pages.loan_creditors_page.loan_creditors_page_common_actions import \
    LoansCreditorsPageCommonActions
from autotests.pages.pages.loans_pages.loan_creditors_page.loan_creditors_page_fill_actions import \
    LoansCreditorsPageFillActions
from autotests.pages.pages.loans_pages.loan_creditors_page.loan_creditors_page_get_actions import \
    LoansCreditorsPageGetActions
from autotests.pages.utils import get_current_date


class LoanCreditorsPageBlocks(
    LoansCreditorsPageCommonActions, LoansCreditorsPageFillActions, LoansCreditorsPageGetActions
):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.common_action = LoansCreditorsPageCommonActions(self.driver, self.cfg)

    def create_loans_creditors(
            self,
            enrollment_id: str,
            account_holder: int,
            debt_type: str,
            creditor: str,
            account: str,
            settlement_letter_due: str,
            current_balance: int

    ) -> NoReturn:
        """
        Метод для создания записи в Creditors.
        """
        with allure.step('Go to page Deal profile and create new creditors record.'):
            self.open_page(page='LoansCreditors', client_id=enrollment_id)
            self.check_js_errors()
            self.click_btn_create_new_creditor()
            if account_holder == 1:
                self.fill_account_holder_applicant()
            if account_holder == 2:
                self.fill_account_holder_coapplicant()
            self.fill_debt_type(debt_type=debt_type)
            self.fill_settlement_letter_due(settlement_letter_due=settlement_letter_due)
            self.fill_creditor_field(creditor=creditor)
            self.fill_creditors_account(account=account)
            self.fill_current_balance(current_balance=current_balance)
            self.click_btn_save()
            self.waiting_for_page_loaded()
            self.success_or_error_check()

    def add_document_with_type_settlement_letter(self) -> NoReturn:
        with allure.step('Added new documents.'):
            self.waiting_for_page_loaded()
            self.click_documents_tab()
            self.upload_documents_in_tabs()
            self.select_type_in_tabs('Settlement Letter')
            self.click_btn_upload()
            self.waiting_for_page_loaded()

    def add_document_with_type_settlement_letter_to_offer(self) -> NoReturn:
        self.click_documents_tab_settlemet_offer()
        self.upload_documents_to_settlement_offer()
        self.select_type_of_file_settlement_offer('Settlement Letter')
        self.click_btn_upload()
        # Remove sleep_time after CRM-3865 will be fixed:
        self.waiting_for_page_loaded(sleep_time=5)
        self.click_elem_by_text('a', 'Offer Details', 5)
        self.waiting_for_page_loaded()
        self.save_settlement_offer()
        expected_text = 'successfully saved'
        result_text = self.success_or_error_check()
        assert expected_text in result_text, AssertionError(
            self.error_handler(
                action='Successfully saved pop-up',
                error='Pop-up not Successfully saved',
                as_is=result_text,
                to_be=expected_text
            )
        )
        self.highlight_and_make_screenshot()
        self.waiting_for_page_loaded()

    def checking_offer_create_error_if_previous_offer_active(self) -> NoReturn:
        with allure.step('Try to add 2nd settlement offer and get error'):
            self.click_tab_settlement_offers_creditor()
            self.click_create_new_settlement_offer_item()
            self.fill_settlement_offer_data()
            self.click_btn_save_settlement_offer()
            error_text = self.success_or_error_text()
            expected_text = 'Errors: A previous offer is currently active, ' \
                            'please review or cancel previous offer'
            assert expected_text == error_text, AssertionError(
                self.error_handler(
                    action='Successfully saved pop-up',
                    error='Pop-up not Successgully saved',
                    as_is=error_text,
                    to_be=expected_text
                )
            )
            self.highlight_and_make_screenshot()

    def create_settlement_offer(self) -> NoReturn:
        with allure.step('Add new settlement offer.'):
            self.click_tab_settlement_offers_creditor()
            self.click_create_new_settlement_offer_item()
            self.fill_settlement_offer_data()
            self.save_settlement_offer()
            self.check_validation_error_in_tab()
            expected_text = 'successfully saved'
            result_text = self.success_or_error_check()
            assert expected_text in result_text, AssertionError(
                self.error_handler(
                    action='Successfully saved pop-up',
                    error='Pop-up not Successgully saved',
                    as_is=result_text,
                    to_be=expected_text
                )
            )
            self.highlight_and_make_screenshot()
            self.waiting_for_page_loaded()

    def fill_settlement_offer_data(
            self,
            nbr_of_month=1,
            first_settlement_date=TestData.get_date(7),
            contact_person=TestData.first_name(),
            contact_phone=TestData.phone_for_sms_consent(),
    ) -> LoansCreditorsSettlementOfferData:
        with allure.step('Fill settlement offer section.'):
            self.fill_nbr_of_month_fee_offer_details(nbr_of_month)
            self.fill_first_settlement_date_offer(first_settlement_date)
            self.fill_contact_person_creditor_offer(contact_person)
            self.fill_contact_phone_creditor_offer(contact_phone)
            return LoansCreditorsSettlementOfferData(
                nbr_of_month=nbr_of_month,
                contact_person=contact_person,
                contact_phone=contact_phone,
                first_settlement_date=first_settlement_date
            )

    def check_not_active_status_offer(self, value) -> NoReturn:
        self.click_dl_status_creditor_offer()
        self.fill_dl_search_status_creditor_offer(value=value)
        aria_disabled_value = self.check_not_clickable_dl_status_settlement_offer()
        assert aria_disabled_value == 'true', AssertionError(
            self.error_handler(
                action='Offer status not clickable in DL list',
                error='Status is not disabled',
                as_is=aria_disabled_value,
                to_be=True
            )
        )
        self.click_dl_status_creditor_offer()

    def check_settlement_offer(self) -> NoReturn:
        with allure.step('Check settlement offer.'):
            # check offer in tab
            self.click_on_offer_again()
            self.check_not_active_status_offer(loans_settlement_offer_statuses.accepted)
            self.check_not_active_status_offer(loans_settlement_offer_statuses.deleted)

    def change_status_offer(self, value) -> NoReturn:
        with allure.step(f'Change offer status to {value}'):
            self.click_tab_settlement_offers_creditor()
            self.click_on_offer_again()
            self.click_dl_status_creditor_offer()
            self.fill_dl_search_status_creditor_offer(value=value)
            self.fill_dl_search_status_creditor_offer_enter()
            self.save_settlement_offer()
            self.waiting_for_page_loaded()

    def check_button_save_override_in_cancelled_status_offer(self) -> NoReturn:
        assert not self.element_is_present(
            self.loans_creditors_page_locators.B_OVERRIDE_ERRORS
        ), AssertionError(self.error_handler(
            action='Check button save is not showing',
            error='The Save button is showing'
        )
        )

    def check_cancelled_offer(self) -> NoReturn:
        with allure.step(f'Check {loans_settlement_offer_statuses.cancelled} offer.'):
            expected_offer_status = loans_settlement_offer_statuses.cancelled.lower()
            offer_status = self.get_offer_status_in_offer_tab()
            assert expected_offer_status in offer_status, AssertionError(
                self.error_handler(
                    action='Checking of the offer status',
                    error='Incorrect offer status',
                    as_is=offer_status,
                    to_be=expected_offer_status
                )
            )
            self.click_on_offer_again()
            self.check_button_save_override_in_cancelled_status_offer()
            self.save_settlement_offer()

    def check_disposition(self, value: str) -> NoReturn:
        self.wait_until_element_not_visible(
            self.loans_creditors_page_locators.F_SETTLEMENT_AMOUNT)
        val = self.get_attribute(self.loans_creditors_page_locators.F_DISPOSITION_2,
                                 attr_name='title')
        assert val == value, AssertionError(
            self.error_handler(
                action='Compare status',
                error='Excepted Creditors section data not equal actual data.',
                as_is=val,
                to_be=value
            )
        )

    def check_letter_due(self) -> NoReturn:
        date_due = self.get_attribute(
            self.loans_creditors_page_locators.F_SETTELMENT_DUE, attr_name='value')
        assert date_due != '', 'Settlement Letter Due should be higher'

    def check_settlement_letter_due_in_offer(self, value) -> NoReturn:
        date_due = self.get_attribute(
            self.loans_creditors_page_locators.F_SETTELMENT_LETTER_DUE_OFFER,
            attr_name='value'
        )
        assert date_due == value, AssertionError(
            self.error_handler(
                action='Check settlement letter due in settlement offer',
                error='Settlement Letter not valid',
                as_is=date_due,
                to_be=value
            )
        )

    def check_status_need_sif_letter_offer(self) -> NoReturn:
        with allure.step(f'Check {loans_settlement_offer_statuses.need_sif_letter} status.'):
            expected_offer_status = loans_settlement_offer_statuses.need_sif_letter.lower()
            offer_status = self.get_offer_status_in_offer_tab().lower()
            assert expected_offer_status in offer_status, AssertionError(
                self.error_handler(
                    action='Checking of the offer status',
                    error='Incorrect offer status',
                    as_is=offer_status,
                    to_be=expected_offer_status
                )
            )
            self.click_tab_acct_information_creditor()
            self.check_disposition('Waiting for Settlement Letter')
            self.check_letter_due()

    def check_status_need_cl_auth_offer(self) -> NoReturn:
        with allure.step(f'Check {loans_settlement_offer_statuses.need_client_auth} status.'):
            expected_offer_status = loans_settlement_offer_statuses.need_client_auth.lower()
            offer_status = self.get_offer_status_in_offer_tab().lower()
            assert expected_offer_status in offer_status, AssertionError(
                self.error_handler(
                    action='Checking of the offer status',
                    error='Incorrect offer status',
                    as_is=offer_status,
                    to_be=expected_offer_status
                )
            )
            self.click_tab_acct_information_creditor()
            self.check_disposition('Pending client approval')

    def check_need_acceptance_state(self) -> NoReturn:
        with allure.step(f'Check {loans_settlement_offer_statuses.need_acceptance} status.'):
            expected_offer_status = loans_settlement_offer_statuses.need_acceptance.lower()
            offer_status = self.get_offer_status_in_offer_tab().lower()
            assert expected_offer_status in offer_status, AssertionError(
                self.error_handler(
                    action='Checking of the offer status',
                    error='Incorrect offer status',
                    as_is=offer_status,
                    to_be=expected_offer_status
                )
            )

    def accepting_settlement_offer(self) -> NoReturn:
        with allure.step(
                f'Change offer status to {loans_settlement_offer_statuses.accepted}'):
            self.click_btn_override_save_and_add_payments_settlement_offer()
            self.confirmation()
            self.success_or_error_check()
            self.highlight_and_make_screenshot()
            self.waiting_for_page_loaded()

    def check_status_accepted_offer(self) -> NoReturn:
        with allure.step('Check override errors acceptance status.'):
            expected_offer_status = loans_settlement_offer_statuses.accepted.lower()
            offer_status = self.get_offer_status_in_offer_tab().lower()
            assert expected_offer_status in offer_status, AssertionError(
                self.error_handler(
                    action='Checking of the offer status',
                    error='Incorrect offer status',
                    as_is=offer_status,
                    to_be=expected_offer_status
                )
            )
            self.click_on_offer_again()
            state_status_disabled = self.check_dl_status_disabled_offer()
            assert state_status_disabled, AssertionError(
                self.error_handler(
                    action='Checking that dl statuses in offer disabled',
                    error='Dl for changing statuses is not disable',
                    as_is=state_status_disabled,
                    to_be=True
                )
            )
            self.save_settlement_offer()

    def turn_off_acceptance_state(self) -> NoReturn:
        with allure.step('Check turn off acceptance state.'):
            self.click_acceptance_toggle()
            self.save_settlement_offer()
            self.check_validation_error_in_tab()
            expected_text = 'successfully saved'
            result_text = self.success_or_error_check()
            assert expected_text in result_text, AssertionError(
                self.error_handler(
                    action='Successfully saved pop-up',
                    error='Pop-up not Successfully saved',
                    as_is=result_text,
                    to_be=expected_text
                )
            )
            self.waiting_for_page_loaded()
            self.highlight_and_make_screenshot()
            expected_offer_status = loans_settlement_offer_statuses.draft.lower()
            offer_status = self.get_offer_status_in_offer_tab()
            assert expected_offer_status in offer_status, AssertionError(
                self.error_handler(
                    action='Checking of the offer status',
                    error='Incorrect offer status',
                    as_is=offer_status,
                    to_be=expected_offer_status
                )
            )

    def delete_settlement_offer(self) -> NoReturn:
        with allure.step('Delete settlement offer.'):
            self.click_delete_offer()
            self.confirmation()
            self.waiting_for_page_loaded()
            self.check_validation_error_in_tab()
            self.success_or_error_check()
            self.highlight_and_make_screenshot()

    def check_offer_in_deleted_status(self) -> NoReturn:
        with allure.step('Check deleted offer.'):
            # acct information:
            self.click_tab_acct_information_creditor()
            settlement_letter_due = self.get_settlement_letter_due()
            status_creditor = self.get_status_creditor_editing_creditor()
            assert settlement_letter_due == '', AssertionError(
                self.error_handler(
                    action='Checking that date settlement letter due is empty',
                    error='Date settlement letter due is not empty',
                    as_is=settlement_letter_due,
                )
            )
            assert status_creditor == loans_creditor_statuses.in_progress, AssertionError(
                self.error_handler(
                    action=f'Checking that status creditor is '
                           f'{loans_creditor_statuses.in_progress}',
                    error=f'Status creditor is not {loans_creditor_statuses.in_progress}',
                    as_is=status_creditor,
                    to_be=loans_creditor_statuses.in_progress
                )
            )

            # offer tab:
            self.click_tab_settlement_offers_creditor()
            row_offer_status = self.get_offer_status_in_offer_tab()
            assert not self.check_btn_delete_not_present(), AssertionError(
                self.error_handler(
                    action='Checking that btn Delete is not Present',
                    error='Btn Delete is present',
                )
            )
            assert 'deleted' in row_offer_status, AssertionError(
                self.error_handler(
                    action='Checking that row Offer status has status "deleted"',
                    error='The row Offer status has not status "deleted"',
                    as_is=row_offer_status,
                    to_be='Offer deleted by ...'
                )
            )

            # offer:
            self.click_on_offer_again()
            state_of_dl_status = self.check_dl_status_disabled_offer()
            state_of_button_save_offer = self.check_button_save_offer_disabled_offer
            state_of_tg_accepted = self.check_tg_accepted_disabled_offer()
            assert state_of_dl_status, AssertionError(
                self.error_handler(
                    action='Checking that dl statuses in offer disabled',
                    error='Dl for changing statuses is not disable',
                    as_is=f'dl status is {state_of_dl_status}',
                )
            )
            assert not state_of_button_save_offer, AssertionError(
                self.error_handler(
                    action='Checking that button save offer is not present',
                    error='Button Save present in Deleted offer',
                    as_is=f'Button Save is {state_of_button_save_offer}'
                )
            )
            assert not state_of_tg_accepted, AssertionError(
                self.error_handler(
                    action='Checking that toggle Accepted offer disabled',
                    error='Toggle Accepted not disabled',
                    as_is=f'Toggle Accepted is {state_of_tg_accepted}'
                )
            )
            self.click_btn_cancel_settlement_offer()

            # payments tab
            self.click_tab_payments_creditor()
            text_status_offer = self.get_status_offer_payments_creditor()
            unaccepted_date = self.get_unaccepted_date_payments_creditor()
            date_now = get_current_date().strftime("%m/%d/%Y")
            assert 'unaccepted' == text_status_offer, AssertionError(
                self.error_handler(
                    action='Checking that status Unaccepted on payments page',
                    error='Not found text Unaccepted',
                    as_is=f'Text status is: {text_status_offer}',
                    to_be='Unaccepted'
                )
            )
            assert date_now in unaccepted_date, AssertionError(
                self.error_handler(
                    action='Checking Unaccepted date on payments page',
                    error='Wrong unaccepted date',
                    as_is=f'Unaccepted date is: {unaccepted_date}',
                    to_be=date_now
                )
            )
            payments_statuses = self.get_payments_status_payments_creditor()
            for status in payments_statuses:
                assert 'void' == status, AssertionError(
                    self.error_handler(
                        action='Checking that payment status is void',
                        error='Payment status is not void',
                        as_is=f'Text status is: {status}',
                        to_be='void'
                    )
                )
            self.click_elem_by_text('a', 'Settlement Fees')
            sf_payments_statuses = self.get_settlement_fee_payments_status_payments_creditor()
            for status in sf_payments_statuses:
                assert 'void' == status, AssertionError(
                    self.error_handler(
                        action='Checking that payment status is void',
                        error='Payment status is not void',
                        as_is=f'Text status is: {status}',
                        to_be='void'
                    )
                )
            self.click_elem_by_text('button', '×')

    def fill_and_save_settlement_letter_due(self, settlement_due):
        self.fill_settlement_letter_due(settlement_due)
        self.creditor_save()
        self.wait_after_saving_creditor()

    def fill_all_creditor_data(self) -> LoansCreditorsAllData:
        with allure.step('Fill Creditors fields.'):
            main_data = self.fill_main_data()
            original_creditor_data = self.fill_original_creditor_data()
            current_creditor_data = self.fill_current_creditor_data()
            override_address_data = self.fill_override_address_data()
            self.creditor_save()
            self.check_validation_error_in_tab()
            self.highlight_and_make_screenshot()
            self.wait_after_saving_creditor()
            return LoansCreditorsAllData(
                main_data=main_data,
                original_creditor_data=original_creditor_data,
                current_creditor_data=current_creditor_data,
                override_address_data=override_address_data,
            )

    def fill_main_data(
            self,
            account_holder=TestData.digits(1, 2),
            cardholder_name=TestData.first_name(),
            debt_type: str = loans_creditor_debt_type.business_credit_card,
            status: str = loans_creditor_status.collections,
            priority: str = loans_creditor_priority.bankruptcy,
            disposition: str = loans_creditor_disposition.account,
            admin_disposition=loans_creditor_admin_disposition.account_settled,
            negotiator='Dmitry Drigo (Irvine)',
            summons_admin='Dmitry Drigo (Irvine)',
            retrieval_admin='Mauro Chavez',
            past_due=TestData.digits(2, 12),
            cycle_date=(TestData.digits(1, 3)),
            charge_off_date=TestData.date(mask='%m/%d/%Y', start=2020, end=2021),
            settlement_balance=str(TestData.digits(200, 500)),
            settlement_payment_date=TestData.date(mask='%m/%d/%Y', start=2020, end=2021),
    ) -> LoansCreditorsMainData:
        with allure.step('Go to page Deal profile and create new creditors record.'):
            if account_holder == 1:
                self.fill_account_holder_applicant()
            if account_holder == 2:
                self.fill_account_holder_coapplicant()
            self.fill_cardholder_name(cardholder_name=cardholder_name)
            self.fill_debt_type(debt_type=debt_type)
            self.fill_status_creditors(status=status)
            self.fill_priority_creditors(priority=priority)
            self.fill_disposition_creditors(disposition=disposition)
            self.fill_admin_disposition_creditors(admin_disposition=admin_disposition)
            self.fill_negotiator_creditors(negotiator=negotiator)
            self.fill_summons_admin_creditors(summons_admin=summons_admin)
            self.fill_retrieval_admin_creditors(retrieval_admin=retrieval_admin)
            self.fill_past_due(past_due=past_due)
            # self.fill_scrublist_last_match(scrublist_last_match=scrublist_last_match)
            self.fill_cycle_date(cycle_date=cycle_date)
            self.fill_charge_off_date(charge_off_date=charge_off_date)
            self.fill_settlement_balance(settlement_balance=settlement_balance)
            self.fill_settlement_payment_date(settlement_payment_date=settlement_payment_date)
            return LoansCreditorsMainData(
                account_holder=account_holder,
                cardholder_name=cardholder_name,
                debt_type=debt_type,
                status=status,
                priority=priority,
                disposition=disposition,
                admin_disposition=admin_disposition,
                negotiator=negotiator,
                summons_admin=summons_admin,
                retrieval_admin=retrieval_admin,
                past_due=past_due,
                cycle_date=cycle_date,
                charge_off_date=charge_off_date,
                settlement_balance=settlement_balance,
                settlement_payment_date=settlement_payment_date
            )

    def fill_original_creditor_data(
            self,
            creditor='1ST FRANKLIN FINANCIAL (ID 31799)',
            account=str(TestData.digits(20000, 25000)),
            original_balance=TestData.digits(200, 500),
            current_balance=TestData.digits(200, 500),
            poa_sent: str = loans_creditor_poa_send.americor,
    ) -> LoansCreditorsOriginalCreditorData:
        with allure.step('Fill the monthly debt expenses fields.'):
            self.fill_creditor_field(creditor=creditor)
            self.fill_creditors_account(account=account)
            self.fill_original_balance(original_balance=original_balance)
            self.fill_current_balance(current_balance=current_balance)
            self.fill_poa_sent_creditors(poa_sent=poa_sent)
            return LoansCreditorsOriginalCreditorData(
                creditor=creditor,
                account=account,
                original_balance=original_balance,
                current_balance=current_balance,
                poa_sent=poa_sent,
            )

    def fill_current_creditor_data(
            self,
            current_creditor='1ST FRANKLIN FINANCIAL (ID 31799)',
            current_account=str(TestData.digits(20000, 25000)),
            current_poa_sent: str = loans_creditor_poa_send.americor,
    ) -> LoansCreditorsCurrentCreditorData:
        with allure.step('Fill current creditor section.'):
            self.click_current_creditor_field()
            self.choose_current_creditor_value(creditor=current_creditor)
            self.click_current_creditors_account()
            self.choose_current_creditors_account(account=current_account)
            self.fill_current_poa_sent_creditors(current_poa_sent=current_poa_sent)
            return LoansCreditorsCurrentCreditorData(
                current_account=current_account,
                current_creditor=current_creditor,
                current_poa_sent=current_poa_sent,
            )

    def fill_override_address_data(
            self,
            address=str(TestData.address()),
            state='CA',
            fax=str(TestData.phone()),
            contact_name=str(TestData.first_name()),
            address2=str(TestData.address()),
            zip=str(TestData.zip_code()),
            pay_to=str(TestData.digits(200, 500)),
            contact_phone='(225) 225-2255',
            city=TestData.city(),
            phone=str(TestData.phone()),
            creditor_name=str(TestData.first_name()),
            payment_notes=str(TestData.first_name()),
    ) -> LoansCreditorsOverrideAddressData:
        with allure.step('Fill override address section.'):
            self.fill_address(address=address)
            self.select_state(state=state)
            self.fill_fax(fax=fax)
            self.fill_contact_name_creditors(contact_name=contact_name)
            self.fill_address2(address2=address2)
            self.fill_zip(zip_code=zip)
            self.fill_pay_to(pay_to=pay_to)
            self.fill_contact_phone(contact_phone=contact_phone)
            self.fill_city(city=city)
            self.fill_phone(phone=phone)
            self.fill_creditor_name(creditor_name=creditor_name)
            self.fill_payment_notes(payment_notes=payment_notes)
            return LoansCreditorsOverrideAddressData(
                address=address,
                state=state,
                fax=fax,
                contact_name=contact_name,
                address2=address2,
                zip=zip,
                pay_to=pay_to,
                contact_phone=contact_phone,
                city=city,
                phone=phone,
                creditor_name=creditor_name,
                payment_notes=payment_notes
            )

    def check_all_creditors_data(self, all_expected_data: LoansCreditorsAllData) -> NoReturn:
        with allure.step('Check all creditors fields after saving.'):
            all_actual_data = self.get_creditors_data()

            with allure.step('Checking main creditors data.'):
                main_actual_data = all_actual_data.main_data
                main_excepted_data = all_expected_data.main_data
                assert main_actual_data == main_excepted_data, AssertionError(
                    self.error_handler(
                        action='Checking main data.',
                        error='Excepted main not equal actual data.',
                        as_is=main_actual_data,
                        to_be=main_excepted_data
                    )
                )
            with allure.step('Checking original creditors data.'):
                original_creditor_actual_data = all_actual_data.original_creditor_data
                original_creditor_expected_data = all_expected_data.original_creditor_data
                assert original_creditor_actual_data == original_creditor_expected_data, AssertionError(
                    self.error_handler(
                        action='original creditors data.',
                        error='Excepted original creditors data not equal actual data.',
                        as_is=original_creditor_actual_data,
                        to_be=original_creditor_expected_data
                    )
                )
            with allure.step('Checking current_creditor_data.'):
                current_creditor_actual_data = all_actual_data.current_creditor_data
                current_creditor_excepted_data = all_expected_data.current_creditor_data
                assert current_creditor_actual_data == current_creditor_excepted_data, AssertionError(
                    self.error_handler(
                        action='Checking current creditor data.',
                        error='Excepted current creditor data not equal actual data.',
                        as_is=current_creditor_actual_data,
                        to_be=current_creditor_excepted_data
                    )
                )
            with allure.step('Checking override address data.'):
                override_address_actual_data = all_actual_data.override_address_data
                override_address_excepted_data = all_expected_data.override_address_data
                assert override_address_actual_data == override_address_excepted_data, AssertionError(
                    self.error_handler(
                        action='Checking override_address data.',
                        error='Excepted override_address not equal actual data.',
                        as_is=override_address_actual_data,
                        to_be=override_address_excepted_data
                    )
                )

    def get_creditors_data(self) -> LoansCreditorsAllData:
        with allure.step('Get creditors data.'):
            main_data = self.get_main_creditors_data()
            original_creditor_data = self.get_original_creditor_data()
            current_creditor_data = self.get_current_creditor_data()
            override_address_data = self.get_override_address_data()
            return LoansCreditorsAllData(
                main_data=main_data,
                original_creditor_data=original_creditor_data,
                current_creditor_data=current_creditor_data,
                override_address_data=override_address_data,
            )

    def get_main_creditors_data(
            self) -> LoansCreditorsMainData:
        with allure.step('Get main data.'):
            return LoansCreditorsMainData(
                account_holder=self.get_account_holder(),
                cardholder_name=self.get_cardholder_name(),
                debt_type=self.get_debt_type(),
                status=self.get_status(),
                priority=self.get_priority(),
                disposition=self.get_disposition(),
                admin_disposition=self.get_admin_disposition(),
                negotiator=self.get_negotiator(),
                summons_admin=self.get_summons_admin(),
                retrieval_admin=self.get_retrieval_admin(),
                past_due=self.get_past_due(),
                cycle_date=self.get_cycle_date(),
                charge_off_date=self.get_charge_off_date(),
                settlement_balance=self.get_settlement_balance(),
                settlement_payment_date=self.get_settlement_payment_date(),
            )

    def get_original_creditor_data(
            self) -> LoansCreditorsOriginalCreditorData:
        with allure.step('Get original creditor data.'):
            return LoansCreditorsOriginalCreditorData(
                account=self.get_original_account(),
                creditor=self.get_original_creditor(),
                original_balance=self.get_original_balance(),
                current_balance=self.get_current_balance(),
                poa_sent=self.get_original_poa_sent()
            )

    def get_current_creditor_data(
            self) -> LoansCreditorsCurrentCreditorData:
        with allure.step('Get current creditor data.'):
            return LoansCreditorsCurrentCreditorData(
                current_account=self.get_current_account(),
                current_creditor=self.get_current_creditor(),
                current_poa_sent=self.get_current_poa_sent(),
            )

    def get_override_address_data(
            self) -> LoansCreditorsOverrideAddressData:
        with allure.step('Get override address data.'):
            return LoansCreditorsOverrideAddressData(
                address=self.get_address(),
                state=self.get_state(),
                fax=self.get_fax(),
                contact_name=self.get_contact_name(),
                address2=self.get_address2(),
                zip=self.get_zip(),
                pay_to=self.get_pay_to(),
                contact_phone=self.get_contact_phone(),
                city=self.get_city(),
                phone=self.get_phone(),
                creditor_name=self.get_creditor_name(),
                payment_notes=self.get_payment_notes()
            )

    def select_creditors(self) -> NoReturn:
        """
        Метод для выбора нужного значения Creditors из списка и клика по нему для получения сохраненных данных.
        """
        with allure.step('Select last creditor'):
            self.refresh_page()
            self.click_elem_by_text('a', 'Full Creditor List')
            self.click_elem_by_text('th', 'ID')
            self.click_elem_by_text('th', 'ID')
            self.waiting_for_page_loaded()
            self.click_last_creditor()
            self.wait_until_form_creditor_is_not_visible()

    def fill_status_creditors(self, status: str) -> NoReturn:
        self.click_status()
        self.choose_status(status=status)

    def fill_priority_creditors(self, priority: str) -> NoReturn:
        self.click_priority()
        self.choose_priority(priority=priority)

    def fill_disposition_creditors(self, disposition: str) -> NoReturn:
        self.click_disposition()
        self.choose_disposition(disposition=disposition)

    def fill_admin_disposition_creditors(self, admin_disposition: str) -> NoReturn:
        self.click_admin_disposition()
        self.choose_admin_disposition(admin_disposition=admin_disposition)

    def fill_negotiator_creditors(self, negotiator: str) -> NoReturn:
        self.click_negotiator()
        self.choose_negotiator(negotiator=negotiator)

    def fill_summons_admin_creditors(self, summons_admin: str) -> NoReturn:
        self.click_summons_admin()
        self.choose_summons_admin(summons_admin)

    def fill_retrieval_admin_creditors(self, retrieval_admin: str) -> NoReturn:
        self.click_retrieval_admin()
        self.choose_retrieval_admin(retrieval_admin)

    def fill_poa_sent_creditors(self, poa_sent: str) -> NoReturn:
        self.click_poa_sent()
        self.choose_poa_sent(poa_sent=poa_sent)

    def fill_current_poa_sent_creditors(self, current_poa_sent: str) -> NoReturn:
        self.click_current_poa_sent()
        self.choose_current_poa_sent(current_poa_sent=current_poa_sent)

    def fill_contact_name_creditors(self, contact_name: str) -> NoReturn:
        self.click_contact_name()
        self.choose_contact_name(contact_name=contact_name)

    def fill_fax(self, fax: str):
        self.click_fax()
        self.choose_fax(fax=fax)

    def save_settlement_offer(self) -> NoReturn:
        self.click_btn_save_settlement_offer()
        if self.element_is_present(self.common_page_locators.E_CONFIRM_ALERT):
            if self.element_is_displayed(self.common_page_locators.E_CONFIRM_ALERT):
                self.confirmation()
        self.wait_until_element_visible(self.loans_creditors_page_locators.T_ROW_OFFER)

    def click_on_offer_again(self, last_offer: bool = True) -> NoReturn:
        self.click_on_button_sort()
        if last_offer:
            self.click_on_button_sort_minus()
        self.click_on_offer()
        self.wait_until_element_visible(self.loans_creditors_page_locators.E_EDITING_OFFER)
        self.waiting_for_page_loaded()

    def creditor_save(self) -> NoReturn:
        self.click_btn_save_creditors()
        self.wait_until_element_visible(
            self.loans_creditors_page_locators.T_ROW_CREDITOR, 20)
        self.check_validation_error_in_tab()
        expected_text = 'successfully saved'
        result_text = self.success_or_error_check()
        assert expected_text in result_text, AssertionError(
            self.error_handler(
                action='Successfully saved pop-up',
                error='Pop-up not Successfully saved',
                as_is=result_text,
                to_be=expected_text
            )
        )
        self.highlight_and_make_screenshot()
        self.waiting_for_page_loaded()
