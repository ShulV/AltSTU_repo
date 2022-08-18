from quiz_game import QuizGame
from math_game import MathGame
from math_game_proxy import MathGameProxy
from english_game import EnglishGame
from game_complex_facade import GameComplexFacade
from information_expert import InformationExpert

QUIZ_ASK_FILE = 'quiz_asks.csv'
ENGLISH_WORDS_FILE = 'english_words.csv'


def main():
    print('Обучающий игровой комплекс для младших школьников')
    quiz_game = QuizGame(QUIZ_ASK_FILE)
    # math_game_proxy = MathGameProxy()
    math_game = MathGame()
    # math_game_proxy.set_original_math(math_game)
    english_game = EnglishGame(ENGLISH_WORDS_FILE)
    info_expert = InformationExpert(math_game, quiz_game, english_game)
    simple_game_interface = GameComplexFacade(info_expert, math_game, quiz_game, english_game)

    while True:
        choice = input(f'\n{"-" * 100}\nСделайте выбор:\n\t1 - математика'
                       f'\n\t2 - викторина (по русскому языку)'
                       f'\n\t3 - английские слова'
                       f'\n\t4 - изменить направление перевода в "Английских словах"'
                       f'\n\t5 - показать информацию об опыте в играх'
                       f'\n\t6 - сохранить/восстановить прогресс'
                       f'\n\t7 - управлять рекламой'
                       f'\n\n\t0 - выйти\n:')
        if choice == '1':
            simple_game_interface.start_math_game_exercise()
        elif choice == '2':
            simple_game_interface.start_quiz_game_exercise()
        elif choice == '3':
            simple_game_interface.start_english_game_exercise()
        elif choice == '4':
            simple_game_interface.change_english_game_state()
        elif choice == '5':
            simple_game_interface.show_information_about_level()
        elif choice == '6':
            simple_game_interface.perform_memento_action()
        elif choice == '7':
            simple_game_interface.manage_ads()
        elif choice == '0':
            return


if __name__ == '__main__':
    main()
