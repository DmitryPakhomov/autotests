import random
from typing import NoReturn

import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.data.loans_data import LoansAchData
from autotests.pages.data.main_data import Configs
from autotests.pages.pages.loans_pages.loan_ach_page.loan_ach_page_common_actions import \
    LoansAchPageCommonActions
from autotests.pages.pages.loans_pages.loan_ach_page.loan_ach_page_fill_actions import \
    LoansAchPageFillActions
from autotests.pages.pages.loans_pages.loan_ach_page.loan_ach_page_get_actions import \
    LoansAchPageGetActions


class LoanAchPageBlocks(LoansAchPageCommonActions, LoansAchPageGetActions, LoansAchPageFillActions):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.cfg = cfg

    def fill_ach_fields(
            self,
            name_of_account: str = 'Carol Turner',
            routing_number: str = '256074974',
            account_number: int = random.randint(10000000, 1000000000),
            bank_name: str = 'NAVY FEDERAL CREDIT UNION',
            bank_phone_number: str = '866-214-5220',
            bank_address: str = '820 FOLLIN LANE',
            bank_city: str = 'VIENNA',
            bank_state: str = 'VA',
            bank_zip: str = '22180',
    ) -> LoansAchData:
        with allure.step('Fill ACH fields.'):
            self.fill_routing_number(routing_number=routing_number)
            self.click_btn_routing_number_search_ach()
            self.fill_bank_account_number(account_number=account_number)
            self.fill_bank_account_number_re_enter(account_number=account_number)
            self.fill_name_of_account(name_of_account=name_of_account)
            self.saving()
            self.success_or_error_check()
            self.highlight_and_make_screenshot()
            return LoansAchData(
                name_of_account=name_of_account,
                routing_number=routing_number,
                account_number=account_number,
                bank_name=bank_name,
                bank_phone_number=bank_phone_number,
                bank_address=bank_address,
                bank_city=bank_city,
                bank_state=bank_state,
                bank_zip=bank_zip,
            )

    def check_all_fields_ach(self, excepted_data: LoansAchData) -> NoReturn:
        actual_data = self.get_ach_data()
        assert actual_data == excepted_data, AssertionError(
            self.error_handler(
                action='Checking ACH data after saving.',
                error='Excepted ACH data not equal actual data.',
                as_is=actual_data,
                to_be=excepted_data
            )
        )

    def get_ach_data(self) -> LoansAchData:
        with allure.step('Get ach data.'):
            return LoansAchData(
                name_of_account=self.get_name_of_account(),
                routing_number=self.get_routing_number(),
                account_number=self.get_bank_account_number(),
                bank_name=self.get_bank_name(),
                bank_phone_number=self.get_bank_phone_number(),
                bank_address=self.get_bank_address(),
                bank_city=self.get_bank_city(),
                bank_state=self.get_bank_state(),
                bank_zip=self.get_bank_zip(),
            )

    def sending_ach_docs(self, sending_type: str) -> NoReturn:
        with allure.step('Send Docs.'):
            self.close_all_hints()
            self.click_btn_ach_send_docs()
            self.click_btn_sending_type(sending_type=sending_type)
            self.success_or_error_check(timeout=4)
            self.confirmation()
            self.success_or_error_check(timeout=4)
            self.highlight_and_make_screenshot()
