import csv


class IFileReader:
    """читатель файла"""
    def get_level_data(self, index):
        raise NotImplementedError()


class QuizFileReader(IFileReader):
    """читатель файла для игры викторина (читает вопрос, варианты ответа, и номер правильного ответа"""
    def __init__(self, filename):
        self.__filename = filename

    def get_level_data(self, index):
        """получать вопрос, номер правильного ответа и варианты ответа"""

        with open('quiz_asks.csv', 'r', newline='') as File:
            reader = csv.reader(File, delimiter=',')
            counter = 0
            for ask_i, row in enumerate(reader):
                ask = row[0]
                correct_answer_num = next(reader)[0]
                answers = next(reader)
                counter += 1
                if ask_i == index:
                    break
        return [ask, correct_answer_num, answers]






