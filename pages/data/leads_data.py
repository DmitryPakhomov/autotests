from typing import NamedTuple


class LeadsHistoryTabs:
    add_note = 'Add a Note'
    send_email = 'Send an Email'
    send_sms = 'Send a SMS'
    pre_made_email = 'Pre-made Email'


class LeadsPages:
    leads = 'Leads'
    leads_history = 'LeadsHistory'
    leads_profile = 'LeadsProfile'
    leads_creditors = 'LeadsCreditors'
    leads_income = 'LeadsIncome'
    leads_budget = 'LeadsBudget'
    leads_calculator = 'LeadsCalculator'
    leads_loan_calculator = 'LeadsLoanCalculator'
    leads_ach = 'LeadsACH'
    leads_document = 'LeadsDocument'
    leads_duplicate = 'LeadsDuplicate'
    leads_tasks = 'LeadsTasks'
    leads_logs = 'LeadsLogs'


class LeadsTabs:
    history = 'History'
    profile = 'Profile'
    creditors = 'Creditors'
    income = 'Income'
    budget = 'Budget'
    calculator = 'Calculator'
    loan_calculator = 'Loan Calculator'
    ach = 'Ach'
    documents = 'Documents'
    duplicates = 'Duplicates'
    tasks = 'Tasks'
    logs = 'Logs'
    loan_pro_plan = 'LoanPro Plan'
    underwriting = 'Underwriting'


class LeadsTypes:
    applicant = 'applicant'
    co_applicant = 'co-applicant'


class LeadsQualities:
    active = 'active'
    rejected = 'rejected'
    unassigned = 'unassigned'
    trickle = 'trickle'
    lead = 'lead'


class LeadsStatuses:
    new = '0'

class DebtTypeEnabledList:
    list_enabled = [
        'Charge Account',
    ]


class LeadsFilters:
    new = 'new'


class LeadsIncomeStatuses:
    full_time_employed = 'Full-Time Employed'


class LeadsBudgetHousingTypes:
    rent = 'Rent'
    own = 'Own'
    live_with_family = 'Live with family'


class LeadsCompany(NamedTuple):
    americor: str = 'Americor'
    credit9: str = 'Credit9'


class LeadsApplicantData(NamedTuple):
    first_name: str
    # middle_name: str
    last_name: str
    phone_mobile: str
    zip_code: str
    city: str
    current_physical_address: str
    email: str
    number_of_months: str
    phone_home: str
    emergency_contact_name: str
    emergency_contact_number: str
    # best_time_to_call: str
    # state: str
    ssn: str
    dob: str
    dl: str
    mothers_maiden_name: str
    us_resident: bool
    # active_military: bool
    # security_clearance: bool
    # spanish_speaker: bool


leads_pages = LeadsPages()
leads_tabs = LeadsTabs()
leads_types = LeadsTypes()
leads_statuses = LeadsStatuses()
leads_qualities = LeadsQualities()
leads_filters = LeadsFilters()
