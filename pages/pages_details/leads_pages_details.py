from selenium.webdriver.common.by import By


"""
Значения букв в начале названий переменных:
E - element
F - field
B - button
T - text
TG - toggle
DL - dropdown list
CB - checkbox
RB - radio button
ET - error text
EE - error element
S - select
"""


ENDPOINT_LEADS = '/leads'
ENDPOINT_LEAD = '/lead'


class LeadsCommon:
    class Locators:
        # Communication panel
        B_CREATE_NOTE = (By.CSS_SELECTOR, '[data-toggle="create-note-modal"]')
        B_CREATE_EMAIL = (By.CSS_SELECTOR, '[data-toggle="send-email-modal"]')
        B_CREATE_TASK = (By.CSS_SELECTOR, '[data-toggle="create-task-modal"]')
        B_UNDO_REJECT = (By.XPATH, '//a[contains(text(), "Undo reject")]')
        F_NOTE_MODAL_EDITOR = (By.CSS_SELECTOR, '#NoteModal-form div.redactor-editor')
        F_EMAIL_MODAL_SUBJECT = (By.CSS_SELECTOR, '[id^=EmailFormModal] #emailformmodal-subject')
        F_EMAIL_MODAL_BODY = (By.CSS_SELECTOR, '[id^=EmailFormModal] .redactor-editor')
        F_TASK_MODAL_TITLE = (By.ID, 'createtaskform-title')
        F_TASK_MODAL_DESCRIPTION = (By.ID, 'createtaskform-description')
        DL_TASK_MODAL_CREDITOR = (By.ID, 'select2-createtaskform-customercreditorid-container')
        DL_TASK_MODAL_CREDITOR_LIST = (By.ID, 'select2-createtaskform-customercreditorid-results')
        F_TASK_MODAL_TITLE_LOAN = (By.ID, 'createmanualtaskcommandform-title')
        F_TASK_MODAL_DESCRIPTION_LOAN = (By.ID, 'createmanualtaskcommandform-description')
        DL_TASK_MODAL_CREDITOR_LOAN = (By.ID, 'select2-createmanualtaskcommandform-customercreditorid-container')
        DL_TASK_MODAL_CREDITOR_LIST_LOAN = (By.ID, 'select2-createmanualtaskcommandform-customercreditorid-results')
        F_REJECTED = (By.CSS_SELECTOR, '.panel-danger')
        F_SSN_EXIST = (By.CSS_SELECTOR, '.text-danger')
        F_SSN_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-personalid')

        # Communication form
        E_NOTE_TAB = (By.CSS_SELECTOR, '.nav-tabs [href="#note-tab"]')
        E_EMAIL_TAB = (By.CSS_SELECTOR, '.nav-tabs [href="#email-tab"]')
        E_SMS_TAB = (By.CSS_SELECTOR, '.nav-tabs [href="#sms-tab"]')
        F_NOTE_TAB_EDITOR = (By.CSS_SELECTOR, '#note-tab div.redactor-editor')
        F_EMAIL_TAB_EDITOR_SUBJECT = (By.CSS_SELECTOR, '#email-tab input#sendemailform-subject')
        F_EMAIL_TAB_EDITOR = (By.CSS_SELECTOR, '#email-tab div.redactor-editor')

        # email form
        DL_SENDER_CHOICE = (By.CSS_SELECTOR, '.field-emailformmodal-applicants_id .col-sm-11')
        E_SENDER_EMAIL_APP = (By.CSS_SELECTOR, 'ul.select2-results__options li')
        E_SENDER_EMAIL_CO_APP = (By.CSS_SELECTOR, 'ul.select2-results__options li:nth-child(2)')
        B_SENDER_CHOICE_REMOVE = (By.CSS_SELECTOR, 'ul.select2-selection__rendered li span')
        B_TEMPLATES = (By.XPATH, "//form[contains(@id, 'EmailFormModal-form')]//a[contains(text(), 'Templates')]")
        T_EMAIL_BODY = (By.CSS_SELECTOR, '#emails-pjax .redactor-editor')

        # Reassign Lead
        B_REASSIGN = (By.CSS_SELECTOR, '[data-toggle="reassign-modal"]')
        DL_REASSIGN_SALES_REP = (By.CSS_SELECTOR, 'span #select2-reassignleadform-sales_rep_id-container')
        DL_REASSIGN_UNDERWRITER = (By.ID, 'select2-reassignform-underwriterid-container')
        DL_REASSIGN_LOC = (By.ID, 'select2-reassignform-locprocessorid-container')
        F_REASSIGN_INPUT = (By.CSS_SELECTOR, '.select2-search--dropdown .select2-search__field')
        B_REASSIGN_SAVE = (By.CSS_SELECTOR, ' .btn-save')
        E_STATUS = (By.CSS_SELECTOR, '[data-id="changestatusform-status"]')
        B_UPLOAD_DOCUMENT = (By.ID, 'emailformmodal-attachmentfiles')
        B_SAVE_REASON_MODAL = (By.CSS_SELECTOR, '.modal-footer .btn-success')

    class LocatorsBrokers:
        F_NOTE_MODAL_EDITOR = (By.CSS_SELECTOR, '#create-note-popup-form .redactor-editor')
        B_CREATE_NOTE = (By.CSS_SELECTOR, '[data-toggle="create-note-modal"]')
        DL_REJECT_REASON = (By.ID, 'select2-rejectleadform-rejectreason-container')
        B_REJECT_MODAL = (By.CSS_SELECTOR, '.modal-footer .btn-success')
        T_STATUS_REJECTED_LEAD = (By.CSS_SELECTOR, '.panel-heading .panel-title')
        T_REASON_REJECTED_LEAD = (By.CSS_SELECTOR, '.panel-subheading .panel-title button span')
        DL_REASSIGN_SALES_REP = (By.CSS_SELECTOR, 'span #select2-reassignleadform-sales_rep_id-container')
        B_SAVE_AND_CLOSE = (By.CSS_SELECTOR, '[data-bb-handler="saveClose"]')


class Leads:
    ENDPOINT = '/lead'
    ENDPOINT_BROKER = '/lead'

    TITLE = 'Leads'

    class Locators:
        B_CREATE_NEW = (By.XPATH, "//a[contains(text(), 'Create New')]")
        # Reassign Lead
        B_REASSIGN = (By.CSS_SELECTOR, '[data-toggle="reassign-modal"]')  # del
        DL_REASSIGN_SALES_REP = (By.CSS_SELECTOR, 'span #select2-reassignleadform-sales_rep_id-container')  # del
        DL_REASSIGN_UNDERWRITER = (By.ID, 'select2-reassignform-underwriterid-container')
        DL_REASSIGN_LOC = (By.ID, 'select2-reassignform-locprocessorid-container')
        F_REASSIGN_INPUT = (By.CSS_SELECTOR, '.select2-search--dropdown .select2-search__field')  # del
        B_REASSIGN_SAVE = (By.CSS_SELECTOR, ' .btn-save')  # del
        # Send Docs
        B_SEND_DOCS = (By.CSS_SELECTOR, 'i.icon.glyphicon.glyphicon-send')
        B_AGREEMENT_ONLY = (By.XPATH, "//a[normalize-space(text())='Agreement only']")
        T_SEND_DOCS_ERROR = (By.CSS_SELECTOR, '.toast.toast-error')

    class LocatorsBrokers:
        B_CREATE_NEW = (By.XPATH, "//a[contains(text(), 'Create New')]")
        # Reassign Lead
        B_REASSIGN = (By.CSS_SELECTOR, '[data-toggle="reassign-modal"]')  # del
        DL_REASSIGN_SALES_REP = (By.CSS_SELECTOR, 'span #select2-reassignleadform-sales_rep_id-container')  # del
        DL_REASSIGN_UNDERWRITER = (By.ID, 'select2-reassignform-underwriterid-container')
        DL_REASSIGN_LOC = (By.ID, 'select2-reassignform-locprocessorid-container')
        F_REASSIGN_INPUT = (By.CSS_SELECTOR, '.select2-search--dropdown .select2-search__field')  # del
        B_REASSIGN_SAVE = (By.CSS_SELECTOR, ' .btn-save')  # del
        # Send Docs
        B_SEND_DOCS = (By.CSS_SELECTOR, 'i.icon.glyphicon.glyphicon-send')
        B_AGREEMENT_ONLY = (By.XPATH, "//a[normalize-space(text())='Agreement only']")
        T_SEND_DOCS_ERROR = (By.CSS_SELECTOR, '.toast.toast-error')

        E_FIRST_LEAD = (By.XPATH, '//*[@id="w1"]/table/tbody/tr[1]/td[1]')
        B_NOTE_ADD = (By.CSS_SELECTOR, '[data-toggle="create-note-modal"]')
        F_NOTE = (By.XPATH, '//*[@id="create-note-popup-form"]/div/div/div/div')
        B_SAVE = (By.XPATH, '//*[@id="create-note-popup-form"]/button[1]')
        E_KPI_DATA = (By.XPATH, '//*[@id="w0"]/table/tbody')
        B_REJECT = (By.CSS_SELECTOR, '[data-bb-handler="reject"]')
        B_SAVE_AND_CLOSE = (By.CSS_SELECTOR, '[data-bb-handler="saveClose"]')


