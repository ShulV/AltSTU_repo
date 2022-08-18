from abc import ABC, abstractmethod


class Observer(ABC):
    """наблюдатель"""

    @abstractmethod
    def __init__(self):
        self.game_states = {}
        self.personal_ads = None

    @abstractmethod
    def update_personal_ads(self, game_name, game_state):
        """подобрать подходящую рекламу"""
        pass
