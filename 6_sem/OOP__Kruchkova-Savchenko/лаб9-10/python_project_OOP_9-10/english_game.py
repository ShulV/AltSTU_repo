from game import Game
# import csv


ENGLISH_WORDS_FILE = 'english_words.csv'


class EnglishGame(Game):
    """игра - обучалка слов по английскому языку"""
    instance = None

    def __init__(self):
        super().__init__()
        if EnglishGame.instance is not None:
            raise Exception("Объект класса Game уже создан!")
        self.filename = ENGLISH_WORDS_FILE
        self.cur_state = None
        EnglishGame.instance = self

    def __init__(self, filename):
        super().__init__()
        if EnglishGame.instance is not None:
            raise Exception("Объект класса Game уже создан!")
        self.filename = filename
        self.cur_state = None
        EnglishGame.instance = self

    def __str__(self):
        return "Игра <<Английские слова>>"

    def set_state(self, state):
        """установить состояние"""
        self.cur_state = state

    def show_ask(self):
        """показ слова """
        words = self.cur_state.get_word_and_translation(self.filename, self.counter)
        if words is None:
            print('Слова кончились!')
            return False
        word_to_translate = words[0]
        self.correct_answer = words[1]
        print(f'Вопрос №{self.counter + 1}\n\tПереведите слово "{word_to_translate}"')
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

