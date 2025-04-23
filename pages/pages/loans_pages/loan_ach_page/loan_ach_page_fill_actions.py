from typing import NoReturn

from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.loans_pages_blocks.loans_common_page_blocks import LoansCommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import LoansACH
from autotests.pages.utils import fill_field


class LoansAchPageFillActions(LoansCommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loans_ach_locators = LoansACH.Locators

    @fill_field('Routing Number')
    def fill_routing_number(self, routing_number: str) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_ROUTING_NUMBER, keys=[routing_number])

    @fill_field('Bank Account Number')
    def fill_bank_account_number(self, account_number: int) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_BANK_ACCOUNT_NUMBER, keys=[account_number])

    @fill_field('Bank Account Number re-enter')
    def fill_bank_account_number_re_enter(self, account_number: int) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_BANK_ACCOUNT_NUMBER_DOUBLE, keys=[account_number])

    @fill_field('Name of Account')
    def fill_name_of_account(self, name_of_account: str) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_NAME_OF_ACCOUNT, keys=[name_of_account])

    @fill_field('Routing number')
    def fill_ach_routing_number(self, routing_number: int) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_ROUTING_NUMBER, keys=[routing_number])

    @fill_field('Bank Account Number')
    def fill_ach_bank_account_number(self, bank_account_number: int) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_BANK_ACCOUNT_NUMBER, keys=[bank_account_number])

    @fill_field('Bank name')
    def fill_ach_bank_name(self, bank_name: str) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_BANK_NAME_ACH, keys=[bank_name])

    @fill_field('Bank phone number')
    def fill_ach_bank_phone_number(self, bank_phone_number: str) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_BANK_PHONE_NUMBER_ACH, keys=[bank_phone_number])

    @fill_field('Bank address')
    def fill_ach_bank_address(self, bank_address: str) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_BANK_ADDRESS_ACH, keys=[bank_address])

    @fill_field('Bank_city')
    def fill_ach_bank_city(self, bank_city: str) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_BANK_CITY_ACH, keys=[bank_city])

    @fill_field('Bank state')
    def fill_ach_bank_state(self, bank_state: str) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_BANK_STATE_ACH, keys=[bank_state])

    @fill_field('Bank zip')
    def fill_ach_bank_zip(self, bank_zip: str) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_BANK_ZIP_ACH, keys=[bank_zip])

    @fill_field('Name on account')
    def fill_ach_name_on_account(self, name_on_account: str) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_NAME_OF_ACCOUNT, keys=[name_on_account])

    @fill_field('Routing Number')
    def fill_routing_number_ach(self, routing_number: str) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_ROUTING_NUMBER, keys=[routing_number])

    @fill_field('Bank Account Number')
    def fill_bank_account_number_ach(self, account_number: int) -> NoReturn:
        self.send_keys(locator=self.loans_ach_locators.F_BANK_ACCOUNT_NUMBER, keys=[account_number])
