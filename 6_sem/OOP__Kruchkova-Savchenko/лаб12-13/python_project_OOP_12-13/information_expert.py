
class InformationExpert:
    """информационный эксперт для инкапсулированных в него игр, выполняет расчеты, связанные со свойствами игр"""
    def __init__(self, math_game_proxy, quiz_game, english_game):
        self.math_game_proxy = math_game_proxy
        self.quiz_game = quiz_game
        self.english_game = english_game

    def count_sum_level(self):
        """подсчитать суммарный уровень для всех игр"""
        math_level = self.math_game_proxy.get_level()
        quiz_level = self.quiz_game.get_level()
        english_level = self.english_game.get_level()
        print(f'Уровни: Math - {math_level}, Rus - {quiz_level}, Eng - {english_level}')
        return math_level + quiz_level + english_level

    def count_average_level(self):
        """подсчитать суммарный уровень для всех игр"""
        game_number = 3
        math_level = self.math_game_proxy.get_level()
        quiz_level = self.quiz_game.get_level()
        english_level = self.english_game.get_level()
        return (math_level + quiz_level + english_level) / game_number
