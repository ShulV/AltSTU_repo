from game import Game
from quiz_file_reader import QuizFileReader

QUIZ_ASK_FILE = 'quiz_asks.csv'


class QuizGame(Game):
    """игра - викторина (по русскому языку)"""
    def __init__(self):
        super().__init__()
        self.file_reader = QuizFileReader(QUIZ_ASK_FILE)

    def show_level_ask(self):
        """показать вопрос и варианты овтета текущего уровня
        level_data= [ask, num_correct_answer, answers]"""
        level_data = self.file_reader.get_level_data(self._counter)
        ask = level_data[0]
        self._correct_answer = level_data[1]
        answers = level_data[2]
        print(f'Вопрос №{self._counter + 1}\n\t{ask}')
        for i, answer in enumerate(answers):
            print(f'\t\t{i + 1}) {answer}')

    def input_answer(self):
        """ввод пользовательского ответа"""
        num = input('Введите номер правильного ответа:\t')
        self._user_answer = num
