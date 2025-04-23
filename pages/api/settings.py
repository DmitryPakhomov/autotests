import os
import random

from dotenv import load_dotenv

from autotests.pages.api.models.response_models.path_talks_models import ClientsResponse, \
    ClientsAuthTokensResponse, GetClientsResponse, GetClientsByIdResponse, \
    PutClientsStatusResponse, GetClientRoleResponse, PostSmsAccountResponse, GetSmsAccountResponse, \
    GetClientAuthTokenId, GetClientAuthToken, GetBrandId, GetClientNotificationUrls, \
    GetClientNotificationUrlsId, PostClientSmsChannel, GetComplianceDncId, GetSmsForbiddenwords, \
    GetSmsForbiddenwordsUsage, PostSmsWithDummy, PutRecipientPhone, GetMarketingDncPhone, \
    GetTcpaConsentPhoneNumber, GetTcpaConsentPhoneNumberHistory, GetEmailsAccounts, \
    PostEmailsAccounts
from autotests.pages.api.models.response_models.rest_v1_auth_models import AuthenticationResponse
from autotests.pages.api.models.response_models.rest_v1_enrollments_models import \
    EnrollmentResponse, EnrollmentFind, \
    EnrollmentResponseAch, EnrollmentResponseUnderwriting, EnrollmentResponseSettlements, \
    EnrollmentsResponseMain, \
    EnrollmentResponsePinnedNote, EnrollmentResponsePartnerCommission, \
    EnrollmentResponsePayoffQuotes
from autotests.pages.api.models.response_models.rest_v1_leads_models import LenderLeadsResponse, \
    ProfileResponse, \
    LenderLeadsCheckDuplicatesResponse, CreditorsResponse, DepositsResponse, SummaryResponse, \
    LeadResponse, PreLeadResponse, CallSchedulerResponse, FetchCreditReport, \
    LeadSetConnectedResponse, LeadSetScheduledResponse, HigbeeAcceptRequest, HigbeeDeclineRequest, \
    HigbeeHoldRequest
from autotests.pages.api.models.response_models.rest_v1_loans_models import LoansResponseMain, \
    DncMain, DncAddresses, \
    LoanResponseAch, LoanDuplicates, DncEmail, PartnerUpdate
from autotests.pages.data.test_data import TestData

load_dotenv()

API_USERS_TOKEN_MAPPING = {
    'leads': os.environ['REST_V1_LEADS_TOKEN']
}

rest = '/rest/v1'

