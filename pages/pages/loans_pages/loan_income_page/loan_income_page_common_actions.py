from typing import NoReturn

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from autotests.pages.blocks.loans_pages_blocks.loans_common_page_blocks import LoansCommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import LoansIncome
from autotests.pages.utils import click_btn, get_value, choose_elem


class LoansIncomePageCommonActions(LoansCommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loans_income_page_locators = LoansIncome.Locators

    @click_btn('Income Source')
    def click_btn_add_income_source(self) -> NoReturn:
        self.click_element(self.loans_income_page_locators.B_ADD_INCOME_SOURCE)

    @get_value('Get added income count')
    def get_added_income_count(self) -> int:
        return len(self.find_element(
            self.loans_income_page_locators.T_INCOME_SOURCE_HEADERS, many=True))

    @click_btn('Mark as Primary')
    def click_toggle_mark_as_primary(self, count: int) -> NoReturn:
        self.click_element((
            By.CSS_SELECTOR, self.loans_income_page_locators.TG_MARK_AS_PRIMARY.format(count=count))
        )

    @click_btn('Mark as Primary first element')
    def click_toggle_mark_as_primary_first(self) -> NoReturn:
        self.click_elem_by_text('label', 'Mark as Primary')

    @click_btn('Status')
    def click_dl_status(self, count: int) -> NoReturn:
        self.click_element((
            By.CSS_SELECTOR, self.loans_income_page_locators.DL_STATUS.format(count=count)))

    @click_btn('Primary Source Of Income')
    def click_dl_primary_source_of_income(self, count: int) -> NoReturn:
        self.click_element((
            By.CSS_SELECTOR,
            self.loans_income_page_locators.DL_PRIMARY_SOURCE_OF_INCOME.format(count=count))
        )

    @click_btn('Occupation')
    def click_dl_occupation(self, count: int) -> NoReturn:
        self.click_element((
            By.CSS_SELECTOR, self.loans_income_page_locators.DL_OCCUPATION.format(count=count)))

    @choose_elem('Status income')
    def select_status_income(self, status: int):
        elem = self.find_element(self.loans_income_page_locators.DL_STATUS)
        elem.click()
        for _ in range(status):
            elem.send_keys(Keys.ARROW_DOWN)
        elem.send_keys(Keys.ENTER)

    @click_btn('Verified the information')
    def click_verified(self) -> NoReturn:
        self.click_elem_by_text('button', 'I verified the information')
        self.waiting_for_page_loaded()

    def click_completed(self) -> NoReturn:
        self.wait_until_element_to_be_clickable(self.loans_income_page_locators.B_COMPLETED)
        self.click_elem_by_text('a', 'Completed')
        self.waiting_for_page_loaded()
