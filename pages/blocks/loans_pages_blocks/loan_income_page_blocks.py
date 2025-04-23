import random
import time
from typing import NoReturn

import allure
from numpy import source
from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.data.loans_data import loans_income_statuses, loans_occupation, \
    loans_type_of_pays, loans_how_to_calculate, loans_bank_statements_review, LoansIncomeData
from autotests.pages.data.main_data import Configs
from autotests.pages.data.test_data import TestData
from autotests.pages.pages.loans_pages.loan_income_page.loan_income_page_common_actions import \
    LoansIncomePageCommonActions
from autotests.pages.pages.loans_pages.loan_income_page. \
    loan_income_page_fill_actions import LoanIncomePageFillActions
from autotests.pages.pages.loans_pages.loan_income_page. \
    loan_income_page_get_actions import LoanIncomePageGetActions
from autotests.pages.utils import get_declension_numbers


class LoanIncomePageBlocks(
    LoansIncomePageCommonActions, LoanIncomePageFillActions, LoanIncomePageGetActions
):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)

    def clean_income_fields(self, count: int):
        self.close_all_hints()
        self.click_toggle_mark_as_primary_first()
        i = 1
        while i <= count:
            self.find_element(self.loans_income_page_locators.B_REMOVE).click()
            time.sleep(1)
            self.confirmation()
            i += 1

    def check_unlock_status(self):
        self.close_all_hints()
        if self.element_is_present(self.loans_income_page_locators.B_UNLOCK):
            self.click_elem_by_text('a', 'Unlock')
            self.success_or_error_check()

    def get_income_count(self) -> int:
        elem = self.loans_income_page_locators.T_INCOME_SOURCE_HEADERS
        count = self.get_added_income_count() if self.element_is_present(elem) else 0
        with allure.step(f'There are {count} income(s).'):
            return count

    def choose_income_status(self, count: int, status: str) -> NoReturn:
        self.click_dl_status(count)
        with allure.step(f'Choose status: {status}.'):
            self.click_elem_by_text('li', status)

    def choose_income_primary_source(self, count: int, source: str) -> NoReturn:
        self.click_dl_primary_source_of_income(count)
        with allure.step(f'Choose primary source: {source}.'):
            self.click_elem_by_text('li', source)

    def choose_income_occupation(self, count: int, occupation: str) -> NoReturn:
        self.click_dl_occupation(count)
        with allure.step(f'Choose occupation: {occupation}.'):
            self.click_elem_by_text('li', occupation)

    def fill_all_income_data(
            self,
            status_income=loans_income_statuses.full_time_employed,
            mark_primary=True,
            primary_source_of_income='',
            occupation=loans_occupation.accountant,
            length_years=str(random.randint(1, 3)),
            length_months=str(random.randint(1, 12)),
            company_name=TestData.words(),
            company_address=TestData.address(),
            city=TestData.city(),
            state='CA',
            company_zip=TestData.zip_code(),
            phone_work=TestData.phone(mask='(###) ###-####'),
            additional_phone_work=TestData.phone(mask='(###) ###-####'),
            net_monthly_income=str(random.randint(10000, 20000)),
            gross_monthly_income=str(random.randint(100, 2000)),
            w2income=str(random.randint(10000, 20000)),
            type_of_pay=loans_type_of_pays.weekly,
            how_to_calculate=loans_how_to_calculate.base,
            bank_statements_review=loans_bank_statements_review.a_borrower_has_direct_deposits

    ) -> LoansIncomeData:
        with allure.step('Fill the income data.'):
            count = self.get_income_count()
            self.click_btn_add_income_source()
            if mark_primary:
                self.click_toggle_mark_as_primary(count=count)
            self.choose_income_status(count=count, status=status_income)
            if status_income not in (
                    loans_income_statuses.unemployed,
                    loans_income_statuses.retired) and occupation:
                self.choose_income_occupation(count=count, occupation=occupation)
            if status_income in (
                    loans_income_statuses.unemployed,
                    loans_income_statuses.retired) and source:
                self.choose_income_primary_source(count=count, source=primary_source_of_income)
            if status_income not in (
                    loans_income_statuses.unemployed,
                    loans_income_statuses.retired) and company_name:
                self.fill_company_name(count=count, name=company_name)
                self.fill_company_address(count=count, company_address=company_address)
                self.fill_company_city(count=count, city=city)
                self.fill_company_state(count=count, state=state)
                self.fill_company_zip(count=count, company_zip=company_zip)
            if length_years:
                self.fill_length_years(count=count, length_years=length_years)
            if length_months:
                self.fill_length_months(count=count, length_months=length_months)
            if phone_work:
                self.fill_phone_work(count=count, phone=phone_work)
            if additional_phone_work:
                self.fill_additional_phone_work(count=count,
                                                additional_phone_work=additional_phone_work)
            if gross_monthly_income:
                self.fill_gross_monthly_income(count=count,
                                               gross_monthly_income=gross_monthly_income)
            if net_monthly_income:
                self.fill_net_monthly_income(count=count, net_monthly_income=net_monthly_income)
            if w2income:
                self.fill_w2income(count=count, w2income=w2income)
            if type_of_pay:
                self.fill_type_of_pay_income(count=count, type_of_pay=type_of_pay)
            if how_to_calculate:
                self.fill_how_to_calculate(count=count, how_to_calculate=how_to_calculate)
            if bank_statements_review:
                if bank_statements_review == 'A Borrower has Direct Deposits':
                    self.fill_bank_statements_review_1(count=count)
                if bank_statements_review == 'Negative Balance Detected':
                    self.fill_bank_statements_review_2(count=count)
                if bank_statements_review == 'Borrower`s Primary Account':
                    self.fill_bank_statements_review_3(count=count)
            time.sleep(1)
            self.saving_income()
            self.click_verified()
            self.click_completed()
            self.confirmation()
            self.check_validation_error_in_tab()
            self.success_or_error_check()
            self.highlight_and_make_screenshot()
            return LoansIncomeData(
                mark_primary=mark_primary,
                status_income=status_income,
                occupation=occupation,
                primary_source_of_income=primary_source_of_income,
                length_years=length_years,
                length_months=length_months,
                company_name=company_name,
                company_address=company_address,
                company_city=city,
                company_state=state,
                company_zip=company_zip,
                phone_work=phone_work,
                additional_phone_work=additional_phone_work,
                gross_monthly_income=gross_monthly_income,
                net_monthly_income=net_monthly_income,
                w2income=w2income,
                type_of_pay=type_of_pay,
                how_to_calculate=how_to_calculate,
                bank_statements_review=bank_statements_review,
            )

    def remove_all_income(self) -> NoReturn:
        with allure.step('Remove all income blocks.'):
            count = self.get_income_count()
            self.wait_until_status_dl_visible()
            if count:
                elems = self.get_remove_btn_elements()
                if elems:
                    for elem in elems:
                        if not elem.get_attribute('style'):
                            elem.click()
                            self.waiting_for_page_loaded()
                            self.click_btn_confirm()

    def get_income_data(self, count: int = 0) -> LoansIncomeData:
        with allure.step(f'Get {get_declension_numbers(count + 1)} income data.'):
            data = LoansIncomeData(
                mark_primary=self.get_mark_as_primary(count=count),
                status_income=self.get_status(count=count),
                occupation=self.get_occupation(count=count),
                primary_source_of_income=self.get_primary_source_of_income(count=count),
                length_years=self.get_length_years(count=count),
                length_months=self.get_length_months(count=count),
                phone_work=self.get_phone_work(count=count),
                net_monthly_income=self.get_net_monthly_income(count=count),
                company_name=self.get_company_name(count=count),
                company_address=self.get_company_address(count=count),
                company_city=self.get_company_city(count=count),
                company_state=self.get_company_state(count=count),
                company_zip=self.get_company_zip(count=count),
                additional_phone_work=self.get_additional_phone_work(count=count),
                gross_monthly_income=self.get_gross_monthly_income(count=count),
                w2income=self.get_w2income(count=count),
                type_of_pay=self.get_type_of_pay(count=count),
                how_to_calculate=self.get_how_to_calculate(count=count),
                bank_statements_review=self.get_bank_statements_review(count=count)
            )
        with allure.step(f'Received {get_declension_numbers(count + 1)} income data: {data}.'):
            return data

    def check_income(self, excepted_income_data: LoansIncomeData, count: int = 0) -> NoReturn:
        actual_income_data = self.get_income_data(count=count)
        assert excepted_income_data == actual_income_data, AssertionError(
            self.error_handler(
                action='Check added income data.',
                error='Expected income data not equal to actual data.',
                to_be=excepted_income_data,
                as_is=actual_income_data
            )
        )
        with allure.step(f'Added income with data: {actual_income_data}.'):
            pass
        self.highlight_and_make_screenshot()

    def adding_income_from_deal(
            self,
            deal_id: str,
            gross_monthly_income: int = random.randint(2000, 2500),
    ) -> NoReturn:
        with allure.step('Go to page lead income.'):
            self.open_page(page='EnrollmentsIncome', client_id=deal_id)
            self.select_status_income(status=4)
            self.fill_gross_monthly(gross_monthly_income=gross_monthly_income)
            self.click_verified()
            self.success_or_error_check()
            self.open_page(page='EnrollmentsIncome', client_id=deal_id)
            self.click_elem_by_text('a', 'Completed')
            time.sleep(2)
            self.confirmation()
            self.highlight_and_make_screenshot(file_name='Fill income')
            self.waiting_for_page_loaded()
            self.success_or_error_check()

    def fill_type_of_pay_income(self, count: int, type_of_pay: str):
        self.click_type_of_pay(count=count)
        self.choose_type_of_pay(type_of_pay=type_of_pay)

    def fill_how_to_calculate(self, count: int, how_to_calculate: str):
        self.click_how_to_calculate(count=count)
        self.choose_how_to_calculate(how_to_calculate=how_to_calculate)

    def get_bank_statements_review(self, count: int):
        val1 = self.get_bank_statements_review_1(count)
        val2 = self.get_bank_statements_review_2(count)
        val3 = self.get_bank_statements_review_3(count)
        if val1:
            return 'A Borrower has Direct Deposits'
        elif val2:
            return 'Negative Balance Detected'
        elif val3:
            return 'Borrower`s Primary Account'
