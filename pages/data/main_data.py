from collections import namedtuple


Configs = namedtuple('Configs', 'common auth ui_data path_talks_data')
ApiData = namedtuple('ApiData', 'data method case')
UIData = namedtuple('UIData', 'data test case')
URL = namedtuple('URL', 'url url_api url_api_path_talks')

class CustomerTypes:
    lead = 'lead'
    deal = 'deal'
    loan = 'loan'


class SendDocs:
    pre_enrollment = 'Pre-Enrollment'
    agreement_only = 'Agreement only'
    agreement_to_sign_and_save_file = 'Agreement to sign and save on files'
    agreement_with_loan = 'Agreement with Loan'
    upfront_final_loan = 'Upfront Final Loan'


class MainTabs:
    dashboard = 'Dashboard'
    tasks = 'Tasks'
    data = 'Data'
    leads = 'Leads'
    enrollments = 'Enrollments'
    loans = 'Loans'


class Roles:
    admin = 'admin'


class States:
    alabama = 'AL'
    alaska = 'AK'
    arizona = 'AZ'
    arkansas = 'AR'
    california = 'CA'
    colorado = 'CO'
    connecticut = 'CT'
    delaware = 'DE'
    district_of_columbia = 'DC'
    florida = 'FL'
    georgia = 'GA'
    hawaii = 'HI'
    idaho = 'ID'
    illinois = 'IL'
    indiana = 'IN'
    iowa = 'IA'
    kansas = 'KS'
    kentucky = 'KY'
    louisiana = 'LA'
    maine = 'ME'
    maryland = 'MD'
    massachusetts = 'MA'
    michigan = 'MI'
    minnesota = 'MN'
    mississippi = 'MS'
    missouri = 'MO'
    montana = 'MT'
    nebraska = 'NE'
    nevada = 'NV'
    new_hampshire = 'NH'
    new_jersey = 'NJ'
    new_mexico = 'NM'
    new_york = 'NY'
    north_carolina = 'NC'
    north_dakota = 'ND'
    ohio = 'OH'
    oklahoma = 'OK'
    oregon = 'OR'
    pennsylvania = 'PA'
    puerto_rico = 'PR'
    rhode_island = 'RI'
    south_carolina = 'SC'
    south_dakota = 'SD'
    tennessee = 'TN'
    texas = 'TX'
    utah = 'UT'
    vermont = 'VT'
    virginia = 'VA'
    washington = 'WA'
    west_virginia = 'WV'
    wisconsin = 'WI'
    wyoming = 'WY'
    guam = 'GU'


class SMSConsentText:
    americor_en = 'Thanks for your interest in our Americor program - https://americor.com/privacy-policy-glba/.'
    credit9_en = 'Thanks for your interest in our Americor program - https://americor.com/privacy-policy-glba/.'
    americor_es = 'Responda YES para suscribirse y recibir mensajes, STOP para cancelar la suscripción o HELP si necesita asistencia. Se pueden aplicar tarifas de mensajes y datos.'
    credit9_es = 'Responda YES para suscribirse y recibir mensajes, STOP para cancelar la suscripción o HELP si necesita asistencia. Se pueden aplicar tarifas de mensajes y datos.'


sms_consent_text = SMSConsentText()
customer_types = CustomerTypes()
send_docs = SendDocs()
main_tabs = MainTabs()
roles = Roles()
states = States()
