from game import Game
from imath import IMath
from datetime import datetime
from random import randint


MATH_LOG_FILE = 'math_log.txt'


MIN_NUM = 1
MAX_NUM = 20


class MathGameProxy(Game, IMath):
    """логирующий заместитель игры - суммирование чисел (математика)"""
    def __init__(self):
        super().__init__()
        self.math_game = None

    def set_original_math(self, math_game):
        self.math_game = math_game

    def generate_rand_nums(self):
        """генерация двух случайных чисел для суммирования"""
        self.math_game.generate_rand_nums()

    def add(self):
        """суммирование 2 чисел"""
        self.math_game.add()
        self.log_add(MATH_LOG_FILE)

    def log_add(self, filename):
        """логирование (хранение истории обращений)"""
        with open(filename, 'a') as file:
            cur_date = datetime.now()
            adding_log = f'add({self.math_game.rand_num_1}, {self.math_game.rand_num_2}); время: {cur_date}\n'
            file.write(adding_log)

    def show_level_ask(self):
        """показать вопрос"""
        self.math_game.show_level_ask()

    def input_answer(self):
        """ввод пользовательского ответа"""
        self.math_game.input_answer()

    def check_correct_answer(self):
        """проверка правильности ответа пользователя"""
        return self.math_game.check_correct_answer()

    def show_message_about_answer(self, is_correct):
        """сообщение о правильности ответа"""
        self.math_game.show_message_about_answer(is_correct)


