
class LevelSystem():
    """уровневая система"""
    def __init__(self):
        pass

    def get_level_by_experience(self, experience):
        """посчитать текущий уровень по количеству опыта
        100 опыта = 1 уровень"""
        return experience // 100
