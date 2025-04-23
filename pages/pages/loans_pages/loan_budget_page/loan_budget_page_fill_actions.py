from typing import NoReturn

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.data.main_data import Configs
from autotests.pages.pages.loans_pages.loans_common_page.loans_common_page import LoansCommonPage
from autotests.pages.pages_details import LoansBudget
from autotests.pages.utils import fill_field


class LoanBudgetPageFillActions(LoansCommonPage):
    def __init__(self, driver: WebDriver, cfg: Configs):
        super().__init__(driver, cfg)
        self.loan_budget_locators = LoansBudget.Locators

    @fill_field('Detailed hardship reason')
    def fill_detailed_hardship_reason(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_DETAILED_HARDSHIP_REASON, keys=[value])

    # housing
    @fill_field('Housing payment desc')
    def fill_housing_payment(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_HOUSING_PAYMENT, keys=[value])

    @fill_field('"Housing Payment" Description')
    def fill_housing_payment_description(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_HOUSING_PAYMENT_DESC, keys=[value])

    # utilities
    @fill_field('Cable tv satellite desc')
    def fill_cable_tv_satellite(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_CABLE_TV_SATELLITE, keys=[value])

    @fill_field('Cable tv satellite desc')
    def fill_cable_tv_satellite_description(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_CABLE_TV_SATELLITE_DESC, keys=[value])

    @fill_field('Telephone')
    def fill_telephone(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_TELEPHONE, keys=[value])

    @fill_field('Telephone desc')
    def fill_telephone_description(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_TELEPHONE_DESC, keys=[value])

    @fill_field('Utilities')
    def fill_utilities(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_UTILITIES, keys=[value])

    @fill_field('Utilities Description')
    def fill_utilities_description(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_UTILITIES_DESC, keys=[value])

    @fill_field('Other')
    def fill_other(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_OTHER, keys=[value])

    @fill_field('Other Description')
    def fill_other_description(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_OTHER_DESC, keys=[value])

    # transportation
    @fill_field('Auto Loans')
    def fill_auto_loans(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_AUTO_LOANS, keys=[value])

    @fill_field('Auto Insurance')
    def fill_auto_insurance(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_AUTO_INSURANCE, keys=[value])

    @fill_field('"Auto Insurance" Description')
    def fill_auto_insurance_description(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_AUTO_INSURANCE_DESC, keys=[value])

    @fill_field('Auto Other')
    def fill_auto_other(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_AUTO_OTHER, keys=[value])

    # personal care/house_hold/misc/food
    @fill_field('House Hold Items')
    def fill_house_hold_items(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_HOUSE_HOLD_ITEMS, keys=[value])

    @fill_field('Clothing')
    def fill_clothing(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_CLOTHING, keys=[value])

    @fill_field('Gym Health')
    def fill_gym_health(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_GYM_HEALTH, keys=[value])

    @fill_field('Personal Care')
    def fill_personal_care(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_PERSONAL_CARE, keys=[value])

    @fill_field('Entertainment')
    def fill_entertainment(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_ENTERTAINMENT, keys=[value])

    @fill_field('Food')
    def fill_food(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_FOOD, keys=[value])

    @fill_field('"Food" Description')
    def fill_food_description(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_FOOD_DESC, keys=[value])

    @fill_field('Laundry Dry Cleaning')
    def fill_laundry_dry_cleaning(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_LAUNDRY_DRY_CLEANING, keys=[value])

    @fill_field('Misc')
    def fill_misc(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_MISC, keys=[value])

    # medical
    @fill_field('Life Insurance')
    def fill_life_insurance(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_LIFE_INSURANCE, keys=[value])

    # legal and court ordered expense
    @fill_field('Support')
    def fill_support(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_SUPPORT, keys=[value])

    @fill_field('Alimony')
    def fill_alimony(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_ALIMONY, keys=[value])

    # other
    @fill_field('Child Care')
    def fill_child_care(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_CHILD_CARE, keys=[value])

    @fill_field('Nursing Care')
    def fill_nursing_care(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_NURSING_CARE, keys=[value])

    @fill_field('Education')
    def fill_education(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_EDUCATION, keys=[value])

    @fill_field('Charity Donations')
    def fill_charity_donations(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_CHARITY_DONATIONS, keys=[value])

    @fill_field('Other Living Expenses')
    def fill_other_living_expenses(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_OTHER_LIVING_EXPENSES, keys=[value])

    @fill_field('"Other Living Expenses" Description')
    def fill_other_living_expenses_description(self, value: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_OTHER_LIVING_EXPENSES_DESC, keys=[value])

    # ----------------------------------------------------------------------------------------------
    @fill_field('Grounds Of Exemption For Negative Budget Description')
    def fill_grounds_of_exemption_description(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_GROUNDS_OF_EXEMPTION_DESC, keys=[value])

    @fill_field('Government student loans')
    def fill_government_student_loans(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_GOVERNMENT_STUDENT_LOANS, keys=[value])

    @fill_field('Private student loans')
    def fill_private_student_loans(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_PRIVATE_STUDENT_LOANS, keys=[value])

    @fill_field('Medical debt')
    def fill_medical_debt(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_MEDICAL_DEBT, keys=[value])

    @fill_field('Other debt')
    def fill_other_debt(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_OTHER_DEBT, keys=[value])

    @fill_field('Other debt Description')
    def fill_other_debt_description(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_OTHER_DEBT_DESCRIPTION, keys=[value])

    @fill_field('Back taxes')
    def fill_back_taxes(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_BACK_TAXES, keys=[value])

    @fill_field('Other cards outside of the program')
    def fill_other_cards_outside_of_the_program(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_OTHER_CARDS_OUTSIDE_OF_THE_PROGRAM, keys=[value])

    @fill_field('"Other cards..." Description')
    def fill_other_cards_description(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_OTHER_CARDS, keys=[value])

    @fill_field('Housing')
    def fill_housing_housing(self, housing: int = None) -> NoReturn:
        elem = self.find_element(self.loan_budget_locators.DL_HOUSING)
        elem.click()

        for _ in range(housing):
            elem.send_keys(Keys.ARROW_DOWN)
        elem.send_keys(Keys.ENTER)

    @fill_field('Homeowners Insurance')
    def fill_homeowners_insurance(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_HOMEOWNERS_INSURANCE, keys=[value])

    @fill_field('Tax')
    def fill_tax(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_TAX, keys=[value])

    @fill_field('HOA')
    def fill_hoa(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_HOA, keys=[value])

    @fill_field('Personal care friends budget')
    def fill_friends_budget_personal_care(self, house_hold_items: int = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_HOUSE_HOLD_ITEMS, keys=[house_hold_items])

    @fill_field('Clothing')
    def fill_clothing_personal_care(self, clothing: int = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_HOUSE_HOLD_ITEMS, keys=[clothing])

    @fill_field('Personal care friends budget')
    def fill_house_hold_items_personal_care(self, house_hold_items: int = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_HOUSE_HOLD_ITEMS, keys=[house_hold_items])

    @fill_field('Gym health')
    def fill_gym_health_personal_care(self, gym_health: int = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_GYM_HEALTH, keys=[gym_health])

    @fill_field('Personal care')
    def fill_personal_care_personal_care(self, personal_care: int = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_PERSONAL_CARE, keys=[personal_care])

    @fill_field('Entertainment')
    def fill_entertainment_personal_care(self, entertainment: int = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_ENTERTAINMENT, keys=[entertainment])

    @fill_field('Food')
    def fill_food_personal_care(self, food: int = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_FOOD, keys=[food])

    @fill_field('Food description')
    def fill_food_desc_personal_care(self, food_desc: str = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_FOOD_DESC, keys=[food_desc])

    @fill_field('laundry_dry_cleaning')
    def fill_laundry_dry_cleaning_personal_care(self, laundry_dry_cleaning: int = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_LAUNDRY_DRY_CLEANING, keys=[laundry_dry_cleaning])

    @fill_field('Personal care friends budget')
    def fill_misc_personal_care(self, misc: int = None) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_MISC, keys=[misc])

    @fill_field('Hardship Reason')
    def select_hardship_reason_budget(self, hardship_reason_text: str) -> NoReturn:
        self.select_element(locator=self.loan_budget_locators.S_HARDSHIP_REASON, text=hardship_reason_text)

    @fill_field('Budget note')
    def fill_budget_note(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_BUDGET_NOTE, keys=[value])

    @fill_field('Medical')
    def fill_medical_care(self, value: str) -> NoReturn:
        self.send_keys(locator=self.loan_budget_locators.F_MEDICAL_CARE, keys=[value])
