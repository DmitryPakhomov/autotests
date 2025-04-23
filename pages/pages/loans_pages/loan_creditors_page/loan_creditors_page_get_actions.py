from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.loans_pages_blocks.loans_common_page_blocks import LoansCommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import LoansCreditors
from autotests.pages.utils import get_value, str_to_bool


class LoansCreditorsPageGetActions(LoansCommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loans_creditors_page_locators = LoansCreditors.Locators

    @get_value('Account holder')
    def get_account_holder(self) -> int:
        account_holder_rb_value = self.get_attribute(
            self.loans_creditors_page_locators.RB_ACCOUNT_HOLDER_CHECKED, attr_name='checked')
        return 1 if account_holder_rb_value else 2

    @get_value('Cardholder name')
    def get_cardholder_name(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_INPUT_CREDITOR_CARDHOLDER_NAME, attr_name='value')

    @get_value('Debt type')
    def get_debt_type(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_DEBT_TYPE_CHECKED, attr_name='title')

    @get_value('Status')
    def get_status(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_STATUS_CHECKED, attr_name='title')

    @get_value('Creditor status')
    def get_status_creditor_editing_creditor(self) -> int:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_STATUS_CHECKED, attr_name='title')

    @get_value('Priority')
    def get_priority(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_PRIORITY_CHECKED, attr_name='title')

    @get_value('Disposition')
    def get_disposition(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_DISPOSITION_CHECKED, attr_name='title')

    @get_value('Sum. Admin Disposition')
    def get_admin_disposition(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_SUM_ADMIN_DISPOSITION_CHECKED, attr_name='title')

    @get_value('Negotiator')
    def get_negotiator(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_NEGOTIATOR_CHECKED, attr_name='title')

    @get_value('Summons Admin')
    def get_summons_admin(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_SUMMONS_ADMIN_CHECKED, attr_name='title')

    @get_value('SIF Retrieval Admin')
    def get_retrieval_admin(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_RETRIEVAL_ADMIN_CHECKED, attr_name='title')

    @get_value('Past Due')
    def get_past_due(self) -> int:
        return int(self.get_attribute(
            self.loans_creditors_page_locators.F_PAST_DUE_CHECKED, attr_name='value'))


    @get_value('Cycle date')
    def get_cycle_date(self) -> int:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_CYCLE_DATE_CHECKED, attr_name='value')

    @get_value('Charge off date')
    def get_charge_off_date(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_CHARGE_OFF_DATE_CHECKED, attr_name='value')

    @get_value('Settlement letter due')
    def get_settlement_letter_due(self) -> str | None:
        self.wait_until_element_visible(
            self.loans_creditors_page_locators.F_INPUT_CREDITOR_SETTLEMENT_LETTER_DUE)
        return self.get_attribute(
            self.loans_creditors_page_locators.F_INPUT_CREDITOR_SETTLEMENT_LETTER_DUE,
            attr_name='value'
        )

    @get_value('Settlement balance')
    def get_settlement_balance(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_SETTLEMENT_BALANCE_CHECKED, attr_name='value'
        )[2: -3]

    @get_value('Settlement payment date')
    def get_settlement_payment_date(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_SETTLEMENT_PAYMENT_DATE_CHECKED, attr_name='value')

    @get_value('Original creditor')
    def get_original_creditor(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_ORIGINAL_CREDITOR_CHECKED, attr_name='title')

    @get_value('Account #')
    def get_original_account(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_ORIGINAL_ACCOUNT_CHECKED, attr_name='value')

    @get_value('POA Sent')
    def get_original_poa_sent(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_ORIGINAL_POA_SENT_CHECKED, attr_name='title')

    @get_value('Current creditor')
    def get_current_creditor(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_CURRENT_CREDITOR_CHECKED, attr_name='title')

    @get_value('Current account')
    def get_current_account(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_CURRENT_ACCOUNT_CHECKED, attr_name='value')

    @get_value('Current POA sent')
    def get_current_poa_sent(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_CURRENT_POA_SENT_CHECKED, attr_name='title')

    @get_value('Original Balance')
    def get_original_balance(self) -> int:
        return int(self.get_attribute(
            self.loans_creditors_page_locators.F_ORIGINAL_BALANCE_CHECKED, attr_name='value'
        )[2: -3])

    @get_value('Current Balance')
    def get_current_balance(self) -> int:
        return int(self.get_attribute(
            self.loans_creditors_page_locators.F_CURRENT_BALANCE_CHECKED, attr_name='value')[2: -3])

    @get_value('Address')
    def get_address(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_ADDRESS_CHECKED, attr_name='value')

    @get_value('State')
    def get_state(self) -> str:
        return self.get_text(self.loans_creditors_page_locators.F_STATE_CHECKED)

    @get_value('FAX')
    def get_fax(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_FAX_CHECKED, attr_name='value')

    @get_value('Contact name')
    def get_contact_name(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_CONTACT_NAME_CHECKED, attr_name='value')

    @get_value('Address 2')
    def get_address2(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_ADDRESS_2CHECKED, attr_name='value')

    @get_value('ZIP')
    def get_zip(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_ZIP_CHECKED, attr_name='value')

    @get_value('Pay to')
    def get_pay_to(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_PAY_TO_CHECKED, attr_name='value')

    @get_value('Contact Phone')
    def get_contact_phone(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_CONTACT_PHONE_CHECKED, attr_name='value')

    @get_value('City')
    def get_city(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_CITY_CHECKED, attr_name='value')

    @get_value('Phone')
    def get_phone(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_PHONE_CHECKED, attr_name='value')

    @get_value('Creditor name')
    def get_creditor_name(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_CREDITOR_NAME_CHECKED, attr_name='value')

    @get_value('Payment Notes')
    def get_payment_notes(self) -> str:
        return self.get_attribute(
            self.loans_creditors_page_locators.F_PAYMENT_NOTES_CHECKED, attr_name='value')

    # offers
    @get_value('Offer status')
    def get_offer_status_in_offer_tab(self) -> str:
        return self.get_text(
            self.loans_creditors_page_locators.E_STATUS_SETTLEMENT_OFFER, lower=True)

    @get_value('Presence of Disabled status offer')
    def check_dl_status_disabled_offer(self) -> bool:
        status_disabled = self.get_attribute(
            self.loans_creditors_page_locators.E_OFFER_STATUSES, attr_name='aria-disabled')
        return str_to_bool(status_disabled)

    @get_value('Presence of Button Save and Add payments')
    def check_button_save_offer_disabled_offer(self) -> bool:
        return self.element_is_clickable(
            self.loans_creditors_page_locators.
            B_CREDITORS_SETTLEMENT_OFFER_OVERRIDE_SAVE_ADD_PAYMENTS
        )

    @get_value('Presence of Disabled toggle accepted in offer')
    def check_tg_accepted_disabled_offer(self) -> bool:
        return self.element_is_clickable(self.loans_creditors_page_locators.TG_ACCEPTED)

    @get_value('Getting status offer on Creditors payments page')
    def get_status_offer_payments_creditor(self) -> str:
        return self.get_text(
            self.loans_creditors_page_locators.E_STATUS_OFFER_PAYMENTS_CREDITOR, lower=True)

    @get_value('Getting unaccepted date Creditors payments page')
    def get_unaccepted_date_payments_creditor(self) -> str:
        return self.get_text(self.get_locator_by_text('div', 'Unaccepted date:'))

    @get_value('Getting payments status in creditor')
    def get_payments_status_payments_creditor(self) -> list[str]:
        return self.get_text(
            locator=self.loans_creditors_page_locators.E_STATUS_PAYMENT_PAYMENTS_CREDITOR,
            many=True,
            lower=True
        )

    @get_value('Getting settlement fee payments status in creditor')
    def get_settlement_fee_payments_status_payments_creditor(self) -> list[str]:
        return self.get_text(
            self.loans_creditors_page_locators.E_STATUS_SETTLEMENT_FEE_PAYMENT_PAYMENTS_CREDITOR,
            many=True,
            lower=True
        )
