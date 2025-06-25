from infra.static.types import CarType, OSAGOType, OwnerType
from pydantic import BaseModel, Field


class OsagoInAPISchema(BaseModel):
    osago_type: OSAGOType
    car_type: CarType

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
