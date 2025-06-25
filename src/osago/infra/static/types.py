import enum


class OwnerType(enum.Enum):
    legal = 1
    individual = 2


class OSAGOType(enum.Enum):
    base = 1
    to_registration = 2
    short = 3


class CarType(enum.Enum):
    passenger = 1
    freight = 2
    moto = 3
