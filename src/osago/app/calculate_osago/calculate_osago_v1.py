from decimal import Decimal

from app.bonus_malus import GetSuitableBonusMalusQuery
from app.dto import (
    DataForOsagoV1DTO,
    InsuranceRateDTO,
    OsagoWithCoefDTO,
    TerritorialCoefficientDTO,
)
from app.horsepower import GetSuitableHorsepowerQuery
from app.insurance_period import GetSuitablePeriodInsuranceQuery
from app.insurance_rate import GetSuitableInsuranceRatesQuery
from app.interfaces.service import OsagoCalculator
from app.mediator_aggregator import MediatorAggregator
from app.periods_use import GetSuitablePeriodsUseQuery
from app.restrictions import GetSuitableRestrictionsQuery
from app.territorial_coefficient import GetSuitableTerritorialCoefficientQuery
from app.years_practices import GetSuitableYearsPracticesQuery
from infra.static.types import CarType, OSAGOType, OwnerType


class OsagoCalculatorImplV1(OsagoCalculator):
    @staticmethod
    async def calculate_osago(mediator: MediatorAggregator, data: DataForOsagoV1DTO):
        insurance_rate: InsuranceRateDTO = await mediator.send(
            GetSuitableInsuranceRatesQuery(group_id=data.group_id),
            context="insurance_rate",
        )
        bonus_malus_coefficient = 1
        years_practice_coefficient = 1
        restriction_coefficient = 1
        horsepower_coefficient = 1
        territorial_coefficient = 1
        period_use_coefficient = 1
        insurance_period_coefficient = 1

        bonus_malus_coefficient = Decimal(
            str(
                (
                    await mediator.send(
                        GetSuitableBonusMalusQuery(kbm_class=data.kbm_class),
                        context="bonus_malus",
                    )
                ).coefficient
            )
        )
        years_practice_coefficient = Decimal(
            str(
                (
                    await mediator.send(
                        GetSuitableYearsPracticesQuery(
                            max_practice=data.max_practice, max_years=data.max_years
                        ),
                        context="years_practice",
                    )
                ).coefficient
            )
        )
        if data.owner_type is OwnerType.legal:
            years_practice_coefficient *= Decimal("1.8")

        restriction_coefficient = Decimal(
            str(
                (
                    await mediator.send(
                        GetSuitableRestrictionsQuery(
                            owner_type=data.owner_type,
                            limitation_flag=data.limitation_flag,
                        ),
                        context="restriction_coefficient",
                    )
                ).coefficient
            )
        )
        if data.car_type == CarType.passenger:
            horsepower_coefficient = Decimal(
                str(
                    (
                        await mediator.send(
                            GetSuitableHorsepowerQuery(
                                max_horsepower=data.max_horsepower
                            ),
                            context="horsepower",
                        )
                    ).coefficient
                )
            )
        match data.osago_type:
            case OSAGOType.base:
                territorial_coefficient_dto: TerritorialCoefficientDTO = (
                    await mediator.send(
                        GetSuitableTerritorialCoefficientQuery(
                            region=data.region, city_name=data.city_name
                        ),
                        context="territorial_coefficient",
                    )
                )
                if (
                    insurance_rate.group
                    == "Тракторы, самоходные дорожно-строительные и иные машины юридических и физических лиц"
                ):
                    territorial_coefficient = Decimal(
                        str(territorial_coefficient_dto.transport_coefficient)
                    )
                territorial_coefficient = Decimal(
                    str(territorial_coefficient_dto.state_transport_coefficient)
                )
                period_use_coefficient = Decimal(
                    str(
                        (
                            await mediator.send(
                                GetSuitablePeriodsUseQuery(
                                    max_month=data.max_month_use
                                ),
                                context="period_use",
                            )
                        ).coefficient
                    )
                )

            case OSAGOType.to_registration:
                insurance_period_coefficient = Decimal(
                    str(
                        (
                            await mediator.send(
                                GetSuitablePeriodInsuranceQuery(
                                    max_month=data.max_month_insurance
                                ),
                                context="insurance_period",
                            )
                        ).coefficient
                    )
                )

            case OSAGOType.short:
                territorial_coefficient = Decimal(
                    str(
                        (
                            await mediator.send(
                                GetSuitableTerritorialCoefficientQuery(
                                    region=data.region, city_name=data.city_name
                                ),
                                context="territorial_coefficient",
                            )
                        ).coefficient
                    )
                )
                insurance_period_coefficient = Decimal(
                    str(
                        (
                            await mediator.send(
                                GetSuitablePeriodInsuranceQuery(
                                    max_month=data.max_month_insurance
                                ),
                                context="insurance_period",
                            )
                        ).coefficient
                    )
                )

        return OsagoWithCoefDTO(
            max_price=insurance_rate.max_price
            * bonus_malus_coefficient
            * years_practice_coefficient
            * restriction_coefficient
            * horsepower_coefficient
            * territorial_coefficient
            * period_use_coefficient
            * insurance_period_coefficient,
            min_price=insurance_rate.min_price
            * bonus_malus_coefficient
            * years_practice_coefficient
            * restriction_coefficient
            * horsepower_coefficient
            * territorial_coefficient
            * period_use_coefficient
            * insurance_period_coefficient,
            bonus_malus_coefficient=bonus_malus_coefficient,
            years_practice_coefficient=years_practice_coefficient,
            restriction_coefficient=restriction_coefficient,
            horsepower_coefficient=horsepower_coefficient,
            territorial_coefficient=territorial_coefficient,
            period_use_coefficient=period_use_coefficient,
            insurance_period_coefficient=insurance_period_coefficient,
        )
