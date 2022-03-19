import csv


class Graph:

    def __init__(self, file_in):
        self.fictive_start_top = -100  # шифр фиктивной стартовой вершины
        self.fictive_end_top = -101  # шифр фиктивной конечной вершины
        self.graph_table = {'arc_start': [],
                            'arc_end': [],
                            'weight': [],
                            'is_visited': [],
                            # 'layer': [],
                            }  # таблица, содержащая дуги и веса графа
        self.struct_graph_table = {'arc_start': [],
                                   'arc_end': [],
                                   'weight': [],
                                   'is_visited': [], }  # упоряденная таблица, содержащая дуги и веса графа
        # таблица, содержащая шифр события, его ранний срок, поздний срок и резервное время
        # количество входящих и выходящих из события работ
        self.graph_events = {'event': [],
                             'early_term': [],
                             'late_term': [],
                             'reserve_time': [],
                             # 'in_works_num': [],
                             # 'out_works_num': [],
                             'in_works': [],
                             'out_works': [],
                             'layer': [],
                             }
        self.first_top = None  # первая вершина графа
        self.last_top = None  # последняя вершина графа
        self.works_num = 0  # количество работ графа
        self.struct_graph_works_num = 0  # количество работ упорядоченного графа
        self.current_way = []  # текущий путь для вывода всех полных путей
        with open(file_in) as File:
            reader = csv.reader(File, delimiter=';')
            for row in reader:
                self.add_row_in_graph_table(int(row[0]), int(row[1]), int(row[2]))
            print('Чтение из файла проведено успешно')

    def append_new_event_in_events_graph(self, event):
        """ добавлние новой вершины в graph_events, инит параметров нулями """
        self.graph_events['event'].append(event)
        self.graph_events['in_works'].append(list())
        self.graph_events['out_works'].append(list())
        self.graph_events['layer'].append(None)
        self.graph_events['early_term'].append(None)
        self.graph_events['late_term'].append(None)
        self.graph_events['reserve_time'].append(None)

    def swap_events(self, i, j):
        """ поменять местами строки """
        # шифр события
        buff = self.graph_events['event'][i]
        self.graph_events['event'][i] = self.graph_events['event'][j]
        self.graph_events['event'][j] = buff
        # входящие работы
        buff = self.graph_events['in_works'][i]
        self.graph_events['in_works'][i] = self.graph_events['in_works'][j]
        self.graph_events['in_works'][j] = buff
        # выходящие работы
        buff = self.graph_events['out_works'][i]
        self.graph_events['out_works'][i] = self.graph_events['out_works'][j]
        self.graph_events['out_works'][j] = buff
        # слои
        buff = self.graph_events['layer'][i]
        self.graph_events['layer'][i] = self.graph_events['layer'][j]
        self.graph_events['layer'][j] = buff
        # ранний срок
        buff = self.graph_events['early_term'][i]
        self.graph_events['early_term'][i] = self.graph_events['early_term'][j]
        self.graph_events['early_term'][j] = buff
        # поздний срок
        buff = self.graph_events['late_term'][i]
        self.graph_events['late_term'][i] = self.graph_events['late_term'][j]
        self.graph_events['late_term'][j] = buff
        # резерв времени
        buff = self.graph_events['reserve_time'][i]
        self.graph_events['reserve_time'][i] = self.graph_events['reserve_time'][j]
        self.graph_events['reserve_time'][j] = buff

    def sort_events_by_layers(self):
        """ сортировка событий по слоям по возрастанию """
        print('Сортировка по слоям')
        n = len(self.graph_events['event'])
        for i in range(n - 1):
            for j in range(n - i - 1):
                # print(
                #     f'i={i} layer[i]={self.graph_events["layer"][i]}; j={j} layer[j]={self.graph_events["layer"][j]}; ')
                if self.graph_events['layer'][j] > self.graph_events['layer'][j+1]:

                    self.swap_events(j, j + 1)

    def find_early_term_for_event(self, event):
        """ нахождение раннего срока события """
        event_index = self.find_index_by_event(event)
        # если событие начальное, ранний срок = 0
        if event == self.first_top:
            self.graph_events['early_term'][event_index] = 0
            return

        # нахождение максимального веса из работах связанных с предыдущими событиями
        max_early_term = 0
        prev_event_early_term = 0
        max_weight = 0
        tmp_event_early_term = 0
        for i in range(0, self.struct_graph_works_num):
            if event == self.struct_graph_table['arc_end'][i]:
                max_weight = self.struct_graph_table['weight'][i]
                prev_event = self.struct_graph_table['arc_start'][i]
                prev_event_index = self.find_index_by_event(prev_event)
                prev_event_early_term = self.graph_events['early_term'][prev_event_index]
                tmp_event_early_term = prev_event_early_term + max_weight
            if max_early_term < tmp_event_early_term:
                max_early_term = tmp_event_early_term

        # ранний срок текущего события = ранний срок предыдущего + макс. вес между текущей и предыдущими вершинами
        print(f'\nнахождение для event {self.graph_events["event"][event_index]}')
        print(f'prev_event_early_term {prev_event_early_term}')
        print(f'max_weight {max_weight}')
        self.graph_events['early_term'][event_index] = max_early_term

    def find_early_term_for_all_event(self):
        """ нахождение раннего срока всех событий """
        print('Нахождение ранних сроков у событий')
        for event in self.graph_events['event']:
            self.find_early_term_for_event(event)

    def find_index_by_event(self, event):
        """ нахождение номера (индекса) события в структуре по его шифру """
        events_len = len(self.graph_events['event'])
        for i in range(events_len):
            if self.graph_events['event'][i] == event:
                return i
        return None

    def check_vertex_includes_only_prev_layers_vertices(self, index):
        """ проверить, что в вершину входят только вершины предыдущих слоев """
        ins_len = len(self.graph_events['in_works'][index])

        for i in range(ins_len):
            if self.graph_events['layer'][i] is None:
                return False
        return True

    def find_vertex_layers(self, vertex_index, layer=0):
        """ находим слой каждой вершины """
        # если нет входящих работ - слой 0
        if not self.graph_events['in_works'][vertex_index]:
            self.graph_events['layer'][vertex_index] = 0  # ноль
            outs_len = len(self.graph_events['out_works'][vertex_index])  # количество выходящих вершин
            # print(f'Кол-во выходящих вершин: {outs_len} у вершины {self.graph_events["event"][vertex_index]}')
            # print('Их шифры/индексы:')
            for i in range(outs_len):
                out_event = self.graph_events['out_works'][vertex_index][i]  # шифр события, выходящего из текущ. соб.
                out_event_index = self.find_index_by_event(out_event)  # индекс события, выходящего из текущ. события
                # print(f'{out_event}/{out_event_index}')
                self.find_vertex_layers(out_event_index, layer + 1)
            return

        # проверяем все выходящие события текущего события на то, что они находятся в уже пройденных слоях
        # если это так, то уже можно работать с текущей вершиной (flag = True),
        # если нет (flag = False), то мы до её слоя ещё не дошли
        flag = self.check_vertex_includes_only_prev_layers_vertices(vertex_index)
        if flag:
            self.graph_events['layer'][vertex_index] = layer
            outs_len = len(self.graph_events['out_works'][vertex_index])  # количество выходящих вершин
            # print(f'Кол-во выходящих вершин: {outs_len} у вершины {self.graph_events["event"][vertex_index]}')
            # print('Их шифры/индексы:')
            for i in range(outs_len):
                out_event = self.graph_events['out_works'][vertex_index][i]  # шифр события, выходящего из текущ. соб.
                out_event_index = self.find_index_by_event(out_event)  # индекс события, выходящего из текущ. события
                # print(f'{out_event}/{out_event_index}')
                self.find_vertex_layers(out_event_index, layer + 1)

    def count_ins_and_outs(self):
        """ считаем количество входящих и исходящих работ у вершин """
        vertices_num = len(self.graph_events['event'])
        for i in range(0, vertices_num):
            for j in range(0, self.works_num):
                # находим и добавляем структуру входящие вершины
                if self.struct_graph_table['arc_end'][j] == self.graph_events['event'][i]:
                    self.graph_events['in_works'][i].append(self.struct_graph_table['arc_start'][j])
                # находим и добавляем исходящие
                if self.struct_graph_table['arc_start'][j] == self.graph_events['event'][i]:
                    self.graph_events['out_works'][i].append(self.struct_graph_table['arc_end'][j])

        # print(self.graph_events['event'])
        # print(f'входящие {self.graph_events["in_works"]}')
        # print(f"исходящие {self.graph_events['out_works']}")
        # print('*************************************')

        # for i in range(0, vertices_num):
        #     print(self.graph_events['event'][i])
        #     print(f'входящие {self.graph_events["in_works"][i]}')
        #     print(f"исходящие {self.graph_events['out_works'][i]}")
        #     print()

    def find_all_vertices(self):
        """ нахождение всех вершин графа """
        print('Находим все вершины:')
        self.current_way = [self.first_top]
        self.append_new_event_in_events_graph(self.first_top)

        for i in range(0, self.works_num):
            if self.graph_table['arc_start'][i] == self.first_top:
                self.current_way.append(self.graph_table['arc_end'][i])  # запомнить следуюущую вершину в списке путей

                if self.graph_table['arc_end'][i] not in self.graph_events['event']:
                    self.append_new_event_in_events_graph(self.graph_table['arc_end'][i])
                self.recursive_find_all_vertices()

    def recursive_find_all_vertices(self):
        """ рекурсивный обход графа """
        if self.current_way[len(self.current_way) - 1] == self.last_top:
            self.current_way.pop()  # удаление последней вершины, возврат по стеку
            return

        for i in range(0, self.works_num):
            if self.graph_table['arc_start'][i] == self.current_way[len(self.current_way) - 1]:
                self.current_way.append(self.graph_table['arc_end'][i])  # запомнить вершину
                if self.graph_table['arc_end'][i] not in self.graph_events['event']:
                    self.append_new_event_in_events_graph(self.graph_table['arc_end'][i])
                self.recursive_find_all_vertices()
        self.current_way.pop()  # удаление последней вершины
        return

    def add_row_in_graph_table(self, start, end, weight, is_visited=False, adding_is_in_sort=False):
        """ добавить строку в таблицу графа """
        if adding_is_in_sort:
            self.struct_graph_table['arc_start'].append(start)
            self.struct_graph_table['arc_end'].append(end)
            self.struct_graph_table['weight'].append(weight)
            self.struct_graph_table['is_visited'].append(is_visited)
            self.struct_graph_works_num += 1
        else:
            self.graph_table['arc_start'].append(start)
            self.graph_table['arc_end'].append(end)
            self.graph_table['weight'].append(weight)
            self.graph_table['is_visited'].append(is_visited)
            self.works_num += 1

    def copy_row_to_struct_graph_table(self, index):
        """ копировать строку из неструктурированного графа в структурированный по индексу """
        start = self.graph_table['arc_start'][index]
        end = self.graph_table['arc_end'][index]
        weight = self.graph_table['weight'][index]
        is_visited = self.graph_table['is_visited'][index]
        self.add_row_in_graph_table(start, end, weight, is_visited, adding_is_in_sort=True)

    def delete_row_from_graph_table(self, index):
        """ удалить строку неструктрированного графа по индексу """
        self.graph_table['arc_start'].pop(index)
        self.graph_table['arc_end'].pop(index)
        self.graph_table['weight'].pop(index)
        self.graph_table['is_visited'].pop(index)
        self.works_num -= 1

    def print_row(self, row_index, sorted_graph=False):
        """ распечатать строку соотвествующего графа """
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

    def print_graph(self, sorted_graph=False):
        """ печать таблицы |A|B|time|"""
        print('_' * 100)
        print('Вывод таблицы путей графа')
        print('|{start:^10}|{end:^10}|{weight:^10}|'.format(start='--A--', end='--B--', weight='--Вес--'))
        for row_index in range(0, self.works_num):
            self.print_row(row_index, sorted_graph)
        print(f'Первая вершина: {self.first_top}')
        print(f'Последняя вершина: {self.last_top}')
        print('_' * 100)

    def search_first_top(self):
        """ поиск первой вершины графа """
        print('нахождение первой вершины')
        for i in range(0, self.works_num):  # итерация 1 по таблице
            is_start_top = True
            for j in range(0, self.works_num):  # итерация 2 по таблице для поиска первой вершины
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
                # иначе она уже не первая, нарушаются правила СГ, нужно создавать фиктив. вершину
                else:
                    print('создание фиктивной первой вершины')
                    self.add_row_in_graph_table(self.fictive_start_top, self.first_top, 0)
                    self.add_row_in_graph_table(self.fictive_start_top, self.graph_table['arc_start'][i], 0)
                    if self.first_top != self.fictive_start_top:
                        self.first_top = self.fictive_start_top

                for index in range(0, self.works_num):
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

    def optimize_graph(self):
        """ оптимизация графа (удаление петель, одинаковых работ, поиск последней вершины"""
        print('оптимизация:')
        i = 0
        while i < self.works_num:
            # one
            i = self.delete_top_loops(i)
            # two
            j = 0
            while j < self.works_num:  # сравнение всех вершин СГ
                temp = self.check_duplication(i, j)
                # None при запуске optimize_graph рекурсивно из check_duplication(i, j). Иначе обнуляется счётчик цикла.
                j += 1
                if temp is not None:
                    j = temp
            i += 1
        self.print_graph()
        self.search_last_top()
        for index in range(0, self.works_num):
            self.graph_table['is_visited'][index] = False

    def search_last_top(self):
        """ поиск последней вершины графа """
        print('нахождение последней вершины')
        for i in range(0, self.works_num):  # итерация 1 по таблице
            is_last_top = True
            for j in range(0, self.works_num):  # итерация 2 по таблице для поиска последней вершины
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
                    for k in range(0, self.works_num):
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

                            for index in range(0, self.works_num):
                                if self.graph_table['arc_end'][index] == self.graph_table['arc_end'][i]:
                                    self.graph_table['is_visited'][index] = True
                        # удаление одной из вершин
                        else:
                            print(f'удаление вершины {self.graph_table["arc_end"][i]}')
                            self.delete_row_from_graph_table(i)
                            self.last_top = None
                            for index in range(0, self.works_num):
                                self.graph_table['is_visited'][index] = False
                            self.search_last_top()
                            break

    # def get_first_top_index(self):
    #     for index in range(0, self.works_num):
    #         if self.first_top == self.graph_table['arc_start'][index]:
    #             return index

    # def find_layers(self):
    #     """ нахождение слоев для каждой вершины """
    #     # найдем индекс первой вершины
    #     first_top_index = 0
    #     for i in range(0, self.works_num):
    #         if [self.first_top] ==  self.graph_table['arc_start'][i]:
    #             first_top_index = i
    #     # присвоим первой вершине слой
    #     layer_level = 0
    #     self.graph_table['layer'][first_top_index] = layer_level
    #     # создадим очередь вершин и поместим туда первую вершину
    #     top_queue = [self.graph_table['layer'][first_top_index]]
    #     # найдем все вершины второго слоя
    #     layer_set = set()
    #     for i in range(0, self.works_num):
    #         if self.graph_table['arc_start'][i] == top_queue[len(top_queue) - 1]:
    #             # поиск конечной вершины работы и проверка, имеет ли она входящие в неё работы,
    #             # находящиеся не в текущем слое
    #             has_prev_tops = False
    #             for k in range(0, self.works_num):
    #                 if self.graph_table['arc_start'][k] == self.graph_table['arc_end'][i]:
    #                     is_last = False
    #             layer_set.add(self.graph_table['arc_end'][i])

    # def find_layer(self, layer_level, top_queue):
    #     # отметка слоев этого уровня и нахождение слоев следующего уровня
    #     self.find_layer(layer_level + 1, top_queue)

    def struct_graph(self):
        print('упорядочивание графа')
        vertex_queue = [self.first_top]
        while self.works_num != self.struct_graph_works_num:
            for i in range(0, self.works_num):
                if vertex_queue[0] == self.graph_table['arc_start'][i] and not self.graph_table['is_visited'][i]:
                    self.copy_row_to_struct_graph_table(i)
                    vertex_queue.append(self.graph_table['arc_end'][i])
                    self.graph_table['is_visited'][i] = True

            vertex_queue.pop(0)

    def search_full_ways(self):
        """ нахождение всех полных путей графа """
        self.current_way = [self.first_top]
        print('полные пути графа:')
        for i in range(0, self.works_num):
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

        for i in range(0, self.works_num):
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
    graph.find_all_vertices()
    print(f'События: {graph.graph_events["event"]}')
    graph.count_ins_and_outs()
    graph.find_vertex_layers(0, layer=0)

    print(f'События: {graph.graph_events["event"]}')


    vertices_num = len(graph.graph_events['event'])
    for i in range(0, vertices_num):
        print('|{event:^5}|{ins:^20}|{outs:^20}|{layer:^5}|{early_term:^5}|'.format(
            event=graph.graph_events['event'][i],
            ins=str(graph.graph_events["in_works"][i]),
            outs=str(graph.graph_events['out_works'][i]),
            layer=graph.graph_events['layer'][i],
            early_term=str(graph.graph_events['early_term'][i]),
        ))

    graph.sort_events_by_layers()

    print()
    for i in range(0, vertices_num):
        print('|{event:^5}|{ins:^20}|{outs:^20}|{layer:^5}|{early_term:^5}|'.format(
            event=graph.graph_events['event'][i],
            ins=str(graph.graph_events["in_works"][i]),
            outs=str(graph.graph_events['out_works'][i]),
            layer=graph.graph_events['layer'][i],
            early_term=str(graph.graph_events['early_term'][i]),
        ))

    # graph.find_early_term_for_all_event()

    # print()
    # for i in range(0, vertices_num):
    #     print('|{event:^5}|{ins:^20}|{outs:^20}|{layer:^5}|{early_term:^5}|'.format(
    #         event=graph.graph_events['event'][i],
    #         ins=str(graph.graph_events["in_works"][i]),
    #         outs=str(graph.graph_events['out_works'][i]),
    #         layer=graph.graph_events['layer'][i],
    #         early_term=str(graph.graph_events['early_term'][i]),
    #     ))

