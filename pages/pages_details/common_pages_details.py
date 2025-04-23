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


class Common:
    class Locators:
        E_SUCCESS_OR_ERROR = (By.ID, 'toast-container-top-alert')
        EE_ICON = (By.CSS_SELECTOR, 'div .erroricon')
        ET = (By.CSS_SELECTOR, '.header > h2')
        T_CLIENT_ID = (By.CSS_SELECTOR, '.page-title')
        E_CONFIRM_ALERT = (By.CSS_SELECTOR, 'div.sweet-alert[data-has-confirm-button="true"]')
        B_CONFIRM = (By.CSS_SELECTOR, 'button.confirm.btn.btn-lg.btn-primary')
        B_CONFIRM_CONTINUE_CHECKBOX = (By.CSS_SELECTOR, '[for="confirmpredisclosurecommandform-confirm"]')
        B_CONFIRM_BUTTON = (By.CLASS_NAME, 'btn btn-primary')
        B_CANCEL = (By.CSS_SELECTOR, 'button.cancel')
        E_SUCCESS_OR_ERROR_BROKERS = (By.ID, 'toast-container')
        ET_ERROR = (By.CSS_SELECTOR, '.toast.toast-error')
        T_SUCCESS = (By.CSS_SELECTOR, '.toast.toast-success')
        B_SAVE = (By.CSS_SELECTOR, '.btn-success')
        DL_AVATAR = (By.CSS_SELECTOR, '.navbar-avatar')
        B_SETTINGS = (By.CSS_SELECTOR, '[href="/settings/user/profile"]')
        B_SMS_FILTERING_LIST = (By.CSS_SELECTOR, '[href="/settings/communications/sms-filtering-list"]')
        F_SMS_FILTERING_LIST = (By.ID, 'smsfilteringlistform-newwords')
        B_SAVE_MODAL = (By.CSS_SELECTOR, '.modal-dialog [type=submit].btn-success')
        B_SAVE_MODAL_FINANCIAL_PROFILE = (By.CSS_SELECTOR, '.modal-dialog [type=button].btn-success')
        B_SEND_EMAIL = (By.CSS_SELECTOR, "[id*='EmailForm'] .btn-success")
        E_ACTIVE_DAY = (By.XPATH, "//td[contains(@class, 'active day')]")
        B_LOCKED = (By.ID, 'docs-sent-locked-block')
        B_UPLOAD_SPINNER = (By.CLASS_NAME, 'ladda-spinner')
        B_CALL_DISABLE = (By.XPATH, "//button[contains(text(), 'Call')]")
        B_Email_DISABLE = (By.XPATH, "//button[contains(text(), 'Email')]")
        B_SEND_SMS = (By.CSS_SELECTOR, "[id*='SmsForm'] .btn-success")
        B_SEND_A_SMS_TAB = (By.CSS_SELECTOR, "#communicate-tabs > li:nth-child(3) > a")

        B_ACCOUNT_EMAIL = (By.ID, 'accounts-menu')
        B_EMAIL_LOGIN = (By.ID, 'address')
        B_EMAIL_PASSWORD = (By.ID, 'password')
        B_LOGIN_EMAIL = (By.XPATH, '//*[@id="accounts-list"]/div/div[4]/a')
        B_DELETE_EMAIL = (By.XPATH, '//*[@id="__layout"]/div/div[2]/main/div/div[2]/div[2]/span[4]/button')
        T_INTERNAL_PAGE_TITLE = (By.CLASS_NAME, 'page-title')
        ET_FIELDS_ERRORS = (By.CSS_SELECTOR, 'small.text-danger')
        ET_BROKERS_FIELDS_ERRORS = (By.CSS_SELECTOR, 'small.help-block-error')
        B_BELL = (By.XPATH, '//*[@id="top-counters-menu"]/ul/li[7]/a')
        T_FIRST_NOTIFICATION = (By.CSS_SELECTOR, '#top-counters-menu li:last-child h6 a')
        TG_LOAN_PRO = (By.XPATH, '//*[@id="info-form"]/div/div[10]/span')
        TG_LOAN_PRO_CREATE = (By.CSS_SELECTOR, '[data-action="button-active_w2"]')
        TG_LOAN_PRO_CREATE_2 = (By.XPATH, '//a[contains(@class, "btn-primary") and contains(text(), "Create Loan")]')
        TG_LOAN_PRO_CREATE_FORM = (By.ID, 'plan-new-form')


        # Sign, Document
        B_GO_TO_NEXT_SIGNATURE = (By.CSS_SELECTOR, '#gotoNextSignature')
        B_CLICK_HERE_TO_SIGN = (By.CSS_SELECTOR, '.btnSign')
        T_SIGNING_SUCCESS = (By.CSS_SELECTOR, 'h1')
        T_CLIENT_SIGNED = (By.CSS_SELECTOR, 'table tr td')
        CB_DOCUSIGN_TERM_OF_SERVICE = (By.CLASS_NAME, 'screen-reader-text')
        B_DOCUSIGN_ACTION_NEXT = (By.ID, 'action-bar-btn-continue')
        B_DOCUSIGN_ACTION_START = (By.ID, 'navigate-btn')
        B_DOCUSIGN_SIGN_ARROW = (By.CSS_SELECTOR, '.signature-tab-content')
        B_DOCUSIGN_SIGN_ACCEPTANCE = (By.XPATH, '//*[@id="adopt-dialog"]/div/div[3]/button[1]')
        B_DOCUSIGN_SIGN_FINAL = (By.ID, 'end-of-document-btn-finish')
        B_DOCUSIGN_SIGN_FINAL2 = (By.CSS_SELECTOR, '.finish-button')
        B_EXPERIAN = (By.XPATH, "//button[normalize-space(text())='Experian']")
        B_FINAL_CHECK_BUTTON_SUBMIT = (By.CSS_SELECTOR, '.save-a-copy-signup-button')
        T_VALIDATION_ERROR_TITLE = (By.CSS_SELECTOR, '.error-summary.alert.alert-danger p')
        T_VALIDATION_ERROR_REASON = (By.CSS_SELECTOR, '.error-summary.alert.alert-danger ul li')

        # reassign
        B_REASSIGN = (By.CSS_SELECTOR, '[data-toggle="reassign-modal"]')
        B_REASSIGN_FORM_CHECK = (By.ID, 'reassignform-salesrepid')
        DL_REASSIGN_SALES_REP = (By.CSS_SELECTOR, 'span #select2-reassignleadform-sales_rep_id-container')
        DL_REASSIGN_C9_LOAN_CONSULTANT = (
            By.CSS_SELECTOR, 'span #select2-reassignleadform-c9loanconsultantid-container')
        F_REASSIGN_INPUT = (By.CSS_SELECTOR, '.select2-search--dropdown .select2-search__field')
        F_SEND_PRE_ENROLLMENT = (By.ID, 'sendpreenrollmentwithlowdebtpercentageform-reason')
        B_REASSIGN_SAVE = (By.CSS_SELECTOR, ' .btn-save')
        F_REASSIGN_INPUT_C9_LOAN_CONSULTANT = (By.ID, 'select2-reassignleadform-c9loanconsultantid-container')

        # Send Docs
        B_SEND_DOCS = (By.CSS_SELECTOR, 'i.icon.glyphicon.glyphicon-send')
        B_AGREEMENT_ONLY = (By.XPATH, "//a[normalize-space(text())='Agreement only']")
        T_SEND_DOCS_ERROR = (By.CSS_SELECTOR, '.toast.toast-error')
        B_SIGN_DOCS = (By.CSS_SELECTOR, '[data-bb-handler="send_docs"]')
        E_LOCKED_STATUS = (By.ID, 'changestatusandcallbackcommandform-docssentlocked')
        DOCS_SEND_STATUS = (By.CSS_SELECTOR, '[data-id="changestatusandcallbackcommandform-status"]')
        B_ENROLL = (By.CSS_SELECTOR, 'i.icon.glyphicon.glyphicon-send')

        # Search
        E_MAIN_SEARCH = (By.XPATH, '//*[@id="site-navbar-collapse"]/ul[1]')
        F_INPUT_MAIN_SEARCH = (By.CSS_SELECTOR, '[name="customer-search"]')
        F_SEARCH_RESULT = (By.CSS_SELECTOR, 'div.tt-suggestion-inner.ellipsis')
        F_SEARCH_RESULT_XPATH = (By.XPATH, '//div[@class="tt-suggestion-inner ellipsis"])[0]')

        # Tasks
        E_FIRST_TASK = (By.CLASS_NAME, 'animation-fade')
        B_DONE_TASK = (By.CSS_SELECTOR, '[data-action="button-active_w1"]')
        B_SNOOZE_TASK = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div/button')
        B_SNOOZE_TASK_SAVE = (
            By.XPATH, '/html/body/div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')
        B_TASK_REASSIGN = (By.CSS_SELECTOR, '[data-toggle="reassign-task-modal"]')
        DL_TASK_ASSIGN = (By.ID, 'select2-reassigntasksform-new_user_id-container')
        F_TASK_ASSIGN = (By.CSS_SELECTOR, '[aria-controls="select2-reassigntasksform-new_user_id-results"]')
        B_SAVE_TASK_REASSIGN = (By.CSS_SELECTOR, '[data-bb-handler="saveClose"]')
