from typing import NamedTuple


class LoansPages:
    loans = 'Loans'
    loans_history = 'LoansHistory'
    loans_creditors = 'LoansCreditors'
    loans_drafts = 'LoansDrafts'
    loans_loan_plan = 'LoansPlan'
    loans_ach = 'LoansACH'
    loans_profile = 'LoansProfile'
    loans_income = 'LoansIncome'
    loans_budget = 'LoansBudget'
    loans_document = 'LoansDocument'
    loans_duplicate = 'LoansDuplicate'
    loans_tasks = 'LoansTasks'
    loans_logs = 'LoansLogs'


class LoansTabs:
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
    underwriting = 'Underwriting'


class LoansTypes:
    applicant = 'applicant'
    co_applicant = 'co-applicant'


class LoansCreditorsSettlementOfferData(NamedTuple):
    nbr_of_month: int
    contact_person: str
    contact_phone: str
    first_settlement_date: str


class LoansStatuses:
    new = 0
    callback = 1
    nurtured = 3
    docs_sent = 13
    overdue = 15
    ready_to_pitch = 16
    ready_to_pitch_now_show = 17
    hot = 18
    automation = 22
    mail_fax_docs = 25
    automation_sr_ai = 34
    follow_up_pitch = 41
    pre_enrollment_sent = 43
    pre_enrollment_completed = 44


class LoansFilters:
    new = 'new'
    callback_today = 'callbackToday'
    starred = 'starred'
    nurture_lead_pool = 'nurtureLeadPool'
    sharktank = 'sharktank'
    goldmine = 'goldmine'
    entities = 'entities'
    kvdate = 'kvdate'
    date_from = 'dateFrom'
    date_to = 'dateTo'
    status = 'status'
    opener = 'opener'
    state = 'state'
    information_label = 'informationLabel'
    source = 'source'
    channels = 'channels'
    companies = 'companies'
    advantage_law = 'advantageLaw'
    bad_Loans = 'badLoans'
    trickle_system = 'trickleSystem'
    spanish_speaker = 'spanishSpeaker'
    upfront = 'upfront'
    c9_loan_processors = 'c9LoanProcessors'
    search = 'search'


class LoansIncomeStatuses:
    full_time_employed = 'Full-Time Employed'
    part_time_employed = 'Part-Time Employed'
    self_employed = 'Self-Employed'
    unemployed = 'Unemployed'
    retired = 'Retired'


class LoansBudgetHousingTypes:
    rent = 'Rent'
    own = 'Own'
    live_with_family = 'Live with family'


class LoansBudgetGroundsOfExampleTypes:
    overtime = 'Overtime at Current Job'
    additional = 'Additional Employment (i.e., second job)'
    gift = 'Gift/Donation from Family or Charity'
    tax_refund = 'Tax Refund Pending'
    future_child = 'Future Child Support/Alimony (i.e., car loan)'
    funds = 'Funds from 401K/Stocks'
    pay_off = 'Pay Off Other Debt in The Next Year (i.e., car loan)'
    reduce = 'Reduce Ongoing Discretionary Subscriptions (i.e., cable, Netflix, gym, etc.)'
    other = 'Other'


class LoansCreditorsAllData(NamedTuple):
    main_data: NamedTuple
    original_creditor_data: NamedTuple
    current_creditor_data: NamedTuple
    override_address_data: NamedTuple


class LoansCreditorsOriginalCreditorData(NamedTuple):
    creditor: str
    account: str
    original_balance: int
    current_balance: int
    poa_sent: str


class LoansCreditorsCurrentCreditorData(NamedTuple):
    current_creditor: str
    current_account: str
    current_poa_sent: str


class LoansCreditorsOverrideAddressData(NamedTuple):
    address: str
    state: str
    fax: str
    contact_name: str
    address2: str
    zip: str
    pay_to: str
    contact_phone: str
    city: str
    phone: str
    creditor_name: str
    payment_notes: str


