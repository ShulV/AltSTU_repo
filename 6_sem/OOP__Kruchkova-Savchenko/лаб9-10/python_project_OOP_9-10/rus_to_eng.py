from english_game_state import EnglishGameState
import csv


class RusToEng(EnglishGameState):
    """состояние игры EnglishGame (с русского на английский)"""

    def __str__(self):
        """преобразование в строку"""
        return "<<перевод с русского на английский>>"

    def get_word_and_translation(self, filename, index):
        """получение слова и его перевода по индексу (номеру упражнения)"""

        with open(filename, 'r', newline='') as File:
            reader = csv.reader(File, delimiter=';')
            counter = 0
            for row_i, row in enumerate(reader):
                word_translation = row[0]  # слово для перевода (русское)
                word_to_translate = row[1]  # сам перевод слова (английское)

                counter += 1
                if row_i == index:
                    return [word_to_translate, word_translation]
        return None