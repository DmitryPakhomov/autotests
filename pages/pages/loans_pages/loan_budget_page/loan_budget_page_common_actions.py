from typing import NoReturn

from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.loans_pages_blocks.loans_common_page_blocks import LoansCommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import LoansBudget
from autotests.pages.utils import choose, click_dl, choose_elem


class LoansBudgetPageCommonActions(LoansCommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loan_budget_locators = LoansBudget.Locators

    @choose('Hardship reason')
    def select_hardship_reason(self, value: str):
        self.select_element(self.loan_budget_locators.S_HARDSHIP_REASON, text=value)

    @click_dl('Housing')
    def click_dl_housing(self) -> NoReturn:
        self.click_element(self.loan_budget_locators.DL_HOUSING)

    @choose_elem('Housing')
    def choose_housing_type(self, value: str) -> NoReturn:
        self.click_elem_by_text('li', value)

    @click_dl('Grounds Of Exemption For Negative Budget')
    def click_dl_grounds_of_exemption(self) -> NoReturn:
        self.click_element(self.loan_budget_locators.DL_GROUNDS_OF_EXEMPTION)

    @choose_elem('Grounds Of Exemption For Negative Budget')
    def choose_grounds_of_exemption_type(self, value: str) -> NoReturn:
        self.click_elem_by_text('li', value)
