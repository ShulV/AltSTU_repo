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

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
INPUT_FILENAME = 'input.csv'
OUTPUT_FILENAME = 'output.csv'


def read_input_data(filename, matrix):
    """Чтение матрицы из файла"""
    with open(filename) as File:
        reader = csv.reader(File, delimiter=',')
        for row_index, row in enumerate(reader):
            matrix.append([])
            for item in row:
                matrix[row_index].append(float(item))
        print('Чтение из файла проведено успешно')


def write_output_data(filename, matrix):
    """Запись результатов в файл"""
    with open(filename, mode="w", encoding='utf-8') as FILE:
        file_writer = csv.writer(FILE, delimiter=",", lineterminator="\r")
        for row in matrix:
            file_writer.writerow(row)
        print('Запись в файл проведена успешно')


def format_print(a, b, selected=None):
    """вывод системы на экран"""
    for row_ind in range(len(b)):
        print("(", end='')
        for col_ind in range(len(a[row_ind])):
            selection_label = ("" if selected is None or selected != (row_ind, col_ind) else "<")
            print("\t{1:10.2f}{0}".format(selection_label, a[row_ind][col_ind]), end='')
        print("\t) = (\t{1:10.2f})".format(row_ind + 1, b[row_ind]))


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


def solve_by_gauss(a, b):
    """решение системы методом Гаусса (приведением к треугольному виду)"""
    column = 0
    while column < len(b):
        print("Ищем максимальный по модулю элемент в {0}-м столбце:".format(column + 1))
        current_row = None
        for r in range(column, len(a)):
            if current_row is None or abs(a[r][column]) > abs(a[current_row][column]):
                current_row = r
        if current_row is None:
            print("решений нет")
            return None
        format_print(a, b, (current_row, column))
        if current_row != column:
            print("Переставляем строку с найденным элементом повыше:")
            swap_rows(a, b, current_row, column)
            format_print(a, b, (column, column))
        print("Нормализуем строку с найденным элементом:")
        divide_row(a, b, column, a[column][column])
        format_print(a, b, (column, column))
        print("Обрабатываем нижележащие строки:")
        for r in range(column + 1, len(a)):
            combine_rows(a, b, r, column, -a[r][column])
        format_print(a, b, (column, column))
        column += 1
    print("Матрица приведена к треугольному виду, считаем решение")
    x = [0 for _ in b]
    for i in range(len(b) - 1, -1, -1):
        x[i] = b[i] - sum(x * a for x, a in zip(x[(i + 1):], a[i][(i + 1):]))
    print("Получили ответ:")
    print("\n".join("X{0} =\t{1:10.2f}".format(i + 1, x) for i, x in enumerate(x)))
    return x
# --- end of решение системы методом Гаусса (приведением к треугольному виду)


def main():
    expanded_matrix = list()
    try:
        read_input_data(INPUT_FILENAME, expanded_matrix)
    except Exception:
        print('Ошибка при чтении файла')
        return
    
    free_factors = []
    for _row in expanded_matrix:
        free_factors.append(_row.pop())
    factors_at_unknowns = expanded_matrix

    print("Исходная система:")
    format_print(factors_at_unknowns, free_factors, None)
    print("Решаем:")
    solve_by_gauss(factors_at_unknowns, free_factors)
    try:
        write_output_data(OUTPUT_FILENAME, expanded_matrix)
    except Exception:
        print('Ошибка при записи в файл')
        return


if __name__ == '__main__':
    main()
