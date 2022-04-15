from func import func


class Lagrange:
    """ интерполирует значения функции в произвольных точках по ее таблице при помощи интерполяционного многочлена
    Лагранжа. """

    def __init__(self):
        self.x_list = []
        self.y_list = []
        self.computed_x_list = []
        self.computed_y_list = []

    def add_point(self, x, y):
        """ добавляет точку в список"""
        self.x_list.append(x)
        self.y_list.append(y)

    def enter_point(self):
        """ вводится x,y с консоли"""
        x = float(input('Введите x:\t'))
        y = float(input('Введите f(x):\t'))
        self.add_point(x, y)

    def show_table(self):
        """ выводится таблица точек """
        for point in self.points:
            print(f'x: {point.x:10.2f}; y: {point.y:10.2f}')

    def ln(self, x_list, x):
        """ интерполяционный многочлен Лагранжа
        mult_up - верхнее k-ое произведение в формуле
        mult_down - нижнее k-ое произведение в формуле (лямбда k)
        ck = mult_up/mult_down- базовый k-ый полином
        func(x) - исследуемая функция
        sum - сумма k-ых произведений ck и func(x)"""
        n = len(x_list)
        _sum = 0
        for k in range(n):
            mult_up = mult_down = 1
            for j in range(n):
                if j != k:
                    mult_up *= x - x_list[j]
                    mult_down *= x_list[k] - x_list[j]
                    if mult_down == 0:
                        print(f'mult_down = 0; j = {j}; k = {k}; x_list[k]={x_list[k]}; x_list[j]={x_list[j]}')
            ck = mult_up / mult_down
            _sum += ck * func(x)
        return _sum
