
class GameCaretaker:
    """опекун, который хранит снимок класса Game"""
    def __init__(self):
        self.memento = None

    def set_memento(self, memento):
        """установить memento"""
        print('Прогресс сохранен!')
        self.memento = memento

    def get_memento(self):
        """получить memento"""
        return self.memento

