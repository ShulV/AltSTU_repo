from level_system_adapter import LevelSystemAdapter
from level_system import LevelSystem


class Game:
    """игра"""
    def __init__(self):
        self._counter = 0
        self._user_answer = None
        self._correct_answer = None
        self._level_system = LevelSystemAdapter(LevelSystem())

    def check_correct_answer(self):
        """проверка правильности ответа пользователя"""
        if self._user_answer == self._correct_answer:
            return True
        return False

    def input_answer(self):
        """ввод пользовательского ответа"""
        pass

    def show_ask(self):
        """показ вопроса"""
        pass

    def go_to_next(self):
        """увеличение счетчика (переход на следующий уровень/вопрос)"""
        self._counter += 1
        print(f'Переход на следующее задание!\nВаш текущий уровень {self.get_level()}!')

    def show_message_about_answer(self, is_correct):
        """сообщение о правильности ответа"""
        if is_correct:
            print(f'Вы ответили правильно! (ответ: {self._correct_answer})')
        else:
            print('Вы ответили неверно!')

    def get_level(self):
        """получить текущий уровень"""
        return self._level_system.get_level_by_counter(self._counter)
