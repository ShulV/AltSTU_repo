from ifile_reader import IFileReader
import csv


class QuizFileReader(IFileReader):
    """читатель файла для игры викторина (читает вопрос, варианты ответа, и номер правильного ответа"""
    def __init__(self, filename):
        self.filename = filename

    def get_filename(self):
        """getter filename"""
        return self.filename

    def get_concrete_data(self, index):
        """получать вопрос, номер правильного ответа и варианты ответа"""

        with open(self.filename, 'r', newline='') as File:
            reader = csv.reader(File, delimiter=',')
            counter = 0
            for ask_i, row in enumerate(reader):
                ask = row[0]
                correct_answer_num = next(reader)[0]
                answers = next(reader)
                counter += 1
                if ask_i == index:
                    return [ask, correct_answer_num, answers]
        return None







