from selenium.webdriver.chrome.webdriver import WebDriver
from autotests.pages.pages.loans_pages.loans_page.loans_page import LoansPage
from autotests.pages.data.main_data import Configs


class LoansPageBlocks(LoansPage):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
    pass
