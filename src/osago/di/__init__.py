from app.mediator_aggregator import MediatorAggregator
from dependency_injector import containers, providers
from di.bonus_malus import BonusMalusContainer
from di.horsepower import HorsepowerContainer
from di.insurance_period import PeriodInsuranceContainer
from di.insurance_rate import InsuranceContainer
from di.period_use import PeriodUseContainer
from di.restriction_coefficient import RestrictionCoefficientContainer
from di.territorial_coefficient import TerritorialCoefficientContainer
from di.uow import UoWContainer
from di.years_practice import YearsPracticeContainer
from infra.database.container import DataContainer


class ApplicationContainer(containers.DeclarativeContainer):
    data_container = providers.Container(DataContainer)
    db_session = data_container.db_session_factory

    uow_factory = providers.Container(UoWContainer, db_session=db_session)
    uow = uow_factory.uow

    bonus_malus_container = providers.Container(BonusMalusContainer, uow=uow)
    horsepower_container = providers.Container(HorsepowerContainer, uow=uow)
    insurance_rate_container = providers.Container(InsuranceContainer, uow=uow)
    period_insurance_container = providers.Container(PeriodInsuranceContainer, uow=uow)
    years_practice_container = providers.Container(YearsPracticeContainer, uow=uow)
    restriction_coefficient_container = providers.Container(
        RestrictionCoefficientContainer, uow=uow
    )
    territorial_coefficient_container = providers.Container(
        TerritorialCoefficientContainer, uow=uow
    )
    period_use_container = providers.Container(PeriodUseContainer, uow=uow)

    mediator = providers.Singleton(
        MediatorAggregator,
        context_mediators={
            "bonus_malus": bonus_malus_container.mediator,
            "horsepower": horsepower_container.mediator,
            "insurance_rate": insurance_rate_container.mediator,
            "insurance_period": period_insurance_container.mediator,
            "years_practice": years_practice_container.mediator,
            "restriction_coefficient": restriction_coefficient_container.mediator,
            "territorial_coefficient": territorial_coefficient_container.mediator,
            "period_use": period_use_container.mediator,
        },
    )
