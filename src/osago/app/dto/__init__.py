from .base import DTO
from .coefficients import (
    BonusMalusDTO,
    HorsepowerDTO,
    InsuranceRateDTO,
    PeriodInsuranceDTO,
    PeriodUseDTO,
    RestrictionCoefficientDTO,
    TerritorialCoefficientDTO,
    YearsPracticeDTO,
)
from .osago import DataForOsagoV1DTO, OsagoDTO, OsagoWithCoefDTO

__all__ = [
    "DTO",
    "BonusMalusDTO",
    "HorsepowerDTO",
    "InsuranceRateDTO",
    "PeriodInsuranceDTO",
    "PeriodUseDTO",
    "RestrictionCoefficientDTO",
    "TerritorialCoefficientDTO",
    "YearsPracticeDTO",
    "DataForOsagoV1DTO",
    "DataForOSAGO",
    "OsagoDTO",
    "OsagoWithCoefDTO",
]
