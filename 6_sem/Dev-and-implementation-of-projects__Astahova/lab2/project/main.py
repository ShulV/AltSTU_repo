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
                                   'is_visited': [],
                                   'full_time_reserve': [],
                                   'independent_time_reserve': [],
                                   }  # упоряденная таблица, содержащая дуги и веса графа
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
                             'visited': []
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
        self.graph_events['visited'].append(None)

    def swap_events(self, i, j):
        """ поменять местами строки событий"""
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
        # посещенность
        buff = self.graph_events['visited'][i]
        self.graph_events['visited'][i] = self.graph_events['visited'][j]
        self.graph_events['visited'][j] = buff

    def sort_events_by_layers(self):
        """ сортировка событий по слоям по возрастанию """
        print('_' * 100)
        print('Сортировка по слоям')
        n = len(self.graph_events['event'])
        for i in range(n - 1):
            for j in range(n - i - 1):
                if self.graph_events['layer'][j] > self.graph_events['layer'][j + 1]:
                    self.swap_events(j, j + 1)
        print('_' * 100)

    def find_early_term_for_event(self, event):
        """ нахождение раннего срока события """
        event_index = self.find_index_by_event(event)
        # если событие начальное, ранний срок = 0
        if event == self.first_top:
            self.graph_events['early_term'][event_index] = 0
            return
        # нахождение максимального веса из работ, связанных с предыдущими событиями
        max_early_term = 0
        tmp_event_early_term = 0
        # ищем работу, у которой конечное событие равно нашему событию
        for i in range(0, self.struct_graph_works_num):
            if event == self.struct_graph_table['arc_end'][i]:
                max_weight = self.struct_graph_table['weight'][i]
                prev_event = self.struct_graph_table['arc_start'][i]
                prev_event_index = self.find_index_by_event(prev_event)
                prev_event_early_term = self.graph_events['early_term'][prev_event_index]
                tmp_event_early_term = prev_event_early_term + max_weight
            if max_early_term < tmp_event_early_term:
                max_early_term = tmp_event_early_term
        self.graph_events['early_term'][event_index] = max_early_term

    def find_early_term_for_all_event(self):
        """ нахождение раннего срока всех событий """
        print('_' * 100)
        print('Нахождение ранних сроков у событий')
        for event in self.graph_events['event']:
            self.find_early_term_for_event(event)
        print('_' * 100)

    def find_late_term_for_event(self, event):
        """ нахождение позднего срока события """
        event_index = self.find_index_by_event(event)
        # если событие конечное, поздний срок = раннему сроку события
        if event == self.last_top:
            self.graph_events['late_term'][event_index] = self.graph_events['early_term'][event_index]
            return
        # нахождение минимального веса из работ, связанных с последующими событиями
        min_late_term = None
        for i in range(self.struct_graph_works_num):
            if event == self.struct_graph_table['arc_start'][i]:
                min_weight = self.struct_graph_table['weight'][i]
                next_event = self.struct_graph_table['arc_end'][i]
                next_event_index = self.find_index_by_event(next_event)
                next_event_late_term = self.graph_events['late_term'][next_event_index]
                tmp_event_late_term = next_event_late_term - min_weight

                if min_late_term is None:
                    min_late_term = tmp_event_late_term
                if min_late_term > tmp_event_late_term:
                    min_late_term = tmp_event_late_term
        self.graph_events['late_term'][event_index] = min_late_term

    def find_late_term_for_all_event(self):
        """ нахождение позднего срока всех событий """
        print('_' * 100)
        print('Нахождение поздних сроков у событий')
        for _i in range(len(self.graph_events['event']) - 1, -1, -1):
            event = self.graph_events['event'][_i]
            self.find_late_term_for_event(event)
        print('_' * 100)

    def find_time_reserves_for_all_event(self):
        """ нахождение резервов времени для всех событий """
        print('_' * 100)
        print('Нахождение резервов времени для событий')
        for event in self.graph_events['event']:
            ind = self.find_index_by_event(event)
            reserve_time = self.graph_events['late_term'][ind] - self.graph_events['early_term'][ind]
            self.graph_events['reserve_time'][ind] = reserve_time
        print('_' * 100)

    def get_critical_path_length(self):
        """ получение критического пути из таблицы событий """
        print('_' * 100)
        n = len(self.graph_events['event'])
        _critical_path_length = self.graph_events['late_term'][n - 1]
        print(f'Критический путь равен: {_critical_path_length}')
        print('_' * 100)
        return _critical_path_length

    def find_time_reserve_for_work(self, index, full=True):
        """ нахождение полного или независмого временного резерва для работы """
        # ПОЛНЫЙ ВРЕМЕННОЙ РЕЗЕРВ = раннее время конечного события работы - позднее время начального события работы -
        # - время выполнения работы (вес работы)
        # НЕЗАВИСИМЫЙ ВРЕМЕННОЙ РЕЗЕРВ = раннее время начального события работы -
        # - позднее время конечного события работы - время выполнения работы (вес работы)
        # full = True, то находится полный временной резерв
        start_work_vertex = self.struct_graph_table['arc_start'][index]  # начальная вершина работы
        end_work_vertex = self.struct_graph_table['arc_end'][index]  # конечная вершина работы
        work_weight = self.struct_graph_table['weight'][index]  # вес работы
        start_work_vertex_index = self.find_index_by_event(start_work_vertex)  # индекс нач вершины в таблице событий
        end_work_vertex_index = self.find_index_by_event(end_work_vertex)  # индекс конеч вершины в таблице событий
        if full:
            end_vertex_late_term = self.graph_events['late_term'][end_work_vertex_index]  # позднее время конеч события
            start_vertex_early_term = self.graph_events['early_term'][start_work_vertex_index]  # раннее время нач соб
            full_time_reserve = end_vertex_late_term - start_vertex_early_term - work_weight  # tп(j)-tр(i)-T(i,j)
            self.struct_graph_table['full_time_reserve'][index] = full_time_reserve
        else:
            start_vertex_late_term = self.graph_events['late_term'][start_work_vertex_index]  # позднее время нач соб
            end_vertex_early_term = self.graph_events['early_term'][end_work_vertex_index]  # раннее время нач события
            ind_time_reserve = end_vertex_early_term - start_vertex_late_term - work_weight  # tр(j)-tп(i)-T(i,j)
            self.struct_graph_table['independent_time_reserve'][index] = ind_time_reserve

    def find_time_reserves_for_all_works(self):
        """ нахождение полных и независимых временных резервов для всех работ """
        print('_' * 100)
        print(f'Нахождение полных и независимых временных резервов для всех работ')
        _n = len(self.struct_graph_table['arc_start'])
        for i in range(_n):
            self.find_time_reserve_for_work(i, full=True)  # подчет полного резерва
            self.find_time_reserve_for_work(i, full=False)  # подсчет независимого резерва
        print('_' * 100)

    def find_index_by_event(self, event):
        """ нахождение номера (индекса) события в структуре по его шифру """
        events_len = len(self.graph_events['event'])
        for i in range(events_len):
            if self.graph_events['event'][i] == event:
                return i
        return None

    def check_vertex_includes_only_prev_layers_vertices(self, index):
        """ проверить, что в вершину входят только вершины предыдущих слоев """
        for in_work in self.graph_events['in_works'][index]:
            in_work_index = self.find_index_by_event(in_work)
            if self.graph_events['layer'][in_work_index] is None:
                return False
        return True

    def get_max_layer_form_prev_vertices(self, index):
        """ получаем максимальный слой предыдущих вершин данной вершины """
        in_works = self.graph_events['in_works'][index]
        max_layer = 0
        for in_work in in_works:
            vertex = self.find_index_by_event(in_work)
            layer = self.graph_events['layer'][vertex]
            if max_layer < layer:
                max_layer = layer
        return max_layer

    def find_vertex_layers(self):
        """ находим слой каждой вершины обходом в ширину"""
        # если нет входящих работ - слой 0
        start_vertex = self.first_top  # начальная вершина
        end_vertex = self.last_top  # конечная вершина
        queue = [start_vertex]
        start_vertex_index = self.find_index_by_event(start_vertex)
        self.graph_events['layer'][start_vertex_index] = 0  # нулевой слой для начальной вершины
        self.graph_events['visited'][start_vertex_index] = True  # посещенность вершины
        layer = 0
        while len(queue) > 0:
            layer += 1
            # удаляем первый (верхний элемент из очереди)
            vertex = queue.pop(0)

            vertex_index = self.find_index_by_event(vertex)
            outs_len = len(self.graph_events['out_works'][vertex_index])  # количество выходящих вершин
            for _i in range(outs_len):
                out_event = self.graph_events['out_works'][vertex_index][_i]  # шифр соб., выходящего из текущ. соб.
                out_event_index = self.find_index_by_event(out_event)  # индекс соб., выходящего из текущ. соб.
                flag = self.check_vertex_includes_only_prev_layers_vertices(out_event_index)
                # flag = True, когда все входящие в текущую вершину вершины пройдены
                if self.graph_events['visited'][out_event_index] is not True and flag:
                    queue.append(out_event)
                    self.graph_events['visited'][out_event_index] = True
                    prev_max_layer = self.get_max_layer_form_prev_vertices(out_event_index)
                    self.graph_events['layer'][out_event_index] = prev_max_layer + 1
                    if out_event_index == end_vertex:
                        return True
        # если конца не обнаружено
        return False

    def find_ins_and_outs(self):
        """ находим входящие и исходящие работы у вершин """
        vertices_number = len(self.graph_events['event'])
        for _i in range(0, vertices_number):
            for j in range(0, self.works_num):
                # находим и добавляем структуру входящие вершины
                if self.struct_graph_table['arc_end'][j] == self.graph_events['event'][_i]:
                    self.graph_events['in_works'][_i].append(self.struct_graph_table['arc_start'][j])
                # находим и добавляем исходящие
                if self.struct_graph_table['arc_start'][j] == self.graph_events['event'][_i]:
                    self.graph_events['out_works'][_i].append(self.struct_graph_table['arc_end'][j])

    def find_all_vertices(self):
        """ нахождение всех вершин графа """
        print('Находим все вершины (события):')
        self.current_way = [self.first_top]
        self.append_new_event_in_events_graph(self.first_top)

        for _i in range(0, self.works_num):
            if self.graph_table['arc_start'][_i] == self.first_top:
                self.current_way.append(self.graph_table['arc_end'][_i])  # запомнить следуюущую вершину в списке путей

                if self.graph_table['arc_end'][_i] not in self.graph_events['event']:
                    self.append_new_event_in_events_graph(self.graph_table['arc_end'][_i])
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
            self.struct_graph_table['full_time_reserve'].append(None)
            self.struct_graph_table['independent_time_reserve'].append(None)
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
            print('|{start:^10}|{end:^10}|{weight:^25}|{full_res:^25}|{ind_res:^25}|'.format(
                start=self.struct_graph_table['arc_start'][row_index],
                end=self.struct_graph_table['arc_end'][row_index],
                weight=self.struct_graph_table['weight'][row_index],
                full_res=str(self.struct_graph_table['full_time_reserve'][row_index]),
                ind_res=str(self.struct_graph_table['independent_time_reserve'][row_index]),
            ))
        else:
            print('|{start:^10}|{end:^10}|{weight:^10}|'.format(
                start=self.graph_table['arc_start'][row_index],
                end=self.graph_table['arc_end'][row_index],
                weight=self.graph_table['weight'][row_index]))

    def print_graph(self, sorted_graph=False):
        """ печать таблицы |A|B|time|"""
        print('_' * 100)
        print('Вывод таблицы путей графа (работ)')
        if sorted_graph:
            print('|{start:^10}|{end:^10}|{weight:^25}|{full_res:^25}|{ind_res:^25}|'.format(
                start='A',
                end='B',
                weight='Продолжительность (τ)',
                full_res='Полный резерв (Rп)',
                ind_res='Независимый резерв (Rн)',
            ))
        else:
            print('|{start:^10}|{end:^10}|{weight:^10}|'.format(
                start='A',
                end='B',
                weight='Вес',
            ))
        for row_index in range(0, self.works_num):
            self.print_row(row_index, sorted_graph)
        print(f'Первая вершина: {self.first_top}')
        print(f'Последняя вершина: {self.last_top}')
        print('_' * 100)

    def print_events_table(self):
        print(f'\nВывод таблицы вершин (событий)')
        print('|{event:^20}|{ins:^20}|{outs:^20}|{layer:^10}|{early_term:^25}|{late_term:^25}|{reserve:^25}|'.format(
            event='Событие',
            ins='Входящие события',
            outs='Выходящие события',
            layer='Слой',
            early_term='Ранний срок (t_р)',
            late_term='Поздний срок (t_п)',
            reserve='Резерв времени (R(i))',
        ))
        n = len(graph.graph_events['event'])
        for _i in range(0, n):
            print(
                '|{event:^20}|{ins:^20}|{outs:^20}|{layer:^10}|{early_term:^25}|{late_term:^25}|{reserve:^25}|'.format(
                    event=self.graph_events['event'][_i],
                    ins=str(self.graph_events["in_works"][_i]),
                    outs=str(self.graph_events['out_works'][_i]),
                    layer=self.graph_events['layer'][_i],
                    early_term=str(self.graph_events['early_term'][_i]),
                    late_term=str(self.graph_events['late_term'][_i]),
                    reserve=str(self.graph_events['reserve_time'][_i]),
                ))

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

    def search_full_ways(self, check_critical=False):
        """ нахождение всех полных путей графа """
        self.current_way = [self.first_top]
        print('полные пути графа:')
        for i in range(0, self.works_num):
            if self.graph_table['arc_start'][i] == self.first_top:
                self.current_way.append(self.graph_table['arc_end'][i])  # запомнить следуюущую вершину в списке путей
                self.search_bfs(check_critical)
        print('_' * 100)

    def check_way_criticality(self):
        """ проверка пути на то, что он является критичным """
        for _i in range(1, len(self.current_way)):
            prev_way_vertex = self.current_way[_i - 1]
            way_vertex = self.current_way[_i]
            for _j in range(self.struct_graph_works_num):
                # если определенная работа и пути найдена
                start_work_vertex = self.struct_graph_table['arc_start'][_j]
                end_work_vertex = self.struct_graph_table['arc_end'][_j]
                if start_work_vertex == prev_way_vertex and end_work_vertex == way_vertex:
                    # если у какого-то события в этом пути Rп != 0 (событие не критическое), то путь не критический
                    if self.struct_graph_table['full_time_reserve'][_j] != 0:
                        return False
        # все события в пути критические, то путь критический
        return True

    def search_bfs(self, check_critical):
        """ обход графа в ширину"""
        if self.current_way[len(self.current_way) - 1] == self.last_top:
            if check_critical:
                way_is_critical = self.check_way_criticality()
                if way_is_critical:
                    print('Критический путь:')
                    for _i in range(0, len(self.current_way)):
                        print(f'{self.current_way[_i]} ', end='')
                    print()
            else:
                for _i in range(0, len(self.current_way)):
                    print(f'{self.current_way[_i]} ', end='')
                print()
            self.current_way.pop()  # удаление последней вершины, возврат по стеку
            return

        for _i in range(0, self.works_num):
            if self.graph_table['arc_start'][_i] == self.current_way[len(self.current_way) - 1]:
                self.current_way.append(self.graph_table['arc_end'][_i])  # запомнить вершину
                self.search_bfs(check_critical)
        self.current_way.pop()  # удаление последней вершины
        return


