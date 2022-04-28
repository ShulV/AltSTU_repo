
class Lagrange:
    """ интерполирует значения функции в произвольных точках по ее таблице при помощи интерполяционного многочлена
    Лагранжа. """

    def __init__(self):
        self.x_list = []  # для использования в формуле Лагранжа
        self.y_list = []
        self.full_x_list = []  # значения больше, чем в x_list (их график выводим)
        self.full_y_list = []
        self.computed_y_list = [] # вычисленные по формуле Лагранжа (их график выводим)

    def create_basic_polynomial(self, i):
        def basic_polynomial(x):
            divider = 1
            result = 1
            for j in range(len(self.x_list)):
                if j != i:
                    result *= (x - self.x_list[j])
                    divider *= (self.x_list[i] - self.x_list[j])
            return result / divider

        return basic_polynomial

    def create_Lagrange_polynomial(self):
        basic_polynomials = []
        for i in range(len(self.x_list)):
            basic_polynomials.append(self.create_basic_polynomial(i))

        def lagrange_polynomial(x):
            result = 0
            for i in range(len(self.y_list)):
                result += self.y_list[i] * basic_polynomials[i](x)
            return result

        return lagrange_polynomial