class LeadsCreate:
    ENDPOINT = f'{ENDPOINT_LEAD}/create'
    ENDPOINT_BROKER = f'{ENDPOINT_LEAD}/create'

    class Locators:
        F_FIRST_NAME = (By.ID, 'createleadform-firstname')
        F_LAST_NAME = (By.ID, 'createleadform-lastname')
        F_CLIENT_PHONE = (By.ID, 'createleadform-clientphone')
        F_ZIP = (By.ID, 'createleadform-zip')
        DL_STATE = (By.ID, 'createleadform-state')
        F_CITY = (By.ID, 'createleadform-city')
        F_ADDRESS = (By.ID, 'createleadform-address')
        F_EMAIL = (By.ID, 'createleadform-email')
        CB_NO_EMAIL = (By.ID, 'createleadform-noemail')
        DL_SOURCE = (By.CSS_SELECTOR, '[aria-labelledby="select2-createleadform-source-container"]')
        DL_COMPANY = (By.CSS_SELECTOR, '[aria-labelledby="select2-createleadform-company-container"]')
        T_SOURCE = (By.ID, 'createleadform-source')
        T_COMPANY = (By.ID, 'createleadform-company')
        B_SAVE = (By.CSS_SELECTOR, '.btn-success')
        ET_FIELDS_ERRORS = (By.CSS_SELECTOR, 'small.text-danger')  # del

    class LocatorsBrokers:
        F_FIRST_NAME = (By.ID, 'createleadcommandform-firstname')
        F_LAST_NAME = (By.ID, 'createleadcommandform-lastname')
        F_PHONE = (By.ID, 'createleadcommandform-clientphone')
        F_PASSWORD = (By.ID, 'createbrokeruserform-password')
        F_ZIP = (By.ID, 'createleadcommandform-zip')
        DL_STATE = (By.ID, 'createleadcommandform-state')
        F_CITY = (By.ID, 'createleadcommandform-city')
        F_ADDRESS = (By.ID, 'createleadcommandform-address')
        F_EMAIL = (By.ID, 'createleadcommandform-email')
        DL_SOURCE = (By.CSS_SELECTOR, '[aria-labelledby="select2-createleadcommandform-source-container"]')
        CB_NO_EMAIL = (By.ID, 'createleadcommandform-noemail')
        T_INCOME_SOURCE_HEADERS = (By.CSS_SELECTOR, '.js-income-source-header')
        B_REMOVE = (By.CSS_SELECTOR, '.js-income-source-remove')
        DL_STATUS = (By.ID, 'select2-applicantincomesourcecommandform-0-status-container')
        B_SAVE = (By.CSS_SELECTOR, '[data-bb-handler="send"]')
        B_ARROW = (By.CSS_SELECTOR, '.fa-angle-right')


class LeadsHistory:
    ENDPOINT = f'{ENDPOINT_LEAD}/history?id='
    ENDPOINT_BROKER = f'{ENDPOINT_LEAD}/main?id='

    class Locators:
        # Left sidebar
        T_HISTORY_TASK_CREDITOR = None
        T_SALES_REP = (By.XPATH, "//b[normalize-space(text())='Sales Rep']/following::span")
        B_ARROW = (By.CSS_SELECTOR, '.fa-angle-right')
        T_SIGN_DOCS_LINK = (By.CSS_SELECTOR, '#description p:nth-child(4) a')
        B_SMS_CONSENT = (By.CSS_SELECTOR, '[data-action="button-active_w4"]')
        B_REASSIGN = (By.CSS_SELECTOR, '[data-toggle="reassign-modal"]')
        DL_REASSIGN_SALES_REP = (By.CSS_SELECTOR, 'span #select2-reassignleadform-sales_rep_id-container')
        F_REASSIGN_INPUT = (By.CSS_SELECTOR, '.select2-search--dropdown .select2-search__field')
        B_SEND_DOCS = (By.CSS_SELECTOR, 'i.icon.glyphicon.glyphicon-send')
        B_AGREEMENT_ONLY = (By.XPATH, "//a[normalize-space(text())='Agreement only']")
        T_SEND_DOCS_ERROR = (By.CSS_SELECTOR, '.toast.toast-error')
        B_EMAIL_PAGE = (By.CSS_SELECTOR, '[data-toggle="send-email-modal"]')
        E_STATUS = (By.CSS_SELECTOR, '[data-id="changestatusandcallbackcommandform-status"]')

        B_SAVE = (By.CSS_SELECTOR, '.btn-success')
        B_LOCKED = (By.ID, 'docs-sent-locked-block')
        B_COPY_EMAIL = (By.ID, 'DontUseWEBuseAPI')
        B_ACCOUNT_EMAIL = (By.ID, 'accounts-menu')
        B_EMAIL_LOGIN = (By.ID, 'address')
        B_EMAIL_PASSWORD = (By.ID, 'password')
        B_LOGIN_EMAIL = (By.XPATH, '//*[@id="accounts-list"]/div/div[4]/a')
        B_DELETE_EMAIL = (By.XPATH, '//*[@id="__layout"]/div/div[2]/main/div/div[2]/div[2]/span[4]/button')
        B_OPEN_EMAIL = (By.CSS_SELECTOR, '.divide-gray-200')

        # History
        T_HISTORY_NOTE_TEXT = (By.CSS_SELECTOR, '[id^=editable-note] div.kv-editable-value')
        T_HISTORY_EVENT_SUBJECT = (By.XPATH, '//*[@id="w0"]/li[4]/div/div[1]/div/div[1]')
        T_HISTORY_EMAIL_SUBJECT = (By.XPATH, "//label[normalize-space(text())='Subject:']/following::span")
        T_HISTORY_EMAIL_IFRAME_TEXT = (By.CSS_SELECTOR, 'body p')
        T_HISTORY_EMAIL_IFRAME_TEXT_CHOICE = (By.CSS_SELECTOR, 'body')
        T_ATTACHMENTS_EMAIL_IFRAME_TEXT = (By.XPATH, '//*[@id="emails-pjax-22260637"]/a')
        T_HISTORY_TASK_TITLE = (By.CSS_SELECTOR, 'div.list-group-message')
        T_HISTORY_SALES_REP = (By.XPATH, "//div[normalize-space(text())='Sales Rep reassigned']/span[3]")
        F_CALLBACK_DATE = (By.ID, 'changestatusandcallbackcommandform-callbackdate')
        F_CALLBACK_TIME = (By.ID, 'changestatusandcallbackcommandform-callbacktime')

        B_SEND_IN_FINANCIAL_PROFILE = (By.XPATH, "//button[text()='Send']")

        # financial profile
        T_CLIENT_NAME_FP = (By.CSS_SELECTOR, '.profile-info div:first-child dd')
        T_BODY_MESSAGE_TEXT = (By.CSS_SELECTOR, 'body')

        # history tabs
        DL_SENDER_CHOICE_TAB = (By.CSS_SELECTOR, '#email-tab .col-sm-11')
        E_SENDER_EMAIL_APP_TAB = (By.CSS_SELECTOR, 'ul.select2-results__options li')
        E_SENDER_EMAIL_CO_APP_TAB = (By.CSS_SELECTOR, 'ul.select2-results__options li:nth-child(2)')
        F_EMAIL_SUBJECT_TAB = (By.CSS_SELECTOR, 'input#sendemailform-subject')
        F_EMAIL_BODY_TAB = (By.CSS_SELECTOR, '#email-tab .redactor-editor')
        E_EMAIL_ATTACHMENT_TAB = (By.CSS_SELECTOR, 'input#sendemailform-attachmentfiles')
        B_TEMPLATES_TAB = (By.XPATH, "//form[contains(@id, 'SendEmailForm-form')]//a[contains(text(), 'Templates')]")
        F_SMS_BODY_TAB = (By.NAME, "SendSmsForm[message]")

    class LocatorsBrokers:
        # History
        T_HISTORY_NOTE_TEXT = (By.CSS_SELECTOR, '[id^=editable-note] div.kv-editable-value')
        T_HISTORY_TASK_TITLE = (By.CSS_SELECTOR, 'div.list-group-message')
        T_HISTORY_SALES_REP = (By.XPATH, "//div[normalize-space(text())='Sales Rep reassigned']/span[3]")


