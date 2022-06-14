
INIT_MESSAGE = '<<init message>>'


class Message:
    """шаблон сообщения"""

    def __init__(self):
        self.message_text = INIT_MESSAGE

    def reset(self):
        """Сбросить текст сообщения"""
        self.message_text = INIT_MESSAGE

    def set_message_text(self, is_correct, correct_answer=''):
        """установка параметров сообщения"""
        if is_correct:
            self.message_text = f'Вы ответили правильно! (ответ: {correct_answer})'
        else:
            self.message_text = 'Вы ответили неверно!'
