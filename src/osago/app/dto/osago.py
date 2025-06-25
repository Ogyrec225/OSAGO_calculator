from decimal import Decimal

from pydantic import Field

from osago.infra.static.types import CarType, OSAGOType, OwnerType

from .base import DTO


class DataForOsagoV1DTO(DTO):
    car_type: CarType
    osago_type: OSAGOType

    kbm_class: int = Field(ge=1)
    max_horsepower: int = Field(ge=1)
    group_id: int = Field(ge=1)
    max_month_use: int = Field(ge=0)
    max_month_insurance: int = Field(ge=0)
    owner_type: OwnerType
    limitation_flag: bool
    region: int = Field(ge=0)
    city_name: str
    max_years: int = Field(ge=16)
    max_practice: int = Field(ge=0)


class OsagoDTO(DTO):
    max_price: float
    min_price: float


class OsagoWithCoefDTO(DTO):
    max_price: float
    min_price: float

    bonus_malus_coefficient: Decimal
    years_practice_coefficient: Decimal
    restriction_coefficient: Decimal
    horsepower_coefficient: Decimal
    territorial_coefficient: Decimal
    period_use_coefficient: Decimal
    insurance_period_coefficient: Decimal
