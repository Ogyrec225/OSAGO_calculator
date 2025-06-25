from osago.infra.static.types import OwnerType

from .base import DTO


class InsuranceRateDTO(DTO):
    id: int
    group: str
    max_price: int
    min_price: int

    state: bool


class TerritorialCoefficientDTO(DTO):
    region: int
    city_name: str
    state_transport_coefficient: float
    transport_coefficient: float


class BonusMalusDTO(DTO):
    kbm_class: int
    coefficient: float


class HorsepowerDTO(DTO):
    max_horsepower: int
    coefficient: float


class RestrictionCoefficientDTO(DTO):
    limitation_flag: bool
    owner_type: OwnerType
    coefficient: float


class YearsPracticeDTO(DTO):
    max_years: int
    max_practice: int
    coefficient: float


class PeriodUseDTO(DTO):
    max_month: int
    coefficient: float


class PeriodInsuranceDTO(DTO):
    max_month: int
    coefficient: float
