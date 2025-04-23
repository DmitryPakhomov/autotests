from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.blocks.loans_pages_blocks.loans_common_page_blocks import LoansCommonPageBlocks
from autotests.pages.data.main_data import Configs
from autotests.pages.pages_details import LoansBudget
from autotests.pages.utils import get_value


class LoansBudgetPageGetActions(LoansCommonPageBlocks):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loan_budget_locators = LoansBudget.Locators

    # budget details
    @get_value('Funds available')
    def get_funds_available(self) -> str:
        return self.get_text(self.loan_budget_locators.T_FUNDS_AVAILABLE).replace('$', '')

    # monthly debt expenses
    @get_value('Government Student Loans')
    def get_government_student_loans(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_GOVERNMENT_STUDENT_LOANS, attr_name='value')[2: -3]

    @get_value('Private Student Loans')
    def get_private_student_loans(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_PRIVATE_STUDENT_LOANS, attr_name='value')[2: -3]

    @get_value('Medical Debt')
    def get_medical_debt(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_MEDICAL_DEBT, attr_name='value')[2: -3]

    @get_value('Other Debt')
    def get_other_debt(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_OTHER_DEBT, attr_name='value')[2: -3]

    @get_value('"Other Debt" Description')
    def get_other_debt_description(self) -> str:
        return self.get_text(self.loan_budget_locators.F_OTHER_DEBT_DESCRIPTION)

    @get_value('Back Taxes')
    def get_back_taxes(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_BACK_TAXES, attr_name='value')[2: -3]

    @get_value('Other Cards Outside Of The Program ')
    def get_other_cards_outside_of_the_program(self) -> str:
        return self.get_attribute(
            self.loan_budget_locators.F_OTHER_CARDS_OUTSIDE_OF_THE_PROGRAM,
            attr_name='value'
        )[2: -3]

    @get_value('Other Cards..." Description')
    def get_other_cards_description(self) -> str:
        return self.get_text(self.loan_budget_locators.F_OTHER_CARDS).lower()

    # monthly living expenses
    # housing
    @get_value('Housing')
    def get_housing(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_HOUSING_READ_HOUSING, attr_name='title')

    @get_value('Housing Payment')
    def get_housing_payment(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_HOUSING_PAYMENT, attr_name='value')[2: -3]

    @get_value('Housing Payment" Description')
    def get_housing_payment_description(self) -> str:
        return self.get_text(self.loan_budget_locators.F_HOUSING_PAYMENT_DESC).lower()

    @get_value('Homeowners Insurance')
    def get_homeowners_insurance(self) -> str:
        return self.get_attribute(
            self.loan_budget_locators.F_HOMEOWNERS_INSURANCE, attr_name='value')[2: -3]

    @get_value('TAX')
    def get_tax(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_TAX, attr_name='value')[2: -3]

    @get_value('HOA')
    def get_hoa(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_HOA, attr_name='value')[2: -3]

    # utilities
    @get_value('Cable TV Satellite')
    def get_cable_tv_satellite(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_CABLE_TV_SATELLITE, attr_name='value')[2: -3]

    @get_value('Cable TV Satellite" Description')
    def get_cable_tv_satellite_description(self) -> str:
        return self.get_text(self.loan_budget_locators.F_CABLE_TV_SATELLITE_DESC)

    @get_value('Telephone')
    def get_telephone(self) -> str:
        return self.get_attribute(
            self.loan_budget_locators.F_TELEPHONE, attr_name='value')[2: -3]

    @get_value('"Telephone" Description ')
    def get_telephone_description(self) -> str:
        return self.get_text(self.loan_budget_locators.F_TELEPHONE_DESC)

    @get_value('Utilities')
    def get_utilities(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_UTILITIES, attr_name='value')[2: -3]

    @get_value('"Utilities" Description')
    def get_utilities_description(self) -> str:
        return self.get_text(self.loan_budget_locators.F_UTILITIES_DESC).lower()

    @get_value('Other')
    def get_other(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_OTHER, attr_name='value')[2: -3]

    @get_value('"Other" Description')
    def get_other_description(self) -> str:
        return self.get_text(self.loan_budget_locators.F_OTHER_DESC)

    # transportation
    @get_value('Auto Loans')
    def get_auto_loans(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_AUTO_LOANS, attr_name='value')[2: -3]

    @get_value('Auto Insurance')
    def get_auto_insurance(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_AUTO_INSURANCE, attr_name='value')[2: -3]

    @get_value('"Auto Insurance" Description')
    def get_auto_insurance_description(self) -> str:
        return self.get_text(self.loan_budget_locators.F_AUTO_INSURANCE_DESC)

    @get_value('Auto Other')
    def get_auto_other(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_AUTO_OTHER, attr_name='value')[2: -3]

    # personal care/house_hold/misc/food
    @get_value('House Hold Items')
    def get_house_hold_items(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_HOUSE_HOLD_ITEMS, attr_name='value')[2: -3]

    @get_value('Clothing')
    def get_clothing(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_CLOTHING, attr_name='value')[2: -3]

    @get_value('Gym Health')
    def get_gym_health(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_GYM_HEALTH, attr_name='value')[2: -3]

    @get_value('Personal Care')
    def get_personal_care(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_PERSONAL_CARE, attr_name='value')[2: -3]

    @get_value('Entertainment')
    def get_entertainment(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_ENTERTAINMENT, attr_name='value')[2: -3]

    @get_value('Food')
    def get_food(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_FOOD, attr_name='value')[2: -3]

    @get_value('"Food" Description')
    def get_food_description(self) -> str:
        return self.get_text(self.loan_budget_locators.F_FOOD_DESC).lower()

    @get_value('Laundry Dry Cleaning')
    def get_laundry_dry_cleaning(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_LAUNDRY_DRY_CLEANING, attr_name='value')[2: -3]

    @get_value('Misc')
    def get_misc(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_MISC, attr_name='value')[2: -3]

    # medical
    @get_value('Life Insurance')
    def get_life_insurance(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_LIFE_INSURANCE, attr_name='value')[2: -3]

    @get_value('Medical Care')
    def get_medical_care(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_MEDICAL_CARE, attr_name='value')[2: -3]

    # legal and court ordered expense
    @get_value('Support')
    def get_support(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_SUPPORT, attr_name='value')[2: -3]

    @get_value('Alimony')
    def get_alimony(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_ALIMONY, attr_name='value')[2: -3]

    # other
    @get_value('Child Care')
    def get_child_care(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_CHILD_CARE, attr_name='value')[2: -3]

    @get_value('Nursing Care')
    def get_nursing_care(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_NURSING_CARE, attr_name='value')[2: -3]

    @get_value('Education')
    def get_education(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_EDUCATION, attr_name='value')[2: -3]

    @get_value('Charity Donations')
    def get_charity_donations(self) -> str:
        return self.get_attribute(self.loan_budget_locators.F_CHARITY_DONATIONS, attr_name='value')[2: -3]

    @get_value('Other Living Expenses')
    def get_other_living_expenses(self) -> str:
        return self.get_attribute(
            self.loan_budget_locators.F_OTHER_LIVING_EXPENSES_OTHER, attr_name='value')[2: -3]

    @get_value('"Other Living Expenses" Description')
    def get_other_living_expenses_description(self) -> str:
        return self.get_text(self.loan_budget_locators.F_OTHER_LIVING_EXPENSES_DESC)

    # ----------------------------------------------------------------------------------------------

    @get_value('Grounds Of Exemption For Negative Budget')
    def get_budget_grounds_of_exemption(self) -> str:
        return self.get_attribute(self.loan_budget_locators.T_GROUNDS_OF_EXEMPTION, attr_name='title')

    @get_value('Grounds Of Exemption For Negative Budget Description')
    def get_budget_grounds_of_exemption_description(self) -> str:
        return self.get_text(self.loan_budget_locators.F_GROUNDS_OF_EXEMPTION_DESC)

    @get_value('Budget note')
    def get_budget_note(self) -> str:
        return self.get_text(self.loan_budget_locators.F_BUDGET_NOTE)

    @get_value('Hardship Reason')
    def get_hardship_reason(self) -> str:
        return self.get_selected_value(self.loan_budget_locators.S_HARDSHIP_REASON)

    @get_value('Detailed Hardship Reason')
    def get_detailed_hardship_reason(self) -> str:
        return self.get_text(self.loan_budget_locators.F_DETAILED_HARDSHIP_REASON)
