from level_system_adapter import LevelSystemAdapter
from level_system import LevelSystem
from game_memento import GameMemento
from game_state import GameState


class Game:
    """игра"""
    def __init__(self):
        self.counter = 0
        self.user_answer = None
        self.correct_answer = None
        self.level_system = LevelSystemAdapter(LevelSystem())
        self.observers = []

    def check_correct_answer(self):
        """проверка правильности ответа пользователя"""
        if self.user_answer == self.correct_answer:
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
        self.counter += 1
        print(f'Переход на следующее задание!\nВаш текущий уровень {self.get_level()}!')
        self.notify()  # передать новую информацию наблюдателям

    def show_message_about_answer(self, is_correct):
        """сообщение о правильности ответа"""
        if is_correct:
            print(f'Вы ответили правильно! (ответ: {self.correct_answer})')
        else:
            print('Вы ответили неверно!')

    def get_level(self):
        """получить текущий уровень"""
        return self.level_system.get_level_by_counter(self.counter)

    def save_state(self):
        """создать и вернуть снимок состояния объекта Game"""
        return GameMemento(GameState(self.counter))

    def restore_state(self, game_memento):
        """восстановить состояние Game из снимка"""
        print('Прогресс восстановлен!')
        self.counter = game_memento.get_game_state().counter

    def setState(self, state):
        """установить состояние Game"""
        self.counter = state.counter

    def getState(self):
        """получить состояние Game"""
        return GameState(self.counter)

    def attach(self, observer):
        """добавить (закрепить) наблюдателя"""
        self.observers.append(observer)

    def detach(self, observer):
        """удалить (открепить) наблюдателя"""
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        """уведомить наблюдателей"""
        for obs in self.observers:
            obs.update_personal_ads(str(self), self.counter)

    def show_ads(self):
        """показать рекламу (если есть рекламщик)"""
        for obs in self.observers:
            print(f'РЕКЛАМА: {obs.personal_ads}')
