from ifile_reader import IFileReader
import csv


class AdvancedQuizFileReader(IFileReader):
    """читатель-декоратор файла для игры викторина
    (читает вопрос, варианты ответа, и номер правильного ответа)
    дополняет функционал за счет способности подсчитывать количество оставшихся в файле уровней"""
    def __init__(self, file_reader):
        pass

    def get_concrete_data(self, index):
        """получать вопрос, номер правильного ответа и варианты ответа"""
        pass

    def get_filename(self):
        """getter filename"""
        pass

    def __get_remaining_data_num(self, index):
        """подсчитывает количество оставшихся вопросов в файле"""
        pass