ENDPOINTS_MAPPING = {
    'authentication': f'{rest}/authentication/token',
    'get_lender_leads': f'{rest}/lead/lender-leads/',
    'put_lender_leads': f'{rest}/lead/lender-leads/',
    'post_lender_leads': f'{rest}/lead/lender-leads',
    'lender_leads_check_duplicates': f'{rest}/lead/lender-leads/check-duplicates',
    'sales_rep': f'{rest}/lead/sales-rep/',
    'purchase': f'{rest}/lead/purchase',
    'creditors': '/rest/v1/lead/{lead_id}/creditors',
    'deposits': '/rest/v1/lead/{lead_id}/deposits',
    'summary': '/rest/v1/lead/{lead_id}/summary',
    'profile': '/rest/v1/lead/{lead_id}/profile',
    'lead': f'{rest}/lead/',
    'pre_lead': f'{rest}/lead/pre-lead/lending-tree/',
    'test_case_upfront': f'{rest}/test-case/lead/upfront-final-loan-document/upload/',
    'undo_reject': '/lead/reject/undo/',
    'payoff-quotes': '/rest/v1/enrollment/payoff-quotes/{enrollment_id}',
    'find': '/rest/v1/enrollment/find?email={email}',
    'enrollments_find': '/rest/v1/enrollments?dateFrom=2023-08-15&dateTo=2023-08-18',
    'offer': '/rest/v1/enrollment/offer/{offer_id}/attorney-approval',
    'ach': '/rest/v1/deal/ach/{enrollment_id}',
    'get_enrollments': '/rest/v1/enrollments',
    'get_enrollment': '/rest/v1/enrollment/',
    'get_enrollment_pinned_note': '/rest/v1/enrollment/{enrollment_uuid_with_pinned}/pinned-note',
    'get_enrollment_partner_commission': '/rest/v1/enrollment/partner-commission?enrollmentUuid[]=',
    'get_enrollment_payoff_quotes': '/rest/v1/deal/payoff-quotes/',
    'get_enrollment_ach': '/rest/v1/deal/ach/',
    'get_enrollment_underwriting': '/rest/v1/deal/underwriting/',
    'get_enrollment_settlement': '/rest/v1/enrollment/settlements',
    'get_enrollment_find': '/rest/v1/enrollment/find',
    'patch_enrollment_mobile_app': '/rest/v1/enrollment/{enrollmentId}/mobile-app',
    'patch_credit9_is_registered_id': '/api/credit9/is-registered/{id}',
    'get_loans': '/rest/v1/loans',
    'get_loan_ach': '/rest/v1/loan/ach/',
    'get_loan_duplicates': '/rest/v1/loan/duplicates',
    'get_dnc_phone': '/rest/v1/communication/dnc-calls',
    'get_dnc_email': '/rest/v1/communication/dnc-communication-emails',
    'get_dnc_sms': '/rest/v1/communication/dnc-sms',
    'post_dnc_phone': '/rest/v1/communication/dnc-calls',
    'post_dnc_email': '/rest/v1/communication/dnc-communication-emails',
    'get_dnc_address': '/rest/v1/communication/dnc-addresses',
    'post_dnc_address': '/rest/v1/communication/dnc-addresses',
    'post_partner': '/rest/v1/partner',
    'put_partner': '/rest/v1/partner/',
    'clients': '/clients',
    'auth_tokens': '/clients/{client_id}/auth-tokens',
    'delete_auth_tokens': '/clients/{client_id}/auth-tokens/{token_id}',
    'get_clients': '/clients',
    'get_clients_id': '/clients/{client_id}',
    'put_client_status': '/clients/{client_id}/status',
    'get_client_roles': '/clients/{client_id}/roles',
    'post_client_roles': '/clients/{client_id}/roles/{role}',
    'delete_client_roles': '/clients/{client_id}/roles/{role}',
    'post_sms_account': '/sms/accounts',
    'put_sms_account_status': '/sms/accounts/{id}/status',
    'put_sms_account': '/sms/accounts/{id}',
    'get_sms_accounts': '/sms/accounts',
    'get_sms_accounts_id': '/sms/accounts/{id}',
    'get_client_auth_token_id': '/clients/{clientId}/auth-tokens/{id}',
    'get_client_auth_token': '/clients/{clientId}/auth-tokens',
    'get_brands': '/brands',
    'get_brands_id': '/brands/{id}',
    'post_brands': '/brands',
    'set-scheduled': '/call-scheduler/automation/set-scheduled/',
    'fetch_credit_report': '/call-scheduler/customer/fetch-credit-report/',
    'set_lead_connected': '/api/v1/lead/set-connected?access-token=',
    'set_lead_scheduled_old': '/api/v1/lead/set-scheduled?access-token=',
    'higbee_approve': '/higbee/approve?access-token=',
    'higbee_decline': '/higbee/decline?access-token=',
    'higbee_hold': '/higbee/hold?access-token=',
    'get_client_notification_urls': '/clients/{clientId}/notification-urls',
    'get_client_notification_urls_id': '/clients/{clientId}/notification-urls/{id}',
    'post_client_sms_channel': '/clients/{clientId}/sms/channels',
    'get_client_sms_channel_id': '/clients/{clientId}/sms/channels/{id}',
    'put_client_sms_channel_id_status': '/clients/{clientId}/sms/channels/{id}/status',
    'approve_offer': '/rest/v1/deal/settlements/{offer_id}/approvals',
    'get_compliance_litigation_dnc_id': '/compliance/litigation-dnc/{id}',
    'post_compliance_litigation_dnc': '/compliance/litigation-dnc',
    'get_sms_forbidden_words': '/sms/forbidden-words',
    'get_sms_forbidden_words_usage': '/sms/forbidden-words/usage',
    'post_test_send_sms_dummy': '/sms',
    'put_recipient_phone': '/clients/{clientId}/recipient-phone/{currentPhoneNumber}',
    'get_marketing_dnc_phone_id': '/brands/{brandId}/compliance/marketing-dnc-phone/{id}',
    'post_marketing_dnc_phone': '/brands/{brandId}/compliance/marketing-dnc-phone',
    'post_emails_account': '/clients/{clientId}/emails/accounts',
    'get_emails_account': '/clients/{clientId}/emails/accounts',
    'get_emails_account_id': '/clients/{clientId}/emails/accounts/{id}',
    'get_sms_outgoing_list': '/clients/{clientId}/sms-outgoing',
    'get_sms_outgoing_id': '/sms/outgoing/{id}',
    'get_tcpa_consent_phone_number': '/brands/{brandId}/tcpa-consent/{phoneNumber}',
    'get_tcpa_consent_phone_number_history': '/brands/{brandId}/tcpa-consent/{phoneNumber}/history',
    'get_brands_id_tcpa_consents': '/brands/{brandId}/tcpa-consents'
}

