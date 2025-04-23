from pydantic import BaseModel, field_validator, ConfigDict


class AuthenticationResponse(BaseModel):
    token: str
    lifetime: int

    model_config = ConfigDict(strict=True, extra='forbid')

    @field_validator('lifetime')
    def lifetime_value_checking(cls, v):
        assert v == 604800, {'as_is': v, 'to_be': 604800}
