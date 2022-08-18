from ilevel_system import ILevelSystem


class LevelSystemAdapter(ILevelSystem):
    """адаптер уровневой системы"""
    def __init__(self, level_system):
        self.level_system = level_system

    def get_level_by_counter(self, counter):
        """посчитать текущий уровень по количеству пройденных уровней
        1 пройденное задание = 50 опыта
        100 опыта = 1 уровень"""
        experience = 50 * counter
        return self.level_system.get_level_by_experience(experience)