if __name__ == "__main__":
    in_file = "input.csv"
    graph = Graph(in_file)
    graph.print_graph()
    # находим первую вершину
    graph.search_first_top()
    # оптимизируем (удаляем петли, дубли), там же находим конечную вершину
    graph.optimize_graph()
    graph.print_graph()
    # структурируем граф
    graph.struct_graph()
    graph.print_graph(sorted_graph=True)
    # находим полные пути
    graph.search_full_ways()
    # находим все вершины
    graph.find_all_vertices()
    # находим входящие и исходящие вершины
    graph.find_ins_and_outs()
    # находим слои у вершин
    graph.find_vertex_layers()
    # сортируем таблицу событий по слоям
    graph.sort_events_by_layers()
    graph.print_events_table()
    # находим ранние сроки для событий
    graph.find_early_term_for_all_event()
    # находим поздние сроки для событий
    graph.find_late_term_for_all_event()
    # находим временной резерв для событий
    graph.find_time_reserves_for_all_event()
    graph.print_events_table()
    # находим полные и независимые временные резервы для работы
    graph.find_time_reserves_for_all_works()
    graph.print_graph(sorted_graph=True)
    # выводим критические пути
    graph.search_full_ways(check_critical=True)
    # находим длину критического пути
    critical_path_length = graph.get_critical_path_length()