class LeadsProfile:
    ENDPOINT = f'{ENDPOINT_LEAD}/profile?id='
    ENDPOINT_BROKER = f'{ENDPOINT_LEAD}/profile?id='

    class Locators:
        B_EXPERIAN = (By.XPATH, "//button[normalize-space(text())='Experian']")
        B_SAVE = (By.CSS_SELECTOR, '.btn-success')
        B_LOCKED = (By.ID, 'docs-sent-locked-block')
        B_COPY_EMAIL = (By.ID, 'DontUseWEBuseAPI')
        B_ACCOUNT_EMAIL = (By.ID, 'accounts-menu')
        B_EMAIL_LOGIN = (By.ID, 'address')
        B_EMAIL_PASSWORD = (By.ID, 'password')
        B_LOGIN_EMAIL = (By.XPATH, '//*[@id="accounts-list"]/div/div[4]/a')
        B_DELETE_EMAIL = (By.XPATH, '//*[@id="__layout"]/div/div[2]/main/div/div[2]/div[2]/span[4]/button')
        B_OPEN_EMAIL = (By.CSS_SELECTOR, '.divide-gray-200')
        TG_CO_APPLICANT = (By.ID, 'updatecustomerprofilecommandform-coapplicantenabled')
        E_SPINNER_EXPERIAN = (
            By.CSS_SELECTOR,
            '.field-updatecustomerprofilecommandform-primaryapplicantcreditreportsource button span.ladda-spinner'
        )
        B_SALES_PHASE = (By.CSS_SELECTOR, '[data-id="changecustomersalesphaseform-salesphase"]')
        B_SALES_PHASE_CHOOSE = (By.CSS_SELECTOR, '[data-original-index="4"]')

        # applicant fields
        F_FIRSTNAME_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-firstname')
        F_LASTNAME_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-lastname')
        F_PHONE_MOBILE_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-phonemobile')
        F_PHONE_HOME_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-phonehome')
        F_EMERGENCY_NAME_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-emergencyname')
        F_EMERGENCY_NUMBER_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-emergencyphone')
        F_DL_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-dln')
        F_EMAIL_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-email')
        F_CURRENT_PHYSICAL_ADDRESS_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-address')
        F_ZIP_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-zip')
        DL_STATE_APPLICANT = (
            By.CSS_SELECTOR, '[aria-labelledby="select2-updatecustomerprofileprimaryapplicantform-state-container"]')
        DL_STATE_CLOSE_APPLICANT = (By.CSS_SELECTOR, )
        F_ADDRESS_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-address')
        F_CITY_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-city')
        F_SSN_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-personalid')
        F_SSN_BROKERS_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-ssn')
        F_DOB_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-dob')
        F_MOTHER_MAIDEN_NAME_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-mothersmaidenname')
        F_NUMBER_OF_MONTH_APPLICANT = (By.ID, 'updatecustomerprofileform-numberofmonthsstrugglingwithdebt')
        TG_US_RESIDENT_APPLICANT = (By.ID, 'updatecustomerprofileprimaryapplicantform-usresident')
        TG_ACTIVE_MILITARY_APPLICANT = (
            By.CSS_SELECTOR, '[for="updatecustomerprofileprimaryapplicantform-activemilitary"]')
        TG_ACTIVE_SECURITY_APPLICANT = (
            By.CSS_SELECTOR, '[for="updatecustomerprofileprimaryapplicantform-securityclearance"]')
        TG_ACTIVE_SPANISH_SPEAKER_APPLICANT = (
            By.CSS_SELECTOR, '[for="updatecustomerprofileprimaryapplicantform-spanishspeaker"]')
        TG_LABEL_FALSE_APPLICANT = (By.CSS_SELECTOR, '[data-switchery-reset-value="0"]')
        TG_LABEL_TRUE_APPLICANT = (By.CSS_SELECTOR, '[data-switchery-reset-value="1"]')
        F_FIRSTNAME_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-firstname')
        F_LASTNAME_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-lastname')
        F_FIRSTNAME_CO_APPLICANT_FOR_EMAIL = (By.ID, 'enrollmentcoapplicantprofileform-firstname')
        F_LASTNAME_CO_APPLICANT_FOR_EMAIL = (By.ID, 'enrollmentcoapplicantprofileform-lastname')
        F_PHONE_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-phonemobile')
        F_HOME_PHONE_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-phonehome')
        F_EMERGENCY_NAME_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-emergencyname')
        F_EMERGENCY_NUMBER_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-emergencyphone')
        F_DL_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-dln')
        F_EMAIL_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-email')
        F_EMAIL_CO_APPLICANT_FOR_EMAIL = (By.ID, 'enrollmentcoapplicantprofileform-email')
        TG_US_RESIDENT_CO_APPLICANT = (By.XPATH, '//*[@id="form-coApplicant"]/div[2]/div[1]/div[1]/label')
        F_ZIP_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-zip')
        DL_STATE_CO_APPLICANT = (
            By.CSS_SELECTOR, '[aria-labelledby="select2-updatecustomerprofilecoapplicantform-state-container"]')
        F_SSN_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-personalid')
        F_DOB_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-dob')
        F_MOTHER_MAIDEN_NAME_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-mothersmaidenname')
        F_ADDRESS_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-address')
        F_STATE_CO_APPLICANT = (
            By.CSS_SELECTOR, '[aria-labelledby="select2-updatecustomerprofilecoapplicantform-state-container"]')
        F_STATE_CO_APPLICANT_FOR_EMAIL = (
            By.CSS_SELECTOR,
            '[aria-labelledby="select2-enrollmentcoapplicantprofileform-state-container"]')
        F_STATE_CO_APPLICANT_INSIDE = (By.ID, 'select2-updatecustomerprofilecoapplicantform-state-container')
        F_CITY_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-city')
        B_EXPERIAN_APPLICANT = (
            By.CSS_SELECTOR, "[name='UpdateCustomerProfileForm[primaryApplicantCreditReportSource]']")
        B_EXPERIAN_BROKER_APPLICANT = (
            By.CSS_SELECTOR, '[name="UpdateCustomerProfileCommandForm[primaryApplicantCreditReportSource]"]')
        TG_US_RESIDENCE_CO_APPLICANT = (By.ID, 'updatecustomerprofilecoapplicantform-usresident')
        B_EXPERIAN_CO_APPLICANT = (
            By.CSS_SELECTOR, "[name='UpdateCustomerProfileForm[coApplicantCreditReportSource]'][value=experian]")
        B_SMS_CONSENT = (By.CSS_SELECTOR, '[data-action="button-active"]')
        TG_SPANISH = (By.CSS_SELECTOR, '[for="updatecustomerprofileprimaryapplicantform-spanishspeaker"]')
        F_STATUS_INCOME = (By.ID, 'select2-applicantincomesourcecommandform-0-status-container')
        F_OCCUPATION_INCOME = (By.ID, 'select2-applicantincomesourcecommandform-0-occupation-container')
        F_LENGTH_YEARS_INCOME = (By.ID, 'applicantincomesourcecommandform-0-lengthyears')
        F_LENGTH_MONTHS_INCOME = (By.ID, 'applicantincomesourcecommandform-0-lengthmonths')
        F_PRIMARY_SOURCE_INCOME = (By.ID, 'select2-applicantincomesourcecommandform-0-primarysourceofincome-container')
        F_PHONE_WORK_INCOME = (By.ID, 'applicantincomesourcecommandform-0-phone')
        F_NET_MONTHLY_INCOME = (By.ID, 'applicantincomesourcecommandform-0-netmonthlyincome')
        F_COMPANY_NAME_INCOME = (By.ID, 'applicantincomesourcecommandform-0-name')
        E_AVATAR = (By.CSS_SELECTOR, '.navbar-avatar')
        E_ALREADY_EXIST_ALERT = (By.CSS_SELECTOR, 'div.sweet-alert')
        E_ALREADY_COAPPLICANT_EXIST_ALERT = (By.CLASS_NAME, 'sa-button-container')


