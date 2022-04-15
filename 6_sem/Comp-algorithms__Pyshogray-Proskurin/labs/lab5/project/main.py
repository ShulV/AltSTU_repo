from lagrange import Lagrange
from graph_drawer import draw_graphs
from func import func
from random import randint


def main():

    lagrange = Lagrange()
    # генерация случайных x-ов (каждый следующий больше предыдущего, т.к. график - ломаная прямая)
    for x in range(-500, 501, 20):
        lagrange.x_list.append(x + randint(-9, 9))
        lagrange.y_list.append(func(x))
    # списки x-ов и y-ов для дальнейшей их передачи на отрисовку (для отрисовки сразу нескольких графиков)
    x_lists = [lagrange.x_list]
    y_lists = [lagrange.y_list]
    lst = lagrange.x_list
    print(sorted(map(abs,lst.copy())))
    print(lst)
    print(lagrange.y_list)
    for i in range(len(lagrange.x_list)):
        x = lagrange.x_list[i]
        lagrange.computed_x_list.append(x)
        y = lagrange.ln(lagrange.x_list, x)
        lagrange.computed_y_list.append(y)
    x_lists.append(lagrange.computed_x_list)
    y_lists.append(lagrange.computed_y_list)
    # графики исходной функции и полученной
    draw_graphs(x_lists, y_lists)


if __name__ == "__main__":
    main()


