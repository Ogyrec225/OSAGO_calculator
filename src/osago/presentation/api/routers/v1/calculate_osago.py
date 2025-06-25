from app.calculate_osago import OsagoCalculatorImplV1
from app.dto import DataForOsagoV1DTO, OsagoWithCoefDTO
from app.mediator_aggregator import MediatorAggregator
from dependency_injector.wiring import Provide, inject
from di import ApplicationContainer
from fastapi import APIRouter, Depends
from presentation.api.responses import OkResponse
from presentation.api.routers.v1.serialization import OsagoInAPISchema

router = APIRouter(prefix="/osago", tags=["v1"])


@router.post(
    "/",
    response_model=OkResponse[OsagoWithCoefDTO],
    description="""
\nosago_type (1-Обычное, 2 - До места регистрации, 3 - Короткое)
\ncar_type (1-B/BE), (2-другие), (3-M)
\nkbm_class - Класс КБМ, где M = 0 (всё смещенно на +1)
\nmax_horsepower - Лошадинные силы
\ngroup_id - Id ставки (insurance_rate)
\nmax_month_use - Времяни в пользование
\nmax_month_insurance - Времяни застраховано
\nowner_type - (1- Юр лицо, 2 - Физ. лицо)
\nlimitation_flag - Есть ли ограничения на управление
\nregion - Номер региона
\ncity_name - Город
\nmax_years - Возраст водителя
\nmax_practice - Стаж
""",
)
@inject
async def calculate_osago(
    data: OsagoInAPISchema,
    mediator: MediatorAggregator = Depends(Provide[ApplicationContainer.mediator]),
):
    osago = await OsagoCalculatorImplV1.calculate_osago(
        mediator=mediator,
        data=DataForOsagoV1DTO(
            car_type=data.car_type,
            osago_type=data.osago_type,
            kbm_class=data.kbm_class,
            max_horsepower=data.max_horsepower,
            group_id=data.group_id,
            max_month_use=data.max_month_use,
            max_month_insurance=data.max_month_insurance,
            owner_type=data.owner_type,
            limitation_flag=data.limitation_flag,
            region=data.region,
            city_name=data.city_name,
            max_years=data.max_years,
            max_practice=data.max_practice,
        ),
    )
    return OkResponse[OsagoWithCoefDTO](result=osago)