class LeadsCreditors:
    ENDPOINT = f'{ENDPOINT_LEAD}/creditors?id='
    ENDPOINT_BROKER = f'{ENDPOINT_LEAD}/creditors?id='

    class Locators:
        F_CREDITOR_TOTAL_PAYMENTS_FROM_UNSECURED_DEBT_SECTION = None
        E_CREDITOR_FORM = (By.ID, 'creditor-form')
        DL_CREDITOR = (By.CSS_SELECTOR, '[aria-labelledby="select2-createcreditorform-creditorid-container"]')
        F_CREDITOR_SEARCH_FIELD = (By.CSS_SELECTOR, '[aria-controls="select2-createcreditorform-creditorid-results"]')
        F_ORIGINAL_BALANCE = (By.ID, 'createcreditorform-balance')
        F_ACCOUNT = (By.ID, 'createcreditorform-accountnumber')
        F_PAYMENT = (By.ID, 'createcreditorform-monthlypayment')
        F_CARDHOLDER_NAME = (By.ID, 'createcreditorform-cardholdername')
        F_LAST_PAY = (By.ID, 'createcreditorform-creditreportlastpaymentdate')
        F_LIMIT = (By.ID, 'createcreditorform-creditlimit')
        F_OPENED_DATE = (By.ID, 'createcreditorform-dateopened')
        DL_DEBT_TYPE = (By.CSS_SELECTOR, '[aria-labelledby="select2-createcreditorform-typeofdebt-container"]')
        E_CREDITOR_END_PAGE_ELEMENT = (By.XPATH, '//*[@id="w12"]/tbody/tr[2]/td/span')
        E_CREDITOR_ANY_LIST_ELEMENT = (By.CSS_SELECTOR, 'td:nth-child(9) input')
        F_COMPANY_CREDITOR = (By.CSS_SELECTOR, '[aria-labelledby="select2-createcreditorform-creditorid-container"]')
        F_COMPANY2_CREDITOR = (By.CSS_SELECTOR, '[aria-controls="select2-createcreditorform-creditorid-results"]')
        F_ORIGINAL_BALANCE_CREDITOR = (By.ID, 'createcreditorform-balance')
        F_ACCOUNT_CREDITOR = (By.ID, 'createcreditorform-accountnumber')
        F_PAYMENTS_CREDITOR = (By.ID, 'createcreditorform-monthlypayment')
        F_CARDHOLDER_CREDITOR = (By.ID, 'createcreditorform-cardholdername')
        F_LASTPAY_CREDITOR = (By.ID, 'createcreditorform-lastpayment')
        F_LIMIT_CREDITOR = (By.ID, 'createcreditorform-creditlimit')
        F_OPENED_DATE_CREDITOR = (By.ID, 'createcreditorform-dateopened')
        F_DEBT_TYPE_CREDITOR = (By.CSS_SELECTOR, '[aria-labelledby="select2-createcreditorform-typeofdebt-container"]')
        F_DELETE_CREDITOR = (By.CSS_SELECTOR, '.jsgrid-delete-button')
        F_INPUT_EDIT_CREDITOR_ACCOUNT = (By.XPATH, '//*[@id="w1"]/div[1]/table/tbody/tr[1]/td[3]/input')
        F_INPUT_EDIT_CREDITOR_RATE = (By.XPATH, '//*[@id="w1"]/div[1]/table/tbody/tr[1]/td[6]/input')
        F_INPUT_EDIT_CREDITOR_PAYMENT = (By.XPATH, '//*[@id="w1"]/div[1]/table/tbody/tr[1]/td[7]/input')
        F_INPUT_EDIT_CREDITOR_LASTPAY = (By.XPATH, '//*[@id="w1"]/div[1]/table/tbody/tr[1]/td[10]/input')
        F_INPUT_EDIT_CREDITOR_BALANCE = (By.XPATH, '//*[@id="w1"]/div[1]/table/tbody/tr[1]/td[11]/input')

        T_ID_BY_NAME_CREDITOR = '//td[contains(text(), "{creditor}")]//preceding-sibling::td'
        T_NAME_BY_NAME_CREDITOR = '//td[contains(text(), "{creditor}")]'
        T_ACCOUNT_BY_NAME_CREDITOR = '//td[contains(text(), "{creditor}")]//following::td'
        T_OPENED_BY_NAME_CREDITOR = '//td[contains(text(), "{creditor}")]//following::td[2]'
        T_DEBT_TYPE_BY_NAME_CREDITOR = '//td[contains(text(), "{creditor}")]//following::td[3]'
        T_RATE_BY_NAME_CREDITOR = '//td[contains(text(), "{creditor}")]//following::td[4]'
        T_PAYMENT_BY_NAME_CREDITOR = '//td[contains(text(), "{creditor}")]//following::td[5]'
        T_LAST_PAY_BY_NAME_CREDITOR = '//td[contains(text(), "{creditor}")]//following::td[9]'
        T_BALANCE_BY_NAME_CREDITOR = '//td[contains(text(), "{creditor}")]//following::td[11]'
        T_LIMIT_BY_NAME_CREDITOR = '//td[contains(text(), "{creditor}")]//following::td[12]'
        T_UTIL_BY_NAME_CREDITOR = '//td[contains(text(), "{creditor}")]//following::td[13]'
        E_ALL_CREDITORS = (By.CSS_SELECTOR, '.jsgrid-grid-body tbody tr')
        TG_INCLUDED = (By.CSS_SELECTOR, '.jsgrid-grid-body tbody tr td:nth-child(9)')
        TG_ALL_CREDITORS = (By.XPATH, '//tbody//input[@name="isIncluded"]')
        T_ALL_CREDITORS_NAME_BY_TG_INCLUDED = (By.XPATH, '//tbody//input[@name="isIncluded"]//preceding::td[7]')

        # all creditors data
        T_ID_CREDITOR = '//*[@id="w2"]/div[1]/table/tbody/tr[{line}]/td[2]'
        T_NAME_CREDITOR = '//*[@id="w2"]/div[1]/table/tbody/tr[{line}]/td[3]'
        T_ACCOUNT_CREDITOR = '//*[@id="w2"]/div[1]/table/tbody/tr[{line}]/td[4]'
        T_OPENED_CREDITOR = '//*[@id="w2"]/div[1]/table/tbody/tr[{line}]/td[5]'
        T_DEBT_TYPE_CREDITOR = '//*[@id="w2"]/div[1]/table/tbody/tr[{line}]/td[6]'
        T_RATE_CREDITOR = '//*[@id="w2"]/div[1]/table/tbody/tr[{line}]/td[7]'
        T_PAYMENT_CREDITOR = '//*[@id="w2"]/div[1]/table/tbody/tr[{line}]/td[8]'
        T_INCLUDED_CREDITOR = '//*[@id="w2"]/div[1]/table/tbody/tr[{line}]/td[11]/input'
        T_LAST_PAY_CREDITOR = '//*[@id="w2"]/div[1]/table/tbody/tr[{line}]/td[12]'
        T_BALANCE_CREDITOR = '//*[@id="w2"]/div[1]/table/tbody/tr[{line}]/td[14]'
        T_LIMIT_CREDITOR = '//*[@id="w2"]/div[1]/table/tbody/tr[{line}]/td[15]'
        T_UTIL_CREDITOR = '//*[@id="w2"]/div[1]/table/tbody/tr[{line}]/td[16]'
        T_ROLE_CREDITOR = '//*[@id="w2"]/div[1]/table/tbody/tr[{line}]/td[18]'

        T_TOTAL_CREDITORS = (By.CSS_SELECTOR, '#creditors-calculators-pjax .clearfix div:nth-child(1) span')
        T_TOTAL_CREDITORS_ON_PROGRAM = (By.CSS_SELECTOR, '#creditors-calculators-pjax .clearfix div:nth-child(2) span')
        T_TOTAL_MONTHLY_PAYMENT = (By.CSS_SELECTOR, '#creditors-calculators-pjax .clearfix div:nth-child(3) span')
        T_TOTAL_DEBT = (By.CSS_SELECTOR, '#creditors-calculators-pjax .clearfix div:nth-child(4) span')

        F_ORIG_BALANCE_CREDITOR = (By.XPATH, '//*[@id="w1"]/div[1]/table/tbody/tr[1]/td[11]')
        F_ORIG_BALANCE_2_CREDITOR = (By.XPATH, '//*[@id="w1"]/div[1]/table/tbody/tr[2]/td[11]')
        F_RATE_CREDITOR = (By.XPATH, '//*[@id="w1"]/div[1]/table/tbody/tr[1]/td[6]')
        F_MONTHLY_PAYMENT_CREDITOR = (By.XPATH, '//*[@id="w1"]/div[1]/table/tbody/tr[1]/td[7]')
        F_AVERAGE_INTEREST_RATE_1_CREDITOR = (By.XPATH, '//*[@id="w1"]/div[1]/table/tbody/tr[1]/td[6]')
        F_AVERAGE_INTEREST_RATE_2_CREDITOR = (By.XPATH, '//*[@id="w1"]/div[1]/table/tbody/tr[2]/td[6]')
        F_PAYMENT_1_CREDITOR = (By.XPATH, '//*[@id="w1"]/div[1]/table/tbody/tr[1]/td[7]')
        F_PAYMENT_2_CREDITOR = (By.XPATH, '//*[@id="w1"]/div[1]/table/tbody/tr[2]/td[7]')

        # creditors section
        T_CREDITOR_CREDITORS_SECTION = (By.XPATH, '//*[@id="w5"]/tbody/tr[1]/td/span/select/option[1]')
        T_TOTAL_DEBT_CREDITORS_SECTION = (By.XPATH, '//*[@id="w5"]/tbody/tr[2]/td/span')
        T_INTEREST_RATE_CREDITORS_SECTION = (By.XPATH, '//*[@id="w5"]/tbody/tr[3]/td/span')
        T_MONTHLY_PAYMENT_CREDITORS_SECTION = (By.XPATH, '//*[@id="w5"]/tbody/tr[4]/td/span')
        T_BALANCE_PAYOFF_CREDITORS_SECTION = (By.XPATH, '//*[@id="w5"]/tbody/tr[5]/td/span')

        # total unsecured debt section
        T_CREDITORS_TOTAL_UNSECURED_DEBT_SECTION = (
            By.XPATH,
            "//h4[text()='Total Unsecured Debt']/following::label[text()='Creditors:']/following-sibling::span"
        )
        T_TOTAL_BALANCE_TOTAL_UNSECURED_DEBT_SECTION = (
            By.XPATH,
            "//h4[text()='Total Unsecured Debt']/following::label[text()='Total balance:']/following-sibling::span/span"
        )
        T_AVERAGE_INTEREST_RATE_TOTAL_UNSECURED_DEBT_SECTION = (
            By.XPATH,
            "//h4[text()='Total Unsecured Debt']/following::"
            "label[text()='Average Interest Rate:']/following-sibling::span"
        )
        T_MONTHLY_PAYMENT_TOTAL_UNSECURED_DEBT_SECTION = (
            By.XPATH,
            "//h4[text()='Total Unsecured Debt']/following::label[text()='Monthly payment:']/following-sibling::span"
        )
        T_BALANCE_PAYOFF_TOTAL_UNSECURED_DEBT_SECTION = (By.XPATH, '//*[@id="w6"]/tbody/tr[6]/td/span')

        # americor program
        T_TOTAL_BALANCE_AMERICOR_PROGRAM_SECTION = (By.XPATH, '//*[@id="w7"]/tbody/tr[1]/td/span')
        T_PROGRAM_LENGTH_AMERICOR_PROGRAM_SECTION = (By.XPATH, '//*[@id="w7"]/tbody/tr[2]/td/span')
        T_INTEREST_RATE_AMERICOR_PROGRAM_SECTION = (By.XPATH, '//*[@id="w7"]/tbody/tr[3]/td/span')
        T_MONTHLY_PAYMENT_AMERICOR_PROGRAM_SECTION = (By.XPATH, '//*[@id="w7"]/tbody/tr[4]/td/span')
        T_TOTAL_PAYMENTS_AMERICOR_PROGRAM_SECTION = (By.XPATH, '//*[@id="w7"]/tbody/tr[5]/td/span')
        T_SAVINGS_FROM_BALANCE_AMERICOR_PROGRAM_SECTION = (By.XPATH, '//*[@id="w7"]/tbody/tr[6]/td/span')
        T_SAVINGS_AMERICOR_PROGRAM_SECTION = (By.XPATH, '//*[@id="w7"]/tbody/tr[7]/td/span')

        # americor + loan (credit9)
        F_CREDITOR_TOTAL_BALANCE_FROM_AMERICOR_LOAN_CREDIT9_SECTION = (By.XPATH, '//*[@id="w11"]/tbody/tr[1]/td/span')
        F_CREDITOR_INTEREST_RATE_FROM_AMERICOR_LOAN_CREDIT9_SECTION = (By.XPATH, '//*[@id="w11"]/tbody/tr[2]/td/span')
        F_CREDITOR_LENGTH_FROM_AMERICOR_LOAN_CREDIT9_SECTION = (By.XPATH, '//*[@id="w11"]/tbody/tr[3]/td/span')
        F_CREDITOR_MONTHLY_PAYMENT_FROM_AMERICOR_LOAN_CREDIT9_SECTION = (By.XPATH, '//*[@id="w11"]/tbody/tr[4]/td/span')


