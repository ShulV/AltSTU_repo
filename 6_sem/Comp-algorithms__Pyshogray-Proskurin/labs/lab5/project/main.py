from lagrange import Lagrange
from graph_drawer import draw_graphs
from func import func
from random import randint
from math import pi


def main():

    lagrange = Lagrange()

    # with open("values.txt", "r") as f:
    #     for x in f:
    #         lagrange.x_list.append(float(x))
    #         lagrange.y_list.append(func(float(x)))

    for x in range(-10, 11):
        # x /= 1
        lagrange.x_list.append(x)
        lagrange.y_list.append(func(x))
    x_lists = [lagrange.x_list]
    y_lists = [lagrange.y_list]
    # списки x-ов и y-ов для дальнейшей их передачи на отрисовку (для отрисовки сразу нескольких графиков)

    for x in range(-120, 121):
        x /= 5
        lagrange.computed_x_list.append(x)
        y = lagrange.ln(lagrange.x_list, x)
        lagrange.computed_y_list.append(y)
    x_lists.append(lagrange.computed_x_list)
    y_lists.append(lagrange.computed_y_list)
    # графики исходной функции и полученной

    print('исходная функция')
    print(f'x', lagrange.x_list)
    print(f'y', lagrange.y_list)
    print(f'всего точек: {len(lagrange.x_list)}')
    print('точки интерполяции')
    print(f'x', lagrange.computed_x_list)
    print(f'y', lagrange.computed_y_list)
    print(f'всего точек: {len(lagrange.computed_x_list)}')


    draw_graphs(x_lists, y_lists)


if __name__ == "__main__":
    main()


