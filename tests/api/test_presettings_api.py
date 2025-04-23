import json
import random
import pytest
import uuid
from typing import Any
from dotenv import load_dotenv
from autotests.pages.data.leads_data import leads_statuses
from autotests.pages.data.main_data import customer_types
from autotests.pages.queries import Customer, LeadPurchaser, Partner
from autotests.pages.settings import Settings


load_dotenv()


class TestPresettingsAPI:
    @pytest.mark.parametrize(
        'test',
        [
            'get_lender_leads',
            'put_lender_leads',
            'lender_leads_check_duplicates',
            'sales_rep',
            'purchase',
            'creditors',
            'summary',
            'profile',
            'lead',
            'set_lead_connected',
            'set_lead_scheduled_old',
            'get_enrollment',
            'get_enrollment_pinned_note',
            'get_enrollment_partner_commission',
            'get_enrollment_payoff_quotes',
            'get_enrollment_ach',
            'get_enrollment_underwriting',
            'get_enrollment_settlement',
            'get_enrollment_find'
            'get_loan_ach',
            'get_loan_duplicates',
            'get_dnc_phone',
            'get_dnc_sms',
            'get_dnc_email',
            'get_dnc_address',
            'put_partner',
            'higbee_approve',
            'higbee_decline',
            'higbee_hold'
        ]
    )
    def test_update_api_data(self, environ: str, test: str, config, request) -> Any:
        """ Update data in config for API tests - """
        temp_data = config.api_data

        if test == 'get_lender_leads':
            data = Customer.get_random_lead_id_with_all_quality_types(request)
            temp_data[test] = {
                "active": str(random.choice(data["active"])[0]),
                "rejected": str(random.choice(data["rejected"])[0]),
                "trickle": str(random.choice(data["trickle"])[0]),
                "unassigned": str(random.choice(data["unassigned"])[0]),
            }
        if test == 'set_lead_connected':
            data = Customer.get_random_lead_id_with_all_quality_types(request)
            temp_data[test] = {
                "set_connected_lead_positive": str(random.choice(data["active"])[0])
            }
        if test == 'set_lead_scheduled_old':
            data = Customer.get_random_lead_id_with_all_quality_types(request)
            temp_data[test] = {
                "set_lead_scheduled_old_positive": str(random.choice(data["active"])[0])
            }
        if test == 'put_lender_leads':
            data = Customer.get_random_lead_id(request)
            temp_data[test] = {
                "with_all_fields": str(random.choice(data["with_all_fields"])[0]),
                "with_credit_report": str(random.choice(data["with_credit_report"])[0]),
                "without_email": str(random.choice(data["without_email"])[0])
            }
        if test == 'lender_leads_check_duplicates':
            data = random.choice(Customer.get_random_duplicate_lead_phone_email(request))
            temp_data[test] = {
                'duplicate_phone_email': {'phone': data[0][1:], 'email': data[1]},
                'duplicate_phone': {'phone': data[0][1:], 'email': ''},
                'duplicate_email': {'phone': '', 'email': data[1]}
            }
        if test == 'sales_rep':
            data = Customer.get_random_leads_without_sales_rep(request)
            temp_data[test] = {'without_sales_rep': str(random.choice(data)[0])}

        if test == 'purchase':
            lead_id = Customer.get_random_leads_with_trusted_form_token(request)
            temp_data[test] = {
                'debt_consolidation': {
                    'lead_id': random.choice(lead_id)[0], 'purchaser_id': 1
                }
            }

        if test == 'creditors':
            data = Customer.get_random_leads_with_and_without_creditors(request)
            temp_data[test] = {
                "with_creditors": random.choice(data["with_creditors"])[0],
                "without_creditors": random.choice(data["without_creditors"])[0]
            }
            temp_data['deposits'] = {
                # "with_creditors": random.choice(data["with_creditors"])[0], # TODO: добавить после фикса бага
                "without_docs": random.choice(data["with_creditors"])[0]
            }

        if test == 'summary':
            data = Customer.get_random_leads_advantage_and_no_advantage(request)
            temp_data[test] = {
                "is_advantage_law": random.choice(data["is_advantage_law"])[0],
                "no_advantage_law": random.choice(data["no_advantage_law"])[0]
            }

        if test == 'profile':
            data = Customer.get_random_leads_third_and_no_third_party(request)
            temp_data[test] = {
                "is_third_party_speaker": random.choice(data["is_third_party_speaker"])[0],
                "no_third_party_speaker": random.choice(data["no_third_party_speaker"])[0]
            }

        if test == 'lead':
            data = Customer.get_random_leads_with_all_status_types(request)
            temp_data[test] = {
                leads_statuses.new: str(random.choice(data[leads_statuses.new])[0]),
                leads_statuses.docs_sent: str(random.choice(data[leads_statuses.docs_sent])[0]),
                leads_statuses.nurtured: str(random.choice(data[leads_statuses.nurtured])[0]),
                leads_statuses.ready_to_pitch: str(
                    random.choice(data[leads_statuses.ready_to_pitch])[0]),
                leads_statuses.hot: str(random.choice(data[leads_statuses.hot])[0]),
                leads_statuses.automation: str(random.choice(data[leads_statuses.automation])[0]),
                leads_statuses.mail_fax_docs: str(
                    random.choice(data[leads_statuses.mail_fax_docs])[0]),
                leads_statuses.pre_enrollment_sent: str(
                    random.choice(data[leads_statuses.pre_enrollment_sent])[0]),
                leads_statuses.pre_enrollment_completed: str(
                    random.choice(data[leads_statuses.pre_enrollment_completed])[0]),
            }
        if test == 'get_enrollment':
            data = Customer.get_random_new_active_deal_uuid(request)
            encode_data = random.choice(data)[0]
            uuid_value = str(uuid.UUID(bytes=encode_data))
            temp_data[test] = {
                "get_enrollment_valid": uuid_value
            }
        if test == 'get_enrollment_pinned_note':
            data = Customer.get_deal_uuid_with_pinned_note(request)
            encode_data = random.choice(data)[0]
            uuid_value = str(uuid.UUID(bytes=encode_data))
            temp_data[test] = {
                "enrollment_uuid_with_pinned": uuid_value
            }
        if test == 'get_enrollment_partner_commission':
            data = Customer.get_random_deal_uuid_with_partner_commission(request)
            encode_data = random.choice(data)[0]
            uuid_value = str(uuid.UUID(bytes=encode_data))
            temp_data[test] = {
                "enrollment_uuid_partner_commission": uuid_value
            }
        if test == 'get_enrollment_payoff_quotes':
            data = Customer.get_random_active_deal_id(request)
            temp_data[test] = {
                "get_enrollment_valid": data
            }
        if test == 'get_enrollment_ach':
            data = Customer.get_random_active_deal_id(request)
            temp_data[test] = {
                "enrollment_id_ach": data
            }
        if test == 'get_enrollment_find':
            data = Customer.get_random_any_data_of_one_applicant(request, user_type=customer_types.deal)
            random_record = random.choice(data['deal'])
            temp_data[test] = {
                'enrollment_find_valid': {
                    "enrollment_email_valid": str(random_record[5]),
                    "find_valid_last4_ssn": str(random_record[6])[-4:]
                }
            }
        if test == 'get_enrollment_underwriting':
            data = Customer.get_random_deal_with_and_without_underwriting(request)
            temp_data[test] = {
                "enrollment_id_with_underwriting":
                    str(random.choice(data["enrollment_id_with_underwriting"])[0])
            }
        if test == 'get_enrollment_settlement':
            data = Customer.get_random_active_deal_id_with_creditors(request)
            temp_data[test] = {
                'valid_creditor_id': {
                    "customerId": str(data[0]),
                    "creditorId": str(data[1])
                }
            }
        if test == 'get_loan_ach':
            data = Customer.get_random_any_data_of_one_applicant(request, user_type=customer_types.loan)
            random_record = random.choice(data['loan'])[0]
            temp_data[test] = {
                'loan_id_ach': str(random_record)
            }
        if test == 'get_loan_duplicates':
            data = Customer.get_random_any_data_of_one_applicant(request, user_type=customer_types.loan)
            random_record = random.choice(data['loan'])[6]
            temp_data[test] = {
                'valid_loan_personal_id': str(random_record)
            }
        if test == 'get_dnc_phone':
            data = Customer.get_random_phone_from_dnc(request)
            random_record = random.choice(data[0])
            temp_data[test] = {
                'valid_dnc_phone_from_get': random_record
            }
        if test == 'get_dnc_sms':
            data = Customer.get_random_sms_phone_from_dnc(request)
            random_record = random.choice(data[0])
            temp_data[test] = {
                'valid_dnc_sms_from_get': random_record
            }
        if test == 'get_dnc_email':
            data = Customer.get_random_email_from_dnc(request)
            random_record = random.choice(data[0])
            temp_data[test] = {
                'valid_email_from_get': random_record
            }
        if test == 'get_dnc_address':
            data = Customer.get_random_address_from_dnc(request)
            random_record = random.choice(data)
            temp_data[test] = {
                'get_dnc_valid_address': {
                    'valid_address_from_get': random_record[0],
                    'valid_city_from_get': random_record[1],
                    'valid_state_from_get': random_record[2],
                    'valid_zip_from_get': random_record[3]
                }
            }
        if test == 'higbee_approve':
            data = Customer.get_random_active_lead_for_higbee_uuid(request)
            encode_data = random.choice(data)[0]
            uuid_value = str(uuid.UUID(bytes=encode_data))
            temp_data[test] = {
                "higbee_uuid_positive": uuid_value
            }
        if test == 'higbee_decline':
            data = Customer.get_random_active_lead_for_higbee_uuid(request)
            encode_data = random.choice(data)[0]
            uuid_value = str(uuid.UUID(bytes=encode_data))
            temp_data[test] = {
                "higbee_uuid_decline": uuid_value
            }
        if test == 'higbee_hold':
            data = Customer.get_random_active_lead_for_higbee_uuid(request)
            encode_data = random.choice(data)[0]
            uuid_value = str(uuid.UUID(bytes=encode_data))
            temp_data[test] = {
                "higbee_uuid_hold": uuid_value
            }
        cfg = f'{Settings.CONFIGS_PATH}/{environ}_cfg/{environ}_api_data_cfg.json'
        with open(cfg, 'w') as f:
            json.dump(temp_data, f, indent=4, ensure_ascii=False)