class LeadsIncome:
    ENDPOINT = f'{ENDPOINT_LEAD}/income?id='
    ENDPOINT_BROKER = f'{ENDPOINT_LEAD}/income?id='

    class Locators:
        TG_MARK_AS_PRIMARY = '.field-applicantincomesourcecommandform-{count}-isprimary .switchery-small'
        TG_UPFRONT_MARK_AS_PRIMARY = ('.field-applicantincomesourceextendedcommandform-{count}-'
                                      'isprimary .switchery-small')
        T_MARK_AS_PRIMARY = 'applicantincomesourcecommandform-{count}-isprimary'
        DL_STATUS = '[aria-labelledby="select2-applicantincomesourcecommandform-{count}-status-container"]'
        DL_STATUS_CO_APPLICANT = ('[aria-labelledby="select2-coapplicantincomesourcecommandform-'
                                  '{count}-status-container"]')
        T_STATUS = 'select2-applicantincomesourcecommandform-{count}-status-container'
        DL_OCCUPATION = '[aria-labelledby="select2-applicantincomesourcecommandform-{count}-occupation-container"]'
        DL_OCCUPATION_CO_APPLICANT = ('[aria-labelledby="select2-coapplicantincomesourcecommandform-'
                                      '{count}-occupation-container"]')
        T_OCCUPATION = 'select2-applicantincomesourcecommandform-{count}-occupation-container'
        DL_PRIMARY_SOURCE_OF_INCOME = ('[aria-labelledby="select2-applicantincomesourcecommandform-{count}-'
                                       'primarysourceofincome-container"]')
        DL_PRIMARY_SOURCE_OF_INCOME_CO_APPLICANT = ('[aria-labelledby="select2-coapplicantincomesourcecommandform-'
                                                    '{count}-primarysourceofincome-container"]')
        T_PRIMARY_SOURCE_OF_INCOME = 'select2-applicantincomesourcecommandform-{count}-primarysourceofincome-container'
        F_COMPANY_NAME = '#applicantincomesourcecommandform-{count}-name'
        F_COMPANY_NAME_CO_APPLICANT = '#coapplicantincomesourcecommandform-{count}-name'
        F_LENGTH_YEARS = '#applicantincomesourcecommandform-{count}-lengthyears'
        F_LENGTH_YEARS_CO_APPLICANT = '#coapplicantincomesourcecommandform-{count}-lengthyears'
        F_LENGTH_MONTHS = '#applicantincomesourcecommandform-{count}-lengthmonths'
        F_LENGTH_MONTHS_CO_APPLICANT = '#coapplicantincomesourcecommandform-{count}-lengthmonths'
        F_PHONE_WORK = '#applicantincomesourcecommandform-{count}-phone'
        F_PHONE_WORK_CO_APPLICANT = '#coapplicantincomesourcecommandform-{count}-phone'
        F_NET_MONTHLY_INCOME = '#applicantincomesourcecommandform-{count}-netmonthlyincome'
        F_NET_MONTHLY_INCOME_CO_APPLICANT = '#coapplicantincomesourcecommandform-{count}-netmonthlyincome'
        F_REMOVE_BUTTON = (By.CSS_SELECTOR, '.js-income-source-remove')
        F_LAST_PAY_DAY = (By.ID, 'paymentscheduleform-lastpayday')
        F_NEXT_PAY_DAY = (By.ID, 'paymentscheduleform-nextpayday')

        TG_MARK_AS_PRIMARY_CO_APPLICNAT = '.field-coapplicantincomesourcecommandform-{count}-isprimary .switchery-small'
        TG_UPFRONT_MARK_AS_PRIMARY_CO_APPLICNAT = ('.field-coapplicantincomesourceextendedcommandform-'
                                                   '{count}-isprimary .switchery-small')
        TG_MARK_AS_SECONDARY_CO_APPLICNAT = ('.field-coapplicantincomesourcecommandform-{count}-'
                                             'isprimary .switchery-small')
        T_INCOME_SOURCE_HEADERS = (By.CSS_SELECTOR, '.js-income-source-header')
        B_ADD_INCOME_SOURCE = (By.CSS_SELECTOR, '.js-add-income-source-button')
        B_ADD_INCOME_SOURCE_CO_APPLICANT = (By.CSS_SELECTOR, '[data-form-name="CoApplicantIncomeSourceCommandForm"]')
        B_SAVE = (By.CSS_SELECTOR, '.btn-success')
        F_OCCUPATION_DESCR01 = (By.ID, 'applicantincomesourcecommandform-0-occupationdescription')
        F_OCCUPATION_DESCR02 = (By.ID, 'coapplicantincomesourcecommandform-0-occupationdescription')
        F_OCCUPATION_DESCR03 = (By.ID, 'applicantincomesourcecommandform-1-occupationdescription')
        F_OCCUPATION_DESCR04 = (By.ID, 'coapplicantincomesourcecommandform-1-occupationdescription')
        F_OCCUPATION_DESCR05 = (By.ID, 'applicantincomesourcecommandform-2-occupationdescription')
        B_REMOVE = (By.CSS_SELECTOR, '.js-income-source-remove')
        # F_NET_MONTHLY_INCOME_EXTENDED = '#applicantincomesourceextendedcommandform-{count}-netmonthlyincome'

        # Upfront Income extended form:
        B_UPFRONT_ADD_INCOME_SOURCE_CO_APPLICANT = (
            By.CSS_SELECTOR, '[data-form-name="CoApplicantIncomeSourceExtendedCommandForm"]')
        DL_UPFRONT_PRIMARY_SOURCE_OF_INCOME = ('[aria-labelledby="select2-applicantincomesourceextendedcommandform-'
                                               '{count}-primarysourceofincome-container"]')
        DL_UPFRONT_PRIMARY_SOURCE_OF_INCOME_CO_APPLICANT = ('[aria-labelledby="select2-'
                                                            'coapplicantincomesourceextendedcommandform-{count}-'
                                                            'primarysourceofincome-container"]')
        DL_UPFRONT_OCCUPATION = ('[aria-labelledby="select2-applicantincomesourceextendedcommandform-{count}-'
                                 'occupation-container"]')
        DL_UPFRONT_OCCUPATION_CO_APPLICANT = ('[aria-labelledby="select2-coapplicantincomesourceextendedcommandform-'
                                              '{count}-occupation-container"]')
        DL_UPFRONT_STATUS = ('[aria-labelledby="select2-applicantincomesourceextendedcommandform-'
                             '{count}-status-container"]')
        DL_UPFRONT_STATUS_CO_APPLICANT = ('[aria-labelledby="select2-coapplicantincomesourceextendedcommandform-{'
                                          'count}-status-container"]')
        F_UPFRONT_COMPANY_NAME = '#applicantincomesourceextendedcommandform-{count}-name'
        F_UPFRONT_COMPANY_NAME_CO_APPLICANT = '#coapplicantincomesourceextendedcommandform-{count}-name'
        F_UPFRONT_LENGTH_YEARS = '#applicantincomesourceextendedcommandform-{count}-lengthyears'
        F_UPFRONT_LENGTH_YEARS_CO_APPLICANT = '#coapplicantincomesourceextendedcommandform-{count}-lengthyears'
        F_UPFRONT_LENGTH_MONTHS = '#applicantincomesourceextendedcommandform-{count}-lengthmonths'
        F_UPFRONT_LENGTH_MONTHS_CO_APPLICANT = '#coapplicantincomesourceextendedcommandform-{count}-lengthmonths'
        F_UPFRONT_PHONE_WORK = '#applicantincomesourceextendedcommandform-{count}-phone'
        F_UPFRONT_PHONE_WORK_CO_APPLICANT = '#coapplicantincomesourceextendedcommandform-{count}-phone'
        F_UPFRONT_NET_MONTHLY_INCOME = '#applicantincomesourceextendedcommandform-{count}-netmonthlyincome'
        F_UPFRONT_NET_MONTHLY_INCOME_CO_APPLICANT = ('#coapplicantincomesourceextendedcommandform-'
                                                     '{count}-netmonthlyincome')
        F_GROSS_MONTHLY_INCOME = (By.ID, 'applicantincomesourceextendedcommandform-0-grossmonthlyincome')
        F_GROSS_MONTHLY_INCOME_CO_APPLICANT = (By.ID, 'coapplicantincomesourceextendedcommandform-0-grossmonthlyincome')
        F_W2INCOME = (By.ID, 'applicantincomesourceextendedcommandform-0-w2income')
        F_W2INCOME_CO_APPLICANT = (By.ID, 'coapplicantincomesourceextendedcommandform-0-w2income')
        F_TYPE_OF_PAY = (
            By.CSS_SELECTOR,
            '[aria-labelledby="select2-applicantincomesourceextendedcommandform-0-typeofpay-container"]'
        )
        F_TYPE_OF_PAY_CO_APPLICANT = (
            By.CSS_SELECTOR,
            '[aria-labelledby="select2-coapplicantincomesourceextendedcommandform-0-typeofpay-container"]'
        )
        F_TYPE_OF_PAY_INPUT = (By.ID, 'select2-applicantincomesourceextendedcommandform-0-typeofpay-container')
        F_TYPE_OF_PAY_INPUT_CO_APPLICANT = (By.ID, 'select2-coapplicantincomesourceextendedcommandform-0-'
                                                   'typeofpay-container')
        F_TYPE_OF_PAY_FORM = '#select2-applicantincomesourceextendedcommandform-{count}-typeofpay-container'
        F_TYPE_OF_PAY_FORM_CO_APPLICANT = ('#select2-coapplicantincomesourceextendedcommandform-{count}-'
                                           'typeofpay-container')
        F_HOW_TO_CALCULATE = (
            By.CSS_SELECTOR,
            '[aria-labelledby="select2-applicantincomesourceextendedcommandform-0-howtocalculate-container"]'
        )
        F_HOW_TO_CALCULATE_CO_APPLICANT = (
            By.CSS_SELECTOR,
            '[aria-labelledby="select2-coapplicantincomesourceextendedcommandform-0-howtocalculate-container"]'
        )
        F_HOW_TO_CALCULATE_FORM = '#select2-applicantincomesourceextendedcommandform-{count}-howtocalculate-container'
        F_HOW_TO_CALCULATE_FORM_CO_APPLICANT = ('#select2-coapplicantincomesourceextendedcommandform-{count}-'
                                                'howtocalculate-container')
        CB_BANK_STATEMENTS_REVIEW_1 = (
            By.CSS_SELECTOR, '[for="applicantincomesourceextendedcommandform-0-isborrowerhasdirectdeposits"]'
        )
        CB_BANK_STATEMENTS_REVIEW_1_CO_APPLICANT = (
            By.CSS_SELECTOR, '[for="coapplicantincomesourceextendedcommandform-0-isborrowerhasdirectdeposits"]'
        )
        E_COMPLETED = (By.CSS_SELECTOR, '[data-toggle="income-documents"]')

        CB_BANK_STATEMENTS_REVIEW_1_FORM = ('#applicantincomesourceextendedcommandform-{count}-'
                                            'isborrowerhasdirectdeposits')
        CB_BANK_STATEMENTS_REVIEW_2_FORM = ('#applicantincomesourceextendedcommandform-{count}-'
                                            'isnegativebalancesdetected')
        CB_BANK_STATEMENTS_REVIEW_3_FORM = '#applicantincomesourceextendedcommandform-{count}-isborrowersprimaryaccount'


