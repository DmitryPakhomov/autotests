from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.loans_pages_blocks.loans_common_page_blocks import LoansCommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import LoansACH
from autotests.pages.utils import get_value


class LoansAchPageGetActions(LoansCommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loans_ach_locators = LoansACH.Locators

    @get_value('Name of account')
    def get_name_of_account(self) -> str:
        return str(self.get_attribute(self.loans_ach_locators.F_NAME_OF_ACCOUNT, attr_name='value'))

    @get_value('Routing number')
    def get_routing_number(self) -> str:
        return str(self.get_attribute(self.loans_ach_locators.F_ROUTING_NUMBER, attr_name='value'))

    @get_value('Account number')
    def get_bank_account_number(self) -> int:
        return int(self.get_attribute(self.loans_ach_locators.F_BANK_ACCOUNT_NUMBER, attr_name='value'))

    @get_value('Bank name')
    def get_bank_name(self) -> str:
        return self.get_attribute(self.loans_ach_locators.F_BANK_NAME_ACH, attr_name='value')

    @get_value('Bank phone number')
    def get_bank_phone_number(self) -> str:
        return self.get_attribute(self.loans_ach_locators.F_BANK_PHONE_NUMBER_ACH, attr_name='value')

    @get_value('Bank address')
    def get_bank_address(self) -> str:
        return self.get_attribute(self.loans_ach_locators.F_BANK_ADDRESS_ACH, attr_name='value')

    @get_value('Bank city')
    def get_bank_city(self) -> str:
        return self.get_attribute(self.loans_ach_locators.F_BANK_CITY_ACH, attr_name='value')

    @get_value('Bank state')
    def get_bank_state(self) -> str:
        return self.get_attribute(self.loans_ach_locators.F_BANK_STATE_ACH, attr_name='value')

    @get_value('Bank zip')
    def get_bank_zip(self) -> str:
        return self.get_attribute(self.loans_ach_locators.F_BANK_ZIP_ACH, attr_name='value')