class LoansBudgetHousingData(NamedTuple):
    housing: str
    housing_payment: str
    housing_payment_desc: str
    homeowners_insurance: str
    tax: str
    hoa: str


class LoansBudgetUtilitiesData(NamedTuple):
    cable_tv_satellite: str
    cable_tv_satellite_desc: str
    telephone: str
    telephone_desc: str
    utilities: str
    utilities_desc: str
    other: str
    other_desc: str


class LoansBudgetTransportationData(NamedTuple):
    auto_loans: str
    auto_insurance: str
    auto_insurance_des: str
    auto_other: str


class LoansBudgetPersonalCareData(NamedTuple):
    house_hold_items: str
    clothing: str
    gym_health: str
    personal_care: str
    entertainment: str
    food: str
    food_desc: str
    laundry_dry_cleaning: str
    misc: str


class LoansBudgetMedicalData(NamedTuple):
    life_insurance: str
    medical_care: str


class LoansBudgetLegalOrderedData(NamedTuple):
    support: str
    alimony: str


class LoansBudgetOtherData(NamedTuple):
    child_care: str
    nursing_care: str
    education: str
    charity_donations: str
    other_living_expenses: str
    other_living_expenses_desc: str


class LoansBudgetGroundsOfExemptionData(NamedTuple):
    grounds_of_exemption: str or None
    grounds_of_exemption_desc: str or None


class LoansBudgetHardshipData(NamedTuple):
    budget_note: str
    hardship_reason: str
    detailed_hardship_reason: str


class LoansBudgetAllData(NamedTuple):
    monthly_debt_expenses_data: NamedTuple
    housing_data: NamedTuple
    utilities_data: NamedTuple
    transportation_data: NamedTuple
    personal_care_data: NamedTuple
    medical_data: NamedTuple
    legal_and_court_ordered_expense_data: NamedTuple
    other_data: NamedTuple
    grounds_of_exemption_data: NamedTuple or None
    hardship_data: NamedTuple


class LoansBudgetPageMonthlyDebtExpensesData(NamedTuple):
    government_student_loans: str
    private_student_loans: str
    medical_debt: str
    other_debt: str
    other_debt_desc: str
    back_taxes: str
    other_cards_outside_of_the_program: str
    other_cards_desc: str


class LoansPersonalCareData(NamedTuple):
    house_hold_items: str
    clothing: str
    gym_health: str
    personal_care: str
    entertainment: str
    food: str
    food_desc: str
    laundry_dry_cleaning: str
    misc: str


class LoansPrimarySources:
    alimony = 'Alimony'
    annuities = 'Annuities'
    child_support = 'Child Support'
    current_savings = 'Current Savings'
    dividends = 'Dividends'
    gambling_lottery = 'Gambling / Lottery'
    gift_family = 'Gift / Family'
    government_benefits = 'Government Benefits'
    inheritance = 'Inheritance'
    investments = 'Investments'
    other_govt_assistance = 'Other Gov’t Assistance'
    pension = 'Pension'
    retirement = 'Retirement'
    ssa_ssi = 'SSA / SSI'
    sale_of_assets = 'Sale of Assets'
    sale_of_property = 'Sale of Property'
    social_security = 'Social Security'
    unemployment_benefits = 'Unemployment Benefits'
    other = 'Other'


