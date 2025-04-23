import random
import uuid
from datetime import date, timedelta, datetime
from typing import NamedTuple

import pandas as pd
from mimesis import Person, Address, Generic, Text
from mimesis.builtins import USASpecProvider
from mimesis.enums import Gender
from mimesis.locales import Locale

from autotests.pages.settings import Settings
from autotests.pages.utils import get_experian_customer_list_from_csv, is_weekday

LOCALE = Locale.EN
PERSON = Person(locale=LOCALE)
ADDRESS = Address(locale=LOCALE)
GENERIC = Generic(locale=LOCALE)
TEXT = Text(locale=LOCALE)
USA = USASpecProvider()


class CreditReportDataApi(dict):
    state: str
    firstName: str
    lastName: str
    phoneMobile: str
    phoneHome: str
    ssn: str
    zip: str
    address: str
    city: str
    dob: str
    source: str
    isValidityCheckRequired: str


class CreditReportData(NamedTuple):
    state: str
    first_name: str
    last_name: str
    ssn: str
    zip_code: str
    address: str
    city: str
    dob: str


class CreditReportDataCsv(NamedTuple):
    first_name: str
    last_name: str
    ssn: str
    zip_code: str
    address: str
    city: str
    dob: str
    state: str


class LoanPlanData(NamedTuple):
    required_loan_amount: float
    prepaid_finance_charge: float
    loan_amount_with_points: float
    annual_percentage_rate: str
    interest_rate: str
    payment_interval: str
    term: str
    loan_payment: float
    total_interest: float
    total_amount_paid: float


