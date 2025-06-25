from .bonus_malus import BonusMalusRepository
from .horsepower import HorsepowerRepository
from .insurance_period import PeriodInsuranceRepository
from .insurance_rate import InsuranceRateRepository
from .practice import YearsPracticeRepository
from .restriction import RestrictionCoefficientRepository
from .territorial import TerritorialCoefficientRepository
from .use_period import UsePeriodRepository

__all__ = [
    "BonusMalusRepository",
    "HorsepowerRepository",
    "InsuranceRateRepository",
    "PeriodInsuranceRepository",
    "YearsPracticeRepository",
    "RestrictionCoefficientRepository",
    "TerritorialCoefficientRepository",
    "UsePeriodRepository",
]
