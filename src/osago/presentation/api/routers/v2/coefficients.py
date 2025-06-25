from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from osago.app.bonus_malus import GetAllBonusMalusQuery
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
from osago.app.horsepower import GetAllHorsepowerQuery
from osago.app.insurance_period import GetAllPeriodInsurancesQuery
from osago.app.insurance_rate import GetAllInsuranceRatesQuery
from osago.app.mediator_aggregator import MediatorAggregator
from osago.app.periods_use import GetAllPeriodsUseQuery
from osago.app.restrictions import GetAllRestrictionsQuery
from osago.app.territorial_coefficient import GetAllTerritorialCoefficientQuery
from osago.app.years_practices import GetAllYearsPracticesQuery
from osago.di import ApplicationContainer
from osago.presentation.api.responses import OkResponse

coefficients_router = APIRouter(prefix="/coeficients", tags=["v2"])


@coefficients_router.get("/bonus_malus", response_model=OkResponse[list[BonusMalusDTO]])
@inject
async def get_bonus_malus(
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    return OkResponse[list[BonusMalusDTO]](
        result=(
            await mediator.send(query=GetAllBonusMalusQuery(), context="bonus_malus")
        )
    )


@coefficients_router.get("/horsepowers", response_model=OkResponse[list[HorsepowerDTO]])
@inject
async def get_horsepowers(
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    return OkResponse[list[HorsepowerDTO]](
        result=(
            await mediator.send(query=GetAllHorsepowerQuery(), context="horsepower")
        )
    )


@coefficients_router.get(
    "/insurance_rates", response_model=OkResponse[list[InsuranceRateDTO]]
)
@inject
async def get_insurance_rates(
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    return OkResponse[list[InsuranceRateDTO]](
        result=(
            await mediator.send(
                query=GetAllInsuranceRatesQuery(), context="insurance_rate"
            )
        )
    )


@coefficients_router.get(
    "/period_insurances", response_model=OkResponse[list[PeriodInsuranceDTO]]
)
@inject
async def get_period_insurances(
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    return OkResponse[list[PeriodInsuranceDTO]](
        result=(
            await mediator.send(
                query=GetAllPeriodInsurancesQuery(), context="insurance_period"
            )
        )
    )


@coefficients_router.get("/periods_uses", response_model=OkResponse[list[PeriodUseDTO]])
@inject
async def get_periods_uses(
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    return OkResponse[list[PeriodUseDTO]](
        result=(
            await mediator.send(query=GetAllPeriodsUseQuery(), context="period_use")
        )
    )


@coefficients_router.get(
    "/restrictions", response_model=OkResponse[list[RestrictionCoefficientDTO]]
)
@inject
async def get_restrictions(
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    return OkResponse[list[RestrictionCoefficientDTO]](
        result=(
            await mediator.send(
                query=GetAllRestrictionsQuery(), context="restriction_coefficient"
            )
        )
    )


@coefficients_router.get(
    "/territorial_coefficients",
    response_model=OkResponse[list[TerritorialCoefficientDTO]],
)
@inject
async def get_territorial_coefficients(
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    return OkResponse[list[TerritorialCoefficientDTO]](
        result=(
            await mediator.send(
                query=GetAllTerritorialCoefficientQuery(),
                context="territorial_coefficient",
            )
        )
    )


@coefficients_router.get(
    "/years_practices", response_model=OkResponse[list[YearsPracticeDTO]]
)
@inject
async def get_years_practices(
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    return OkResponse[list[YearsPracticeDTO]](
        result=(
            await mediator.send(
                query=GetAllYearsPracticesQuery(), context="years_practice"
            )
        )
    )
