import csv


# Решение уравнений методом Гаусса
#
# P.S.
# В функциях используются переменные a и b
# a - матрица коэффициентов при неизвестных
# b - столбец свободных коэффициентов
#
# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ТЕОРИЯ:
# --- Единичная матрица (E) - матрица, у которой на главной диагонали единицы, а на всех остальных местах нули.
#
# 1 0 0     Пример
# 0 1 0
# 0 0 1
#
# --- Умножение матрицы на её обратную матрицы даёт единичную матрицу: A * A^(-1) = E или A^(-1) * A = E
# --- Чтобы найти определитель матрицы, нужно:
# - Пример для матрицы 2x2:
#
# 1 2
# 3 4
#
# определитель A = delta A = det A = 1*2 - 3*2 = -4
#
# - Пример для матрицы 3x3 (сводится к 2x2):
#
# 1 2 3
# 4 5 6
# 7 8 9
#
# det A = + 1 * (5*9 - 8*6) - 2 * (4*9 - 7*6) + 3 * (4*8-7*5)
#
# Знаки:
#       + - +
#       - + -
#       + - +
#
# --- Вырожденная матрица - матрица, определитель которой равен НУЛЮ. У неё не может быть обратной матрицы.
# --- Алгебраическое дополнение:
#
# 1 2 3
# 4 5 6
# 7 8 9
#       1 * 3
#       4 * 6
#       * * *
#
# Алгебраическое дополнение A32 =
# (-1)^(3+2)  * |1 3|   =   -1 * (6-4*3)    =   6
#               |4 6|
#
# --- Обратная матрица
#
# A =
# 1 2
# 3 4
#
# A^(1) =
#           |A11 * detA      A21 * detA|
#           |A12 * detA      A22 * detA|
#
# --- Решение с выбором главного ведущего
# Среди элементов  a(k)sk,  s=k,k+1,…,m  находят наибольший по модулю,
# который называют  главным  или ведущим  элементом, и перестановкой строк выводят его на главную диагональ,
# после чего выполняют цикл исключения.
# Такая модификация алгоритма называется методом Гаусcа с выбором главного элемента.
#
# --- Величина невязки
# Контроль вычислений можно вести по величине невязки - векторе,
# который получается при вычитании из правой части системы левой, в которую подставлено полученное решение.
#
# --- Ортогона́льная ма́трица
# - это квадратная матрица A с вещественными элементами,
# результат умножения которой на транспонированную матрицу A^T равен единичной матрице[1]:
# или, что эквивалентно, её обратная матрица (которая обязательно существует) равна транспонированной матрице
#
# --- Прямой ход метода Гаусса
# заключается в приведении матрицы системы к треугольному виду
#
# --- Количество операций для решения
# Для решений системы m линейных алгебраических уравнений с m неизвестными требуется порядка M алгебраических операций.
# M равно: 2/3 * m^3
#
# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
INPUT_FILENAME = 'input.csv'
OUTPUT_FILENAME = 'output.csv'


def count(func):
    """декоратор - счётчик"""
    def wrapper(*a, **kw):
        wrapper.count += 1
        return func(*a, **kw)

    wrapper.count = 0
    return wrapper


def read_input_data(filename, matrix):
    """чтение матрицы из файла"""
    with open(filename) as File:
        reader = csv.reader(File, delimiter=',')
        for row_index, row in enumerate(reader):
            matrix.append([])
            for item in row:
                matrix[row_index].append(float(item))
        print('Чтение из файла проведено успешно')


def write_output_matrix(filename, matrix, title=""):
    """запись результатов в файл"""
    with open(filename, mode="a", encoding='utf-8') as FILE:
        file_writer = csv.writer(FILE, delimiter=",", lineterminator="\r")
        file_writer.writerow([title])
        for row in matrix:
            file_writer.writerow(row)
        print(f'\nЗапись в файл проведена успешно ({title})')


def write_output_list(filename, _list, title=""):
    """запись результатов в файл"""
    with open(filename, mode="a", encoding='utf-8') as FILE:
        file_writer = csv.writer(FILE, delimiter=",", lineterminator="\r")
        file_writer.writerow([title])
        file_writer.writerow([_list])
        print(f'\nЗапись в файл проведена успешно ({title})')


def format_print(n, a, b=None, selected=None):
    """вывод системы на экран"""
    for row_ind in range(n):
        print("(", end='')
        for col_ind in range(n):
            selection_label = ("" if selected is None or selected != (row_ind, col_ind) else "<")
            print("\t{1:10.2f}{0}".format(selection_label, a[row_ind][col_ind]), end='')
        if b is not None:
            print("\t) = (\t{1:10.2f})".format(row_ind + 1, b[row_ind]))
        else:
            print("\t)")


def check_discrepancy(a, b, x):
    """проверка на соотвествие (невязка)"""
    print("\nПодсчёт невязки:")
    text_discrepancy = ''
    for row_ind in range(len(b)):
        _sum = 0
        for col_ind in range(len(a[row_ind])):
            _sum += a[row_ind][col_ind] * x[col_ind]
        text_discrepancy += f'Невязка в {row_ind + 1}-й строке = {_sum - b[row_ind]}\n'
        print(f'Невязка в {row_ind + 1}-й строке = {_sum - b[row_ind]}\n')
    return text_discrepancy


@count
def swap_rows(a, b, row1, row2):
    """перемена местами двух строк системы"""
    a[row1], a[row2] = a[row2], a[row1]
    b[row1], b[row2] = b[row2], b[row1]


def divide_row(a, b, changeable_row, divider):
    """деление строки системы на число"""
    a[changeable_row] = [a / divider for a in a[changeable_row]]
    b[changeable_row] /= divider


