from typing import Annotated, Any

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

intpk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):
    __abstract__ = True
    id: Any


class BaseInt(Base):
    __abstract__ = True

    id: Mapped[intpk]
