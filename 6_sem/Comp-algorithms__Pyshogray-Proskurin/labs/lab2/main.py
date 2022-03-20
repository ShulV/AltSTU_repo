import csv

# ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
INPUT_FILENAME = 'input.csv'
OUTPUT_FILENAME = 'output.csv'


# def count(func):
#     """декоратор - счётчик"""
#
#     def wrapper(*a, **kw):
#         wrapper.count += 1
#         return func(*a, **kw)
#
#     wrapper.count = 0
#     return wrapper


def read_input_data(filename, expended_matrix):
    """ чтение расширенной матрицы из файла """
    with open(filename) as File:
        reader = csv.reader(File, delimiter=';')
        for row_index, row in enumerate(reader):
            expended_matrix.append([])
            for item in row:
                expended_matrix[row_index].append(float(item))
        print('Чтение из файла проведено успешно')


def write_output_matrix(filename, matrix, title=""):
    """ запись результатов в файл """

    # TODO сделать запись расишернной, записывается без столбца свободных членов
    with open(filename, mode="a", encoding='utf-8') as FILE:
        file_writer = csv.writer(FILE, delimiter=",", lineterminator="\r")
        file_writer.writerow([title])
        for row in matrix:
            file_writer.writerow(row)
        print(f'\nЗапись в файл проведена успешно ({title})')


def write_output_list(filename, _list, title=""):
    """ запись результатов в файл """

    with open(filename, mode="a", encoding='utf-8') as FILE:
        file_writer = csv.writer(FILE, delimiter=",", lineterminator="\r")
        file_writer.writerow([title])
        file_writer.writerow([_list])
        print(f'\nЗапись в файл проведена успешно ({title})')


def format_print(n, a, b=None, selected=None):
    """ вывод системы на экран """

    for row_ind in range(n):
        print("(", end='')
        for col_ind in range(n):
            selection_label = ("" if selected is None or selected != (row_ind, col_ind) else "<")
            print("\t{1:10.2f}{0}".format(selection_label, a[row_ind][col_ind]), end='')
        if b is not None:
            print("\t) = (\t{1:10.2f})".format(row_ind + 1, b[row_ind]))
        else:
            print("\t)")


def check_diagonal_dominance(factors_at_unknowns):
    """ проверка матрицы на диагональное преобладание """

    print('\nПРОВЕРКА МАТРИЦЫ НА ДИАГОНАЛЬНОЕ ПРЕОБЛАДАНИЕ')
    cols = len(factors_at_unknowns[0])
    rows = len(factors_at_unknowns)
    is_diagonal_dominant = True
    for i in range(rows):
        row_off_diagonal_sum = 0
        for j in range(cols):
            if i != j:
                row_off_diagonal_sum += abs(factors_at_unknowns[i][j])
        diagonal_elem = abs(factors_at_unknowns[i][i])
        print(
            f'Диаг. элемент {i}-й строки = {factors_at_unknowns[i][i]}; сумма недиаг. элементов строки = {row_off_diagonal_sum}')
        if diagonal_elem > row_off_diagonal_sum:
            print('В строке выполняется диагональное преобладание')
        else:
            is_diagonal_dominant = False
            print('В строке не выполняется диагональное преобладание')
    if is_diagonal_dominant:
        print('В матрице выполняется диагональное преобладание')
    else:
        print('В матрице не выполняется диагональное преобладание')
    return is_diagonal_dominant


def count_null_x(b, diagonal_a):
    """ посчет x для нулевого приближения
    b - свободный член строки,
    diagonal_a - свободный член диагонального элемента строки """

    return b / diagonal_a


def get_null_x_list(factors_at_unknowns, free_factors):
    """ подсчет всех x для нулевого приближения и их возврат
    factors_at_unknowns - двумерных массив членов при неизвестных
    free_factors - столбец свободных членов """

    print('\nПОДСЧЕТ ВСЕХ X ДЛЯ НУЛЕВОГО ПРИБЛИЖЕНИЯ (k=0)')
    null_x_list = []
    for i in range(len(free_factors)):
        null_x = count_null_x(free_factors[i], factors_at_unknowns[i][i])
        null_x_list.append(null_x)

    for i in range(len(null_x_list)):
        print(f'x{i + 1} (k=0) = {null_x_list[i]}')

    return null_x_list


def func_x(b, a_array, diagonal_x_index):
    """ динамическое создание функции для подсчёта x (для строки)
    b - свободный член строки,
    a_array - массив свободных членов строки,
    diagonal_x_index - индекс подсчитываемого x (этот элем. на главной диагонали) """

    def created_func_x(x_array, k):
        """ формула подсчета x с предустановленными свободными членами """
        print(f'подсчёт x{diagonal_x_index + 1} (k={k})')
        a_array_len = len(a_array)
        x = b
        for i in range(0, a_array_len):
            if i != diagonal_x_index:
                x -= a_array[i] * x_array[i]  # вычитаем все a[i]*x[i], кроме диагонального
                # print(f'минус {a_array[i] * x_array[i]}')
        x /= a_array[diagonal_x_index]  # делим на коэф. a текущего x
        # print(f'делим на {a_array[diagonal_x_index]}')
        return x

    return created_func_x


