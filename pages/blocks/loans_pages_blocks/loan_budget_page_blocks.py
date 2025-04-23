import random
from typing import NoReturn

import allure
from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.data.loans_data import LoansBudgetAllData, \
    LoansBudgetPageMonthlyDebtExpensesData, LoansBudgetHousingData, LoansBudgetUtilitiesData, \
    LoansBudgetTransportationData, LoansBudgetPersonalCareData, LoansBudgetMedicalData, \
    LoansBudgetLegalOrderedData, LoansBudgetOtherData, LoansBudgetGroundsOfExemptionData, \
    LoansBudgetHardshipData, LoansBudgetHousingTypes, LoansPersonalCareData, \
    loans_budget_ground_of_example_types, loans_hardship_reason
from autotests.pages.data.main_data import Configs
from autotests.pages.data.test_data import TestData
from autotests.pages.pages.loans_pages.loan_budget_page.loan_budget_page_common_actions import \
    LoansBudgetPageCommonActions
from autotests.pages.pages.loans_pages.loan_budget_page.loan_budget_page_fill_actions import \
    LoanBudgetPageFillActions
from autotests.pages.pages.loans_pages.loan_budget_page.loan_budget_page_get_actions import \
    LoansBudgetPageGetActions


class LoanBudgetPageBlocks(
    LoansBudgetPageCommonActions,
    LoansBudgetPageGetActions,
    LoanBudgetPageFillActions
):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.cfg = cfg

    def fill_all_budget_data(self) -> LoansBudgetAllData:
        with allure.step('Fill Budget fields.'):
            monthly_debt_expenses_data = self.fill_monthly_debt_expenses_fields()
            housing_data = self.fill_housing_fields()
            utilities_data = self.fill_utilities_fields()
            transportation_data = self.fill_transportation_fields()
            personal_care_data = self.fill_personal_care_fields()
            medical_data = self.fill_medical_fields()
            legal_and_court_ordered_expense_data = self.fill_legal_and_court_ordered_expense_fields()
            other_data = self.fill_other_fields()
            hardship_data = self.fill_hardship_fields()
            self.saving()
            grounds_of_exemption_data = None
            if self.check_funds_available_negative_or_not():
                grounds_of_exemption_data = self.fill_grounds_of_exemption_fields()
            self.saving()
            self.check_validation_error_in_tab()
            self.success_or_error_check()
            self.highlight_and_make_screenshot()
            return LoansBudgetAllData(
                monthly_debt_expenses_data=monthly_debt_expenses_data,
                housing_data=housing_data,
                utilities_data=utilities_data,
                transportation_data=transportation_data,
                personal_care_data=personal_care_data,
                medical_data=medical_data,
                legal_and_court_ordered_expense_data=legal_and_court_ordered_expense_data,
                other_data=other_data,
                grounds_of_exemption_data=grounds_of_exemption_data,
                hardship_data=hardship_data
            )

    def check_all_budget_data(self, all_expected_data: LoansBudgetAllData) -> NoReturn:
        with allure.step('Check all budget fields after saving.'):
            all_actual_data = self.get_budget_data()
            with allure.step('Checking monthly debt expenses data.'):
                monthly_debt_actual_data = all_actual_data.monthly_debt_expenses_data
                monthly_debt_excepted_data = all_expected_data.monthly_debt_expenses_data
                assert monthly_debt_actual_data == monthly_debt_excepted_data, AssertionError(
                    self.error_handler(
                        action='Checking monthly debt expenses data.',
                        error='Excepted budget data not equal actual data.',
                        as_is=monthly_debt_actual_data,
                        to_be=monthly_debt_excepted_data
                    )
                )
            with allure.step('Checking housing data.'):
                housing_actual_data = all_actual_data.housing_data
                housing_excepted_data = all_expected_data.housing_data
                assert housing_actual_data == housing_excepted_data, AssertionError(
                    self.error_handler(
                        action='Checking housing data.',
                        error='Excepted budget data not equal actual data.',
                        as_is=housing_actual_data,
                        to_be=housing_excepted_data
                    )
                )
            with allure.step('Checking utilities data.'):
                utilities_actual_data = all_actual_data.utilities_data
                utilities_excepted_data = all_expected_data.utilities_data
                assert utilities_actual_data == utilities_excepted_data, AssertionError(
                    self.error_handler(
                        action='Checking utilities data.',
                        error='Excepted budget data not equal actual data.',
                        as_is=utilities_actual_data,
                        to_be=utilities_excepted_data
                    )
                )
            with allure.step('Checking transportation data.'):
                transportation_actual_data = all_actual_data.transportation_data
                transportation_excepted_data = all_expected_data.transportation_data
                assert transportation_actual_data == transportation_excepted_data, AssertionError(
                    self.error_handler(
                        action='Checking transportation data.',
                        error='Excepted budget data not equal actual data.',
                        as_is=transportation_actual_data,
                        to_be=transportation_excepted_data
                    )
                )
            with allure.step('Checking personal care data.'):
                personal_care_actual_data = all_actual_data.personal_care_data
                personal_care_excepted_data = all_expected_data.personal_care_data
                assert personal_care_actual_data == personal_care_excepted_data, AssertionError(
                    self.error_handler(
                        action='Checking personal care data.',
                        error='Excepted budget data not equal actual data.',
                        as_is=personal_care_actual_data,
                        to_be=personal_care_excepted_data
                    )
                )
            with allure.step('Checking medical data.'):
                medical_actual_data = all_actual_data.medical_data
                medical_excepted_data = all_expected_data.medical_data
                assert medical_actual_data == medical_excepted_data, AssertionError(
                    self.error_handler(
                        action='Checking housing data.',
                        error='Excepted budget data not equal actual data.',
                        as_is=medical_actual_data,
                        to_be=medical_excepted_data
                    )
                )
            with allure.step('Checking legal and court ordered expense data.'):
                legal_ordered_actual_data = all_actual_data.legal_and_court_ordered_expense_data
                legal_ordered_excepted_data = all_expected_data.legal_and_court_ordered_expense_data
                assert legal_ordered_actual_data == legal_ordered_excepted_data, AssertionError(
                    self.error_handler(
                        action='Checking legal and court ordered expense data.',
                        error='Excepted budget data not equal actual data.',
                        as_is=legal_ordered_actual_data,
                        to_be=legal_ordered_excepted_data
                    )
                )
            with allure.step('Checking other data.'):
                other_actual_data = all_actual_data.other_data
                other_excepted_data = all_expected_data.other_data
                assert other_actual_data == other_excepted_data, AssertionError(
                    self.error_handler(
                        action='Checking other data.',
                        error='Excepted budget data not equal actual data.',
                        as_is=other_actual_data,
                        to_be=other_excepted_data
                    )
                )
            with allure.step('Checking grounds of exemption for negative budget data.'):
                grounds_of_exemption_actual_data = all_actual_data.grounds_of_exemption_data
                grounds_of_exemption_excepted_data = all_expected_data.grounds_of_exemption_data
                assert grounds_of_exemption_actual_data == grounds_of_exemption_excepted_data, \
                    AssertionError(
                        self.error_handler(
                            action='Checking grounds of exemption for negative budget data.',
                            error='Excepted budget data not equal actual data.',
                            as_is=grounds_of_exemption_actual_data,
                            to_be=grounds_of_exemption_excepted_data
                        )
                    )
            with allure.step('Checking hardship data.'):
                hardship_actual_data = all_actual_data.hardship_data
                hardship_excepted_data = all_expected_data.hardship_data
                assert hardship_actual_data == hardship_excepted_data, AssertionError(
                    self.error_handler(
                        action='Checking hardship data.',
                        error='Excepted budget data not equal actual data.',
                        as_is=hardship_actual_data,
                        to_be=hardship_excepted_data
                    )
                )

    def get_budget_data(self) -> LoansBudgetAllData:
        with allure.step('Get budget data.'):
            monthly_debt_expenses_data = self.get_monthly_debt_expenses_data()
            housing_data = self.get_housing_data()
            utilities_data = self.get_utilities_data()
            transportation_data = self.get_transportation_data()
            personal_care_data = self.get_personal_care_data()
            medical_data = self.get_medical_data()
            legal_and_court_ordered_expense_data = self.get_legal_and_court_ordered_expense_data()
            other_data = self.get_other_data()
            grounds_of_exemption_data = None
            if self.check_funds_available_negative_or_not():
                grounds_of_exemption_data = self.get_budget_grounds_of_exemption_data()
            hardship_data = self.get_hardship_data()
            return LoansBudgetAllData(
                monthly_debt_expenses_data=monthly_debt_expenses_data,
                housing_data=housing_data,
                utilities_data=utilities_data,
                transportation_data=transportation_data,
                personal_care_data=personal_care_data,
                medical_data=medical_data,
                legal_and_court_ordered_expense_data=legal_and_court_ordered_expense_data,
                other_data=other_data,
                grounds_of_exemption_data=grounds_of_exemption_data,
                hardship_data=hardship_data
            )

    def get_monthly_debt_expenses_data(self) -> LoansBudgetPageMonthlyDebtExpensesData:
        with allure.step('Get monthly debt expenses data.'):
            return LoansBudgetPageMonthlyDebtExpensesData(
                government_student_loans=self.get_government_student_loans(),
                private_student_loans=self.get_private_student_loans(),
                medical_debt=self.get_medical_debt(),
                other_debt=self.get_other_debt(),
                back_taxes=self.get_back_taxes(),
                other_debt_desc=self.get_other_debt_description(),
                other_cards_outside_of_the_program=self.get_other_cards_outside_of_the_program(),
                other_cards_desc=self.get_other_cards_description()
            )

    def get_housing_data(self) -> LoansBudgetHousingData:
        with allure.step('Get housing data.'):
            return LoansBudgetHousingData(
                housing=self.get_housing(),
                housing_payment=self.get_housing_payment(),
                housing_payment_desc=self.get_housing_payment_description(),
                homeowners_insurance=self.get_homeowners_insurance(),
                tax=self.get_tax(),
                hoa=self.get_hoa()
            )

    def get_utilities_data(self) -> LoansBudgetUtilitiesData:
        with allure.step('Get utilities data.'):
            return LoansBudgetUtilitiesData(
                cable_tv_satellite=self.get_cable_tv_satellite(),
                cable_tv_satellite_desc=self.get_cable_tv_satellite_description(),
                telephone=self.get_telephone(),
                telephone_desc=self.get_telephone_description(),
                utilities=self.get_utilities(),
                utilities_desc=self.get_utilities_description(),
                other=self.get_other(),
                other_desc=self.get_other_description()
            )

    def get_transportation_data(self) -> LoansBudgetTransportationData:
        with allure.step('Get transportation data.'):
            return LoansBudgetTransportationData(
                auto_loans=self.get_auto_loans(),
                auto_insurance=self.get_auto_insurance(),
                auto_insurance_des=self.get_auto_insurance_description(),
                auto_other=self.get_auto_other()
            )

    def get_personal_care_data(self) -> LoansBudgetPersonalCareData:
        with allure.step('Get personal care/house hold/misc/food data.'):
            return LoansBudgetPersonalCareData(
                house_hold_items=self.get_house_hold_items(),
                clothing=self.get_clothing(),
                gym_health=self.get_gym_health(),
                personal_care=self.get_personal_care(),
                entertainment=self.get_entertainment(),
                food=self.get_food(),
                food_desc=self.get_food_description(),
                laundry_dry_cleaning=self.get_laundry_dry_cleaning(),
                misc=self.get_misc()
            )

    def get_medical_data(self) -> LoansBudgetMedicalData:
        with allure.step('Get medical data.'):
            return LoansBudgetMedicalData(
                life_insurance=self.get_life_insurance(),
                medical_care=self.get_medical_care()
            )

    def get_legal_and_court_ordered_expense_data(self) -> LoansBudgetLegalOrderedData:
        with allure.step('Get legal and court ordered expenses data.'):
            return LoansBudgetLegalOrderedData(
                support=self.get_support(),
                alimony=self.get_alimony()
            )

    def get_other_data(self) -> LoansBudgetOtherData:
        with allure.step('Get other data.'):
            return LoansBudgetOtherData(
                child_care=self.get_child_care(),
                nursing_care=self.get_nursing_care(),
                education=self.get_education(),
                charity_donations=self.get_charity_donations(),
                other_living_expenses=self.get_other_living_expenses(),
                other_living_expenses_desc=self.get_other_living_expenses_description()
            )

    def get_budget_grounds_of_exemption_data(self) -> LoansBudgetGroundsOfExemptionData:
        with allure.step('Get grounds of exemption for negative budget data.'):
            return LoansBudgetGroundsOfExemptionData(
                grounds_of_exemption=self.get_budget_grounds_of_exemption(),
                grounds_of_exemption_desc=self.get_budget_grounds_of_exemption_description()
            )

    def get_hardship_data(self) -> LoansBudgetHardshipData:
        with allure.step('Get hardship data.'):
            return LoansBudgetHardshipData(
                budget_note=self.get_budget_note(),
                hardship_reason=self.get_hardship_reason(),
                detailed_hardship_reason=self.get_detailed_hardship_reason()
            )

    def fill_monthly_debt_expenses_fields(
            self,
            government_student_loans=str(random.randint(5, 500)),
            private_student_loans=str(random.randint(5, 500)),
            medical_debt=str(random.randint(5, 500)),
            other_debt=str(random.randint(5, 500)),
            other_debt_desc=str(random.randint(5, 500)),
            back_taxes=str(random.randint(5, 500)),
            other_cards_outside_of_the_program=str(random.randint(5, 500)),
            other_cards_desc=TestData.words().lower()
    ) -> LoansBudgetPageMonthlyDebtExpensesData:
        with allure.step('Fill the monthly debt expenses fields.'):
            self.fill_government_student_loans(value=government_student_loans)
            self.fill_private_student_loans(value=private_student_loans)
            self.fill_medical_debt(value=medical_debt)
            self.fill_other_debt(value=other_debt)
            self.fill_other_debt_description(value=other_debt_desc)
            self.fill_back_taxes(value=back_taxes)
            self.fill_other_cards_outside_of_the_program(value=other_cards_outside_of_the_program)
            self.fill_other_cards_description(value=other_cards_desc)
            return LoansBudgetPageMonthlyDebtExpensesData(
                government_student_loans=government_student_loans,
                private_student_loans=private_student_loans,
                medical_debt=medical_debt,
                other_debt=other_debt,
                other_debt_desc=other_debt_desc,
                back_taxes=back_taxes,
                other_cards_outside_of_the_program=other_cards_outside_of_the_program,
                other_cards_desc=other_cards_desc
            )

    def fill_housing_fields(
            self,
            housing: str = LoansBudgetHousingTypes.own,
            housing_payment: str = str(random.randint(99, 999)),
            housing_payment_desc: str = TestData.words(),
            homeowners_insurance: str = str(random.randint(99, 999)),
            tax: str = str(random.randint(99, 999)),
            hoa: str = str(random.randint(99, 999))
    ) -> LoansBudgetHousingData:
        with allure.step('Fill the housing fields.'):
            self.choose_housing(value=housing)
            self.fill_housing_payment(value=housing_payment)
            self.fill_housing_payment_description(value=housing_payment_desc)
            self.fill_homeowners_insurance(value=homeowners_insurance)
            self.fill_tax(value=tax)
            self.fill_hoa(value=hoa)
            return LoansBudgetHousingData(
                housing=housing,
                housing_payment=housing_payment,
                housing_payment_desc=housing_payment_desc,
                homeowners_insurance=homeowners_insurance,
                tax=tax,
                hoa=hoa
            )

    def fill_utilities_fields(
            self,
            cable_tv_satellite: str = str(random.randint(99, 999)),
            cable_tv_satellite_desc: str = TestData.words(),
            telephone: str = str(random.randint(99, 999)),
            telephone_desc: str = TestData.words(),
            utilities: str = str(random.randint(99, 999)),
            utilities_desc: str = TestData.words(),
            other: str = str(random.randint(99, 999)),
            other_desc: str = TestData.words()
    ) -> LoansBudgetUtilitiesData:
        with allure.step('Fill the utilities fields.'):
            self.fill_cable_tv_satellite(value=cable_tv_satellite)
            self.fill_cable_tv_satellite_description(value=cable_tv_satellite_desc)
            self.fill_telephone(value=telephone)
            self.fill_telephone_description(value=telephone_desc)
            self.fill_utilities(value=utilities)
            self.fill_utilities_description(value=utilities_desc)
            self.fill_other(value=other)
            self.fill_other_description(value=other_desc)
            return LoansBudgetUtilitiesData(
                cable_tv_satellite=cable_tv_satellite,
                cable_tv_satellite_desc=cable_tv_satellite_desc,
                telephone=telephone,
                telephone_desc=telephone_desc,
                utilities=utilities,
                utilities_desc=utilities_desc,
                other=other,
                other_desc=other_desc
            )

    def fill_transportation_fields(
            self,
            auto_loans: str = str(random.randint(99, 999)),
            auto_insurance: str = str(random.randint(99, 999)),
            auto_insurance_des: str = TestData.words(),
            auto_other: str = str(random.randint(99, 999))
    ) -> LoansBudgetTransportationData:
        with allure.step('Fill the transportation fields.'):
            self.fill_auto_loans(value=auto_loans)
            self.fill_auto_insurance(value=auto_insurance)
            self.fill_auto_insurance_description(value=auto_insurance_des)
            self.fill_auto_other(value=auto_other)
            return LoansBudgetTransportationData(
                auto_loans=auto_loans,
                auto_insurance=auto_insurance,
                auto_insurance_des=auto_insurance_des,
                auto_other=auto_other
            )

    def fill_personal_care_fields(
            self,
            house_hold_items: str = str(random.randint(99, 999)),
            clothing: str = str(random.randint(99, 999)),
            gym_health: str = str(random.randint(99, 999)),
            personal_care: str = str(random.randint(99, 999)),
            entertainment: str = str(random.randint(99, 999)),
            food: str = str(random.randint(99, 999)),
            food_desc: str = TestData.words(),
            laundry_dry_cleaning: str = str(random.randint(99, 999)),
            misc: str = str(random.randint(99, 999))
    ) -> LoansPersonalCareData:
        with allure.step('Fill the personal care fields.'):
            self.fill_house_hold_items(value=house_hold_items)
            self.fill_clothing(value=clothing)
            self.fill_gym_health(value=gym_health)
            self.fill_personal_care(value=personal_care)
            self.fill_entertainment(value=entertainment)
            self.fill_food(value=food)
            self.fill_food_description(value=food_desc)
            self.fill_laundry_dry_cleaning(value=laundry_dry_cleaning)
            self.fill_misc(value=misc)
            return LoansPersonalCareData(
                house_hold_items=house_hold_items,
                clothing=clothing,
                gym_health=gym_health,
                personal_care=personal_care,
                entertainment=entertainment,
                food=food,
                food_desc=food_desc,
                laundry_dry_cleaning=laundry_dry_cleaning,
                misc=misc
            )

    def fill_medical_fields(
            self,
            life_insurance: str = str(random.randint(99, 999)),
            medical_care: str = str(random.randint(99, 999))
    ) -> LoansBudgetMedicalData:
        with allure.step('Fill the medical fields.'):
            self.fill_life_insurance(value=life_insurance)
            self.fill_medical_care(value=medical_care)
            return LoansBudgetMedicalData(
                life_insurance=life_insurance,
                medical_care=medical_care
            )

    def fill_legal_and_court_ordered_expense_fields(
            self,
            support: str = str(random.randint(99, 999)),
            alimony: str = str(random.randint(99, 999))
    ) -> LoansBudgetLegalOrderedData:
        with allure.step('Fill the legal and court ordered expense fields.'):
            self.fill_support(value=support)
            self.fill_alimony(value=alimony)
            return LoansBudgetLegalOrderedData(
                support=support,
                alimony=alimony
            )

    def fill_other_fields(
            self,
            child_care: str = str(random.randint(99, 999)),
            nursing_care: str = str(random.randint(99, 999)),
            education: str = str(random.randint(99, 999)),
            charity_donations: str = str(random.randint(99, 999)),
            other_living_expenses: str = str(random.randint(99, 999)),
            other_living_expenses_desc: str = TestData.words()
    ) -> LoansBudgetOtherData:
        with allure.step('Fill the other fields.'):
            self.fill_child_care(value=child_care)
            self.fill_nursing_care(value=nursing_care)
            self.fill_education(value=education)
            self.fill_charity_donations(value=charity_donations)
            self.fill_other_living_expenses(value=other_living_expenses)
            self.fill_other_living_expenses_description(value=other_living_expenses_desc)
            return LoansBudgetOtherData(
                child_care=child_care,
                nursing_care=nursing_care,
                education=education,
                charity_donations=charity_donations,
                other_living_expenses=other_living_expenses,
                other_living_expenses_desc=other_living_expenses_desc
            )

    def fill_grounds_of_exemption_fields(
            self,
            grounds_of_exemption: str = loans_budget_ground_of_example_types.additional,
            grounds_of_exemption_desc: str = TestData.words()
    ) -> LoansBudgetGroundsOfExemptionData:
        with allure.step('Fill the grounds of example for negative budget fields.'):
            self.choose_grounds_of_exemption(value=grounds_of_exemption)
            self.fill_grounds_of_exemption_description(value=grounds_of_exemption_desc)
            return LoansBudgetGroundsOfExemptionData(
                grounds_of_exemption=grounds_of_exemption,
                grounds_of_exemption_desc=grounds_of_exemption_desc
            )

    def fill_hardship_fields(
            self,
            budget_note: str = TestData.words(),
            hardship_reason: str = loans_hardship_reason.medical,
            detailed_hardship_reason: str = TestData.words()
    ) -> LoansBudgetHardshipData:
        with allure.step('Fill the hardship fields.'):
            self.fill_budget_note(value=budget_note)
            self.select_hardship_reason(value=hardship_reason)
            self.fill_detailed_hardship_reason(value=detailed_hardship_reason)
            return LoansBudgetHardshipData(
                budget_note=budget_note,
                hardship_reason=hardship_reason,
                detailed_hardship_reason=detailed_hardship_reason
            )

    def check_funds_available_negative_or_not(self) -> bool:
        return True if '-' in self.get_funds_available() else False

    def choose_housing(self, value: str) -> NoReturn:
        self.click_dl_housing()
        self.choose_housing_type(value=value)

    def choose_grounds_of_exemption(self, value: str) -> NoReturn:
        self.click_dl_grounds_of_exemption()
        self.choose_grounds_of_exemption_type(value=value)