class TestData:
    """
    Class for test data.
    """

    @staticmethod
    def first_name(gender: str = 'male') -> str:
        """
        Get first name of a person.

        :param gender: Gender - male or female.
        :return: First name.
        """
        return PERSON.first_name(Gender.MALE) if gender == 'male' \
            else PERSON.first_name(Gender.FEMALE)

    @staticmethod
    def last_name(gender: str = 'male') -> str:
        """
        Get last name of a person.

        :param gender: Gender - male or female.
        :return: Last name.
        """
        return PERSON.last_name(Gender.MALE) if gender == 'male' \
            else PERSON.last_name(Gender.FEMALE)

    @staticmethod
    def email(unique: bool = True) -> str:
        """
        Get email address with unique domain.

        :param unique: Parameter for get unique domain.
        :return: Email address.
        """
        return PERSON.email(domains=['test.com'], unique=unique)

    @staticmethod
    def phone(mask: str = '###-###-####') -> str:
        """
        Get phone number with mask.

        :param mask: Mask for phone number.
        :return: Phone number.
        """
        return PERSON.telephone(mask=mask)

    @staticmethod
    def phone_for_sms_consent() -> str:
        """
        Get random phone number from list of phone numbers.
        """
        phone = ['5704414263', '5704414264', '5704414262', '5704414261']

        return random.choice(phone)

    @staticmethod
    def address() -> str:
        """
        Get full address of a person.
        """
        return ADDRESS.address()

    @staticmethod
    def city() -> str:
        """
        Get city.
        """
        return ADDRESS.city()

    @staticmethod
    def zip_code() -> str:
        """
        Get zip code.
        """
        return ADDRESS.zip_code()

    @staticmethod
    def state() -> str:
        """
        Get state.
        """
        return ADDRESS.state()

    @staticmethod
    def state_short() -> str:
        """
        Get state short name.
        """
        return ADDRESS.state(abbr=True)

    @staticmethod
    def ssn() -> str:
        """
        Get SSN(Social Security number).
        """
        return ''.join(USA.ssn().split('-'))

    @staticmethod
    def dob(start: int = 1940, end: int = 2000, mask: str = '%m/%d/%Y') -> str:
        """
        Get date.

        :param start: Start date.
        :param end: End date.
        :param mask: Mask for date.
        :return: Date.
        """
        return GENERIC.datetime.date(start=start, end=end).strftime(mask)

    @staticmethod
    def date(start: int = 1990, end: int = 2000, mask: str = '%Y-%m-%d') -> str:
        """
        Get date.

        :param start: Start date.
        :param end: End date.
        :param mask: Mask for date.
        :return: Date.
        """
        return GENERIC.datetime.date(start=start, end=end).strftime(mask)

    @staticmethod
    def get_date(days: int) -> str:
        """
        Returns the date +/- {{days}} from the current date.

        :param days: Number of days.
        :return: Date.
        """
        delta_date = (date.today() + timedelta(days=days)).strftime("%m/%d/%Y")
        return delta_date

    @staticmethod
    def get_only_working_date(days: int) -> str:
        """
        Returns the date +/- {{days}} from the current date and only working date.

        :param days: Number of days.
        :return: Date.
        """
        current_date = date.today()
        while days:
            current_date += timedelta(days=1 if days > 0 else -1)
            if is_weekday(current_date):
                days -= 1 if days > 0 else -1
        return current_date.strftime("%m/%d/%Y")

    @staticmethod
    def get_only_working_date_from_any_date(input_date: str, days: int) -> str:
        """
        Returns the date +/- {{days}} from the input date and only working date.

        :param input_date: Input date.
        :param days: Number of days.
        :return: Date.
        """
        date_object = datetime.strptime(input_date, "%m/%d/%Y")
        while days:
            date_object += timedelta(days=1 if days > 0 else -1)
            if is_weekday(date_object):
                days -= 1 if days > 0 else -1
        return date_object.strftime("%m/%d/%Y")

    @staticmethod
    def sales_rep(all_sales_rep: bool = False) -> str | list[str]:
        """
        Get Sales Rep.

        :param all_sales_rep: True for all sales rep, False for only one random sales rep.
        :return: Sales Rep or list of sales reps.
        """
        sales_rep = ['autotest.c9_upfront_loan_processor+sales+opener', 'dmitry paxomov']

        return sales_rep if all_sales_rep else random.choice(sales_rep)

    @staticmethod
    def sources(all_sources: bool = False) -> str | list[str]:
        """
        Get random source from list of sources or all sources.

        :param all_sources: True if all sources, False if only one random sources.
        :return: Source or list of sources.
        """
        sources = [
            'Americor Google SEM', 'Americor Mailbox', 'Americor Web Lead', 'Credit9 Mailbox', 'Credit.org',
            'Credit Sesame', 'Google', 'Facebook', 'Other Digital', 'Referral', 'Mailer (no code)',
            'HSM_CTC', 'EVO', 'EX', 'NT', 'NT2', 'Radio', 'Sales VM', 'Other'
        ]

        return sources if all_sources else random.choice(sources)

    @staticmethod
    def companies(all_companies: bool = False) -> str | list[str]:
        """
        Get random company from list of companies or all companies.

        :param all_companies: True if all companies, False if only one random companies.
        :return: List of companies or one random company.
        """
        companies = [
            'Americor', 'Credit9'
        ]

        return companies if all_companies else random.choice(companies)

    @staticmethod
    def channels(all_channels: bool = False) -> str | list[str]:
        """
        Get random channel from list of channels or all channels.

        :param all_channels: True for all channels or False for only one random channel.
        :return: List of channels or one channel.
        """
        channels = [
            'apply.americor.com', 'apply.americor.com/new', 'apply.americor.com/new1', 'apply.americor.com/new2',
            'apply.americor.com/new3', 'apply.americor.com/new4', 'apply.americor.com/new5'
        ]

        return channels if all_channels else random.choice(channels)

    @staticmethod
    def hardship_reason(all_reasons: bool = False) -> str | dict:
        """
        Get random hardship reason from list of reasons or all reasons.

        :param all_reasons: True for all reasons, False for only one random hardship reasons.
        :return: Hardship reason or list of reasons.
        """
        hardship_reasons = {
            1: 'Avoid Bankruptcy',
            3: 'Divorced',
            5: 'Illness in Family',
            6: 'Loss of Income',
            7: 'Widowed',
            8: 'Medical Issues',
            9: 'Other',
            10: 'Birth',
            11: 'Special Needs Family',
            12: 'Loss of Job',
            13: 'Laid Off',
            14: 'Widowed'
        }

        return hardship_reasons if all_reasons else random.choice(list(hardship_reasons.values()))

    @staticmethod
    def grounds_of_exemption(all_grounds_of_exemption: bool = False) -> str | list[str]:
        """
        Get random ground of exemption from list of grounds of exemption or all grounds of exemption.

        :param all_grounds_of_exemption: True if all grounds of exemption, False if only one random exemption.
        :return: Random ground of exemption or all grounds of exemption.
        """
        grounds_of_exemption = {
            'Overtime at Current Job': 0,
            'Additional Employment (i.e., second job)': 1,
            'Gift/Donation from Family or Charity': 2,
            'Tax Refund Pending': 3,
            'Future Child Support/Alimony (i.e., car loan)': 4,
            'Funds from 401K/Stocks': 5,
            'Pay Off Other Debt in The Next Year (i.e., car loan)': 6,
            'Reduce Ongoing Discretionary Subscriptions (i.e., cable, Netflix, gym, etc.)': 7
        }

        return grounds_of_exemption if all_grounds_of_exemption else random.choice(list(grounds_of_exemption.values()))

    @staticmethod
    def states(all_states: bool = False) -> dict | list[dict]:
        """
        Get random state from list of states or all states.

        :param all_states: True for all states data, False for only specific state.
        :return: Dict of random state or all states data.
        """
        states = [
            {"name": "Alabama", "code": "AL"}, {"name": "Alaska", "code": "AK"}, {"name": "Arizona", "code": "AZ"},
            {"name": "Arkansas", "code": "AR"}, {"name": "California", "code": "CA"}, {"name": "Iowa", "code": "IA"},
            {"name": "Colorado", "code": "CO"}, {"name": "Connecticut", "code": "CT"}, {"name": "Kansas", "code": "KS"},
            {"name": "Florida", "code": "FL"}, {"name": "Georgia", "code": "GA"}, {"name": "Hawaii", "code": "HI"},
            {"name": "Idaho", "code": "ID"}, {"name": "Illinois", "code": "IL"}, {"name": "Indiana", "code": "IN"},
            {"name": "Kentucky", "code": "KY"}, {"name": "Louisiana", "code": "LA"}, {"name": "Texas", "code": "TX"},
            {"name": "Maine", "code": "ME"}, {"name": "Maryland", "code": "MD"}, {"name": "Mississippi", "code": "MS"},
            {"name": "Massachusetts", "code": "MA"}, {"name": "Michigan", "code": "MI"}, {"name": "Ohio", "code": "OH"},
            {"name": "Missouri", "code": "MO"}, {"name": "Montana", "code": "MT"}, {"name": "Nebraska", "code": "NE"},
            {"name": "Nevada", "code": "NV"}, {"name": "New Hampshire", "code": "NH"}, {"name": "Utah", "code": "UT"},
            {"name": "New Jersey", "code": "NJ"}, {"name": "Minnesota", "code": "MN"}, {"name": "Guam", "code": "GU"},
            {"name": "New Mexico", "code": "NM"}, {"name": "New York", "code": "NY"}, {"name": "Oregon", "code": "OR"},
            {"name": "Oklahoma", "code": "OK"}, {"name": "Vermont", "code": "VT"}, {"name": "Virginia", "code": "VA"},
            {"name": "Delaware", "code": "DE"}, {"name": "District of Columbia", "code": "DC"},
            {"name": "North Carolina", "code": "NC"}, {"name": "North Dakota", "code": "ND"},
            {"name": "Pennsylvania", "code": "PA"}, {"name": "Puerto Rico", "code": "PR"},
            {"name": "Rhode Island", "code": "RI"}, {"name": "South Carolina", "code": "SC"},
            {"name": "South Dakota", "code": "SD"}, {"name": "Tennessee", "code": "TN"},
            {"name": "Washington", "code": "WA"}, {"name": "West Virginia", "code": "WV"},
            {"name": "Wisconsin", "code": "WI"}, {"name": "Wyoming", "code": "WY"}
        ]

        return states if all_states else random.choice(states)

    @staticmethod
    def status_income(all_statuses: bool = False) -> str | list[str]:
        """
        Get random status of income from list of statuses or all statuses.

        :param all_statuses: True if all statuses, False if only one random status.
        :return: random status of income or list of statuses.
        """
        statuses = {
            'Full-Time Employed': 0,
            'Part-Time Employed': 1,
            'Self-Employed': 2,
            'Unemployed': 3,
            'Retired': 4
        }

        return statuses if all_statuses else random.choice(list(statuses.values()))

    @staticmethod
    def occupations_income(all_occupations: bool = False) -> str | list[str]:
        """
        Get random occupation from list of occupations or all occupations.

        :param all_occupations: True if all occupations, False if only one random occupations.
        :return: Random occupation or all occupations.
        """
        occupations = {
            'ATM Owner / Operator': 0,
            'Accountant': 1,
            'Administrative / Office Support': 2,
            'Agriculture / Farming': 3,
            'Antiquities / Auctions': 4
        }

        return occupations if all_occupations else random.choice(list(occupations.values()))

    @staticmethod
    def primary_sources_of_income(all_sources: bool = False) -> str | list[str]:
        """
        Get random source of income from list of sources or all sources.

        :param all_sources: True for all sources, False for only one random source.
        :return: Random source of income.
        """
        sources = {
            'Alimony': 0,
            'Annuities': 1,
            'Child Support': 2,
            'Current Savings': 3,
            'Dividends': 4
        }

        return sources if all_sources else random.choice(list(sources.values()))

    @staticmethod
    def words(quantity: int = 0) -> str | list[str]:
        """
        Get random word or list of words.

        :param quantity: number of words to return
        :return: random word or list of words
        """
        return TEXT.words(quantity) if quantity else TEXT.word()

    @staticmethod
    def creditors() -> str:  # TODO необходимо добавить еще кредиторов и возвомжность выбора
        """
        Get creditor. use for now: ASTRA.
        """
        return 'AD ASTRA'

    @staticmethod
    def digits(start: int = 0, end: int = 0) -> int:
        """
        Get random digit.

        :param start: start index
        :param end: end index
        :return: random digit
        """
        return random.randint(start, end) if start else random.randint(1, 10)

    @staticmethod
    def routing_number(all_numbers: bool = False) -> str | list[str]:
        """
        Get random routing number.

        :param all_numbers: True for all routing numbers, False for only one random routing number.
        :return: random routing number or list of routing numbers.
        """
        routing_numbers = ['256074974', '122106455', '103000648']

        return routing_numbers if all_numbers else random.choice(routing_numbers)

    @staticmethod
    def uuid() -> uuid:
        """
        Get random UUID.

        :return: random UUID.
        """
        return str(uuid.uuid4())

    @staticmethod
    def credit_report_data(state: str = None) -> CreditReportData:
        """
        Get credit report data.

        :param state: State
        :return: Credit report data
        """
        clients_data = [
            {
                'CA': {
                    'state': 'CA',
                    'first_name': 'paul',
                    'last_name': 'burnia',
                    'ssn': '666390427',
                    'zip_code': '90746',
                    'address_full': '19103 tajauta ave',
                    'city': 'carson',
                    'dob': '08101961'
                },
                'NC': {
                    'state': 'NC',
                    'first_name': 'GARY',
                    'last_name': 'WORD',
                    'ssn': '666293067',
                    'zip_code': '27106',
                    'address_full': '3960 WINDSOR PLACE DR',
                    'city': 'WINSTON SALEM',
                    'dob': '12221953'
                }
            }
        ]

        data = {}
        if not state:
            filename = f'{Settings.DATA_PATH}/leads_list.csv'
            df = pd.read_csv(filename)
            leads_list_from_csv = df.to_dict('records')
            data = random.choice(leads_list_from_csv)
        if state:
            for i in clients_data:
                data = i[state]

        return CreditReportData(
            state=data['state'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            ssn=str(data['ssn']),
            zip_code=str(data['zip_code'])[:5],
            address=data['address_full'],
            city=data['city'],
            dob=data['dob'],
        )

    @staticmethod
    def credit_report_data_for_api(state: str = None) -> dict:
        """
        Get credit report data for API.

        :param state: State
        :return: Credit report data
        """
        clients_data = [
            {
                'CA': {
                    'state': 'CA',
                    'firstName': 'paul',
                    'lastName': 'burnia',
                    'ssn': '666390427',
                    'zip': '90746',
                    'address': '19103 tajauta ave',
                    'city': 'carson',
                    'dob': '1961-08-10',  # Y-m-d
                },
                'NC': {
                    'state': 'NC',
                    'firstName': 'robert',
                    'lastName': 'miller',
                    'ssn': '666232884',
                    'zip': '28518',
                    'address': '504 E BOSTIC ST',
                    'city': 'Beulaville',
                    'dob': '1952-12-28',  # Y-m-d
                }
            }
        ]

        data = {}
        if not state:
            filename = f'{Settings.DATA_PATH}/leads_list.csv'
            df = pd.read_csv(filename)
            leads_list_from_csv = df.to_dict('records')
            data = random.choice(leads_list_from_csv)
        if state:
            for i in clients_data:
                data = i[state]

        return CreditReportDataApi(
            state=data['state'],
            firstName=data['firstName'],
            lastName=data['lastName'],
            ssn=str(data['ssn']),
            zip=str(data['zip'])[:5],
            address=data['address'],
            city=data['city'],
            dob=data['dob'],
        )

    @staticmethod
    def credit_report_data_from_csv(state: str = None) -> dict:
        """
        Get credit report data from CSV.

        :param state: State
        :return: CreditReportData
        """
        customer_list = get_experian_customer_list_from_csv(state)
        data = random.choice(customer_list)
        date_string = str(int(data['dob']))
        dob = f'{date_string[-4:]}-{date_string[-8:-6]}-{date_string[-6:-4]}'
        credit = {
            'firstName': data['first_name'],
            'lastName': data['last_name'],
            'ssn': data['ssn'],
            'zip': str(data['zip_code'])[:5],
            'state': data['state'],
            'address': data['address_full'],
            'city': data['city'],
            'dob': dob
        }
        return credit

    @staticmethod
    def report_data_from_specific_creditors(customer_first_name: str = None) -> CreditReportData | None:
        """
        Get credit report data for specific customer.

        :param customer_first_name: Customer first name
        :return: CreditReportData if exists else None
        """
        clients_data = [
            {
                'PAUL': {
                    'state': 'CA',
                    'first_name': 'paul',
                    'last_name': 'burnia',
                    'ssn': '666390426',
                    'zip_code': '90746',
                    'address_full': '19103 tajauta ave',
                    'city': 'carson',
                    'dob': '08101961'
                },
                'JAMES': {
                    'state': 'OH',
                    'first_name': 'james',
                    'last_name': 'kline',
                    'ssn': '666682230',
                    'zip_code': '434129746',
                    'address_full': '418 clubhouse blvd',
                    'city': 'curtice',
                    'dob': '08291946'
                },
                'PETULA': {
                    'state': 'TX',
                    'first_name': 'petula',
                    'last_name': 'kiefer',
                    'ssn': '666328740',
                    'zip_code': '75495',
                    'address_full': '981 springtown rd',
                    'city': 'van alstyne',
                    'dob': '11041953'
                },
                'BRIAN': {
                    'state': 'CA',
                    'first_name': 'brian',
                    'last_name': 'blakely',
                    'ssn': '666416169',
                    'zip_code': '900352601',
                    'address_full': '1077 s hayworth ave',
                    'city': 'los angeles',
                    'dob': '2081967'
                }
            }
        ]

        data = {}
        if not customer_first_name:
            return None

        if customer_first_name:
            for i in clients_data:
                data = i[customer_first_name]

        return CreditReportData(
            state=data['state'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            ssn=str(data['ssn']),
            zip_code=str(data['zip_code'])[:5],
            address=data['address_full'],
            city=data['city'],
            dob=data['dob']
        )

    @staticmethod
    def check_whether_to_eom_check_box(amount_of_working_days: int) -> bool:
        today = date.today()
        working_days_count = 0

        for i in range(amount_of_working_days):
            future_date = today + timedelta(days=i)
            if future_date.month != today.month:
                break
            if future_date.weekday() < 5:
                working_days_count += 1
        if working_days_count <= (amount_of_working_days - 1):
            return True
        else:
            return False
