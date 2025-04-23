import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.data.main_data import Configs
from autotests.pages.pages.loans_pages.loan_profile_page.loan_profile_page_common_actions import \
    LoansProfilePageCommonActions
from autotests.pages.pages.loans_pages.loan_profile_page.loan_profile_page_fill_actions import \
    LoansProfilePageFillActions
from autotests.pages.pages.loans_pages.loan_profile_page.loan_profile_page_get_actions import \
    LoansProfilePageGetActions


class LoanProfilePageBlocks(
    LoansProfilePageCommonActions, LoansProfilePageFillActions, LoansProfilePageGetActions
):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.common_action = LoansProfilePageCommonActions(self.driver, self.cfg)
        self.fill_action = LoansProfilePageFillActions(self.driver, self.cfg)
        self.get_action = LoansProfilePageGetActions(self.driver, self.cfg)

    def delete_mobile_phone_loan(self):
        with allure.step('Delete mobile phone'):
            self.delete_m_phone()
            self.click_via_js(self.find_element(self.common_page_locators.B_SAVE))
            self.waiting_for_page_loaded(10)