class LoansOccupation:
    atm = 'ATM Owner / Operator'
    accountant = 'Accountant'
    administrative = 'Administrative / Office Support'
    agriculture = 'Agriculture / Farming'
    antiquities = 'Antiquities / Auctions'
    architecture = 'Architecture / Engineering'
    arms = 'Arms / Ammunition Dealing'
    artist = 'Artist / Entertainment'
    attorney = 'Attorney / Judge'
    cleaning = 'Cleaning / Maintenance'
    construction = 'Construction / Tradesperson / Extraction'
    convenience = 'Convenience / Liquor Store Owner'
    counseling = 'Counseling / Therapy / Social Work'
    cryptocurrency = 'Cryptocurrency'
    currency = 'Currency Exchange / Transmitter'
    education = 'Education / Research'
    executive = 'Executive / Management Professional'
    finance = 'Finance / Banking / Insurance'
    fitness = 'Fitness / Health / Sports'
    gambling = 'Gambling / Gaming'
    government = 'Government / Civil Servant'
    hospitality = 'Hospitality / Travel / Tourism'
    import_export = 'Import / Export'
    jeweler = 'Jeweler / Gem / Metal Dealing'
    manufacturing = 'Manufacturing'
    medical = 'Medical / Dental / Veterinary / Pharmacy'
    non_profit = 'Non-Profit'
    parking = 'Parking Lot / Garage Operator'
    police = 'Police / Fire / Military / EMT / Security'
    real = 'Real Estate'
    religious = 'Religious Professional'
    restaurant = 'Restaurant / Food Service'
    retail = 'Retail / Sales / Service / Marketing'
    technology = 'Technology / Software Development'
    transportation = 'Transportation / Moving / Logistics'
    vending = 'Vending Machine Operator'
    other = 'Other'


class LoansHardshipReason:
    avoid = 'Avoid Bankruptcy'
    birth = 'Birth'
    divorced = 'Divorced'
    illness = 'Illness in Family'
    laid_off = 'Laid Off'
    loss_of_income = 'Loss of Income'
    loss_of_job = 'Loss of Job'
    medical = 'Medical Issues'
    other = 'Other'
    special = 'Special Needs Family'
    unexpected = 'Unexpected Expenses'
    widowed = 'Widowed'


class LoansAccountType:
    checking = 'Checking'
    saving = 'Saving'


class LoansAccountHolder:
    applicant = 'Applicant'
    co_applicant = 'Co-Applicant'
    joint = 'Joint'


class LoansDebtType:
    automobile = 'Automobile'
    business = 'Business'
    government = 'Government'
    unknown = 'Unknown'
    credit_card = 'Credit Card'


class LoansTypeOfPays:
    monthly = 'Monthly'
    bimonthly = 'Bi-Monthly'
    weekly = 'Weekly'
    beweekly = 'Be-Weekly'
    semimonthly = 'Semi-monthly'


class LoansHowToCalculate:
    base = 'Base gross income'
    ytd = 'YTD due to paystub showing regular OT or incentive income (bonus)'


class LoansBankStatementsReview:
    a_borrower_has_direct_deposits = 'A Borrower has Direct Deposits'
    negative_balance_detected = 'Negative Balance Detected'
    borrowers_primary_account = 'Borrower`s Primary Account'


class LoansCompany(NamedTuple):
    americor: str = 'Americor'
    credit9: str = 'Credit9'


class LoansApplicantData(NamedTuple):
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


class LoansCreateFormData(NamedTuple):
    first_name: str
    last_name: str
    phone_mobile: str
    zip_code: str
    # state: str
    city: str
    current_physical_address: str
    email: str
    # source: str
    # company: str


class LoansApplicantEmptyFieldsData(NamedTuple):
    number_of_months: str
    phone_home: str
    emergency_contact_name: str
    emergency_contact_number: str
    ssn: str
    dob: str
    dl: str
    mothers_maiden_name: str
    us_resident: bool = True


class LoansIncomeData(NamedTuple):
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


class LoansCoApplicantData(NamedTuple):
    status_income: int
    occupation: str
    primary_source_of_income: str
    length_years: int
    length_months: int
    phone_work: str
    net_monthly_income: int
    company_name: str
    primary_source_of_income: int


class LoansCreditorData(NamedTuple):
    id: str
    name: str
    account: str
    opened: str
    debt_type: str
    rate: float
    payment: str
    last_pay: str
    balance: str
    limit: str
    util: float


