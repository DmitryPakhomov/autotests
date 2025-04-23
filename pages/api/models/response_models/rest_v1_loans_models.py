from pydantic import BaseModel, ConfigDict, RootModel


class BestTimeToCall(RootModel):
    root: dict[str, str]


class TypeOfAuth(RootModel):
    root: dict[str, str]


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


class LoansResponseMain(BaseModel):
    items: list[Item]
    _links: Links
    _meta: Meta

    model_config = ConfigDict(strict=True, extra='ignore')


class LoanResponseAch(BaseModel):
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


class LoanResponseUnderwriting(BaseModel):
    UnderwritingStatus:  None | UnderwritingStatus
    Underwriter: None | Underwriter
    LoanParams: LoanParams
    LocProcessor: None | LocProcessor

    model_config = ConfigDict(strict=True, extra='forbid')


class LoanDuplicatesList(BaseModel):
    id:  int
    firstName: str
    lastName: str
    personalId: str
    duplicatedApplicantType: str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class LoanDuplicates(RootModel):
    root: list[LoanDuplicatesList]


class DncMain(BaseModel):
    id: int
    phone: str
    firstName: str | None
    lastName: str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class DncEmail(BaseModel):
    id: int
    email: str
    firstName: str | None
    lastName: str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class DncAddresses(BaseModel):
    id: int
    address: str
    city: str
    state: str
    zip: str
    firstName: str | None
    lastName: str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class PartnerUpdate(BaseModel):
    uuid: str
    title: str
    contactEmail: str
    isTest: int
