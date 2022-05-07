from random import uniform


class MonteCarlo:
    """ метод Монте-Карло """
    def __init__(self, integral, n):
        self.integral = integral  # пределы интегрирования и подыинтегральная функция
        self.n = n  # количество точек
        self.x_list = []  # список x-ов
        self.y_list = []  # список y-ов
        self.min_y = None  # минимальный y из списка y_list
        self.max_y = None  # максимальный y из списка y_list

        self.under_graphic_x_list = []  # координаты x точек находящихся ниже графика
        self.under_graphic_y_list = []  # координаты y точек находящихся ниже графика
        self.over_graphic_x_list = []  # координаты x точек находящихся выше графика
        self.over_graphic_y_list = []  # координаты y точек находящихся выше графика

        self.under_points_num = 0  # кол-во точек, которые ниже графика
        self.over_points_num = 0  # кол-во точек, которые выше графика

        self.square_area = 0  # площадь прямоугольника
        self.proportion = 0  # часть графика, которую он занимает в прямоугольнике
        self.integral_value = 0  # площадь под графиком (значение интеграла)

    def get_integral_by_monte_carlo(self):
        """ вычисление определнного интеграла методом Монте-Карло на отрезке """
        self.__generate_n_x()
        self.__calculate_n_y()
        self.__find_min_max_y()
        self.__generate_n_y()
        self.__get_under_over_points()
        self.__get_square_area()
        self.__get_integral_value()

    def __generate_n_x(self):
        """ генерация координат x для n точек в интервале от lower_limit до upper_limit"""
        self.x_list = [uniform(self.integral.lower_limit, self.integral.upper_limit) for _ in range(0, self.n)]
        self.x_list.sort()

    def __calculate_n_y(self):
        """ подсчет координат y=f(x) для n точек, где f(x) - подынтегральная функция """
        self.y_list = [self.integral.integrand(x) for x in self.x_list]

    def __find_min_max_y(self):
        """ нахождение минимального и максимального y в списке y_list """
        self.min_y = min(self.y_list)
        self.max_y = max(self.y_list)

    def __generate_n_y(self):
        """ генерация координат y для n точек в интервале от min_y до max_y"""
        self.random_y_list = [uniform(self.min_y, self.max_y) for _ in self.x_list]

    def __get_under_over_points(self):
        """ нахождение точек, которые расположены под графиком """
        for rand_y, y, x in zip(self.random_y_list, self.y_list, self.x_list):
            if rand_y < y:
                self.under_graphic_x_list.append(x)
                self.under_graphic_y_list.append(rand_y)
                self.under_points_num += 1
            else:
                self.over_graphic_x_list.append(x)
                self.over_graphic_y_list.append(rand_y)
                self.over_points_num += 1

    def __get_square_area(self):
        """ подсчет площади прямоугольника, в котором мы генерируем точки """
        x = abs(self.integral.lower_limit) + abs(self.integral.upper_limit)
        y = abs(self.min_y) + (self.max_y)
        self.square_area = x * y

    def __get_integral_value(self):
        """ получение значения интеграла (площади под графиком) """
        self.proportion = self.under_points_num / (self.under_points_num + self.over_points_num)
        self.integral_value = self.square_area * self.proportion





