from observer import Observer


class Advertiser(Observer):
    """наблюдатель-рекламщик"""

    def __init__(self):
        self.game_states = {}
        self.personal_ads = f'Общая реклама'  # сюда будет записана персонализированная реклама

    def update_personal_ads(self, game_name, counter):
        """подобрать подходящую рекламу"""
        if self.game_states.get(game_name):
            self.game_states.update({game_name: counter})
        else:
            self.game_states.setdefault(game_name, counter)
        self.personal_ads = f'Реклама для тех, кто предпочитает {max(self.game_states, key=self.game_states.get)}'
        print(f'\nDEBUG\n'
              f'max = {max(self.game_states, key=self.game_states.get)}\n'
              f'self.game_states = {self.game_states}\n')
