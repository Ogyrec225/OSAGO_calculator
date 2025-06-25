from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from osago.app.bonus_malus import GetSuitableBonusMalusQuery
from osago.app.dto import (
    BonusMalusDTO,
    HorsepowerDTO,
    InsuranceRateDTO,
    PeriodInsuranceDTO,
    PeriodUseDTO,
    RestrictionCoefficientDTO,
    TerritorialCoefficientDTO,
    YearsPracticeDTO,
)
from osago.app.horsepower import GetSuitableHorsepowerQuery
from osago.app.insurance_period import GetSuitablePeriodInsuranceQuery
from osago.app.insurance_rate import GetSuitableInsuranceRatesQuery
from osago.app.mediator_aggregator import MediatorAggregator
from osago.app.periods_use import GetSuitablePeriodsUseQuery
from osago.app.restrictions import GetSuitableRestrictionsQuery
from osago.app.territorial_coefficient import GetSuitableTerritorialCoefficientQuery
from osago.app.years_practices import GetSuitableYearsPracticesQuery
from osago.di import ApplicationContainer
from osago.infra.static.types import OwnerType
from osago.presentation.api.responses import OkResponse

coefficients_router = APIRouter(prefix="/coefficients", tags=["v1"])


@coefficients_router.get(
    "/bonus_malus/{kbm_class}", response_model=OkResponse[BonusMalusDTO]
)
@inject
async def get_suitable_bonus_malus(
    kbm_class: int,
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    bonus_malus = await mediator.send(
        GetSuitableBonusMalusQuery(kbm_class=kbm_class), context="bonus_malus"
    )
    return OkResponse[BonusMalusDTO](result=bonus_malus)


@coefficients_router.get(
    "/horsepower/{max_horsepower}", response_model=OkResponse[HorsepowerDTO]
)
@inject
async def get_suitable_horsepower(
    max_horsepower: int,
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    horsepower_dto = await mediator.send(
        GetSuitableHorsepowerQuery(max_horsepower=max_horsepower), context="horsepower"
    )
    return OkResponse[HorsepowerDTO](result=horsepower_dto)


@coefficients_router.get(
    "/insurance_rate/{group_id}", response_model=OkResponse[InsuranceRateDTO]
)
@inject
async def get_suitable_insurance_rate(
    group_id: int,
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    insurance_rate = await mediator.send(
        GetSuitableInsuranceRatesQuery(group_id=group_id),
        context="insurance_rate",
    )
    return OkResponse[InsuranceRateDTO](result=insurance_rate)


@coefficients_router.get(
    "/insurance_period/{max_month}", response_model=OkResponse[PeriodInsuranceDTO]
)
@inject
async def get_suitable_insurance_period(
    max_month: int,
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    insurance_period_dto = await mediator.send(
        GetSuitablePeriodInsuranceQuery(max_month=max_month), context="insurance_period"
    )
    return OkResponse[PeriodInsuranceDTO](result=insurance_period_dto)


@coefficients_router.get(
    "/period_use/{max_month}", response_model=OkResponse[PeriodUseDTO]
)
@inject
async def get_suitable_period_use(
    max_month: int,
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    period_use_dto = await mediator.send(
        GetSuitablePeriodsUseQuery(max_month=max_month), context="period_use"
    )
    return OkResponse[PeriodUseDTO](result=period_use_dto)


@coefficients_router.get(
    "/restrictions/{owner_type}/{limitation_flag}",
    response_model=OkResponse[RestrictionCoefficientDTO],
)
@inject
async def get_suitable_restriction(
    owner_type: OwnerType = OwnerType.individual,
    limitation_flag: bool = False,
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    restriction = await mediator.send(
        GetSuitableRestrictionsQuery(
            owner_type=owner_type, limitation_flag=limitation_flag
        ),
        context="restriction_coefficient",
    )
    return OkResponse[RestrictionCoefficientDTO](result=restriction)


@coefficients_router.get(
    "/territorial_coefficient/{region}/{city_name}",
    response_model=OkResponse[TerritorialCoefficientDTO],
)
@inject
async def get_suitable_territorial_coefficient(
    region: int,
    city_name: str,
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    territorial_coefficient_dto = await mediator.send(
        GetSuitableTerritorialCoefficientQuery(region=region, city_name=city_name),
        context="territorial_coefficient",
    )
    return OkResponse[TerritorialCoefficientDTO](result=territorial_coefficient_dto)


@coefficients_router.get(
    "/years_practice/{max_years}/{max_practice}",
    response_model=OkResponse[YearsPracticeDTO],
)
@inject
async def get_suitable_years_practice(
    max_years: int,
    max_practice: int,
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    years_practice = await mediator.send(
        GetSuitableYearsPracticesQuery(max_practice=max_practice, max_years=max_years),
        context="years_practice",
    )
    return OkResponse[YearsPracticeDTO](result=years_practice)
