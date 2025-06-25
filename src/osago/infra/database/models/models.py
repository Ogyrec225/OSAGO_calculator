from sqlalchemy.orm import Mapped, mapped_column

from osago.infra.database.models.base import Base, BaseInt
from osago.infra.static.types import OwnerType


class InsuranceRate(BaseInt):
    """Страховые тарифы."""

    __tablename__ = "insurance_rates"

    group: Mapped[str] = mapped_column()
    max_price: Mapped[int] = mapped_column()
    min_price: Mapped[int] = mapped_column()

    state: Mapped[bool] = mapped_column()


class TerritorialCoefficient(BaseInt):
    """Территориальный коэффицент."""

    __tablename__ = "territorial_coefficients"

    region: Mapped[int] = mapped_column()
    city_name: Mapped[str] = mapped_column()
    state_transport_coefficient: Mapped[float] = mapped_column()
    transport_coefficient: Mapped[float] = mapped_column()


class BonusMalus(BaseInt):
    __tablename__ = "bonus_malus"

    kbm_class: Mapped[int] = mapped_column()
    coefficient: Mapped[float] = mapped_column()


class Horsepower(BaseInt):
    __tablename__ = "horsepowers"

    max_horsepower: Mapped[int] = mapped_column()
    coefficient: Mapped[float] = mapped_column()


class RestrictionCoefficient(BaseInt):
    __tablename__ = "restriction_coefficients"

    limitation_flag: Mapped[bool] = mapped_column()
    owner_type: Mapped[OwnerType] = mapped_column()
    coefficient: Mapped[float] = mapped_column()


class YearsPractice(BaseInt):
    __tablename__ = "years_practices"

    max_years: Mapped[int] = mapped_column()
    max_practice: Mapped[int] = mapped_column()
    coefficient: Mapped[float] = mapped_column()


class PeriodUse(BaseInt):
    __tablename__ = "use_coefficients"

    max_month: Mapped[int] = mapped_column()
    coefficient: Mapped[float] = mapped_column()


class PeriodInsurance(BaseInt):
    __tablename__ = "insurance_coefficients"

    max_month: Mapped[int] = mapped_column()
    coefficient: Mapped[float] = mapped_column()
