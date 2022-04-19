from game import Game
from random import randint
from imath import IMath


MIN_NUM = 1
MAX_NUM = 20


class MathGame(Game, IMath):
    """игра - суммирование чисел (математика)"""
    def __init__(self):
        super().__init__()
        self.rand_num_1 = None
        self.rand_num_2 = None

    def show_level_ask(self):
        """показать вопрос"""
        print(f'Вопрос №{self._counter + 1}\n\tЧему равно {self.rand_num_1} + {self.rand_num_2}?')

    def input_answer(self):
        """ввод пользовательского ответа"""
        num = input('Введите сумму чисел:\t')
        self._user_answer = num

    def generate_rand_nums(self):
        """генерация двух случайных чисел для суммирования"""
        self.rand_num_1 = randint(MIN_NUM, MAX_NUM)
        self.rand_num_2 = randint(MIN_NUM, MAX_NUM)

    def add(self):
        """суммирование 2 чисел"""
        self._correct_answer = str(self.rand_num_1 + self.rand_num_2)
        return self._correct_answer

