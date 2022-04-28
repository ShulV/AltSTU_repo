from lagrange import Lagrange
from graph_drawer import draw_graphs
from func import func, label


def frange(start, stop, step):
    """range для float"""
    i = start
    while i < stop:
        yield i
        i += step


def main():
    lagrange = Lagrange()

    with open("values.txt", "r") as f:
        for x in f:
            lagrange.x_list.append(float(x))
            lagrange.y_list.append(func(float(x)))

    min_x_list = min(lagrange.x_list)
    max_x_list = max(lagrange.x_list)
    for x in frange(min_x_list, max_x_list, 0.01):
        lagrange.full_x_list.append(x)
        lagrange.full_y_list.append(func(x))
        f = lagrange.create_Lagrange_polynomial()
        lagrange.computed_y_list.append(f(x))

    print('исходная функция')
    print(f'x', lagrange.x_list)
    print(f'y', lagrange.y_list)
    print(f'всего точек: {len(lagrange.x_list)}')
    print('\nточки интерполяции')
    print(f'y', lagrange.computed_y_list)
    print('точки f(x)')
    print(f'y', lagrange.full_y_list)
    print(f'всего точек: {len(lagrange.full_x_list)}')

    draw_graphs(lagrange.full_x_list, lagrange.full_y_list, lagrange.computed_y_list, label)


if __name__ == "__main__":
    main()