class LoansCreditorsTotalDataCalc(NamedTuple):
    total_creditors: int
    total_creditors_on_program: int
    total_monthly_payment: int
    total_debt: int
    average_interest_rate: str


class LoansCreditorsTotalData(NamedTuple):
    total_creditors: int
    total_creditors_on_program: int
    total_monthly_payment: int
    total_debt: int


class LoansCreditorsSectionData(NamedTuple):
    creditor: str
    total_debt: str
    interest_rate: float
    monthly_payment: str
    # balance_payoff: str
    # total_payments: str


class LoansCreditorsTotalUnsecuredDebtData(NamedTuple):
    creditors: str
    total_balance: str
    average_interest_rate: str
    monthly_payment: str
    # balance_payoff: str
    # total_payments: str


class LoansCreditorsAmericorProgram(NamedTuple):
    total_balance: int
    program_length: str
    interest_rate: str
    monthly_payment: float
    total_payments: float
    savings_from_balance: str
    savings: str


class LoansCreditorsAmericorLoanCredit9(NamedTuple):
    total_balance: int
    interest_rate: str
    americor_program_length: str
    monthly_payment: int


class LeadBudgetPageMonthlyDebtExpensesData(NamedTuple):
    government_student_loans: str
    private_student_loans: str
    medical_debt: str
    other_debt: str
    other_debt_desc: str
    back_taxes: str
    other_cards_outside_of_the_program: str
    other_cards_desc: str


class LoansBudgetData(NamedTuple):
    government_student_loans: int
    private_student_loans: int
    medical_debt: int
    other_debt: int
    back_taxes: int
    other_debt_description: str
    other_cards_outside_of_the_program: int
    other_cards_description: str
    housing: int
    housing_payment: int
    housing_payment_description: str
    homeowners_insurance: int
    tax: int
    hoa: int
    cable_tv_satellite: int
    cable_tv_satellite_description: str
    telephone: int
    telephone_description: str
    utilities: int
    utilities_description: str
    utilities_other: int
    utilities_other_description: str
    auto_loans: int
    auto_insurance: int
    auto_insurance_description: str
    auto_other: int
    house_hold_items: int
    clothing: int
    gym_health: int
    personal_care: int
    entertainment: int
    food: int
    food_description: str
    laundry_dry_cleaning: int
    misc: int
    life_insurance: int
    medical_care: int
    support: int
    alimony: int
    child_care: int
    nursing_care: int
    education: int
    charity_donations: int
    other_living_expenses: int
    other_living_expenses_description: str
    grounds_of_exemption: int
    grounds_of_exemption_description: str
    budget_note: str
    hardship_reason: str
    detailed_hardship_reason: str


class LoansCreditorsData(NamedTuple):
    total_debt: str
    interest_rate: str
    monthly_payment: str
    balance_payoff: str
    # total_payments: str


class LoansCreditorsDataUnsecuredDebt(NamedTuple):
    creditors_value: int
    summ_original_balance: int
    average_interest_rate: int
    monthly_payment: int
    balance_payoff: str


class LoansCreditorsAmericorProgramDebt(NamedTuple):
    total_balance: int
    program_length: str
    interest_rate: str
    monthly_payment: int
    total_payments: int
    savings_from_balance: str
    savings: str


class LoansSettlementOfferStatuses:
    draft = 'Draft'
    accepted = 'Accepted'
    deleted = 'Deleted'
    cancelled = 'Cancelled'
    need_sif_letter = 'Need SIF Letter'
    need_client_auth = 'Need Client Auth'
    need_acceptance = 'Need Acceptance'


class LoansCreditorDebtType:
    agricultural_loan = 'Agricultural Loan'
    appliance = 'Appliance/Furniture'
    attorney = 'Attorney Fees'
    credit_card = 'Credit Card'
    business_credit_card = 'Business Credit Card'


