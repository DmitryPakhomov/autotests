from pydantic import BaseModel, field_validator, ConfigDict, RootModel
from pydantic_core.core_schema import ValidationInfo


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


class BestTimeToCall(RootModel):
    root: dict[str, str]


class TypeOfAuth(RootModel):
    root: dict[str, str]


class EnrollmentResponse(BaseModel):
    uuid: str
    type: str
    firstName: str
    lastName: str
    middleName: str | None
    status: int
    paymentStatus: int
    currentFico: int | None
    initialFico: int | None
    programLength: int
    fileStatus: int | None
    collectionRecoveryStatus: int | None
    collectionRecoveryFileStatus: int | None
    cancellationDatetime: str | None
    cancellationReason: str | None
    firstDepositClearedDate: str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class Item(BaseModel):
    id: int
    type: str
    clientTypeChangeDate: str | None
    firstName: str
    lastName: str
    cellNumber:  str | None
    homeNumber:  str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class Href(BaseModel):
    href: str

    model_config = ConfigDict(strict=True, extra='forbid')


class Self(BaseModel):
    href: Href

    model_config = ConfigDict(strict=True, extra='forbid')


class First(BaseModel):
    href: Href

    model_config = ConfigDict(strict=True, extra='forbid')


class Last(BaseModel):
    href: Href

    model_config = ConfigDict(strict=True, extra='forbid')


class Links(BaseModel):
    self: Self
    first: First
    last: Last

    model_config = ConfigDict(strict=True, extra='forbid')


class Meta(BaseModel):
    totalCount: int
    pageCount: int
    currentPage: int
    perPage: int

    model_config = ConfigDict(strict=True, extra='forbid')


class EnrollmentsResponseMain(BaseModel):
    items: list[Item]
    _links: Links
    _meta: Meta

    model_config = ConfigDict(strict=True, extra='ignore')


class EnrollmentResponsePinnedNote(BaseModel):
    id: int
    datetime: str
    text: str
    uuid: str

    model_config = ConfigDict(strict=True, extra='forbid')


class EnrollmentResponseOfferApproval(BaseModel):
    id: int

    model_config = ConfigDict(strict=True, extra='forbid')


class EnrollmentApprovals(BaseModel):
    id: int

    model_config = ConfigDict(strict=True, extra='forbid')


class PartnerCommission(BaseModel):
    enrollmentUuid: str
    commissionStatus: str
    commissionDate: str | None
    debtChange: int

    model_config = ConfigDict(strict=True, extra='forbid')


class EnrollmentResponsePartnerCommission(RootModel):
    root: list[PartnerCommission]


class EnrollmentResponsePayoffQuotes(BaseModel):
    payoffQuoteValue: float | int
    quoteGoodUntilDraftCreditorPayment: str| None
    haveAllDebtsBeenNegotiated: bool
    balanceDueOnDebtSettledScheduled: float | None
    feeAmountDueOnDebtSettledScheduled: int | float
    lastRamMonthlyFee: float | None
    totalRamGcsCheckFeesDue: float | None
    ramGcsWireFee: int | None
    balanceDueAmericorRecoup: int | float
    balanceDueAttorneyFees: int | float
    currentRamBalance: float | None

    model_config = ConfigDict(strict=True, extra='forbid')


class EnrollmentResponseAch(BaseModel):
    nameOnAccount: str | None
    routingNumber: str | None
    bankAccountNumber: str | None
    accountType: str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class UnderwritingStatus(BaseModel):
    id: int
    title: str


class Underwriter(BaseModel):
    id: int
    name: str
    email: str


class LocProcessor(BaseModel):
    id: int
    name: str
    email: str


class LoanParams(BaseModel):
    loanAmount: float
    loanAmountWithPoints: float
    prePaidFinanceCharge: float
    apr: float
    interestRate: float
    paymentInterval: int
    paymentAmount: float
    term: int
    totalInterest: float
    totalAmountPaid: float


class EnrollmentResponseUnderwriting(BaseModel):
    underwritingStatus:  None | UnderwritingStatus
    underwriter: None | Underwriter
    loanParams: LoanParams
    locProcessor: None | LocProcessor

    model_config = ConfigDict(strict=True, extra='forbid')


class DealCreditors(BaseModel):
    id: int
    customerCreditorId: int
    originalCreditor: str
    originalBalance: int
    originalCreditorGroupId: int | None
    originalCreditorGroupName: str | None
    currentCreditor: str | None
    currentBalance: float
    currentCreditorGroupId: int | None
    currentCreditorGroupName: str | None
    offerDate: str | None
    offerAmount: float | None
    offerPercent: float | None
    offerPercentCurrent: float | None
    offerStatus: int
    customerCreditorSavings: float | None
    offerAccepted: bool
    customerCreditorStatus: str
    offerUpdatedDate: str | None
    offerNumberOfTerms: int
    offerFirstPaymentDate: str
    customerCreditorLast4DigitsOfAccountNumber: str
    clientApproval: int
    offerExpirationDate: str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class EnrollmentResponseSettlements(RootModel):
    root: list[DealCreditors]


class EnrollmentFind(BaseModel):
    id:  int
    status: int
    statusDate: str
    name: str
    type: str
    firstName: str
    lastName: str
    email: str
    phoneMobile: str
    phoneHome: str | None
    ssnLast4: str
    dateOfBirth: str
    city: str
    state: str
    street: str
    zipcode: str
    creditReportId: int | None
    salesId: int | None
    salesIp: str | None
    salesName: str | None
    lang: str
    fileStatus: int
    isRegistered: bool | None
    paperStatementsEnabled: int | None
    negotiatorId: int | None
    negotiatorName: str | None
    processingPaymentsService: str | None
    processingPaymentsServiceAccountNumber: int | None

    model_config = ConfigDict(strict=True, extra='forbid')
