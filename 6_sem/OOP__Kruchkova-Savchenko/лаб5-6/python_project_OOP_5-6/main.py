from quiz_game import QuizGame
from math_game import MathGame
from math_game_proxy import MathGameProxy
from english_game import EnglishGame

QUIZ_ASK_FILE = 'quiz_asks.csv'
ENGLISH_WORDS_FILE = 'english_words.csv'


def main():
    print('Обучающий игровой комплекс для младших школьников')
    quiz_game = QuizGame(QUIZ_ASK_FILE)
    math_game_proxy = MathGameProxy()
    math_game = MathGame()
    math_game_proxy.set_original_math(math_game)
    english_game = EnglishGame(ENGLISH_WORDS_FILE)

    while True:
        choice = input(f'\n{"-" * 100}\nСделайте выбор:\n\t1 - математика\n\t2 - викторина (по русскому языку)'
                       f'\n\t3 - английские слова\n\n\t0 - выйти\n:')
        if choice == '1':

            math_game_proxy.generate_rand_nums()
            math_game_proxy.add()
            math_game_proxy.show_ask()
            math_game_proxy.input_answer()
            is_correct = math_game_proxy.check_correct_answer()
            math_game_proxy.show_message_about_answer(is_correct)
            if is_correct:
                math_game_proxy.go_to_next()

        elif choice == '2':
            if quiz_game.show_ask():
                quiz_game.input_answer()
                is_correct = quiz_game.check_correct_answer()
                quiz_game.show_message_about_answer(is_correct)
                if is_correct:
                    quiz_game.go_to_next()
        elif choice == '3':
            if english_game.show_ask():
                english_game.input_answer()
                is_correct = english_game.check_correct_answer()
                english_game.show_message_about_answer(is_correct)
                if is_correct:
                    english_game.go_to_next()
        elif choice == '0':
            return


if __name__ == '__main__':
    main()
