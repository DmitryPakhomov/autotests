from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.loans_pages_blocks.loans_common_page_blocks import LoansCommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import LoansProfile
from autotests.pages.utils import get_value


class LoansProfilePageGetActions(LoansCommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loan_profile_page_locators = LoansProfile.Locators

    @get_value('Email')
    def get_email_applicant(self) -> str:
        return self.get_attribute(
            self.loan_profile_page_locators.F_EMAIL_APPLICANT, attr_name='value')

    @get_value('Phone (Mobile)')
    def get_phone_mobile_applicant(self) -> str:
        return self.get_attribute(
            self.loan_profile_page_locators.F_PHONE_MOBILE_APPLICANT, attr_name='value')
