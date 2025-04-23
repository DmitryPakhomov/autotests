from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.loans_pages_blocks.loans_common_page_blocks import LoansCommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import LoansProfile
from autotests.pages.utils import click_btn


class LoansProfilePageCommonActions(LoansCommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loans_main_locators = LoansProfile.Locators

    @click_btn('Delete mobile phone')
    def delete_m_phone(self):
        self.click_element(self.loans_main_locators.F_PHONE_MOBILE_APPLICANT)
