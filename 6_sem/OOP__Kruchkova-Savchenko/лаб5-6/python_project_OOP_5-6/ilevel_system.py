from abc import ABC, abstractmethod

class ILevelSystem(ABC):
    """интерфейс уровневой системы"""

    @abstractmethod
    def get_level_by_counter(self, counter):
        """посчитать текущий уровень по количеству пройденных уровней"""
        pass