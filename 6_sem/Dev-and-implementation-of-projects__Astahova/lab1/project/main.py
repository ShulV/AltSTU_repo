import csv


class Graph:

    def __init__(self, file_in):
        self.fictive_start_top = -100  # шифр фиктивной стартовой вершины
        self.fictive_end_top = -101  # шифр фиктивной конечной вершины
        self.graph_table = {'arc_start': [],
                            'arc_end': [],
                            'weight': [],
                            'is_visited': [],
                            'layer': [], }  # таблица, содержащая дуги и веса графа
        self.struct_graph_table = {'arc_start': [],
                                   'arc_end': [],
                                   'weight': [],
                                   'is_visited': [], }  # упоряденная таблица, содержащая дуги и веса графа
        self.first_top = None  # первая вершина графа
        self.last_top = None  # последняя вершина графа
        self.ways_num = 0  # количество путей (работ) графа
        self.struct_graph_ways_num = 0  # количество путей (работ) упорядоченного графа
        self.current_way = []  # текущий путь для вывода всех полных путей
        with open(file_in) as File:
            reader = csv.reader(File, delimiter=';')
            for row in reader:
                self.add_row_in_graph_table(int(row[0]), int(row[1]), int(row[2]))
            print('Чтение из файла проведено успешно')

    def add_row_in_graph_table(self, start, end, weight, is_visited=False, adding_is_in_sort=False):
        if adding_is_in_sort:
            self.struct_graph_table['arc_start'].append(start)
            self.struct_graph_table['arc_end'].append(end)
            self.struct_graph_table['weight'].append(weight)
            self.struct_graph_table['is_visited'].append(is_visited)
            self.struct_graph_ways_num += 1
        else:
            self.graph_table['arc_start'].append(start)
            self.graph_table['arc_end'].append(end)
            self.graph_table['weight'].append(weight)
            self.graph_table['is_visited'].append(is_visited)
            self.ways_num += 1

    def copy_row_to_struct_graph_table(self, index):
        start = self.graph_table['arc_start'][index]
        end = self.graph_table['arc_end'][index]
        weight = self.graph_table['weight'][index]
        is_visited = self.graph_table['is_visited'][index]
        self.add_row_in_graph_table(start, end, weight, is_visited, adding_is_in_sort=True)

    def delete_row_from_graph_table(self, index):
        self.graph_table['arc_start'].pop(index)
        self.graph_table['arc_end'].pop(index)
        self.graph_table['weight'].pop(index)
        self.graph_table['is_visited'].pop(index)
        self.ways_num -= 1

    def print_graph(self, sorted_graph=False):
        """ печать таблицы |A|B|time|"""
        print('_' * 100)
        print('Вывод таблицы путей графа')
        print('|{start:^10}|{end:^10}|{weight:^10}|'.format(start='--A--', end='--B--', weight='--Вес--'))
        for row_index in range(0, self.ways_num):
            self.print_row(row_index, sorted_graph)
        print(f'Первая вершина: {self.first_top}')
        print(f'Последняя вершина: {self.last_top}')
        print('_' * 100)

    def print_row(self, row_index, sorted_graph=False):
        if sorted_graph:
            print('|{start:^10}|{end:^10}|{weight:^10}|'.format(
                start=self.struct_graph_table['arc_start'][row_index],
                end=self.struct_graph_table['arc_end'][row_index],
                weight=self.struct_graph_table['weight'][row_index]))
        else:
            print('|{start:^10}|{end:^10}|{weight:^10}|'.format(
                start=self.graph_table['arc_start'][row_index],
                end=self.graph_table['arc_end'][row_index],
                weight=self.graph_table['weight'][row_index]))

    def search_first_top(self):
        """ поиск первой вершины графа """
        print('нахождение первой вершины')
        for i in range(0, self.ways_num):  # итерация 1 по таблице
            is_start_top = True
            for j in range(0, self.ways_num):  # итерация 2 по таблице для поиска первой вершины
                # условие, что в вершину входит дуга (кроме петель), если входит, то это не стартовая вершина
                if (self.graph_table['arc_start'][i] == self.graph_table['arc_end'][j] and
                        self.graph_table['arc_start'][i] != self.graph_table['arc_start'][j]):
                    is_start_top = False
                    break

            # если это непосещенная первая вершина
            if is_start_top and not self.graph_table['is_visited'][i]:
                # если это первая первая вершина (не изменялась после инициализации)
                if self.first_top is None:
                    self.first_top = self.graph_table['arc_start'][i]
                else:
                    print('создание фиктивной первой вершины')
                    self.add_row_in_graph_table(self.fictive_start_top, self.first_top, 0)
                    self.add_row_in_graph_table(self.fictive_start_top, self.graph_table['arc_start'][i], 0)
                    if self.first_top != self.fictive_start_top:
                        self.first_top = self.fictive_start_top

                for index in range(0, self.ways_num):
                    if self.graph_table['arc_start'][index] == self.graph_table['arc_start'][i]:
                        self.graph_table['is_visited'][index] = True

    def delete_top_loops(self, index):
        """ удаление петель """
        start_top = self.graph_table['arc_start'][index]
        end_top = self.graph_table['arc_end'][index]
        if start_top == end_top:
            print(f'найдена петля ({start_top}, {end_top})! автоматическое удаление работы')
            self.delete_row_from_graph_table(index)
            return 0
        return index

    def check_duplication(self, i, j):
        """ проверка дубликатов работ """
        start_work = self.graph_table['arc_start'][i]
        starts_are_equal = start_work == self.graph_table['arc_start'][j]
        end_work = self.graph_table['arc_end'][i]
        ends_are_equal = end_work == self.graph_table['arc_end'][j]
        # если есть дубликаты
        if starts_are_equal and ends_are_equal and i != j:
            print(f'ошибка! работа ({start_work}, {end_work}) дублируется')
            # если веса разные
            if self.graph_table['weight'][i] != self.graph_table['weight'][j]:
                weight_i = self.graph_table['weight'][i]
                weight_j = self.graph_table['weight'][j]
                print(f'работа имеет 2 веса: {weight_i} и {weight_j}')
                choice = input('Введите нужный вариант (1 или 2):')
                if choice == '1':
                    self.delete_row_from_graph_table(i)
                    self.optimize_graph()
                    return None
                else:
                    self.delete_row_from_graph_table(j)
                    return 0
            # если веса одинаковые
            else:
                print(f'работа имеет одинаковый вес {self.graph_table["weight"][i]}; автоматическое удаление')
                self.delete_row_from_graph_table(j)
                return 0

    def search_last_top(self):
        """ поиск последней вершины графа """
        print('нахождение последней вершины')
        for i in range(0, self.ways_num):  # итерация 1 по таблице
            is_last_top = True
            for j in range(0, self.ways_num):  # итерация 2 по таблице для поиска последней вершины
                # условие, что из вершины выходит дуга (кроме петель), если выходит, то это не последняя вершина
                if (self.graph_table['arc_end'][i] == self.graph_table['arc_start'][j] and
                        self.graph_table['arc_end'][i] != self.graph_table['arc_end'][j]):
                    is_last_top = False
                    break

            # если это непосещенная последняя вершина
            if is_last_top and not self.graph_table['is_visited'][i]:
                # если это первая последняя вершина (не изменялась после инициализации)
                if self.last_top is None:
                    self.last_top = self.graph_table['arc_end'][i]
                    # отметка всех работ с таким шифром как посещенные
                    for k in range(0, self.ways_num):
                        if self.graph_table['arc_end'][k] == self.graph_table['arc_end'][i]:
                            self.graph_table['is_visited'][k] = True
                else:
                    # если это не одна и та же вершина
                    if self.last_top != self.graph_table['arc_end'][i]:
                        print(f'вершины графа {self.last_top} и {self.graph_table["arc_end"][i]} конечные')
                        choice = input('Ввести фиктивную конечную вершину (иначе удалить) (1-да, 2-нет): ')
                        if choice == '1':
                            print('создание фиктвной последней вершины')
                            self.add_row_in_graph_table(self.last_top, self.fictive_end_top, 0)
                            self.add_row_in_graph_table(self.graph_table['arc_end'][i], self.fictive_end_top, 0)
                            if self.last_top != self.fictive_end_top:
                                self.last_top = self.fictive_end_top

                            for index in range(0, self.ways_num):
                                if self.graph_table['arc_end'][index] == self.graph_table['arc_end'][i]:
                                    self.graph_table['is_visited'][index] = True
                        # удаление одной из вершин
                        else:
                            print(f'удаление вершины {self.graph_table["arc_end"][i]}')
                            self.delete_row_from_graph_table(i)
                            self.last_top = None
                            for index in range(0, self.ways_num):
                                self.graph_table['is_visited'][index] = False
                            self.search_last_top()
                            break

    # def get_first_top_index(self):
    #     for index in range(0, self.ways_num):
    #         if self.first_top == self.graph_table['arc_start'][index]:
    #             return index

    def optimize_graph(self):
        """ оптимизация графа (удаление петель, одинаковых работ, поиск последней вершины"""
        print('оптимизация:')
        i = 0
        while i < self.ways_num:
            # one
            i = self.delete_top_loops(i)
            # two
            j = 0
            while j < self.ways_num:  # сравнение всех вершин СГ
                temp = self.check_duplication(i, j)
                # None при запуске optimize_graph рекурсивно из check_duplication(i, j). Иначе обнуляется счётчик цикла.
                if temp is not None:
                    j = temp
                j += 1
            i += 1
        self.print_graph()
        self.search_last_top()
        for index in range(0, self.ways_num):
            self.graph_table['is_visited'][index] = False

    # def find_layers(self):
    #     """ нахождение слоев для каждой вершины """
    #     # найдем индекс первой вершины
    #     first_top_index = 0
    #     for i in range(0, self.ways_num):
    #         if [self.first_top] ==  self.graph_table['arc_start'][i]:
    #             first_top_index = i
    #     # присвоим первой вершине слой
    #     layer_level = 0
    #     self.graph_table['layer'][first_top_index] = layer_level
    #     # создадим очередь вершин и поместим туда первую вершину
    #     top_queue = [self.graph_table['layer'][first_top_index]]
    #     # найдем все вершины второго слоя
    #     layer_set = set()
    #     for i in range(0, self.ways_num):
    #         if self.graph_table['arc_start'][i] == top_queue[len(top_queue) - 1]:
    #             # поиск конечной вершины работы и проверка, имеет ли она входящие в неё работы,
    #             # находящиеся не в текущем слое
    #             has_prev_tops = False
    #             for k in range(0, self.ways_num):
    #                 if self.graph_table['arc_start'][k] == self.graph_table['arc_end'][i]:
    #                     is_last = False
    #             layer_set.add(self.graph_table['arc_end'][i])

    def find_layer(self, layer_level, top_queue):
        # отметка слоев этого уровня и нахождение слоев следующего уровня
        self.find_layer(layer_level + 1, top_queue)

    def struct_graph(self):
        print('упорядочивание графа')
        vertex_queue = [self.first_top]
        while self.ways_num != self.struct_graph_ways_num:
            for i in range(0, self.ways_num):
                if vertex_queue[0] == self.graph_table['arc_start'][i] and not self.graph_table['is_visited'][i]:
                    self.copy_row_to_struct_graph_table(i)
                    vertex_queue.append(self.graph_table['arc_end'][i])
                    self.graph_table['is_visited'][i] = True

            vertex_queue.pop(0)

    def search_full_ways(self):
        """ нахождение всех полных путей графа """
        self.current_way = [self.first_top]
        print('полные пути графа:')
        for i in range(0, self.ways_num):
            if self.graph_table['arc_start'][i] == self.first_top:
                self.current_way.append(self.graph_table['arc_end'][i])  # запомнить следуюущую вершину в списке путей
                self.recursive_search()

    def recursive_search(self):
        """ рекурсивный обход графа """
        if self.current_way[len(self.current_way) - 1] == self.last_top:
            for i in range(0, len(self.current_way)):
                print(f'{self.current_way[i]} ', end='')
            print()
            self.current_way.pop()  # удаление последней вершины, возврат по стеку
            return

        for i in range(0, self.ways_num):
            if self.graph_table['arc_start'][i] == self.current_way[len(self.current_way) - 1]:
                self.current_way.append(self.graph_table['arc_end'][i])  # запомнить вершину
                self.recursive_search()
        self.current_way.pop()  # удаление последней вершины
        return


if __name__ == "__main__":
    in_file = "input.csv"
    graph = Graph(in_file)
    graph.print_graph()
    graph.search_first_top()
    graph.optimize_graph()
    graph.print_graph()
    graph.struct_graph()
    graph.print_graph(sorted_graph=True)
    graph.search_full_ways()
