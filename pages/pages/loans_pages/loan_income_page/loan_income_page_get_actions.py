from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from autotests.pages.data.main_data import Configs
from autotests.pages.pages.loans_pages.loans_common_page.loans_common_page import LoansCommonPage
from autotests.pages.pages_details import LoansIncome
from autotests.pages.utils import str_to_bool, get_value


class LoanIncomePageGetActions(LoansCommonPage):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loans_income_page_locators = LoansIncome.Locators

    @get_value('Remove')
    def get_remove_btn_elements(self) -> list[WebElement]:
        return self.find_element(self.loans_income_page_locators.B_REMOVE, many=True)

    def wait_until_status_dl_visible(self):
        self.wait_until_element_not_visible(self.loans_income_page_locators.DL_STATUS)

    @get_value('Primary value')
    def get_mark_as_primary(self, count: int) -> bool:
        mark = self.get_attribute(
            (By.ID, self.loans_income_page_locators.T_MARK_AS_PRIMARY.format(count=count)),
            attr_name='data-switchery-reset-value'
        )
        return str_to_bool(mark)

    @get_value('Status')
    def get_status(self, count: int) -> str:
        return self.get_attribute(
            (By.ID, self.loans_income_page_locators.T_STATUS.format(count=count)), attr_name='title'
        )

    @get_value('Occupation')
    def get_occupation(self, count: int) -> str:
        return self.get_attribute(
            (By.ID, self.loans_income_page_locators.T_OCCUPATION.format(count=count)),
            attr_name='title'
        )

    @get_value('Primary Source')
    def get_primary_source_of_income(self, count: int) -> str:
        return self.get_attribute(
            (By.ID, self.loans_income_page_locators.T_PRIMARY_SOURCE_OF_INCOME.format(count=count)),
            attr_name='title'
        )

    @get_value('Company name')
    def get_company_name(self, count: int) -> str:
        return self.get_attribute(
            (By.CSS_SELECTOR, self.loans_income_page_locators.F_COMPANY_NAME.format(count=count)),
            attr_name='value'
        )

    @get_value('Company address')
    def get_company_address(self, count: int) -> str:
        return self.get_attribute(
            (
                By.CSS_SELECTOR,
                self.loans_income_page_locators.F_COMPANY_ADDRESS.format(count=count)
            ),
            attr_name='value'
        )

    @get_value('Company city')
    def get_company_city(self, count: int) -> str:
        return self.get_attribute(
            (By.CSS_SELECTOR, self.loans_income_page_locators.F_COMPANY_CITY.format(count=count)),
            attr_name='value'
        )

    @get_value('Company state')
    def get_company_state(self, count: int) -> str:
        return self.get_attribute(
            (
                By.CSS_SELECTOR,
                self.loans_income_page_locators.F_COMPANY_STATE_FORM.format(count=count)
            ),
            attr_name='title'
        )

    @get_value('company ZIP')
    def get_company_zip(self, count: int) -> str:
        return self.get_attribute(
            (By.CSS_SELECTOR, self.loans_income_page_locators.F_COMPANY_ZIP.format(count=count)),
            attr_name='value'
        )

    @get_value('Additional Phone (Work)')
    def get_additional_phone_work(self, count: int) -> str:
        return self.get_attribute(
            (
                By.CSS_SELECTOR,
                self.loans_income_page_locators.F_PHONE_WORK_ADDITIONAL.format(count=count)
            ),
            attr_name='value'
        )

    @get_value('Gross monthly')
    def get_gross_monthly_income(self, count: int) -> str:
        return self.get_attribute(
            (
                By.CSS_SELECTOR,
                self.loans_income_page_locators.F_GROSS_MONTHLY_INCOME.format(count=count)
            ),
            attr_name='value'
        )[0: -3]

    @get_value('w2income')
    def get_w2income(self, count: int) -> str:
        return self.get_attribute(
            (By.CSS_SELECTOR, self.loans_income_page_locators.F_W2INCOME.format(count=count)),
            attr_name='value'
        )[0: -3]

    @get_value('Type of pay')
    def get_type_of_pay(self, count: int) -> str:
        return self.get_attribute(
            (
                By.CSS_SELECTOR,
                self.loans_income_page_locators.F_TYPE_OF_PAY_FORM.format(count=count)
            ),
            attr_name='title'
        )

    @get_value('How to calculate')
    def get_how_to_calculate(self, count: int) -> str:
        return self.get_attribute(
            (
                By.CSS_SELECTOR,
                self.loans_income_page_locators.F_HOW_TO_CALCULATE_FORM.format(count=count)),
            attr_name='title'
        )

    @get_value('Bank statement review')
    def get_bank_statements_review_1(self, count: int) -> str:
        return self.get_attribute(
            (
                By.CSS_SELECTOR,
                self.loans_income_page_locators.CB_BANK_STATEMENTS_REVIEW_1_FORM.format(count=count)
            ),
            attr_name='checked'
        )

    @get_value('Negative Balance Detected')
    def get_bank_statements_review_2(self, count: int) -> str:
        return self.get_attribute(
            (
                By.CSS_SELECTOR,
                self.loans_income_page_locators.CB_BANK_STATEMENTS_REVIEW_2_FORM.format(count=count)
            ),
            attr_name='checked'
        )

    @get_value('Borrower`s Primary Account')
    def get_bank_statements_review_3(self, count: int) -> str:
        return self.get_attribute(
            (
                By.CSS_SELECTOR,
                self.loans_income_page_locators.CB_BANK_STATEMENTS_REVIEW_3_FORM.format(count=count)
            ),
            attr_name='checked'
        )

    @get_value('length years')
    def get_length_years(self, count: int) -> str:
        return self.get_attribute(
            (By.CSS_SELECTOR, self.loans_income_page_locators.F_LENGTH_YEARS.format(count=count)),
            attr_name='value'
        )

    @get_value('length months')
    def get_length_months(self, count: int) -> str:
        return self.get_attribute(
            (By.CSS_SELECTOR, self.loans_income_page_locators.F_LENGTH_MONTHS.format(count=count)),
            attr_name='value'
        )

    @get_value('phone (work)')
    def get_phone_work(self, count: int) -> str:
        return self.get_attribute(
            (By.CSS_SELECTOR, self.loans_income_page_locators.F_PHONE_WORK.format(count=count)),
            attr_name='value'
        )

    @get_value('Net Monthly')
    def get_net_monthly_income(self, count: int) -> str:
        return self.get_attribute(
            (
                By.CSS_SELECTOR,
                self.loans_income_page_locators.F_NET_MONTHLY_INCOME.format(count=count)
            ),
            attr_name='value'
        )[0:-3]
