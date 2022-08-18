from abc import ABC, abstractmethod


class EnglishGameState(ABC):
    """интерфейс состояния игры EnglishGame"""

    @abstractmethod
    def __str__(self):
        """преобразование в строку"""
        pass
    @abstractmethod
    def get_word_and_translation(self, filename, index):
        """получение слова и его перевода по индексу (номеру упражнения)"""
        pass