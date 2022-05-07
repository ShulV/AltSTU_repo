
class Simpson:
    """ метод Симпсона """
    def __init__(self, integral, n, x_list, y_list):
        self.func = integral.integrand  # подыинтегральная функция
        self.min_x = integral.lower_limit
        self.max_x = integral.upper_limit  # пределы интегрирования
        self.n = n  # количество точек
        self.x_list = x_list
        self.y_list = y_list

        self.integral_value = 0


    def get_integral_by_simpson(self):
        """ вычисление определнного интеграла методом Симпсона на отрезке """
        h = (self.max_x - self.min_x) / self.n  # шаг
        _sum = self.func(self.min_x) + self.func(self.max_x)
        k = 0
        for i in range(1, self.n):
            k = 2 + 2 * (i % 2)
            _sum += k * self.func(self.min_x + i * h)
        _sum *= h/3
        self.integral_value = _sum
