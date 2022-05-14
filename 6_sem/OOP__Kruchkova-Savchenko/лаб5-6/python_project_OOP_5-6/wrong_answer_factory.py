from russian_wrong_answer import RussianWrongAnswer


class WrongAnswerFactory:
    """фабрика неправильных ответов в игре по английскому языку"""
    wrong_answers = {}  # статический словарь уникальных объектов RussianWrongAnswer
    wrong_answers_counter = {}  # статический словарь счётчиков уникальных объектов RussianWrongAnswer

    @staticmethod
    def get_wrong_answer(word):
        """создание объекта неправильного ответа"""
        if word in WrongAnswerFactory.wrong_answers_counter.keys():
            WrongAnswerFactory.wrong_answers_counter[word] += 1
        else:
            WrongAnswerFactory.wrong_answers_counter.setdefault(word, 1)
        return WrongAnswerFactory.wrong_answers.setdefault(word, RussianWrongAnswer(word))