class LoansCreditorPoaSend:
    americor = 'Americor ATC Sent'
    higbee = 'Higbee ATC sent'
    sands = 'Sands ATC sent'


class LoansCreditorAdminDisposition:
    account_settled = 'Account Settled'
    answer_filed = 'Answer Filed'
    client_contacted = 'Client Contacted'


class LoansCreditorDisposition:
    account = 'Account Recalled to Original Creditor'
    account_is_current = 'Account is current'
    client = 'Client Declined Add Funds'
    client_settlement = 'Client Declined Settlement'
    client_states_paid = 'Client States Paid'
    client_unresponsive = 'Client Unresponsive'
    combined_balance = 'Combined Balance'
    combined_zero = 'Combined Zero Balance'


class LoansCreditorStatus:
    monthly = 'Charge off'
    collections = 'Collections'
    ne2020 = 'Defaulted Due to NE2020'
    due_to_nsf = 'Defaulted Due to NFS'
    settlement_working = 'Defaulted Settlement-Working'
    forgiven_by_creditor = 'Forgiven by Creditor'
    in_progress = 'In progress'
    legal_collections = 'Legal Collections'
    legal_defaulted = 'Legal Defaulted'
    placement_wait = 'Loan - Placement Wait'
    not_signed = 'Loan Not Signed'
    not_started = 'Not started'
    offer_made = 'Offer Made'
    on_scrublist = 'On scrublist'
    pending = 'Pending'
    poa_sent = 'Poa Sent'
    possible_default = 'Possible default - NFS'
    re_settled = 'Re-Settled'
    removed_from_program = 'Removed from Program'
    sent_back_to_creditor = 'Sent Back to Creditor'
    settled = 'Settled'
    summons_defaulted = 'Summons Defaulted'
    unaccepted = 'Unaccepted'


class LoansCreditorStatuses:
    in_progress = 'In progress'


class LoansCreditorPriority:
    bankruptcy = 'Bankruptcy'
    decease = 'Decease Client/Co-Client'
    overpayment = 'Overpayment to creditor/Refund'
    regular = 'Regular'
    urgent = 'Urgent'
    urgent_recalled = 'Urgent - Recalled'
    urgent_credit9 = 'Urgent Credit9'
    urgent_legal = 'Urgent Legal'
    verify_settlement = 'Verify Settlement'


class LoansCreditorsMainData(NamedTuple):
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


class LoansAchData(NamedTuple):
    name_of_account: str
    routing_number: str
    account_number: int
    bank_name: str
    bank_phone_number: str
    bank_address: str
    bank_city: str
    bank_state: str
    bank_zip: str


loans_pages = LoansPages()
loans_tabs = LoansTabs()
loans_types = LoansTypes()
loans_statuses = LoansStatuses()
loans_filters = LoansFilters()
loans_income_statuses = LoansIncomeStatuses()
loans_budget_housing_types = LoansBudgetHousingTypes()
loans_budget_ground_of_example_types = LoansBudgetGroundsOfExampleTypes()
loans_primary_sources = LoansPrimarySources()
loans_occupation = LoansOccupation()
loans_hardship_reason = LoansHardshipReason()
loans_account_type = LoansAccountType()
loans_account_holder = LoansAccountHolder()
loans_debt_type = LoansDebtType()
loans_type_of_pays = LoansTypeOfPays()
loans_how_to_calculate = LoansHowToCalculate()
loans_bank_statements_review = LoansBankStatementsReview()
loans_settlement_offer_statuses = LoansSettlementOfferStatuses()
loans_creditor_debt_type = LoansCreditorDebtType()
loans_creditor_poa_send = LoansCreditorPoaSend()
loans_creditor_priority = LoansCreditorPriority()
loans_creditor_status = LoansCreditorStatus()
loans_creditor_disposition = LoansCreditorDisposition()
loans_creditor_admin_disposition = LoansCreditorAdminDisposition()
loans_creditor_statuses = LoansCreditorStatuses()
