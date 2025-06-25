from abc import ABC, abstractmethod


class OsagoCalculator(ABC):
    @staticmethod
    @abstractmethod
    def calculate_osago():
        raise NotImplementedError
