from selenium.webdriver.chrome.webdriver import WebDriver
from autotests.pages.pages.loans_pages.loan_plan_page.loan_plan_page_common_actions import \
    LoansPlanPageCommonActions
from autotests.pages.data.main_data import Configs


class LoanPlanPageBlocks(LoansPlanPageCommonActions):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.common_action = LoansPlanPageCommonActions(self.driver, self.cfg)
