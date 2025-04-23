from typing import NoReturn


from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.loans_pages_blocks.loans_common_page_blocks import LoansCommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import LoansACH
from autotests.pages.utils import click_btn


class LoansAchPageCommonActions(LoansCommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loans_ach_locators = LoansACH.Locators

    @click_btn('Routing number search ACH')
    def click_btn_routing_number_search_ach(self) -> NoReturn:
        self.click_element(self.loans_ach_locators.B_ROUTING_NUMBER_SEARCH)

    @click_btn('Send docs')
    def click_btn_ach_send_docs(self) -> NoReturn:
        self.wait_until_element_not_visible(self.loans_ach_locators.B_SEND_DOCS).click()

    def click_btn_ach_sending_type(self, sending_type: str) -> NoReturn:
        with allure.step(f'Click on the button "{sending_type}".'):
            self.click_elem_by_text('a', sending_type)