def combine_rows(a, b, changeable_row, source_row, multiplier):
    """сложение строки системы с другой строкой, умноженной на число"""
    a[changeable_row] = [(a + k * multiplier) for a, k in zip(a[changeable_row], a[source_row])]
    b[changeable_row] += b[source_row] * multiplier


def fill_identity_matrix(max_i, max_j):
    identity_matrix = [[0 for j in range(max_j)] for i in range(max_i)]
    for i in range(0, max_i):
        for j in range(0, max_j):
            if i == j:
                identity_matrix[i][j] = 1
            else:
                identity_matrix[i][j] = 0
    return identity_matrix


def solve_by_gauss(a, b, n):
    """решение системы методом Гаусса (приведением к треугольному виду)"""
    column = 0
    while column < n:
        current_row = None
        for r in range(column, n):
            if current_row is None or abs(a[r][column]) > abs(a[current_row][column]):
                current_row = r
        if current_row is None:
            return None
        if current_row != column:
            swap_rows(a, b, current_row, column)
        try:
            divide_row(a, b, column, a[column][column])
        except ZeroDivisionError:
            raise ZeroDivisionError
        for r in range(column + 1, n):
            combine_rows(a, b, r, column, -a[r][column])
        column += 1
    det = calc_det_triangular_matrix(a)
    if det == 0:
        return None
    else:
        x = [0 for _ in b]
        for i in range(n - 1, -1, -1):
            x[i] = b[i] - sum(x * a for x, a in zip(x[(i + 1):], a[i][(i + 1):]))  # zip создает итератор кортежей
        return x


def transpose_matrix(a, n):
    """транспонировать матрицу"""
    transposed_matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            transposed_matrix[j][i] = a[i][j]
    return transposed_matrix


def get_inverse_matrix(a, n):
    """получить обратную матрицу"""
    inverse_matrix = []  # обартная матрица
    identity_row = [0 for j in range(n)]  # столбец свободных слагаемых
    for i in range(n):
        for j in range(n):
            if i == j:
                identity_row[j] = 1
            else:
                identity_row[j] = 0
        inverse_matrix_col = solve_by_gauss(a.copy(), identity_row, n)
        inverse_matrix.append(inverse_matrix_col)

    return transpose_matrix(inverse_matrix, n)


def detailed_solve_by_gauss(a, b, n):
    """решение системы методом Гаусса (приведением к треугольному виду)"""
    column = 0
    unchanged_a = a.copy()
    unchanged_b = b.copy()

    while column < n:
        print("Ищем максимальный по модулю элемент в {0}-м столбце:".format(column + 1))
        current_row = None
        for r in range(column, n):
            if current_row is None or abs(a[r][column]) > abs(a[current_row][column]):
                current_row = r
        if current_row is None:
            print("решений нет")
            return None
        format_print(n, a, b, (current_row, column))
        if current_row != column:
            print("Переставляем строку с найденным элементом повыше:")
            swap_rows(a, b, current_row, column)
            format_print(n, a, b, (column, column))
        print(f"Нормализуем строку с найденным элементом (делим на {a[column][column]}):")
        try:
            divide_row(a, b, column, a[column][column])
        except ZeroDivisionError:
            raise ZeroDivisionError
        format_print(n, a, b, (column, column))
        print("Обрабатываем нижележащие строки:")
        for r in range(column + 1, n):
            combine_rows(a, b, r, column, -a[r][column])
        format_print(n, a, b, (column, column))
        column += 1
    print("Матрица приведена к треугольному виду, находим определитель")
    det = calc_det_triangular_matrix(a)
    if det == 0:
        print('Определитель равен нулю => матрица вырожденная')
        return None
    else:
        print("Определитель равен {0} => матрица невырожденная, считаем решение".format(det))
        x = [0 for _ in b]
        for i in range(n - 1, -1, -1):
            x[i] = b[i] - sum(x * a for x, a in zip(x[(i + 1):], a[i][(i + 1):]))  # zip создает итератор кортежей
        print("\nПолучили ответ:")
        print("\n".join("X{0} =\t{1:10.2f}".format(i + 1, x) for i, x in enumerate(x)))

        list_discrepancy = check_discrepancy(unchanged_a, unchanged_b, x)
        write_output_list(OUTPUT_FILENAME, list_discrepancy, 'Невязка')
        inverse_matrix = get_inverse_matrix(unchanged_a, n)

        print("\nОбратная матрица:")
        format_print(n, inverse_matrix)
        write_output_matrix(OUTPUT_FILENAME, inverse_matrix, 'Обратная матрица')
        return x


def calc_det_triangular_matrix(matrix):
    swap_number = swap_rows.count
    det = (1 if swap_number % 2 == 0 else -1)
    for i in range(len(matrix)):
        det *= matrix[i][i]
    return det


def main():
    swap_number = 0
    expanded_matrix = list()
    with open(OUTPUT_FILENAME, mode="w", encoding='utf-8'):
        pass
    try:
        read_input_data(INPUT_FILENAME, expanded_matrix)
    except Exception:
        print("Ошибка при чтении файла")
        return

    free_factors = []
    for _row in expanded_matrix:
        free_factors.append(_row.pop())
    factors_at_unknowns = expanded_matrix
    n = len(factors_at_unknowns)
    print("\nИсходная система:")
    format_print(n, factors_at_unknowns, free_factors, None)
    print("\nРешаем:")

    try:
        detailed_solve_by_gauss(factors_at_unknowns, free_factors, n)
    except ZeroDivisionError:
        print("Определитель равен нулю!")

    try:
        write_output_matrix(OUTPUT_FILENAME, expanded_matrix, 'Расширенная матрица')
    except Exception:
        print("Ошибка при записи в файл")
        return


if __name__ == '__main__':
    main()
