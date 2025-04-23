from selenium.webdriver.chrome.webdriver import WebDriver
from autotests.pages.pages.loans_pages.loan_payments_page.loan_payments_page_common_actions import \
    LoansPaymentsPageCommonActions
from autotests.pages.data.main_data import Configs


class LoanPaymentsPageBlocks(LoansPaymentsPageCommonActions):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.common_action = LoansPaymentsPageCommonActions(self.driver, self.cfg)

