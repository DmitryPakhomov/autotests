from typing import Literal

from pydantic import BaseModel, field_validator, ConfigDict


class ClientsResponse(BaseModel):
    id: str
    brandId: str
    name: str
    status: str
    updatedAt: str
    createdAt: str

    model_config = ConfigDict(strict=True, extra='forbid')

    @field_validator('status')
    def reject_status_value_checking(cls, v):
        assert v == 'inactive', {'as_is': v, 'to_be': 'inactive'}
        return v


class ClientsAuthTokensResponse(BaseModel):
    id: str
    jwt: str

    model_config = ConfigDict(strict=True, extra='forbid')


class ItemsClients(BaseModel):
    id: str
    brandId: str
    name: str
    status: Literal['inactive', 'active']
    updatedAt: str
    createdAt: str

    model_config = ConfigDict(strict=True, extra='forbid')


class PaginationClients(BaseModel):
    total: int
    limit: int
    offset: int

    model_config = ConfigDict(strict=True, extra='forbid')


class GetClientsResponse(BaseModel):
    items: list[ItemsClients]
    pagination: PaginationClients

    model_config = ConfigDict(strict=True, extra='forbid')


class GetClientsByIdResponse(BaseModel):
    id: str
    brandId: str
    name: str
    status: str
    updatedAt: str
    createdAt: str

    model_config = ConfigDict(strict=True, extra='forbid')


class PutClientsStatusResponse(BaseModel):
    id: str
    brandId: str
    name: str
    status: str
    updatedAt: str
    createdAt: str

    model_config = ConfigDict(strict=True, extra='forbid')


class GetClientRoleResponse(BaseModel):
    items: list[str]

    model_config = ConfigDict(strict=True, extra='forbid')


class SmsAccountSettingsResponse(BaseModel):
    accountSid: str
    dispatchStatus: str | None
    status: str | None
    code: str | None
    accountToken: str | None
    deliveryStatus: str | None
    status: str | None
    code: str | None
    updatedAt: str | None
    createdAt: str | None


class PostSmsAccountResponse(BaseModel):
    id: str
    name: str
    status: str
    description: str
    brandId: str
    gatewayType: str
    settings: list[SmsAccountSettingsResponse]


class GetSmsAccountResponse(BaseModel):
    items: list[ItemsClients]
    pagination: PaginationClients
    settings: list[SmsAccountSettingsResponse]

    model_config = ConfigDict(strict=True, extra='forbid')


class GetClientAuthTokenId(BaseModel):
    id: str
    description: str
    isActive: str
    lastUsedAt: str
    updatedAt: str
    createdAt: str

    model_config = ConfigDict(strict=True, extra='forbid')


class GetClientAuthToken(BaseModel):
    items: list[GetClientAuthTokenId]
    pagination: PaginationClients

    model_config = ConfigDict(strict=True, extra='forbid')


class GetBrandId(BaseModel):
    id: str
    Name: str
    description: str
    updatedAt: str
    createdAt: str

    model_config = ConfigDict(strict=True, extra='forbid')


class GetClientNotificationUrls(BaseModel):
    id: str
    url: str
    type: str
    signatureKey: str
    updatedAt: str
    createdAt: str
    pagination: PaginationClients

    model_config = ConfigDict(strict=True, extra='forbid')


class GetClientNotificationUrlsId(BaseModel):
    items: list[GetClientNotificationUrls]

    model_config = ConfigDict(strict=True, extra='forbid')


class SettingsPostClientSmsChannel(BaseModel):
    phoneFrom: str | None
    externalPoolId: str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class PostClientSmsChannel(BaseModel):
    id: str
    accountId: str
    name: str
    description: str | None
    status: str
    strategy: str
    settings: list[SettingsPostClientSmsChannel]
    updatedAt: str
    createdAt: str
    pagination: PaginationClients

    model_config = ConfigDict(strict=True, extra='forbid')


class GetComplianceDncId(BaseModel):
    id: str
    phone: str
    createdAt: str
    creatorId: str
    description: str

    model_config = ConfigDict(strict=True, extra='forbid')


class GetSmsForbiddenwords(BaseModel):
    items: list[str]
    pagination: PaginationClients

    model_config = ConfigDict(strict=True, extra='forbid')


class GetSmsForbiddenwordsUsage(BaseModel):
    items: list[str]

    model_config = ConfigDict(strict=True, extra='forbid')


class PostSmsWithDummy(BaseModel):
    id: str
    smsChannelId: str
    phoneTo: str
    body: str
    timeZone: str
    status: str
    recipientCategory: str
    communicationCategory: str
    createdAt: str
    updatedAt: str
    smsAccountId: str | None
    externalPoolId: str | None
    errorCode: str | None
    errorDescription: str | None
    errorGroup: str | None
    phoneFrom: str | None
    deliveryStatus: str | None
    sentAt: str | None
    deliveredAt: str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class PutRecipientPhone(BaseModel):
    currentPhone: str
    previousPhone: str
    brandId: str
    clientId: str
    createdAt: str

    model_config = ConfigDict(strict=True, extra='forbid')


class GetMarketingDncPhone(BaseModel):
    id: str
    phone: str
    brandId: str
    creatorId: str
    createdAt: str
    description: str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class PostEmailsAccounts(BaseModel):
    id: str
    brandId: str
    clientId: str
    status: Literal['inactive', 'active', 'empty']
    createdAt: str
    updatedAt: str
    providerType: str | None
    addresses: str
    provider: str | None

    model_config = ConfigDict(strict=True, extra='forbid')


class GetEmailsAccounts(BaseModel):
    items: list[PostEmailsAccounts]
    pagination: PaginationClients

    model_config = ConfigDict(strict=True, extra='forbid')


class GetTcpaConsentPhoneNumber(BaseModel):
    id: str
    phone: str
    description: str
    confirmationUrl: str
    expiresAt: str
    createdAt: str
    updatedAt: str

    model_config = ConfigDict(strict=True, extra='forbid')


class GetTcpaConsentPhoneNumberHistory(BaseModel):
    id: str
    phone: str
    description: str
    confirmationUrl: str
    expiresAt: str
    createdAt: str
    updatedAt: str
    action: str
    clientId: str

    model_config = ConfigDict(strict=True, extra='forbid')