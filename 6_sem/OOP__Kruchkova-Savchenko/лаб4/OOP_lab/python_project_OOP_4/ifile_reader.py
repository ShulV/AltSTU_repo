from abc import ABC, abstractmethod


class IFileReader(ABC):
    """читатель файла"""
    @abstractmethod
    def get_concrete_data(self, index):
        """получение данных для уровня"""
        pass
