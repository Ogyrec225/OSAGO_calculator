from unittest.mock import AsyncMock

import pytest
from app.calculate_osago import (
    OsagoCalculatorImplV1,
)
from app.dto import (
    BonusMalusDTO,
    DataForOsagoV1DTO,
    HorsepowerDTO,
    InsuranceRateDTO,
    PeriodUseDTO,
    RestrictionCoefficientDTO,
    TerritorialCoefficientDTO,
    YearsPracticeDTO,
)
from app.mediator_aggregator import MediatorAggregator
from fastapi import status
from httpx import AsyncClient
from infra.static.types import CarType, OSAGOType, OwnerType


@pytest.mark.asyncio
class TestCalculateOsago:
    """Тесты для API v1/osago/."""

    @pytest.mark.parametrize(
        "test_data, test_answer, valid_answer_result, response_status",
        [
            (
                {
                    "osago_type": 1,
                    "car_type": 1,
                    "kbm_class": 5,
                    "max_horsepower": 100,
                    "group_id": 3,
                    "max_month_use": 3,
                    "max_month_insurance": 0,
                    "owner_type": 2,
                    "limitation_flag": True,
                    "region": 63,
                    "city_name": "",
                    "max_years": 40,
                    "max_practice": 20,
                },
                {
                    "status": 200,
                    "result": {
                        "max_price": 3469.5661,
                        "min_price": 757.91716,
                        "bonus_malus_coefficient": 1.0,
                        "years_practice_coefficient": 0.91,
                        "restriction_coefficient": 1.0,
                        "horsepower_coefficient": 1.1,
                        "territorial_coefficient": 0.92,
                        "period_use_coefficient": 0.5,
                        "insurance_period_coefficient": 1,
                    },
                },
                {
                    "max_price": 3469.5661,
                    "min_price": 757.91716,
                    "bonus_malus_coefficient": 1.0,
                    "years_practice_coefficient": 0.91,
                    "restriction_coefficient": 1.0,
                    "horsepower_coefficient": 1.1,
                    "territorial_coefficient": 0.92,
                    "period_use_coefficient": 0.5,
                    "insurance_period_coefficient": 1,
                },
                status.HTTP_200_OK,
            ),
            (
                {
                    "status": 200,
                    "result": {
                        "max_price": 3469.5661,
                        "min_price": 757.91716,
                        "bonus_malus_coefficient": 1.0,
                        "years_practice_coefficient": 0.91,
                        "restriction_coefficient": 1.0,
                        "horsepower_coefficient": 1.1,
                        "territorial_coefficient": 0.92,
                        "period_use_coefficient": 0.5,
                        "insurance_period_coefficient": 1,
                    },
                },
                {
                    "max_price": 3469.5661,
                    "min_price": 757.91716,
                    "bonus_malus_coefficient": 1.0,
                    "years_practice_coefficient": 0.91,
                    "restriction_coefficient": 1.0,
                    "horsepower_coefficient": 1.1,
                    "territorial_coefficient": 0.92,
                    "period_use_coefficient": 0.5,
                    "insurance_period_coefficient": 1,
                },
                {
                    "max_price": 3469.5661,
                    "min_price": 757.91716,
                    "bonus_malus_coefficient": 1.0,
                    "years_practice_coefficient": 0.91,
                    "restriction_coefficient": 1.0,
                    "horsepower_coefficient": 1.1,
                    "territorial_coefficient": 0.92,
                    "period_use_coefficient": 0.5,
                    "insurance_period_coefficient": 1,
                },
                status.HTTP_422_UNPROCESSABLE_ENTITY,
            ),
        ],
    )
    async def test_calculate_osago_api(
        self,
        test_data,
        test_answer,
        valid_answer_result,
        response_status,
        async_client: AsyncClient,
    ):
        """Интеграционный тест ОСАГО."""
        OsagoCalculatorImplV1.calculate_osago = AsyncMock(return_value=test_answer)

        response = await async_client.post("/v1/osago/", json=test_data)
        assert response.status_code == response_status
        if response_status == status.HTTP_200_OK:
            json_response = response.json()
            assert "result" in json_response
            assert isinstance(json_response["result"], dict)
            result = json_response["result"]["result"]
            assert "max_price" in result
            assert isinstance(result["max_price"], float)
            assert (
                result["bonus_malus_coefficient"]
                == valid_answer_result["bonus_malus_coefficient"]
            )
            assert (
                result["years_practice_coefficient"]
                == valid_answer_result["years_practice_coefficient"]
            )
            assert (
                result["restriction_coefficient"]
                == valid_answer_result["restriction_coefficient"]
            )
            assert (
                result["horsepower_coefficient"]
                == valid_answer_result["horsepower_coefficient"]
            )
            assert (
                result["territorial_coefficient"]
                == valid_answer_result["territorial_coefficient"]
            )
            assert (
                result["period_use_coefficient"]
                == valid_answer_result["period_use_coefficient"]
            )
            assert (
                result["insurance_period_coefficient"]
                == valid_answer_result["insurance_period_coefficient"]
            )

    @pytest.mark.parametrize(
        "data, bonus_malus, horsepower, insurance_rate, insurance_period, years_practice, restriction_coefficient, territorial_coefficient, period_use, max_price, min_price",
        [
            (
                DataForOsagoV1DTO(
                    car_type=CarType.passenger,
                    osago_type=OSAGOType.base,
                    kbm_class=5,
                    max_horsepower=100,
                    group_id=3,
                    max_month_use=3,
                    max_month_insurance=0,
                    owner_type=OwnerType.individual,
                    limitation_flag=True,
                    region=63,
                    city_name="",
                    max_years=40,
                    max_practice=20,
                ),
                BonusMalusDTO(kbm_class=5, coefficient=1.0),
                HorsepowerDTO(max_horsepower=100, coefficient=1.1),
                InsuranceRateDTO(
                    id=3,
                    group='Транспортные средства категорий "B", "BE" физических лиц (в том числе транспортные средства, используемые для бытовых и семейных нужд), индивидуальных предпринимателей',
                    max_price=7535,
                    min_price=1646,
                    state=False,
                ),
                None,
                YearsPracticeDTO(max_years=49, max_practice=9999, coefficient=0.91),
                RestrictionCoefficientDTO(
                    limitation_flag=True,
                    owner_type=OwnerType.individual,
                    coefficient=1.0,
                ),
                TerritorialCoefficientDTO(
                    region=63,
                    city_name="Прочие города и населенные пункты",
                    state_transport_coefficient=0.92,
                    transport_coefficient=0.6,
                ),
                PeriodUseDTO(max_month=3, coefficient=0.5),
                3469.5661,
                757.91716,
            ),
            (
                DataForOsagoV1DTO(
                    car_type=CarType.passenger,
                    osago_type=OSAGOType.base,
                    kbm_class=5,
                    max_horsepower=100,
                    group_id=3,
                    max_month_use=3,
                    max_month_insurance=0,
                    owner_type=OwnerType.individual,
                    limitation_flag=True,
                    region=63,
                    city_name="",
                    max_years=40,
                    max_practice=20,
                ),
                BonusMalusDTO(kbm_class=5, coefficient=1.0),
                HorsepowerDTO(max_horsepower=100, coefficient=1.1),
                InsuranceRateDTO(
                    id=3,
                    group='Транспортные средства категорий "B", "BE" физических лиц (в том числе транспортные средства, используемые для бытовых и семейных нужд), индивидуальных предпринимателей',
                    max_price=7535,
                    min_price=1646,
                    state=False,
                ),
                None,
                YearsPracticeDTO(max_years=49, max_practice=9999, coefficient=0.91),
                RestrictionCoefficientDTO(
                    limitation_flag=True,
                    owner_type=OwnerType.individual,
                    coefficient=1.0,
                ),
                TerritorialCoefficientDTO(
                    region=63,
                    city_name="Прочие города и населенные пункты",
                    state_transport_coefficient=0.92,
                    transport_coefficient=0.6,
                ),
                PeriodUseDTO(max_month=3, coefficient=0.5),
                3469.5661,
                757.91716,
            ),
        ],
    )
    async def test_calculate_osago_no_insurance_rate(
        self,
        data,
        bonus_malus,
        horsepower,
        insurance_rate,
        insurance_period,
        years_practice,
        restriction_coefficient,
        territorial_coefficient,
        period_use,
        max_price,
        min_price,
    ):
        """Unit тест ОСАГО."""
        mock_mediator = AsyncMock(spec=MediatorAggregator)

        async def get_coefficient(query, context):
            match context:
                case "bonus_malus":
                    return bonus_malus
                case "horsepower":
                    return horsepower
                case "insurance_rate":
                    return insurance_rate
                case "insurance_period":
                    return insurance_period
                case "years_practice":
                    return years_practice
                case "restriction_coefficient":
                    return restriction_coefficient
                case "territorial_coefficient":
                    return territorial_coefficient
                case "period_use":
                    return period_use

        mock_mediator.send.side_effect = get_coefficient

        out_data = await OsagoCalculatorImplV1.calculate_osago(
            mediator=mock_mediator, data=data
        )
        assert max_price == out_data.max_price
        assert min_price == out_data.min_price
