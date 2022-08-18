from english_game_state import EnglishGameState
import csv


class EngToRus(EnglishGameState):
    """состояние игры EnglishGame (с английского на русский)"""
    def __str__(self):
        """преобразование в строку"""
        return "<<перевод с английского на русский>>"

    def get_word_and_translation(self, filename, index):
        """получение слова и его перевода по индексу (номеру упражнения)"""

        with open(filename, 'r', newline='') as File:
            reader = csv.reader(File, delimiter=';')
            counter = 0
            for row_i, row in enumerate(reader):
                word_to_translate = row[0]  # слово для перевода (английское)
                word_translation = row[1]   # сам перевод слова (русское)
                counter += 1
                if row_i == index:
                    return [word_to_translate, word_translation]
        return None
