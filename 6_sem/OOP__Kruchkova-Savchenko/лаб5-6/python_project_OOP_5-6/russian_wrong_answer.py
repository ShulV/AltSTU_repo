
from wrong_answer import WrongAnswer


class RussianWrongAnswer(WrongAnswer):
    """Класс-легковес неправильного русского ответа в игре-обучалке по английскому (конкретный)"""
    def __init__(self, word):
        super().__init__(word)
        self.word = word

