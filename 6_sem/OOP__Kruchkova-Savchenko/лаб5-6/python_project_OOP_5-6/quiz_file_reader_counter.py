from advanced_quiz_file_reader import AdvancedQuizFileReader
import csv


class QuizFileReaderCounter(AdvancedQuizFileReader):
    """читатель-декоратор файла для игры викторина
    (читает вопрос, варианты ответа, и номер правильного ответа)
    дополняет функционал за счет способности подсчитывать количество оставшихся в файле уровней"""
    def __init__(self, file_reader):
        self.__file_reader = file_reader

    def get_concrete_data(self, index):
        """получать вопрос, номер правильного ответа и варианты ответа"""
        counter = self.__get_remaining_data_num(index)
        print(f'Осталось вопросов: {counter}')
        return self.__file_reader.get_concrete_data(index)

    def get_filename(self):
        """getter filename"""
        return self.__file_reader.get_filename()

    def __get_remaining_data_num(self, index):
        """подсчитывает количество оставшихся вопросов в файле"""
        with open(self.__file_reader.get_filename(), 'r', newline='') as File:
            reader = csv.reader(File, delimiter=',')
            counter = 0
            for ask_i, row in enumerate(reader):
                next(reader)
                next(reader)
                if ask_i < index:
                    continue
                counter += 1
        return counter
