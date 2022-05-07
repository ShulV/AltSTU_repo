from integral import Integral
from monte_carlo import MonteCarlo
from simpson import Simpson
from drawer import show_graphics_for_monte_carlo, show_figure_for_finding_gravity_center
from figure_gravity_center import Figure


def main():
    n = 50  # количество точек
    integral = Integral()  # создаем интеграл (подынтегральная функция, пределы присваиваются в классе)
    mc = MonteCarlo(integral, n)  # создаем объект, вычисляющий интеграл методом Монте-Карло
    mc.get_integral_by_monte_carlo()  # вычисляем интеграл

    print(mc.x_list)
    print(mc.y_list)
    print(mc.random_y_list)
    print(f'\nМЕТОД МОНТЕ-КАРЛО')
    print(f'точек выше {mc.over_points_num}; точек ниже {mc.under_points_num}')
    print(f'часть, занимаемая графиком {mc.proportion}')
    print(f'площадь прямоугольника {mc.square_area}')
    print(f'интеграл (площадь фигуры под графиком) {mc.integral_value}')

    s = Simpson(integral, n, mc.x_list, mc.y_list)# создаем объект, вычисляющий интеграл методом Симпсона
    s.get_integral_by_simpson()  # вычисляем интеграл

    print(f'\nМЕТОД СИМПСОНА')
    print(f'интеграл {s.integral_value}')

    graphic = {'x': mc.x_list, 'y': mc.y_list}
    under_points = {'x': mc.under_graphic_x_list, 'y': mc.under_graphic_y_list}
    over_points = {'x': mc.over_graphic_x_list, 'y': mc.over_graphic_y_list}
    show_graphics_for_monte_carlo(graphic, under_points, over_points)

    figure = Figure()
    figure.find_gravity_center()

    print(f'\nНАХОДИМ ЦЕНТР ТЯЖЕСТИ У ФИГУРЫ (У ТРЕУГОЛЬНИКА)')
    print(f'центр тяжести фигуры {figure.gravity_center}')

    show_figure_for_finding_gravity_center({'x': figure.x_list, 'y': figure.y_list}, figure.gravity_center)


if __name__ == '__main__':
    main()