class LeadsIncomeOld:
    ENDPOINT = f'{ENDPOINT_LEAD}/income?id='
    ENDPOINT_BROKER = f'{ENDPOINT_LEAD}/income?id='

    class Locators:
        def __init__(self, income_count):
            self.count = income_count

            self.TG_MARK_AS_PRIMARY = (
                By.CSS_SELECTOR, f'.field-applicantincomesourcecommandform-{self.count}-isprimary .switchery-small')
            self.DL_STATUS = (
                By.CSS_SELECTOR,
                f'[aria-labelledby="select2-applicantincomesourcecommandform-{self.count}-status-container"]'
            )
            self.DL_OCCUPATION = (
                By.CSS_SELECTOR,
                f'[aria-labelledby="select2-applicantincomesourcecommandform-{self.count}-occupation-container"]'
            )
            self.DL_PRIMARY_SOURCE_OF_INCOME = (
                By.CSS_SELECTOR,
                f'[aria-labelledby="select2-applicantincomesourcecommandform-{self.count}-'
                f'primarysourceofincome-container"]'
            )
            self.F_COMPANY_NAME = (By.CSS_SELECTOR, f'#applicantincomesourcecommandform-{self.count}-name')
            self.F_LENGTH_YEARS = (By.CSS_SELECTOR, f'#applicantincomesourcecommandform-{self.count}-lengthyears')
            self.F_LENGTH_MONTHS = (By.CSS_SELECTOR, f'#applicantincomesourcecommandform-{self.count}-lengthmonths')
            self.F_PHONE_WORK = (By.CSS_SELECTOR, f'#applicantincomesourcecommandform-{self.count}-phone')
            self.F_NET_MONTHLY_INCOME = (
                By.CSS_SELECTOR, f'#applicantincomesourcecommandform-{self.count}-netmonthlyincome')

        TG_MARK_AS_PRIMARY_COAPPLICNAT = (
            By.CSS_SELECTOR, '.field-applicantincomesourcecommandform-0-isprimary .switchery-small')
        TG_MARK_AS_SECONDARY_COAPPLICNAT = (
            By.CSS_SELECTOR, '.field-coapplicantincomesourcecommandform-0-isprimary .switchery-small')
        T_INCOME_SOURCE_HEADERS = (By.CSS_SELECTOR, '.js-income-source-header')
        B_ADD_INCOME_SOURCE = (By.CSS_SELECTOR, '.js-add-income-source-button')
        B_ADD_INCOME_SOURCE_COAPPLICANT = (By.CSS_SELECTOR, '[data-form-name="CoApplicantIncomeSourceCommandForm"]')
        B_SAVE = (By.CSS_SELECTOR, '.btn-success')
        F_OCCUPATION_DESCR01 = (By.ID, 'applicantincomesourcecommandform-0-occupationdescription')
        F_OCCUPATION_DESCR02 = (By.ID, 'coapplicantincomesourcecommandform-0-occupationdescription')
        F_OCCUPATION_DESCR03 = (By.ID, 'applicantincomesourcecommandform-1-occupationdescription')
        F_OCCUPATION_DESCR04 = (By.ID, 'coapplicantincomesourcecommandform-1-occupationdescription')
        F_OCCUPATION_DESCR05 = (By.ID, 'applicantincomesourcecommandform-2-occupationdescription')
        F_REMOVE_BUTTON = (By.CSS_SELECTOR, '.js-income-source-remove')


