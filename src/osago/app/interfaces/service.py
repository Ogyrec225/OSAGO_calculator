from abc import ABC, abstractmethod

from osago.app.abc.uow import BaseUoW


class OsagoCalculator(ABC):
    @staticmethod
    @abstractmethod
    def calculate_osago():
        raise NotImplementedError