def create_x_functions(factors_at_unknowns, free_factors):
    """ динамическое создание формул (функций) для подсчёта x (для строки)
    factors_at_unknowns - двумерных массив членов при неизвестных
    free_factors - столбец свободных членов """

    print('\nДИНАМИЧЕСКОЕ СОЗДАНИЕ ФОРМУЛ (ФУНКЦИЙ) ДЛЯ ПОДСЧЁТА X (ДЛЯ КАЖДОЙ СТРОКИ)')
    x_counting_functions = []
    rows = len(free_factors)
    for i in range(rows):
        x_counting_func = func_x(free_factors[i], factors_at_unknowns[i], i)
        x_counting_functions.append(x_counting_func)
    return x_counting_functions


def count_x_error(x_prev, x):
    """ подсчитывает погрешность для x
    |x (k) - x (k-1)|/ |x (k)| """
    return abs(x - x_prev) / abs(x)


def check_accuracy_is_done(epsilon, errors):
    """ проверка выполнения всеми x заданной погрешности,
    если все погрешности меньше, чем заданная - True, иначе - False """
    for i in range(len(errors)):
        if epsilon < errors[i]:
            print('проверка достижений погрешности: требуемая погрешность пока не достигнута')
            return False
        print('проверка достижений погрешности: требуемая погрешность достигнута')
        return True


def format_print_x_and_errors(x_lists, x_errors):
    """ вывод таблицы вида | k | x1 x2 ... xn | e1 e2 ... en |"""
    print('\nВЫВОД X-ОВ И ИХ ПОГРЕШНОСТЕЙ')
    print("|{0:^4}".format('k'), end='')
    for i in range(len(x_lists[0])):
        print('|{0:^8}'.format(f'x{i + 1}'), end='')
    for i in range(len(x_lists[0])):
        print('|{0:^8}'.format(f'e{i + 1}'), end='')
    print('|')
    for k in range(len(x_lists)):
        print("|{0:^4}".format(k), end='')
        for i in range(len(x_lists[0])):
            print('|{0:^8.4f}'.format(x_lists[k][i]), end='')
        for i in range(len(x_lists[0])):
            if k == 0:
                print('|{0:^8}'.format(x_errors[k][i]), end='')
            else:
                print('|{0:^8.4f}'.format(x_errors[k][i]), end='')
        print('|')


def solve_by_yacobi(factors_at_unknowns, free_factors, x_lists, x_errors, epsilon):
    """ решение системы методом Якоби
    factors_at_unknowns - двумерных массив членов при неизвестных
    free_factors - столбец свободных членов
    x_lists - таблица x-ов по всем приближениям
    x_errors - таблица погрешностей (по x-ам) для всех приближений
    epsilon - величина допустимой погрешности """
    print('\nРЕШЕНИЕ СИСТЕМЫ МЕТОДОМ ЯКОБИ')
    cols = len(factors_at_unknowns[0])
    rows = len(factors_at_unknowns)

    null_x_list = get_null_x_list(factors_at_unknowns, free_factors)  # подсчет всех x для нулевого приближения
    x_lists.append(null_x_list)  # добавление x-ов (0-го приближения) в таблицу x-ов всех приближений
    empty_error_list = ["-" for _ in range(cols)]  # пустая строка для первой строки таблицы погрешностей
    x_errors.append(empty_error_list)  # добавление пустой строки в таблицу погрешностей
    x_counting_functions = create_x_functions(factors_at_unknowns, free_factors)  # создание формул для подсчёта x-ов

    # цикл по приближениям (k)
    accuracy_is_done = False
    k = 0
    while accuracy_is_done is not True:
        # счетчик номера приближения
        k += 1
        print(f'\nПОДСЧЕТ X И ПОГРЕШНОСТЕЙ ДЛЯ {k}-ОГО ПРИБЛИЖЕНИЯ')
        # подсчёт x-ов и их погрешностей
        cur_x_list = []
        cur_x_error_list = []
        for i in range(rows):
            x = x_counting_functions[i](x_lists[k - 1], k)
            cur_x_list.append(x)
            x_prev = x_lists[k - 1][i]  # соотвествующий предыдущий x (k-1)
            x_error = count_x_error(x_prev, x)
            cur_x_error_list.append(x_error)
        x_lists.append(cur_x_list)
        x_errors.append(cur_x_error_list)
        print(f'k: {k};\nx: {cur_x_list};\nпогрешности: {cur_x_error_list}')
        # проверка достижения требуемой погрешности
        accuracy_is_done = check_accuracy_is_done(epsilon, cur_x_error_list)


def check_discrepancy(a, b, x):
    """проверка на соотвествие (невязка) """
    print("\nПодсчёт невязки:")
    text_discrepancy = ''
    for row_ind in range(len(b)):
        _sum = 0
        for col_ind in range(len(a[row_ind])):
            _sum += a[row_ind][col_ind] * x[col_ind]
        text_discrepancy += f'Невязка в {row_ind + 1}-й строке = {_sum - b[row_ind]}\n'
        print(f'Невязка в {row_ind + 1}-й строке = {_sum - b[row_ind]}\n')
    return text_discrepancy


def main():
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
    check_diagonal_dominance(factors_at_unknowns)
    x_lists = []
    x_errors = []
    epsilon = 0.01
    solve_by_yacobi(factors_at_unknowns, free_factors, x_lists, x_errors, epsilon)
    format_print_x_and_errors(x_lists, x_errors)

    try:
        write_output_matrix(OUTPUT_FILENAME, expanded_matrix, 'Расширенная матрица')
    except Exception:
        print("Ошибка при записи в файл")
        return


if __name__ == '__main__':
    main()
