from game import Game
from random import randint
from imath import IMath


MATH_LOG_FILE = 'math_log.txt'


MIN_NUM = 1
MAX_NUM = 20


class MathGameProxy(Game, IMath):
    """игра - суммирование чисел (математика)"""
    def __init__(self):
        super().__init__()
        self.math = None

    def set_original_math(self, math):
        self.math = math

    def add(self):
        """суммирование 2 чисел"""
        super().add()
        self.log_add(MATH_LOG_FILE)

    def log_add(self, filename):
        with open(filename, 'a') as file:
            # TODO записать a, b и время вызова
            file.write('input')