class LeadsBudget:
    ENDPOINT = f'{ENDPOINT_LEAD}/budget?id='
    ENDPOINT_BROKER = f'{ENDPOINT_LEAD}/budget?id='

    class Locators:
        S_HARDSHIP_REASON = (By.ID, 'updatebudgetcommandform-hardshipreason')
        F_DETAILED_HARDSHIP_REASON = (By.ID, 'updatebudgetcommandform-detailedhardshipreason')
        B_SAVE = (By.CSS_SELECTOR, '.btn-success')
        T_FUNDS_AVAILABLE = (By.XPATH, '//label[contains(text(), "Funds Available")]//following-sibling::span')

        # housing
        DL_HOUSING = (By.CSS_SELECTOR, '[aria-labelledby="select2-updatebudgetexpensescommandform-housing-container"]')
        F_HOUSING_READ_HOUSING = (By.ID, 'select2-updatebudgetexpensescommandform-housing-container')
        F_HOUSING_PAYMENT = (By.ID, 'updatebudgetexpensescommandform-housingpayment')
        F_HOUSING_PAYMENT_DESC = (By.ID, 'updatebudgetexpensescommandform-housingpaymentdescription')
        F_HOMEOWNERS_INSURANCE = (By.ID, 'updatebudgetexpensescommandform-homeownersinsurance')
        F_TAX = (By.ID, 'updatebudgetexpensescommandform-tax')
        F_HOA = (By.ID, 'updatebudgetexpensescommandform-hoa')

        F_CASH_RESERVES = (By.ID, 'updatebudgetapplicantcommandform-cashreserves')

        # MONTHLY DEBT EXPENSES
        F_GOVERNMENT_STUDENT_LOANS = (By.ID, 'updatebudgetexpensescommandform-governmentstudentloans')
        F_PRIVATE_STUDENT_LOANS = (By.ID, 'updatebudgetexpensescommandform-privatestudentloans')
        F_MEDICAL_DEBT = (By.ID, 'updatebudgetexpensescommandform-medicaldebt')
        F_OTHER_DEBT = (By.ID, 'updatebudgetexpensescommandform-otherdebt')
        F_OTHER_CARDS = (By.ID, 'updatebudgetexpensescommandform-othercardsoutsideoftheprogramdescription')
        F_OTHER_DEBT_DESCRIPTION = (By.ID, 'updatebudgetexpensescommandform-otherdebtdescription')
        F_OTHER_CARDS_OUTSIDE_OF_THE_PROGRAM = (By.ID, 'updatebudgetexpensescommandform-othercardsoutsideoftheprogram')
        F_BACK_TAXES = (By.ID, 'updatebudgetexpensescommandform-backtaxes')

        # utilities
        F_CABLE_TV_SATELLITE = (By.ID, 'updatebudgetexpensescommandform-cabletvsatellite')
        F_CABLE_TV_SATELLITE_DESC = (By.ID, 'updatebudgetexpensescommandform-cabletvsatellitedescription')
        F_TELEPHONE = (By.ID, 'updatebudgetexpensescommandform-telephone')
        F_TELEPHONE_DESC = (By.ID, 'updatebudgetexpensescommandform-telephonedescription')
        F_UTILITIES = (By.ID, 'updatebudgetexpensescommandform-utilities')
        F_UTILITIES_DESC = (By.ID, 'updatebudgetexpensescommandform-utilitiesdescription')
        F_OTHER = (By.ID, 'updatebudgetexpensescommandform-utilitiesother')
        F_OTHER_DESC = (By.ID, 'updatebudgetexpensescommandform-utilitiesotherdescription')

        # personal care/house_hold/misc/food
        F_HOUSE_HOLD_ITEMS = (By.ID, 'updatebudgetexpensescommandform-householditems')
        F_CLOTHING = (By.ID, 'updatebudgetexpensescommandform-clothing')
        F_GYM_HEALTH = (By.ID, 'updatebudgetexpensescommandform-gymhealth')
        F_PERSONAL_CARE = (By.ID, 'updatebudgetexpensescommandform-personalcare')
        F_ENTERTAINMENT = (By.ID, 'updatebudgetexpensescommandform-entertainment')
        F_FOOD = (By.ID, 'updatebudgetexpensescommandform-food')
        F_FOOD_DESC = (By.ID, 'updatebudgetexpensescommandform-fooddescription')
        F_LAUNDRY_DRY_CLEANING = (By.ID, 'updatebudgetexpensescommandform-laundrydrycleaning')
        F_MISC = (By.ID, 'updatebudgetexpensescommandform-misc')

        # transportation
        F_AUTO_LOANS = (By.ID, 'updatebudgetexpensescommandform-autoloans')
        F_AUTO_INSURANCE = (By.ID, 'updatebudgetexpensescommandform-autoinsurance')
        F_AUTO_INSURANCE_DESC = (By.ID, 'updatebudgetexpensescommandform-autoinsurancedescription')
        F_AUTO_OTHER = (By.ID, 'updatebudgetexpensescommandform-autoother')

        # medical
        F_LIFE_INSURANCE = (By.ID, 'updatebudgetexpensescommandform-lifeinsurance')
        F_MEDICAL_CARE = (By.ID, 'updatebudgetexpensescommandform-medicalcare')

        # legal and court ordered eхpense
        F_SUPPORT = (By.ID, 'updatebudgetexpensescommandform-support')
        F_ALIMONY = (By.ID, 'updatebudgetexpensescommandform-alimony')

        # other
        F_CHILD_CARE = (By.ID, 'updatebudgetexpensescommandform-childcare')
        F_NURSING_CARE = (By.ID, 'updatebudgetexpensescommandform-nursingcare')
        F_EDUCATION = (By.ID, 'updatebudgetexpensescommandform-education')
        F_CHARITY_DONATIONS = (By.ID, 'updatebudgetexpensescommandform-charitydonations')
        F_OTHER_LIVING_EXPENSES_OTHER = (By.ID, 'updatebudgetexpensescommandform-otherlivingexpenses')
        F_OTHER_LIVING_EXPENSES = (By.ID, 'updatebudgetexpensescommandform-otherlivingexpenses')
        F_OTHER_LIVING_EXPENSES_DESC = (By.ID, 'updatebudgetexpensescommandform-otherlivingexpensesdescription')
        DL_GROUNDS_OF_EXEMPTION = (
            By.CSS_SELECTOR,
            '[aria-labelledby="select2-updatebudgetexpensescommandform-groundsofexemptionfornegativebudget-container"]'
        )
        T_GROUNDS_OF_EXEMPTION = (
            By.ID, 'select2-updatebudgetexpensescommandform-groundsofexemptionfornegativebudget-container')
        F_GROUNDS_OF_EXEMPTION_DESC = (
            By.ID, 'updatebudgetexpensescommandform-groundsofexemptionfornegativebudgetdescription')
        F_BUDGET_NOTE = (By.ID, 'updatebudgetcommandform-budgetnote')


class LeadsCalculator:
    ENDPOINT = f'{ENDPOINT_LEAD}/calculator?id='
    ENDPOINT_BROKER = f'{ENDPOINT_LEAD}/calculator?id='

    class Locators:
        F_NUMBER_OF_MONTHS = (By.ID, 'leaddebtsettlementform-numberofmonths')
        F_FUNDING_DEPOSIT_DATE = (By.ID, 'leaddebtsettlementform-fundingdepositdate')
        F_FUNDING_DEPOSIT = (By.ID, 'updatepaymentschedulecalculatorcommandform-fundingdeposit')
        F_INITIAL_DEPOSIT = (By.ID, 'leaddebtsettlementform-fundingdepositamount')
        F_NEXT_PAY_DATE = (By.ID, 'leaddebtsettlementform-recurringdepositstartdate')
        RB_DEPOSIT_FREQUENCY_1 = (
            By.XPATH, '//*[@id="updatepaymentschedulecalculatorcommandform-payfrequency"]/label[1]/input')
        RB_DEPOSIT_FREQUENCY_2 = (
            By.XPATH, '//*[@id="updatepaymentschedulecalculatorcommandform-payfrequency"]/label[2]/input')
        RB_DEPOSIT_FREQUENCY_3 = (
            By.XPATH, '//*[@id="updatepaymentschedulecalculatorcommandform-payfrequency"]/label[3]/input')
        T_EFFECTIVE_RATE = (By.XPATH, '//*[@id="calculator-loan-form"]/div/div[1]/div[3]/div/p')
        T_NUMBER_OF_MONTHS_TILL_LOAN = (By.XPATH, '//*[@id="calculator-loan-form"]/div/div[1]/div[4]/div/p')
        T_TOTAL_PAYMENTS_TO_RAM = (By.XPATH, '//*[@id="calculator-loan-form"]/div/div[1]/div[5]/div/p')
        T_PAYMENTS = (By.XPATH, '//*[@id="calculator-loan-form"]/div/div[1]/div[6]/div/p')
        T_TERM = (By.XPATH, '//*[@id="calculator-loan-form"]/div/div[2]/div[2]/div/p')
        T_DEPOSIT_SCHEDULE = '//tr[@data-key="{count}"]'


