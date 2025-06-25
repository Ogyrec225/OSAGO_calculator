from sqlalchemy.ext.asyncio import AsyncSession

from osago.app.abc.uow import BaseUoW
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
from osago.infra.database.uow import SQLAlchemyUoW


class UoWImpl(SQLAlchemyUoW, BaseUoW):
    def __init__(
        self,
        db_session: AsyncSession,
        bonus_malus_repo: BonusMalusRepository,
        horsepower_repo: HorsepowerRepository,
        insurance_rate_repo: InsuranceRateRepository,
        period_insurance_repo: PeriodInsuranceRepository,
        years_practice_repo: YearsPracticeRepository,
        restriction_coefficient_repo: RestrictionCoefficientRepository,
        territorial_coefficient_repo: TerritorialCoefficientRepository,
        period_use_repo: UsePeriodRepository,
    ):
        super().__init__(db_session)

        self._bonus_malus_repo = bonus_malus_repo
        self._horsepower_repo = horsepower_repo
        self._insurance_rate_repo = insurance_rate_repo
        self._period_insurance_repo = period_insurance_repo
        self._years_practice_repo = years_practice_repo
        self._restriction_coefficient_repo = restriction_coefficient_repo
        self._territorial_coefficient_repo = territorial_coefficient_repo
        self._period_use_repo = period_use_repo

    @property
    def bonus_malus_repo(self) -> BonusMalusRepository:
        return self._bonus_malus_repo(self.db_session)

    @property
    def horsepower_repo(self) -> HorsepowerRepository:
        return self._horsepower_repo(self.db_session)

    @property
    def insurance_rate_repo(self) -> InsuranceRateRepository:
        return self._insurance_rate_repo(self.db_session)

    @property
    def period_insurance_repo(self) -> PeriodInsuranceRepository:
        return self._period_insurance_repo(self.db_session)

    @property
    def years_practice_repo(self) -> YearsPracticeRepository:
        return self._years_practice_repo(self.db_session)

    @property
    def restriction_coefficient_repo(self) -> RestrictionCoefficientRepository:
        return self._restriction_coefficient_repo(self.db_session)

    @property
    def territorial_coefficient_repo(self) -> TerritorialCoefficientRepository:
        return self._territorial_coefficient_repo(self.db_session)

    @property
    def period_use_repo(self) -> UsePeriodRepository:
        return self._period_use_repo(self.db_session)
