from dependency_injector import containers, providers

from osago.app.uow import UoWImpl
from osago.di.repositories import (
    BonusMalusRepositoryContainer,
    HorsepowerRepositoryContainer,
    InsuranceRateRepositoryContainer,
    PeriodInsuranceRepositoryContainer,
    RestrictionCoefficientRepositoryContainer,
    TerritorialCoefficientRepositoryContainer,
    UsePeriodRepositoryContainer,
    YearsPracticeRepositoryContainer,
)


class UoWContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()

    bonus_malus_container = providers.Container(BonusMalusRepositoryContainer)
    horsepower_container = providers.Container(HorsepowerRepositoryContainer)
    insurance_rate_container = providers.Container(InsuranceRateRepositoryContainer)
    period_insurance_container = providers.Container(PeriodInsuranceRepositoryContainer)
    years_practice_container = providers.Container(YearsPracticeRepositoryContainer)
    restriction_coefficient_container = providers.Container(
        RestrictionCoefficientRepositoryContainer
    )
    territorial_coefficient_container = providers.Container(
        TerritorialCoefficientRepositoryContainer
    )
    period_use_container = providers.Container(UsePeriodRepositoryContainer)

    uow = providers.Factory(
        UoWImpl,
        db_session=db_session,
        bonus_malus_repo=bonus_malus_container.provided.bonus_malus_repo,
        horsepower_repo=horsepower_container.provided.horsepower_repo,
        insurance_rate_repo=insurance_rate_container.provided.insurance_rate_repo,
        period_insurance_repo=period_insurance_container.provided.period_insurance_repo,
        years_practice_repo=years_practice_container.provided.years_practice_repo,
        restriction_coefficient_repo=restriction_coefficient_container.provided.restriction_coefficient_repo,
        territorial_coefficient_repo=territorial_coefficient_container.provided.territorial_coefficient_repo,
        period_use_repo=period_use_container.provided.period_use_repo,
    )
