from game import Game
from quiz_file_reader import QuizFileReader
from quiz_file_reader_counter import QuizFileReaderCounter

QUIZ_ASK_FILE = 'quiz_asks.csv'


class QuizGame(Game):
    """игра - викторина (по русскому языку)"""
    instance = None

    def __init__(self):
        super().__init__()
        if QuizGame.instance is not None:
            raise Exception("Объект класса Game уже создан!")
        self.file_reader = QuizFileReaderCounter(QuizFileReader(QUIZ_ASK_FILE))  # QuizFileReader(QUIZ_ASK_FILE)
        QuizGame.instance = self

    def __init__(self, filename):
        super().__init__()
        if QuizGame.instance is not None:
            raise Exception("Объект класса Game уже создан!")
        self.file_reader = QuizFileReaderCounter(QuizFileReader(filename))  # QuizFileReader(filename)
        QuizGame.instance = self

    def __str__(self):
        return "Игра <<Русский язык>>"

    def show_ask(self):
        """показ вопроса и вариантов овтета текущего уровня
        concrete_data= [ask, num_correct_answer, answers]"""
        conrete_data = self.file_reader.get_concrete_data(self.counter)
        if conrete_data is None:
            print('Вопросы кончились!')
            return False
        ask = conrete_data[0]
        self.correct_answer = conrete_data[1]
        answers = conrete_data[2]
        print(f'Вопрос №{self.counter + 1}\n\t{ask}')
        for i, answer in enumerate(answers):
            print(f'\t\t{i + 1}) {answer}')
        return True

    def input_answer(self):
        """ввод пользовательского ответа"""
        num = input('Введите номер правильного ответа:\t')
        self.user_answer = num
