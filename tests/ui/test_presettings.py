import json
import os
import random
from typing import Any

import pytest
from dotenv import load_dotenv
from selenium.webdriver.chrome.webdriver import WebDriver

from autotests.pages.data.enrollments_data import enrollments_pages
from autotests.pages.data.leads_data import leads_statuses, leads_pages
from autotests.pages.data.main_data import roles, customer_types
from autotests.pages.data.test_data import TestData
from autotests.pages.queries import Customer, Applicant
from autotests.pages.settings import Settings

load_dotenv()


class TestPresettings:
    @pytest.mark.parametrize(
        'role',
        [
            roles.admin
        ]
    )
    def test_update_auth_cookies(
            self,
            role: str,
            browser: WebDriver,
            environ: str,
            login_page
    ) -> Any:
        """ Update auth cookies in config - """
        cookies = login_page.login_with_cookies_hmac(role=role)
        cfg = f'{Settings.CONFIGS_PATH}/{environ}_cfg/{environ}_auth_cfg.json'

        with open(cfg) as config_file:
            config_data = config_file.read()

        temp_data = json.loads(config_data)
        temp_data[role]['cookies'] = cookies

        with open(cfg, 'w') as f:
            json.dump(temp_data, f, indent=4, ensure_ascii=False)

    @pytest.mark.parametrize(
        'role',
        [
            roles.admin,
            roles.sales_debt_consultant,
            roles.sales_upfront_loan_processor
        ]
    )
    def test_update_auth_cookies_from_prepare_leads(
            self,
            role: str,
            browser: WebDriver,
            environ: str,
            login_page
    ) -> Any:
        """ Update auth cookies in config - """
        cookies = login_page.login_with_cookies_hmac(role=role)
        cfg = f'{Settings.CONFIGS_PATH}/{environ}_cfg/{environ}_auth_cfg.json'

        with open(cfg) as config_file:
            config_data = config_file.read()

        temp_data = json.loads(config_data)
        temp_data[role]['cookies'] = cookies

        with open(cfg, 'w') as f:
            json.dump(temp_data, f, indent=4, ensure_ascii=False)

    @pytest.mark.parametrize(
        'role',
        [
            roles.admin,
            roles.admin2,
            roles.sales,
            roles.sales_upfront_loan_processor,
            roles.sales_debt_consultant,
            roles.sales_debt_consultant_sp,
            roles.negotiations,
            roles.opener,
            roles.accounting,
            roles.enrollments,
            roles.customer_service,
            roles.customer_service_team_leads,
            roles.retention,
            roles.underwriting_manager,
            roles.loc_customer_service,
            roles.loan_consultant
        ]
    )
    def test_update_auth_cookies_full(
            self,
            role: str,
            browser: WebDriver,
            environ: str,
            login_page
    ) -> Any:
        """ Update auth cookies in config - """
        cookies = login_page.login_with_cookies_hmac(role=role)
        cfg = f'{Settings.CONFIGS_PATH}/{environ}_cfg/{environ}_auth_cfg.json'

        with open(cfg) as config_file:
            config_data = config_file.read()

        temp_data = json.loads(config_data)
        temp_data[role]['cookies'] = cookies

        with open(cfg, 'w') as f:
            json.dump(temp_data, f, indent=4, ensure_ascii=False)

    @pytest.mark.parametrize(
        'test',
        [
             'leads_pages_console_log',
             'common_page_search',
             'email',
             'email_for_agreement'
        ]
    )
    def test_update_ui_data(
            self,
            environ: str,
            test: str,
            config,
            lead_create_page,
            get_token_leads,
            login_page,
            lead_profile_page,
            request
    ) -> Any:
        """ Update data in config for UI tests - """
        temp_data = config.ui_data

        if test == 'email':
            data = Customer.get_random_customer_id_by_email(request)
            if data:
                lead_id = str(random.choice(data)[0])
            else:
                credit_data = TestData.credit_report_data_for_api(state='CA')
                credit_data.update(email=os.environ['GMAIL_LOGIN'])
                lead_id = lead_create_page.create_lead_via_api(get_token_leads, **credit_data)
                login_page.login_with_cookies(page=leads_pages.leads_profile, client_id=lead_id)
                lead_profile_page.check_rejected_lead()
                lead_profile_page.added_co_applicant_by_email()
            #
            data_deal = Customer.get_random_customer_id_by_email(request, customer_type=customer_types.deal)
            if data_deal:
                deal_id = str(random.choice(data_deal)[0])
            else:
                deals = Customer.get_random_any_data_of_one_applicant(request, user_type=customer_types.deal)
                deal = random.choice(deals[customer_types.deal])
                deal_id = int(deal[0])
                applicant_id = int(deal[7])
                Applicant.update_applicant_2(
                    request,
                    applicant_id=applicant_id,
                    first_name='paul',
                    email=os.environ['GMAIL_LOGIN']
                )
                deal_id = str(deal_id)
                login_page.login_with_cookies(
                    page=enrollments_pages.enrollments_profile, client_id=deal_id)
                lead_profile_page.added_co_applicant_lite()
            temp_data[test] = {
                "deal_id": deal_id,
                "lead_id": lead_id
            }

        if test == 'email_for_agreement':
            leads = Customer.get_applicant_prepare_for_email_agreement(request,
                user_type=customer_types.lead)
            if leads:
                lead = random.choice(leads[customer_types.lead])
                lead_id = str(lead[0])
                applicant_id = int(lead[6])
                Applicant.update_applicant_2(
                    request,
                    applicant_id=applicant_id,
                    first_name='paul',
                    email=os.environ['GMAIL_LOGIN']
                )
            temp_data[test] = {
                "lead_id_agreement_send_email": lead_id,
            }
        if test == 'leads_pages_console_log':
            data = Customer.get_random_leads_with_all_status_types(request)
            temp_data[test] = {
                leads_statuses.new: str(random.choice(data[leads_statuses.new])[0]),
                leads_statuses.docs_sent: str(random.choice(data[leads_statuses.docs_sent])[0]),
                leads_statuses.nurtured: str(random.choice(data[leads_statuses.nurtured])[0]),
                leads_statuses.ready_to_pitch: str(
                    random.choice(data[leads_statuses.ready_to_pitch])[0]),
                leads_statuses.hot: str(random.choice(data[leads_statuses.hot])[0]),
                #leads_statuses.automation: str(random.choice(data[leads_statuses.automation])[0]), #TODO исчезли такие лиды, пока закоментил что бы не падало
                leads_statuses.mail_fax_docs: str(
                    random.choice(data[leads_statuses.mail_fax_docs])[0]),
                leads_statuses.pre_enrollment_sent: str(
                    random.choice(data[leads_statuses.pre_enrollment_sent])[0]),
                leads_statuses.pre_enrollment_completed: str(
                    random.choice(data[leads_statuses.pre_enrollment_completed])[0]),
            }
        if test == 'common_page_search':
            leads = Customer.get_random_any_data_of_one_applicant(request, user_type=customer_types.lead)
            lead = random.choice(leads[customer_types.lead])
            lead_data = {
                'id': str(lead[0]),
                'type': lead[1],
                'name': f"{lead[2]} {lead[3]}".lower(),
                'phone': lead[4],
                'email': lead[5]
            }

            deals = Customer.get_random_any_data_of_one_applicant(request, user_type=customer_types.deal)
            deal = random.choice(deals[customer_types.deal])
            deal_data = {
                'id': str(deal[0]),
                'type': 'enrollment',
                'name': f"{deal[2]} {deal[3]}".lower(),
                'phone': deal[4],
                'email': deal[5]
            }
            loans = Customer.get_random_any_data_of_one_applicant(request, user_type=customer_types.loan)
            loan = random.choice(loans[customer_types.loan])
            loan_data = {
                'id': str(loan[0]),
                'type': loan[1],
                'name': f"{loan[2]} {loan[3]}".lower(),
                'phone': loan[4],
                'email': loan[5]
            }
            loans_pro = Customer.get_random_any_data_of_one_applicant(request,
                user_type=customer_types.loan_pro)
            loan_pro = random.choice(loans_pro[customer_types.loan_pro])
            loan_pro_data = {
                'id': str(loan_pro[0]),
                'type': 'loan pro',
                'name': f"{loan_pro[2]} {loan_pro[3]}".lower(),
                'phone': loan_pro[4],
                'email': loan_pro[5]
            }
            temp_data[test] = {
                customer_types.lead: lead_data,
                customer_types.deal: deal_data,
                customer_types.loan: loan_data,
                customer_types.loan_pro: loan_pro_data
            }

        cfg = f'{Settings.CONFIGS_PATH}/{environ}_cfg/{environ}_ui_data_cfg.json'
        with open(cfg, 'w') as f:
            json.dump(temp_data, f, indent=4, ensure_ascii=False)