class LeadsLoanCalculator:
    ENDPOINT = f'{ENDPOINT_LEAD}/loan-calculator/index?id='

    class Locators:
        F_FUNDING_DATE = (By.ID, 'loanplancalculatorform-fundingdate')
        F_START_DATE = (By.ID, 'loanplancalculatorform-startdate')
        F_TERM = (By.ID, 'overrideloanplanform-term')

        # B_EXPERIAN = (By.XPATH, "//button[normalize-space(text())='Experian']")
        T_REQUIRED_LOAN_AMOUNT = (By.XPATH, "//label[contains(text(), 'Required Loan Amount')]//ancestor::tr")
        T_PREPARE_FINANCE = (By.XPATH, "//label[contains(text(), 'Prepaid Finance Charge')]//ancestor::tr")
        T_LOAN_AMOUNT_WITH_POINTS = (By.XPATH, "//label[contains(text(), 'Loan Amount with Points')]//ancestor::tr")
        T_ANNUAL_PERCENTAGE_RATE = (By.XPATH, "//label[contains(text(), 'Annual Percentage Rate')]//ancestor::tr")
        T_INTEREST_RATE = (By.XPATH, "//label[contains(text(), 'Interest Rate')]//ancestor::tr")
        T_PAYMENT_INTERVAL = (By.XPATH, "//label[contains(text(), 'Payment Interval')]//ancestor::tr")
        T_TERM = (By.XPATH, "//label[contains(text(), 'Term')]//ancestor::tr")
        T_LOAN_PAYMENT = (By.XPATH, "//label[contains(text(), 'Loan Payment')]//ancestor::tr")
        T_TOTAL_INTEREST = (By.XPATH, "//label[contains(text(), 'Total Interest')]//ancestor::tr")
        T_TOTAL_AMOUNT_PAID = (By.XPATH, "//label[contains(text(), 'Total Amount Paid')]//ancestor::tr")


class LeadsACH:
    ENDPOINT = f'{ENDPOINT_LEAD}/ach?id='
    ENDPOINT_BROKER = f'{ENDPOINT_LEAD}/ach?id='

    class Locators:
        F_ROUTING_NUMBER = (By.ID, 'updateleadachcommandform-routingnumber')
        B_ROUTING_NUMBER_SEARCH = (By.CSS_SELECTOR, '.btn-routing-number-info')
        F_BANK_ACCOUNT_NUMBER = (By.ID, 'updateleadachcommandform-bankaccountnumber')
        F_SECOND_DEPOSIT_DATE = (By.ID, 'updateleadachcommandform-startdateforsubsequentdeposits')
        RB_ACCOUNT_TYPE_CHECKING_ACH = (By.CSS_SELECTOR, '#updateleadachcommandform-accounttype label input')
        RB_ACCOUNT_TYPE_SAVING_ACH = (By.CSS_SELECTOR, '#updateleadachcommandform-accounttype label:nth-child(2) input')
        RB_ACCOUNT_TYPE = (By.ID, 'updateleadachcommandform-accounttype')
        F_BANK_NAME_ACH = (By.ID, 'updateleadachcommandform-bankname')
        F_BANK_PHONE_NUMBER_ACH = (By.ID, 'updateleadachcommandform-bankphonenumber')
        F_BANK_CITY_ACH = (By.ID, 'updateleadachcommandform-bankcity')
        F_BANK_STATE_ACH = (By.ID, 'updateleadachcommandform-bankstate')
        F_BANK_ZIP_ACH = (By.ID, 'updateleadachcommandform-bankzip')
        F_BANK_ADDRESS_ACH = (By.ID, 'updateleadachcommandform-bankaddress')
        F_NAME_OF_ACCOUNT = (By.ID, 'updateleadachcommandform-nameonaccount')
        F_DATE_OF_INITIAL_PAYMENT = (By.ID, 'updateleadachcommandform-dateofinitialpayment')
        F_SECOND_DATE_OF_INITIAL_PAYMENT = (By.ID, 'updateleadachcommandform-startdateforsubsequentpayments')
        F_SSN = (By.ID, 'updateleadachcommandform-ssn')
        F_DOB = (By.ID, 'updateleadachcommandform-dob')
        B_SAVE = (By.CSS_SELECTOR, '.btn-success')
        F_MOTHERS_MAIDEN_NAME = (By.ID, 'updateleadachcommandform-mothersmaidenname')
        E_PREVALIDATE_ALERT = (By.CLASS_NAME, 'sweet-alert')


class LeadsUnderwriting:
    ENDPOINT = f'{ENDPOINT_LEADS}/underwriting?id='

    class Locators:
        # Right sidebar
        T_SALES_REP = (By.XPATH, "//b[normalize-space(text())='Sales Rep']/following::span")
        B_ARROW = (By.CSS_SELECTOR, '.fa-angle-right')
        T_SIGN_DOCS_LINK = (By.CSS_SELECTOR, '#description p:nth-child(4) a')
        POPUP_OFFER_CONFIRMATION = (By.XPATH, '/html/body/div[5]/p')
        B_CLICK_DOCUMENTS = (By.XPATH, '//*[@id="loan-funding-reasons-tabs"]/li[2]/a')
        B_UPLOAD_DOCUMENT = (By.ID, 'uploadverificationdocumentform-file')
        S_TYPE_OF_FILE = (By.CSS_SELECTOR, '[aria-labelledby="select2-uploadverificationdocumentform-type-container"]')
        S_TYPE_OF_FILE_FIELD = (
            By.CSS_SELECTOR, '[aria-controls="select2-uploadverificationdocumentform-type-results"]')
        MANUAL_APPROVED_1 = (By.ID, 'verifylocprocessingmanuallyssnform-1-1-ismanuallyverified')
        MANUAL_APPROVED_2 = (By.ID, 'verifylocprocessingmanuallydobform-1-2-ismanuallyverified')
        MANUAL_APPROVED_4 = (By.ID, 'verifylocprocessingmanuallyaddressform-0-4-ismanuallyverified')
        MANUAL_APPROVED_5 = (By.ID, 'verifylocprocessingmanuallyofacform-1-5-ismanuallyverified')
        MANUALLY_VERIFIED = (By.CSS_SELECTOR, 'label [id*="verifylocprocessingmanually"]')
        B_BUTTON_APPROVED_FILES = (By.XPATH, '//*[@id="verify-applicant-data-form"]/div[3]/div/button')
        B_MODAL_UPLOAD_DOCUMENT = (
            By.XPATH, '//*[@id="loan-disqualified-reasons-modal"]//button[contains(text(), "Upload Document")]')


class LeadsDocument:
    ENDPOINT = f'{ENDPOINT_LEAD}/document?id='
    ENDPOINT_BROKER = f'{ENDPOINT_LEAD}/document?id='

    class Locators:
        B_UPLOAD_DOCUMENT_IN_TAB = (By.ID, 'uploaddocumentform-file')
        S_TYPE_OF_FILE_IN_TABS = (By.CSS_SELECTOR, '.field-uploaddocumentform-type span.select2')
        S_TYPE_OF_FILE_FIELD_IN_TABS = (By.CSS_SELECTOR, '[aria-controls="select2-uploaddocumentform-type-results"]')
        B_UPLOAD_DOCUMENT_IN_FORM = (By.CSS_SELECTOR, '#documents-form button[type=submit]')
        S_APPLICANT_IN_TABS = (By.CSS_SELECTOR, '[aria-labelledby="select2-uploaddocumentform-applicantid-container"]')
        S_APPLICANT_FIELD_IN_TABS = (By.ID, 'select2-uploaddocumentform-applicantid-container')


class LeadsDuplicate:
    ENDPOINT = f'{ENDPOINT_LEAD}/duplicate?id='
    ENDPOINT_BROKER = f'{ENDPOINT_LEAD}/duplicate?id='


class LeadsTasks:
    ENDPOINT = f'{ENDPOINT_LEAD}/tasks?id='


class LeadsLogs:
    ENDPOINT = f'{ENDPOINT_LEAD}/log?id='