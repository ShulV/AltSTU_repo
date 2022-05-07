from game import Game
from imath import IMath
from datetime import datetime


MATH_LOG_FILE = 'math_log.txt'


MIN_NUM = 1
MAX_NUM = 20


def log_add(filename):
    """логирование (хранение истории обращений)"""
    with open(filename, 'a') as file:
        cur_date = datetime.now()
        adding_log = f'addding; время: {cur_date}\n'
        file.write(adding_log)


class MathGameProxy(Game, IMath):
    """логирующий заместитель игры - суммирование чисел (математика)"""
    def __init__(self):
        super().__init__()
        self.__math_game = None

    def set_original_math(self, math_game):
        """ленивая инициализация реального объекта"""
        if self.__math_game is None:
            self.__math_game = math_game

    def generate_rand_nums(self):
        """генерация двух случайных чисел для суммирования"""
        self.__math_game.generate_rand_nums()

    def add(self):
        """суммирование 2 чисел"""
        self.__math_game.add()
        log_add(MATH_LOG_FILE)

    def show_ask(self):
        """показать вопрос"""
        self.__math_game.show_ask()

    def input_answer(self):
        """ввод пользовательского ответа"""
        self.__math_game.input_answer()

    def check_correct_answer(self):
        """проверка правильности ответа пользователя"""
        return self.__math_game.check_correct_answer()

    def show_message_about_answer(self, is_correct):
        """сообщение о правильности ответа"""
        self.__math_game.show_message_about_answer(is_correct)

    def go_to_next(self):
        """увеличение счетчика (переход на следующий уровень/вопрос)"""
        self.__math_game.go_to_next()


