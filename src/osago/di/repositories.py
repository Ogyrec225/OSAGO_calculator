from dependency_injector import containers, providers

from osago.infra.database.repositories import (
    BonusMalusRepository,
    HorsepowerRepository,
    InsuranceRateRepository,
    PeriodInsuranceRepository,
    RestrictionCoefficientRepository,
    TerritorialCoefficientRepository,
    UsePeriodRepository,
    YearsPracticeRepository,
)


class BonusMalusRepositoryContainer(containers.DeclarativeContainer):
    bonus_malus_repo = providers.Factory(BonusMalusRepository)


class HorsepowerRepositoryContainer(containers.DeclarativeContainer):
    horsepower_repo = providers.Factory(HorsepowerRepository)


class InsuranceRateRepositoryContainer(containers.DeclarativeContainer):
    insurance_rate_repo = providers.Factory(InsuranceRateRepository)


class PeriodInsuranceRepositoryContainer(containers.DeclarativeContainer):
    period_insurance_repo = providers.Factory(PeriodInsuranceRepository)


class YearsPracticeRepositoryContainer(containers.DeclarativeContainer):
    years_practice_repo = providers.Factory(YearsPracticeRepository)


class RestrictionCoefficientRepositoryContainer(containers.DeclarativeContainer):
    restriction_coefficient_repo = providers.Factory(RestrictionCoefficientRepository)


class TerritorialCoefficientRepositoryContainer(containers.DeclarativeContainer):
    territorial_coefficient_repo = providers.Factory(TerritorialCoefficientRepository)


class UsePeriodRepositoryContainer(containers.DeclarativeContainer):
    period_use_repo = providers.Factory(UsePeriodRepository)
