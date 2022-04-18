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
        self.rand_num_1 = None
        self.rand_num_2 = None
        self.math_game = None

    def set_original_math(self, math_game):
        self.math_game = math_game

    def log_add(self, filename):
        """логирование (хранение истории обращений)"""
        with open(filename, 'a') as file:
            cur_date = datetime.now()
            adding_log = f'число {self.math_game.rand_num_1} прибавили к числу {self.math_game.rand_num_2}; время: {cur_date}\n'
            print(f' adding_log { adding_log}')
            file.write(adding_log)

    def add(self):
        """суммирование 2 чисел"""
        self.math_game.add()
        self.log_add(MATH_LOG_FILE)

    def show_level_ask(self):
        """показать вопрос"""
        self.math_game.show_level_ask()

    def input_answer(self):
        """ввод пользовательского ответа"""
        self.math_game.input_answer()

    def generate_rand_nums(self):
        """генерация двух случайных чисел для суммирования"""
        self.math_game.generate_rand_nums()