REQUEST_MODELS_MAPPING = {}

RESPONSE_MODELS_MAPPING = {
    'authentication': AuthenticationResponse,
    'get_lender_leads': LenderLeadsResponse,
    'put_lender_leads': LenderLeadsResponse,
    'post_lender_leads': LenderLeadsResponse,
    'lender_leads_check_duplicates': LenderLeadsCheckDuplicatesResponse,
    'creditors': CreditorsResponse,
    'deposits': DepositsResponse,
    'summary': SummaryResponse,
    'profile': ProfileResponse,
    'lead': LeadResponse,
    'set_lead_connected': LeadSetConnectedResponse,
    'set_lead_scheduled_old': LeadSetScheduledResponse,
    'pre_lead': PreLeadResponse,
    'get_enrollment': EnrollmentResponse,
    'get_enrollments': EnrollmentsResponseMain,
    'get_enrollment_pinned_note': EnrollmentResponsePinnedNote,
    'get_enrollment_partner_commission': EnrollmentResponsePartnerCommission,
    'get_enrollment_payoff_quotes': EnrollmentResponsePayoffQuotes,
    'get_enrollment_ach': EnrollmentResponseAch,
    'get_enrollment_underwriting': EnrollmentResponseUnderwriting,
    'get_enrollment_settlement': EnrollmentResponseSettlements,
    'get_enrollment_find': EnrollmentFind,
    'get_loans': LoansResponseMain,
    'get_loan_ach': LoanResponseAch,
    'get_loan_duplicates': LoanDuplicates,
    'get_dnc_phone': DncMain,
    'get_dnc_email': DncEmail,
    'get_dnc_sms': DncMain,
    'post_dnc_phone': DncMain,
    'post_dnc_email': DncEmail,
    'get_dnc_address': DncAddresses,
    'post_dnc_address': DncAddresses,
    'put_partner': PartnerUpdate,
    'clients': ClientsResponse,
    'auth_tokens': ClientsAuthTokensResponse,
    'get_clients': GetClientsResponse,
    'get_clients_id': GetClientsByIdResponse,
    'put_client_status': PutClientsStatusResponse,
    'get_client_roles': GetClientRoleResponse,
    'post_sms_account': PostSmsAccountResponse,
    'put_sms_account_status': PostSmsAccountResponse,
    'put_sms_account': PostSmsAccountResponse,
    'get_sms_accounts': GetSmsAccountResponse,
    'get_sms_accounts_id': PostSmsAccountResponse,
    'get_client_auth_token_id': GetClientAuthTokenId,
    'get_client_auth_token': GetClientAuthToken,
    'get_brands': GetClientAuthToken,
    'get_brands_id': GetBrandId,
    'post_brands': GetBrandId,
    'set-scheduled': CallSchedulerResponse,
    'fetch_credit_report': FetchCreditReport,
    'higbee_approve': HigbeeAcceptRequest,
    'higbee_decline': HigbeeDeclineRequest,
    'higbee_hold': HigbeeHoldRequest,
    'get_client_notification_urls': GetClientNotificationUrls,
    'get_client_notification_urls_id': GetClientNotificationUrlsId,
    'post_client_sms_channel': PostClientSmsChannel,
    'get_client_sms_channel_id': PostClientSmsChannel,
    'get_compliance_litigation_dnc_id': GetComplianceDncId,
    'post_compliance_litigation_dnc': GetComplianceDncId,
    'get_sms_forbidden_words': GetSmsForbiddenwords,
    'get_sms_forbidden_words_usage': GetSmsForbiddenwordsUsage,
    'post_test_send_sms_dummy': PostSmsWithDummy,
    'put_recipient_phone': PutRecipientPhone,
    'get_marketing_dnc_phone_id': GetMarketingDncPhone,
    'post_marketing_dnc_phone': GetMarketingDncPhone,
    'post_emails_account': PostEmailsAccounts,
    'get_emails_account': GetEmailsAccounts,
    'get_emails_account_id': GetEmailsAccounts,
    'get_tcpa_consent_phone_number': GetTcpaConsentPhoneNumber,
    'get_tcpa_consent_phone_number_history': GetTcpaConsentPhoneNumberHistory,
    'get_brand_id_tcpa_consent': GetTcpaConsentPhoneNumber,
}


