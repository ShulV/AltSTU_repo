
class GameComplexFacade:
    """Класс фасад для реализации простого интерфейса работы с играми"""
    def __init__(self, info_expert, math_game_proxy, quiz_game, english_game):
        self.info_expert = info_expert
        self.math_game_proxy = math_game_proxy
        self.quiz_game = quiz_game
        self.english_game = english_game

    def show_information_about_level(self):
        """получить информации, связанную с опытом"""
        print(f'Суммарный уровень для всех игр {self.info_expert.count_sum_level()}')
        print(f'Средний уровень для всех игр {self.info_expert.count_average_level()}')

    def start_math_game_exercise(self):
        """запустить упражнение для математической игры"""
        self.math_game_proxy.generate_rand_nums()
        self.math_game_proxy.add()
        self.math_game_proxy.show_ask()
        self.math_game_proxy.input_answer()
        is_correct = self.math_game_proxy.check_correct_answer()
        self.math_game_proxy.show_message_about_answer(is_correct)
        if is_correct:
            self.math_game_proxy.go_to_next()

    def start_quiz_game_exercise(self):
        """запустить упражнение для игры-викторины"""
        if self.quiz_game.show_ask():
            self.quiz_game.input_answer()
            is_correct = self.quiz_game.check_correct_answer()
            self.quiz_game.show_message_about_answer(is_correct)
            if is_correct:
                self.quiz_game.go_to_next()

    def start_english_game_exercise(self):
        """запустить упражнение для игры-обучалки английского языка"""
        if self.english_game.show_ask():
            self.english_game.input_answer()
            is_correct = self.english_game.check_correct_answer()
            self.english_game.show_message_about_answer(is_correct)
            if is_correct:
                self.english_game.go_to_next()

