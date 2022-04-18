from quiz_game import QuizGame
from math_game import MathGame


def main():
    print('Обучающий игровой комплекс для младших школьников')
    quiz_game = QuizGame()
    math_game = MathGame()
    while True:
        choice = input(f'\n{"-" * 100}\nСделайте выбор:\n\t1 - математика\n\t2 - викторина (по русскому языку)'
                       f'\n\n\t0 - выйти\n:')
        if choice == '1':
            math_game.generate_rand_nums()
            math_game.show_level_ask()
            math_game.input_answer()
            is_correct = math_game.check_correct_answer()
            math_game.show_message_about_answer(is_correct)
            if is_correct:
                math_game.go_to_next_level()

        elif choice == '2':
            quiz_game.show_level_ask()
            quiz_game.input_answer()
            is_correct = quiz_game.check_correct_answer()
            quiz_game.show_message_about_answer(is_correct)
            if is_correct:
                quiz_game.go_to_next_level()
        elif choice == '3':
            pass
        elif choice == '0':
            return


if __name__ == '__main__':
    main()