def leads_creating_request_body(*args: str, **kwargs: str | dict) -> dict:
    """
    Метод для получения тела запроса для создания лида.

    :param args: Список параметров, которые необходимо удалить из тела запроса.
    :param kwargs: Список именованных параметров и значений,
    которые необходимо изменить в теле запроса.
    :return: Тело запроса в виде словаря.
    """
    request_body = {
        "firstName": TestData.first_name(),
        "lastName": TestData.last_name(),
        "email": TestData.email(),
        "phoneMobile": TestData.phone(),
        "phoneHome": TestData.phone(),
        "address": TestData.address(),
        "city": TestData.city(),
        "zip": TestData.zip_code(),
        "state": TestData.states()['code'],
        "ssn": TestData.ssn(),
        "dob": TestData.date(),
        "mailCode": "2",
        "source": TestData.sources(),
        "company": TestData.companies(),
        "campaign": "campaign",
        "channel": TestData.channels(),
        "trustedFormToken": "1ea3f6181ef47921bff18e61311da45a69fc276f",
        "unsecuredDebt": round(random.uniform(1000, 10000), 1),
        "isLoanRequired": False,
        "isValidityCheckRequired": False,
        "reason": "Some valid reason"
    }
    if kwargs:
        for key, value in kwargs.items():
            request_body[key] = value
    if args:
        for parameter in args:
            del request_body[parameter]
    return request_body


def communication_creating_request_body(*args: str, **kwargs: str | dict) -> dict:
    """
    Метод для получения тела запроса для создания Отправке запросов communication.

    :param args: Список параметров, которые необходимо удалить из тела запроса.
    :param kwargs: Список именованных параметров и значений,
    которые необходимо изменить в теле запроса.
    :return: Тело запроса в виде словаря.
    """
    request_body = {
        "phone": "+19286514129",
        "email": TestData.email(),
        "address": TestData.address(),
        "city": TestData.city(),
        "state": TestData.state_short(),
        "zip": TestData.zip_code()
    }
    if kwargs:
        for key, value in kwargs.items():
            request_body[key] = value
    if args:
        for parameter in args:
            del request_body[parameter]
    return request_body


def partner_creating_request_body(*args: str, **kwargs: str | dict) -> dict:
    """
    Метод для получения тела запроса для создания отправке запросов partner.

    :param args: Список параметров, которые необходимо удалить из тела запроса.
    :param kwargs: Список именованных параметров и значений, которые необходимо изменить в теле запроса.
    :return: Тело запроса в виде словаря.
    """
    request_body = {
        "uuid": TestData.uuid(),
        "title": TestData.words(),
        "contactEmail": TestData.email(),
        "isTest": 1
    }
    if kwargs:
        for key, value in kwargs.items():
            request_body[key] = value
    if args:
        for parameter in args:
            del request_body[parameter]
    return request_body
