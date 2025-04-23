import random
from typing import NoReturn

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.loans_pages_blocks.loans_common_page_blocks import LoansCommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import LoansCreditors
from autotests.pages.utils import click_elem, check_visibility_elem, fill_field, click_dl, choose


class LoansCreditorsPageFillActions(LoansCommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loan_creditors_page_locators = LoansCreditors.Locators

    @click_elem('Creditor in list')
    def click_last_creditor(self) -> NoReturn:
        self.wait_until_element_not_visible(
            self.loan_creditors_page_locators.T_ROW_CREDITOR).click()

    @check_visibility_elem('Creditor form')
    def wait_until_form_creditor_is_not_visible(self) -> NoReturn:
        self.wait_until_element_not_visible(self.loan_creditors_page_locators.F_DEBT_TYPE).click()

    @fill_field('Cardholder name')
    def fill_cardholder_name(self, cardholder_name: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_CARDHOLDER_NAME,
            keys=[cardholder_name]
        )

    @fill_field('Debt type')
    def fill_debt_type(self, debt_type: str) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.F_DEBT_TYPE)
        self.click_elem_by_text('li', debt_type)

    @fill_field('Settlement letter due')
    def fill_settlement_letter_due(self, settlement_letter_due: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_SETTLEMENT_LETTER_DUE,
            keys=[settlement_letter_due])
        self.click_elem_by_text('label', 'Charge Off Date')

    @fill_field('Settlement Balance')
    def fill_settlement_balance(self, settlement_balance: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_SETTLEMENT_BALANCE,
            keys=[settlement_balance]
        )

    @fill_field('Settlement Payment Date')
    def fill_settlement_payment_date(self, settlement_payment_date: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_SETTLEMENT_BALANCE_DATE,
            keys=[settlement_payment_date]
        )

    @fill_field('Creditor')
    def fill_creditor_field(self, creditor: str) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.F_INPUT_CREDITOR_COMPANY)
        self.click_elem_by_text('strong', creditor, 4)

    @fill_field('Account')
    def fill_creditors_account(self, account: str) -> NoReturn:
        self.send_keys(self.loan_creditors_page_locators.F_INPUT_CREDITOR_ACCOUNT, keys=[account])

    @fill_field('Original balance')
    def fill_original_balance(self, original_balance: int) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_ORIGINAL_BALANCE,
            keys=[original_balance]
        )

    @fill_field('Current balance')
    def fill_current_balance(self, current_balance: int) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_CURRENT_BALANCE,
            keys=[current_balance]
        )

    @fill_field('Account')
    def fill_current_creditors_account(self, account: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CURRENT_CREDITOR_ACCOUNT, keys=[account])

    @click_dl('Status')
    def click_status(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.F_STATUS)

    @choose('Status')
    def choose_status(self, status: str) -> NoReturn:
        self.click_elem_by_text('li', status)

    @click_dl('Priority')
    def click_priority(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.F_PRIORITY)

    @choose('Priority')
    def choose_priority(self, priority: str):
        self.click_elem_by_text('li', priority)

    @click_dl('Disposition')
    def click_disposition(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.F_DISPOSITION)

    @choose('Disposition')
    def choose_disposition(self, disposition: str):
        self.click_elem_by_text('li', disposition)

    @click_dl('Admin disposition')
    def click_admin_disposition(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.F_ADMIN_DISPOSITION)

    @choose('Admin disposition')
    def choose_admin_disposition(self, admin_disposition: str) -> NoReturn:
        self.click_elem_by_text('li', admin_disposition)

    @click_dl('Negotiator')
    def click_negotiator(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.F_ADMIN_NEGOTIATOR)

    @choose('Negotiator')
    def choose_negotiator(self, negotiator: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_ADMIN_NEGOTIATOR_INPUT, keys=[negotiator])
        self.click_elem_by_text('li', negotiator)

    @click_dl('Summons Admin')
    def click_summons_admin(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.F_ADMIN_SUMMONS)

    @choose('Summons Admin')
    def choose_summons_admin(self, summons_admin: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_ADMIN_SUMMONS_INPUT, keys=[summons_admin])
        self.click_elem_by_text('li', summons_admin)

    @click_dl('SIF Retrieval Admin')
    def click_retrieval_admin(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.F_ADMIN_SIF)

    @choose('SIF Retrieval Admin')
    def choose_retrieval_admin(self, retrieval_admin: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_ADMIN_SIF_INPUT, keys=[retrieval_admin])
        self.click_elem_by_text('li', retrieval_admin)

    @fill_field('Past due')
    def fill_past_due(self, past_due: int) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_PAST_DUE, keys=[past_due])


    @fill_field('Cycle date')
    def fill_cycle_date(self, cycle_date: int) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CYCLE_DATE, keys=[cycle_date])

    @fill_field('Charge Off Date')
    def fill_charge_off_date(self, charge_off_date: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_CHANGE_OFF_DATE,
            keys=[charge_off_date]
        )

    @click_dl('POA Sent')
    def click_poa_sent(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.F_INPUT_CREDITOR_POA_SEND)

    @choose('POA Sent')
    def choose_poa_sent(self, poa_sent: str) -> NoReturn:
        self.click_elem_by_text('li', poa_sent)

    @click_dl('Current POA Sent')
    def click_current_poa_sent(self) -> NoReturn:
        self.click_element(self.loan_creditors_page_locators.F_INPUT_CURRENT_CREDITOR_POA_SEND)

    @choose('Current POA Sent')
    def choose_current_poa_sent(self, current_poa_sent: str) -> NoReturn:
        self.click_elem_by_text('li', current_poa_sent)

    @fill_field('Address')
    def fill_address(self, address: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_OVERRIDE_ADDRESS, keys=[address])

    @fill_field('Select state')
    def select_state(self, state: str = None):
        self.select_element(
            locator=self.loan_creditors_page_locators.F_INPUT_CREDITOR_OVERRIDE_STATE,
            text=state
        )

    @fill_field('State')
    def fill_state(self, state: str = None) -> NoReturn:
        elem = self.find_element(self.loan_creditors_page_locators.F_INPUT_CREDITOR_OVERRIDE_STATE)
        elem.click()
        states = [
            'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA',
            'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT',
            'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI',
            'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'
        ]

        state_index = states.index(state) + 1 if state else random.randint(1, len(states) + 1)

        for _ in range(state_index):
            elem.send_keys(Keys.ARROW_DOWN)

    @click_dl('Fax')
    def click_fax(self) -> NoReturn:
        self.click_elem_by_text('label', 'Fax')

    @choose('Fax')
    def choose_fax(self, fax: str):
        self.send_keys(self.loan_creditors_page_locators.F_INPUT_CREDITOR_OVERRIDE_FAX, keys=[fax])

    @click_dl('Contact Name')
    def click_contact_name(self) -> NoReturn:
        self.click_elem_by_text('label', 'Contact Name')

    @choose('Contact_name')
    def choose_contact_name(self, contact_name: str):
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_OVERRIDE_CONTACT_NAME,
            keys=[contact_name]
        )

    @fill_field('Address2')
    def fill_address2(self, address2: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_OVERRIDE_ADDRESS2,
            keys=[address2]
        )

    @fill_field('Zip')
    def fill_zip(self, zip_code: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_OVERRIDE_ZIP, keys=[zip_code])

    @fill_field('Pay To')
    def fill_pay_to(self, pay_to: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_OVERRIDE_PAY_TO, keys=[pay_to])

    @fill_field('Contact Phone')
    def fill_contact_phone(self, contact_phone: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_OVERRIDE_CONTACT_PHONE,
            keys=[contact_phone]
        )

    @fill_field('City')
    def fill_city(self, city: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_OVERRIDE_CITY, keys=[city])

    @fill_field('Phone')
    def fill_phone(self, phone: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_OVERRIDE_PHONE, keys=[phone])

    @fill_field('Creditor Name')
    def fill_creditor_name(self, creditor_name: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_OVERRIDE_CREDITOR_NAME,
            keys=[creditor_name]
        )

    @fill_field('Payment Notes')
    def fill_payment_notes(self, payment_notes: str) -> NoReturn:
        self.send_keys(
            self.loan_creditors_page_locators.F_INPUT_CREDITOR_OVERRIDE_PAYMENT_NOTES,
            keys=[payment_notes]
        )

    # settlement offers
    @fill_field('Contact Person')
    def fill_contact_person_creditor_offer(self, contact_name: str) -> NoReturn:
        self.click_elem_by_text('label', 'Contact Person')
        self.send_keys(
            LoansCreditors.Locators.F_CONTACT_PERSON_CREDITOR_OFFER, keys=[contact_name])

    @fill_field('Contact Phone')
    def fill_contact_phone_creditor_offer(self, contact_phone: str) -> NoReturn:
        self.click_elem_by_text('label', 'Contact Phone')
        self.send_keys(
            LoansCreditors.Locators.F_CONTACT_PHONE_CREDITOR_OFFER, keys=[contact_phone])

    @fill_field('First settlement date')
    def fill_first_settlement_date_offer(self, value: str) -> NoReturn:
        self.send_keys(
            locator=self.loan_creditors_page_locators.F_FIRST_SETTLEMENT_DATE_CREDITOR_OFFER,
            keys=[value]
        )

    @fill_field('Number of Month fee')
    def fill_nbr_of_month_fee_offer_details(self, value) -> NoReturn:
        self.send_keys(
            locator=self.loan_creditors_page_locators.F_NBR_OF_MONTH_FEE,
            keys=[Keys.BACK_SPACE, value]
        )

    @fill_field('Select offer status')
    def select_offer_status(self, value: str = None):
        self.select_element(
            locator=self.loan_creditors_page_locators.DL_STATUSES,
            text=value
        )

    @fill_field('Offer status')
    def fill_dl_search_status_creditor_offer(self, value: str) -> NoReturn:
        self.find_element(
            self.loan_creditors_page_locators.DL_STATUSES_INPUT).send_keys(value)

    def fill_dl_search_status_creditor_offer_enter(self) -> NoReturn:
        self.find_element(
            self.loan_creditors_page_locators.DL_STATUSES_INPUT).send_keys(Keys.ENTER)
