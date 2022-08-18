

class GameMemento:
    """хранитель состояния игры"""
    def __init__(self, game_state=None):
        self.game_state = game_state

    def set_game_state(self, game_state):
        """установить состояние в хранителе"""
        self.game_state = game_state

    def get_game_state(self):
        """получить состояние в хранителе"""
        return self.game_state
