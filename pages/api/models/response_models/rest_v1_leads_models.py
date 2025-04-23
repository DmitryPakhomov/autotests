from pydantic import BaseModel, field_validator, ConfigDict, RootModel
from pydantic_core.core_schema import ValidationInfo


class RejectReason(BaseModel):
    id: int
    title: str
    duplicateCustomerDate: str | None
    firstDuplicateCustomerRejectReason: str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class LenderLeadsCreditors(BaseModel):
    name: str
    balance: int


class LenderLeadsResponse(BaseModel):
    id: int
    firstName: str
    lastName: str
    email: str | None
    noEmail: bool | None
    phoneMobile: str | None
    phoneHome: str | None
    address: str | None
    city: str | None
    zip: str | None
    ssn: str | None
    dob: str | None
    source: str | None
    campaign: str | None
    channel: str | None
    quality: str | None
    rejectReason: RejectReason | None
    validityCheckStatus: str
    creditors: list[LenderLeadsCreditors]
    isRejected: bool | None

    model_config = ConfigDict(strict=True, extra='forbid')

    @field_validator('noEmail')
    def no_email_value_checking(cls, v, info: ValidationInfo):
        if info.data['email'] is None:
            assert v, {'as_is': v, 'to_be': True}
        else:
            assert not v, {'as_is': v, 'to_be': False}
        return v

    @field_validator('rejectReason')
    def reject_reason_value_checking(cls, v, info: ValidationInfo):
        if info.data['quality'] == 'rejected':
            assert v, {'as_is': v, 'to_be': 'reject reason'}
        if info.data['quality'] == 'active':
            assert not v, {'as_is': v, 'to_be': None}
        return v

class LenderLeadsCheckDuplicatesResponse(BaseModel):
    id: int
    insTs: str
    originalStatus: int
    originalStatusText: str
    rejectReason: int | None
    rejectReasonText: str | None

    model_config = ConfigDict(strict=True, extra='forbid')

    @field_validator('rejectReasonText')
    def reject_reason_text_value_checking(cls, v, info: ValidationInfo):
        if info.data['rejectReason'] == 4:
            assert v == 'Duplicate Lead', {'as_is': v, 'to_be': 'Duplicate Lead'}
        if info.data['rejectReason'] is None:
            assert not v, {'as_is': v, 'to_be': None}
        return v


class Creditors(BaseModel):
    id: int
    status: int
    statusText: str
    originalCreditor: str
    originalAccount: str
    originalBalance: int
    originalCurrentBalance: int
    originalCreditorGroupId: int | None
    originalCreditorGroupName: str | None
    cardholderName: str
    clientConfirmFullAccountNumber: int | None
    fullAccountNumberDigits: int | None

    model_config = ConfigDict(strict=True, extra='forbid')


class CreditorsResponse(RootModel):
    root: list[Creditors]


class Deposits(BaseModel):
    id: int | None
    date: str | None
    description: str | None
    statusDate: str | None
    status: int | None
    statusText: str | None
    amount: float
    memo: str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class DepositsResponse(RootModel):
    root: list[Deposits]


class SummaryResponse(BaseModel):
    id: int
    name: str
    type: str
    lastPaymentMadeDate: str | None
    lastPaymentMadeAmount: str | None
    accountSavings: int
    nextWithdrawDate: str | None
    nextWithdrawAmount: int | None
    accountSettled: int
    settlementOffers: int
    accountInTheProgram: int
    timeInProgram: int
    estimatedPayments: int
    paymentsMade: int
    totalProgramDebt: int
    currentDebt: int | float
    remainingBalance: int | float
    savings: float
    savingMonths: int
    programMonth: int
    programStartDate: str | None
    programEndDate: str | None
    nomUntilLoanAvailable: int
    loanAvailable: bool
    loanIsSigned: bool
    loanAmount: int | None
    loanAvailableIn: str | None
    loanAvailableDate: str | None
    settlementFeePercent: int
    detailedHardshipReason: str | None
    isAdvantageLaw: bool

    model_config = ConfigDict(strict=True, extra='forbid')


class Address(BaseModel):
    street: str | None
    city: str | None
    state: str | None
    zip: str | None


class EmergencyContact(BaseModel):
    name: str | None
    phoneNumber: str | None


class ThirdPartySpeaker(BaseModel):
    fullName: str
    phone: str
    email: str
    typeOfAuth: int


class Profile(BaseModel):
    email: str
    phoneMobile: str | None
    phoneHome: str | None
    bestTimeToCall: int | None
    thirdPartySpeaker: None | ThirdPartySpeaker
    address: Address
    emergencyContact: EmergencyContact
    bankAccount: str | None


class BestTimeToCall(RootModel):
    root: dict[str, str]


class TypeOfAuth(RootModel):
    root: dict[str, str]


class ProfileResponse(BaseModel):
    profile: Profile
    bestTimeToCall: BestTimeToCall
    typeOfAuth: TypeOfAuth

    model_config = ConfigDict(strict=True, extra='forbid')


class PreLeadResponse(BaseModel):
    preLeadId: int
    customerId: int
    firstName: str
    lastName: str
    phone: str
    email: str
    loanAmount: int
    totalDebt: float
    company: str

    model_config = ConfigDict(strict=True, extra='forbid')


class CallSchedulerResponse(BaseModel):
    callschedulerScheduled: bool
    automationState: int

    model_config = ConfigDict(strict=True, extra='forbid')


class FetchCreditReport(BaseModel):
    callschedulerScheduled: bool
    automationState: int

    model_config = ConfigDict(strict=True, extra='forbid')


class HigbeeAcceptRequest(BaseModel):
    callschedulerScheduled: bool
    model_config = ConfigDict(strict=True, extra='forbid')


class HigbeeDeclineRequest(BaseModel):
    callschedulerScheduled: bool
    model_config = ConfigDict(strict=True, extra='forbid')


class HigbeeHoldRequest(BaseModel):
    callschedulerScheduled: bool
    model_config = ConfigDict(strict=True, extra='forbid')


class LeadSetConnectedResponse(BaseModel):
    id: int
    callscheduler_connected: int
    automation_state: int

    model_config = ConfigDict(strict=True, extra='forbid')


class LeadSetScheduledResponse(BaseModel):
    id: int
    callscheduler_scheduled: int
    automation_state: int

    model_config = ConfigDict(strict=True, extra='forbid')


class LeadResponse(BaseModel):
    id: int
    status: int
    statusDate: str
    name: str
    type: str
    firstName: str
    lastName: str
    email: str | None
    phoneMobile: str | None
    phoneHome: str | None
    ssnLast4: str | None
    dateOfBirth: str | None
    city: str | None
    state: str | None
    street: str | None
    zipCode: str | None
    creditReportId: int | None
    salesId: int | None
    salesIp: str | None
    salesName: str | None
    lang: str | None
    fileStatus: str | None
    processingPaymentsService: str | None
    isRegistered: bool
    paperStatementsEnabled: bool
    negotiatorId: str | None
    negotiatorName: str | None
    processingPaymentsServiceAccountNumber: str | None
    enrollmentEsignaturePrimaryApplicantUrl: str | None
    enrollmentEsignatureCoApplicantUrl: str | None
    isRejected: bool

    model_config = ConfigDict(strict=True, extra='forbid')


    @field_validator('lang')
    def lang_value_checking(cls, v):
        assert v in ['EN', 'ES'], {'as_is': v, 'to_be': 'EN or ES'}
        return v
