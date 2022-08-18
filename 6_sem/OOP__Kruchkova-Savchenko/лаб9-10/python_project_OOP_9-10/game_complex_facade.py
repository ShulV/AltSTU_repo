from rus_to_eng import RusToEng
from eng_to_rus import EngToRus
from game_caretaker import GameCaretaker
from advertiser import Advertiser
from message_pool import MessagePool
from math_game import MathGame
from quiz_game import QuizGame
from english_game import EnglishGame


class GameComplexFacade:
    """Класс фасад для реализации простого интерфейса работы с играми"""
    def __init__(self, info_expert, math_game_proxy, quiz_game, english_game):
        self.info_expert = info_expert
        self.math_game_proxy = math_game_proxy
        self.quiz_game = quiz_game
        self.english_game = english_game
        # State
        self.eng_to_rus_state = EngToRus()
        self.rus_to_eng_state = RusToEng()
        self.english_game.set_state(self.eng_to_rus_state)  # установить состояние для игры EnglishGame
        # Memento
        self.game_caretakers = {  # игры и их хранители снимков
            self.math_game_proxy: GameCaretaker(),
            self.quiz_game: GameCaretaker(),
            self.english_game: GameCaretaker()
        }
        # Observer
        self.ads_observer = Advertiser()
        self.math_game_proxy.attach(self.ads_observer)  # добавляем наблюдателей
        self.quiz_game.attach(self.ads_observer)
        self.english_game.attach(self.ads_observer)
        # Object pool
        self.message_pool = MessagePool(math_game_proxy, quiz_game, english_game)

    def show_information_about_level(self):
        """получить информации, связанную с опытом"""
        print(f'Суммарный уровень для всех игр {self.info_expert.count_sum_level()}')
        print(f'Средний уровень для всех игр {self.info_expert.count_average_level()}')

    def show_message_about_answer_for_game(self, game, is_correct):
        """показать сообщение о результате игры, используя пул объектов сообщений"""
        message = self.message_pool.acquire(game)
        message.set_message_text(is_correct, game.correct_answer)
        game.show_message_about_answer(message)
        self.message_pool.release(game, message)

    def start_math_game_exercise(self):
        """запустить упражнение для математической игры"""
        self.math_game_proxy.generate_rand_nums()
        self.math_game_proxy.add()
        self.math_game_proxy.show_ask()
        self.math_game_proxy.input_answer()
        is_correct = self.math_game_proxy.check_correct_answer()
        self.show_message_about_answer_for_game(self.math_game_proxy, is_correct)
        if is_correct:
            self.math_game_proxy.go_to_next()
        self.math_game_proxy.show_ads()

    def start_quiz_game_exercise(self):
        """запустить упражнение для игры-викторины"""
        if self.quiz_game.show_ask():
            self.quiz_game.input_answer()
            is_correct = self.quiz_game.check_correct_answer()
            self.show_message_about_answer_for_game(self.quiz_game, is_correct)
            if is_correct:
                self.quiz_game.go_to_next()
        self.quiz_game.show_ads()

    def start_english_game_exercise(self):
        """запустить упражнение для игры-обучалки английского языка"""
        if self.english_game.show_ask():
            self.english_game.input_answer()
            is_correct = self.english_game.check_correct_answer()
            self.show_message_about_answer_for_game(self.english_game, is_correct)
            if is_correct:
                self.english_game.go_to_next()
        self.english_game.show_ads()

    def change_english_game_state(self):
        """изменить состояние игры EnglishGame"""
        while True:
            choice = input(f'Текущий режим игры - {self.english_game.cur_state}'
                           f'\n\t1 - изменить режим на {self.rus_to_eng_state}'
                           f'\n\t2 - изменить режим на {self.eng_to_rus_state}\n'
                           f'\n\t0 - назад\n\t\t:\t')
            if choice == '1':
                self.english_game.cur_state = self.rus_to_eng_state
                return
            if choice == '2':
                self.english_game.cur_state = self.eng_to_rus_state
                return
            if choice == '0':
                return

    def choice_game(self):
        """выбрать игру"""
        while True:
            choice = input(f'Выберите игру:'
                           f'\n\t1 - {self.math_game_proxy}'
                           f'\n\t2 - {self.quiz_game}'
                           f'\n\t3 - {self.english_game}\n')
            if choice == '1':
                return self.math_game_proxy
            if choice == '2':
                return self.quiz_game
            if choice == '3':
                return self.english_game

    def perform_memento_action(self):
        """выполнить действие, связанное со снимком"""
        game = self.choice_game()
        while True:
            choice = input(f'Выберите действия, связанные с прогрессом:'
                           f'\n\t1 - сохранить прогресс'
                           f'\n\t2 - восстановить сохраненное состояние прогресса\n'
                           f'\n\t0 - назад\n\t\t:\t')
            if choice == '0':
                return
            if choice == '1':
                self.game_caretakers[game].set_memento(game.save_state())
                return
            if choice == '2':
                memento = self.game_caretakers[game].get_memento()
                if memento is None:
                    print('Нет бэкапов!')
                else:
                    game.restore_state(memento)
                return

    def manage_ads(self):
        """управлять рекламой"""
        while True:
            choice = input(f'Отключить рекламу?'
                           f'\n\t1 - да (выбрать игру)'
                           f'\n\t2 - да (для всех игр)'
                           f'\n\t0 - нет\n\t\t:\t')
            if choice == '0':
                return
            if choice == '1':
                game = self.choice_game()
                game.detach(self.ads_observer)
                return
            if choice == '2':
                self.math_game_proxy.detach(self.ads_observer)
                self.quiz_game.detach(self.ads_observer)
                self.english_game.detach(self.ads_observer)
                return

    def create_games(self):
        """создать игры"""
        try:
            self.math_game_proxy = MathGame()
            self.english_game = EnglishGame('filename.txt')
            self.quiz_game = QuizGame('filename2.txt')
            print('Создание игр произошло успешно')
        except:
            print('Создать игры не удалось')



