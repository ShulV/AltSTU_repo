from abc import ABC, abstractmethod


class IMath(ABC):
    """интерфейс игры математика (сложение чисел)"""
    @abstractmethod
    def add(self):
        """суммирование 2 чисел"""
        pass
