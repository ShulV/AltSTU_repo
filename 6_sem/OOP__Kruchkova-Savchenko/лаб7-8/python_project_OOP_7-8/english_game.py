from game import Game
import csv


ENGLISH_WORDS_FILE = 'english_words.csv'


class EnglishGame(Game):
    """игра - обучалка слов по английскому языку"""
    def __init__(self):
        super().__init__()
        self.filename = ENGLISH_WORDS_FILE

    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def get_word_and_translation(self, index):
        """получение слова и его перевода по индексу (номеру упражнения)"""
        with open(self.filename, 'r', newline='') as File:
            reader = csv.reader(File, delimiter=';')
            counter = 0
            for row_i, row in enumerate(reader):
                english_word = row[0]
                russian_word = row[1]
                counter += 1
                if row_i == index:
                    return [english_word, russian_word]
        return None

    def show_ask(self):
        """показ слова """
        words = self.get_word_and_translation(self.counter)
        if words is None:
            print('Слова кончились!')
            return False
        english_word = words[0]
        self.correct_answer = words[1]
        print(f'Вопрос №{self.counter + 1}\n\tПереведите слово "{english_word}" на русский язык')
        return True

    def input_answer(self):
        """ввод пользовательского ответа"""
        word = input('Введите перевод:\t')
        self.user_answer = word

    def check_correct_answer(self):
        """проверка правильности ответа и запись в список неправильных, если ответ неверный"""
        if super().check_correct_answer():
            return True
        return False

