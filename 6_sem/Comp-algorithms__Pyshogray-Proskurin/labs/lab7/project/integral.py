from math import e, pow, sin, pi


class Integral:
    def __init__(self):
        self.lower_limit = 0  # нижний предел интегрирования
        self.upper_limit = 4  # верхний предел интегрирования
        self.integrand = lambda x: pow(x, 3)  # -x * x + 4  # x * pow(e, -x)  # подынтегральная функция
