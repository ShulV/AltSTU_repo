from random import uniform

class Figure:
    """ фигура, у которой находим центр тяжести """
    def __init__(self):
        # треугольник
        self.x_list = [0, 0, 6, 0]
        self.y_list = [0, 5, 0, 0]
        self.max_x = max(self.x_list)
        self.min_x = min(self.x_list)
        self.max_y = max(self.y_list)
        self.min_y = min(self.y_list)
        self.tries_num = 100000  # кол-во испытаний
        self.gravity_center = {'x': 0, 'y': 0}

    def find_gravity_center(self):
        """ нахождение центра тяжести """
        upx = upy = dow = 0  # upx - числитель в формуле поиска x центра тяжести, upy - то же самое, но для y,
        # dow - знаменатель для обеих формул
        for i in range(0, self.tries_num):
            x = uniform(self.min_x, self.max_x)
            y = uniform(self.min_y, self.max_y)
            # проверка того, входит ли очередная точка в область фигуры
            if self.min_y < y < -x * (5/6) + 5:
                upx += x
                upy += y
                dow += 1
        self.gravity_center['x'] = upx/dow
        self.gravity_center['y'] = upy/dow

