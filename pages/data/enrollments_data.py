from typing import NamedTuple


class EnrollmentsPages:
    enrollments = 'Enrollments'
    enrollments_main = 'EnrollmentsMain'
    enrollments_creditors = 'EnrollmentsCreditors'
    enrollments_creditors_tab = 'Creditors'
    enrollments_ram_payments = 'RAM payments'
    enrollments_gcs_payments = 'GCS payments'
    enrollments_ram_payments_deposits = 'Deposits'
    enrollments_ram_payments_creditor_payments = 'Creditors Payments'
    enrollments_ram_payments_settlement_fees = 'Settlements Fees'
    enrollments_ram_payments_account_schedule = 'Account Schedule'
    enrollments_ram_payments_temporary_account_schedule = 'Temporary Account Schedule'
    enrollments_ram_payments_advanced_regroups = 'Advances & Recoups'
    enrollments_ram_payments_attorney_payment = 'Attorney Payment'
    enrollments_customer_creditors = 'EnrollmentsCustomerCreditors'
    enrollments_customer_creditors_offers = 'EnrollmentsCustomerCreditorsSettlementOffers'
    enrollments_customer_creditors_documents = 'EnrollmentsCustomerCreditorsDocuments'
    enrollments_customer_creditors_payments = 'EnrollmentsCustomerCreditorsPayments'
    enrollments_drafts = 'EnrollmentsDrafts'
    enrollments_plan = 'EnrollmentsPlan'
    enrollments_loan_plan = 'EnrollmentsLoanPlan'
    enrollments_profile = 'EnrollmentsProfile'
    enrollments_income = 'EnrollmentsIncome'
    enrollments_budget = 'EnrollmentsBudget'
    enrollments_strategy = 'EnrollmentsStrategy'
    enrollments_ach = 'EnrollmentsACH'
    enrollments_document = 'EnrollmentsDocument'
    enrollments_duplicate = 'EnrollmentsDuplicate'
    enrollments_tasks = 'EnrollmentsTasks'
    enrollments_logs = 'EnrollmentsLogs'


class EnrollmentsTabs:
    history = 'History'
    profile = 'Profile'
    creditors = 'Creditors'
    plan = 'Plan'
    income = 'Income'
    budget = 'Budget'
    calculator = 'Calculator'
    loan_calculator = 'Loan Calculator'
    ach = 'Ach'
    documents = 'Documents'
    duplicates = 'Duplicates'
    tasks = 'Tasks'
    logs = 'Logs'
    underwriting = 'Underwriting'


class EnrollmentsHistoryEvents:
    lead_to_enrollment_event = 'Type changed Lead Enrollment'
    docs_signed_event = 'Status changed Docs sent Docs Signed'
    docs_sent_event = 'Status changed New Docs sent'
    reassign_event = 'Property changed Unassigned Active'


class EnrollmentsCreditorsMainData(NamedTuple):
    account_holder: int
    cardholder_name: str
    debt_type: str
    status: str
    priority: str
    disposition: str
    admin_disposition: str
    negotiator: str
    summons_admin: str
    retrieval_admin: str
    past_due: int
    cycle_date: int
    charge_off_date: str
    settlement_balance: str
    settlement_payment_date: str

class EnrollmentsIncomeData(NamedTuple):
    status_income: str
    mark_primary: bool
    occupation: str
    primary_source_of_income: str
    length_years: str
    length_months: str
    company_name: str
    company_address: str
    company_city: str
    company_state: str
    company_zip: str
    phone_work: str
    additional_phone_work: str
    gross_monthly_income: int
    net_monthly_income: str
    gross_monthly_income: str
    w2income: str
    type_of_pay: str
    how_to_calculate: str
    bank_statements_review: str


class EnrollmentsIncomeStatuses:
    full_time_employed = 'Full-Time Employed'
    part_time_employed = 'Part-Time Employed'
    self_employed = 'Self-Employed'
    unemployed = 'Unemployed'
    retired = 'Retired'


class EnrollmentsCreditorStatuses:
    in_progress = 'In progress'


class EnrollmentsSettlementOfferStatuses:
    draft = 'Draft'
    accepted = 'Accepted'
    deleted = 'Deleted'
    cancelled = 'Cancelled'
    need_sif_letter = 'Need SIF Letter'
    need_client_auth = 'Need Client Auth'
    need_acceptance = 'Need Acceptance'


class EnrollmentsPaymentsStatuses:
    void = 'void'


class EnrollmentsHowToCalculate:
    base = 'Base gross income'
    ytd = 'YTD due to paystub showing regular OT or incentive income (bonus)'


class EnrollmentsBankStatementsReview:
    a_borrower_has_direct_deposits = 'A Borrower has Direct Deposits'
    negative_balance_detected = 'Negative Balance Detected'
    borrowers_primary_account = 'Borrower`s Primary Account'


class EnrollmentsAchData(NamedTuple):
    name_of_account: str
    routing_number: str
    account_number: int
    bank_name: str
    bank_phone_number: str
    bank_address: str
    bank_city: str
    bank_state: str
    bank_zip: str


class EnrollmentsPaymentData(NamedTuple):
    deposits_data: bool
    creditors_payments_data: bool
    settlement_fees: bool
    account_schedule_description: str
    account_schedule_balance: str
    advanced_regroups: bool
    attorney_payment: bool


enrollments_pages = EnrollmentsPages()
enrollments_tabs = EnrollmentsTabs()
enrollments_income_statuses = EnrollmentsIncomeStatuses()
enrollments_how_to_calculate = EnrollmentsHowToCalculate()

