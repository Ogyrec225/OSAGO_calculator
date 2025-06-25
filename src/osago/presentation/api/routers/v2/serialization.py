from pydantic import BaseModel, Field

from osago.infra.static.types import CarType, OSAGOType, OwnerType


class OsagoInAPISchema(BaseModel):
    car_type: CarType
    osago_type: OSAGOType
    group_id: int = Field(ge=1)
    owner_type: OwnerType

    transport_coefficient: float = Field(ge=0)
    bonus_malus_coefficient: float = Field(ge=0)
    horsepower_coefficient: float = Field(ge=0)
    restriction_coefficient: float = Field(ge=0)
    practice_coefficient: float = Field(ge=0)
    use_coefficient: float = Field(ge=0)
    insurance_coefficient: float = Field(ge=0)
    territorial_coefficient: float = Field(ge=0)
