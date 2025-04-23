import random
from typing import NoReturn

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from autotests.pages.data.main_data import Configs
from autotests.pages.pages.loans_pages.loans_common_page.loans_common_page import LoansCommonPage
from autotests.pages.pages_details import LoansIncome
from autotests.pages.utils import fill_field, click_dl, choose


class LoanIncomePageFillActions(LoansCommonPage):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loan_income_page_locators = LoansIncome.Locators

    @fill_field('Company name')
    def fill_company_name(self, count: int, name: str) -> NoReturn:
        self.send_keys(
            (By.CSS_SELECTOR, self.loan_income_page_locators.F_COMPANY_NAME.format(count=count)),
            keys=[name]
        )

    @fill_field('Company address')
    def fill_company_address(self, count: int, company_address: str) -> NoReturn:
        self.send_keys(
            (By.CSS_SELECTOR, self.loan_income_page_locators.F_COMPANY_ADDRESS.format(count=count)),
            keys=[company_address]
        )

    @fill_field('Company city')
    def fill_company_city(self, count: int, city: str) -> NoReturn:
        self.send_keys(
            (By.CSS_SELECTOR, self.loan_income_page_locators.F_COMPANY_CITY.format(count=count)),
            keys=[city]
        )

    @fill_field('Zip')
    def fill_company_zip(self, count: int, company_zip: str) -> NoReturn:
        self.send_keys(
            (By.CSS_SELECTOR, self.loan_income_page_locators.F_COMPANY_ZIP.format(count=count)),
            keys=[company_zip]
        )

    @fill_field('State')
    def fill_company_state(self, count: int, state: str = None) -> NoReturn:
        elem = self.find_element((
            By.CSS_SELECTOR, self.loan_income_page_locators.F_COMPANY_STATE.format(count=count)))
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
        elem.send_keys(Keys.ENTER)

    @fill_field('Length Years')
    def fill_length_years(self, count: int, length_years: str) -> NoReturn:
        self.send_keys(
            (By.CSS_SELECTOR, self.loan_income_page_locators.F_LENGTH_YEARS.format(count=count)),
            keys=[length_years]
        )

    @fill_field('Length Months')
    def fill_length_months(self, count: int, length_months: str) -> NoReturn:
        self.send_keys(
            (By.CSS_SELECTOR, self.loan_income_page_locators.F_LENGTH_MONTHS.format(count=count)),
            keys=[length_months]
        )

    @fill_field('Phone (Work)')
    def fill_phone_work(self, count: int, phone: str) -> NoReturn:
        self.send_keys(
            (By.CSS_SELECTOR, self.loan_income_page_locators.F_PHONE_WORK.format(count=count)),
            keys=[phone]
        )

    @fill_field('Additional phon work')
    def fill_additional_phone_work(self, count: int, additional_phone_work: str) -> NoReturn:
        self.send_keys(
            (
                By.CSS_SELECTOR,
                self.loan_income_page_locators.F_PHONE_WORK_ADDITIONAL.format(count=count)
            ),
            keys=[additional_phone_work]
        )

    @fill_field('Net Monthly Income')
    def fill_net_monthly_income(self, count: int, net_monthly_income: str) -> NoReturn:
        self.send_keys(
            (
                By.CSS_SELECTOR,
                self.loan_income_page_locators.F_NET_MONTHLY_INCOME.format(count=count)
            ),
            keys=[net_monthly_income]
        )

    @fill_field('Gross Monthly Income')
    def fill_gross_monthly_income(self, count: int, gross_monthly_income: str) -> NoReturn:
        self.send_keys(
            (
                By.CSS_SELECTOR,
                self.loan_income_page_locators.F_GROSS_MONTHLY_INCOME.format(count=count)
            ),
            keys=[gross_monthly_income]
        )

    @fill_field('w2income')
    def fill_w2income(self, count: int, w2income: str) -> NoReturn:
        self.send_keys(
            (By.CSS_SELECTOR, self.loan_income_page_locators.F_W2INCOME.format(count=count)),
            keys=[w2income]
        )

    @fill_field('Type of pay')
    def click_type_of_pay(self, count: int) -> NoReturn:
        self.click_element(
            (By.CSS_SELECTOR, self.loan_income_page_locators.F_TYPE_OF_PAY.format(count=count)))

    @choose('Type of pay')
    def choose_type_of_pay(self, type_of_pay: str) -> NoReturn:
        self.click_elem_by_text('li', type_of_pay)

    @click_dl('How to calculate')
    def click_how_to_calculate(self, count: int) -> NoReturn:
        self.click_element((
            By.CSS_SELECTOR, self.loan_income_page_locators.F_HOW_TO_CALCULATE.format(count=count)))

    @choose('How to calculate')
    def choose_how_to_calculate(self, how_to_calculate: str) -> NoReturn:
        self.click_elem_by_text('li', how_to_calculate)

    @fill_field('Bank statements review 1')
    def fill_bank_statements_review_1(self, count: int) -> NoReturn:
        self.click_element((
            By.CSS_SELECTOR,
            self.loan_income_page_locators.CB_BANK_STATEMENTS_REVIEW_1.format(count=count)
        ))

    @fill_field('Bank statements review 2')
    def fill_bank_statements_review_2(self, count: int) -> NoReturn:
        self.click_element((
            By.CSS_SELECTOR,
            self.loan_income_page_locators.CB_BANK_STATEMENTS_REVIEW_2.format(count=count)
        ))

    @fill_field('Bank statements review 3')
    def fill_bank_statements_review_3(self, count: int) -> NoReturn:
        self.click_element((
            By.CSS_SELECTOR,
            self.loan_income_page_locators.CB_BANK_STATEMENTS_REVIEW_3.format(count=count)
        ))

    @fill_field('Gross Monthly Income and Gross Annual Income')
    def fill_gross_monthly(self, gross_monthly_income: int) -> NoReturn:
        self.send_keys(
            self.loan_income_page_locators.F_GROSS_MONTHLY_INCOME,
            keys=[gross_monthly_income, Keys.ENTER]
        )
