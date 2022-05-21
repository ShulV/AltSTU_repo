"""В программе используется символическое использование букв:
p(parent), g(grandparent), u(uncle)"""

import os
from colorama import Fore, Back, Style
from termcolor import colored, cprint
import colorama

colorama.init()

# Константы
NUM_MARKS = 5
BLACK = 0
RED = 1
FILE_IN = "input.dat"
FILE_OUT = "output.dat"
SPEC_STR_CUR_TREE = "\nТЕКУЩЕЕ ДЕРЕВО:\n"
SPEC_STR_NEW_TREE = "\nСФОРМИРОВАННОЕ ДЕРЕВО:\n"
DEBUG_MODE = True  # режим отладки (выводится много дополнительных сообщений при работе с деревом)


def cls():
    """Очистка консоли"""
    os.system('cls')
    print('\r')


def color_print(text, red=False):
    if red:
        print(Fore.RED + text)

    else:
        print(Fore.BLACK + text)
    print(Style.RESET_ALL, end='')


def clear_file(filename):
    with open(filename, "w"):
        pass


class Node:
    """класс узла студент для КЧД
    только у NIL узла left,right,parent=None.
    у всех других узлов left,right,parent=NIL
    """

    def __init__(self, key, surname, marks, nil=None):
        self.key = key  # номер зачетной книжки
        self.surname = surname
        self.marks = marks
        self.red = True
        self.left = nil
        self.right = nil
        self.parent = nil

    def print_tree(self, indent=0):
        if self is not NIL:
            if self.left is not NIL:
                self.left.print_tree(indent + 8)
            color_print(f"{' ' * indent} {self.key}({self.surname})", self.red)
            if self.right is not NIL:
                self.right.print_tree(indent + 8)
        else:
            print("tree is empty")

    def write_tree_in_file(self, filename):
        """Запись дерева в файл"""
        if self is not NIL:
            if self.left is not NIL:
                self.left.write_tree_in_file(filename)
            self.add_record_in_file(filename)
            # color_print(f"{self.key}({self.surname})", self.red)
            if self.right is not NIL:
                self.right.write_tree_in_file(filename)

    def add_record_in_file(self, filename, spec_str=None):
        with open(filename, "a") as f:
            if spec_str is None:
                marks = ";".join(self.marks)
                record = ";".join([self.surname, self.key, marks, "\n"])
                f.write(record)
            else:
                f.write(spec_str)

    def create_new_tree(self, new_tree):
        if self is not NIL:
            if self.left is not NIL:
                self.left.create_new_tree(new_tree)
            if self.marks == ["5" for _ in range(0, NUM_MARKS)]:
                if DEBUG_MODE:
                    cprint(f"{self.key}({self.surname}) - отличник", on_color='on_magenta')
                new_tree.insert(self.key, self.surname, self.marks)
            if self.right is not NIL:
                self.right.create_new_tree(new_tree)


NIL = Node(None, None, None)
NIL.red = False


class RBTree:
    def __init__(self):
        self.root = NIL

    # TODO метод не используется
    def search(self, key):
        """поиск места для вставки"""
        current_node = self.root
        while current_node is not NIL and key != current_node.key:
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node

    def insert(self, key, surname, marks):
        """вставка узла"""
        node = Node(key, surname, marks, NIL)
        # СЛУЧАЙ 1 - дерево пустое
        if self.root is NIL:
            node.red = False
            self.root = node
            if DEBUG_MODE:
                print(f"Вставка в корень {self.root.key}({self.root.surname})")
            return  # Конец случая 1 (выход)
        # Поиск NIL-узла (места для вставки) и его предка
        last_node = self.root
        while last_node is not NIL:
            potential_parent = last_node
            if node.key < last_node.key:
                last_node = last_node.left
            else:
                last_node = last_node.right
        # Назначить родителей и братьев новому узлу
        node.parent = potential_parent
        if DEBUG_MODE:
            print(f"Новый узел - {node.key} его родитель - {node.parent.key}")
        if node.key < node.parent.key:
            node.parent.left = node
            if DEBUG_MODE:
                print(f"Вставляемый узел - левый потомок узла {node.parent.key}")
        else:
            node.parent.right = node
            if DEBUG_MODE:
                print(f"Вставляемый узел - правый потомок узла {node.parent.key}")
        node.left = NIL
        node.right = NIL
        if DEBUG_MODE:
            self.root.print_tree()
        self.fix_tree1(node)
        if DEBUG_MODE:
            self.root.print_tree()

    def fix_tree1(self, node):
        """случай балансировки 1: node - в корне, иначе - случай 2"""
        if node.parent == NIL:
            node.red = False
            if DEBUG_MODE:
                print(f"случай 1 (корень: {node.key}({node.surname}))")
        else:
            self.fix_tree2(node)

    def fix_tree2(self, node):
        """случай балансировки 2: родитель - черный, иначе - случай 3"""
        if not node.parent.red:
            if DEBUG_MODE:
                print("случай 2 (родитель - чёрный)")
        else:
            self.fix_tree3(node)

    def fix_tree3(self, node):
        """случай балансировки 3: родитель и дядя - красные,
        родитель и дядя становятся красными,
        иначе - случай 4"""
        uncle = self.get_uncle(node)
        if (uncle is not NIL) and uncle.red and node.parent.red:
            if DEBUG_MODE:
                print("случай 3 (родитель и дядя - красные)")
            node.parent.red = False
            uncle.red = False
            node_g = self.get_grandparent(node)
            node_g.red = True
            self.fix_tree1(node_g)
        else:
            self.fix_tree4(node)

    def fix_tree4(self, node):
        """случай балансировки 4: родитель - красный, дядя - чёрный (родитель и дед с разных сторон)"""
        node_g = self.get_grandparent(node)
        # узел - правый потомок, а родитель - левый потомок
        if (node is node.parent.right) and (node.parent is node_g.left):
            if DEBUG_MODE:
                print(f"случай 4 - левый поворот от {node.parent.key}({node.parent.surname})")
            self.rotate_left(node.parent)
            node = node.left
        # узел - левый потомок, а родитель - правый потомок
        elif (node is node.parent.left) and (node.parent is node_g.right):
            if DEBUG_MODE:
                print(f"случай 4 - правый поворот от {node.parent.key}({node.parent.surname})")
            self.rotate_right(node.parent)
            node = node.right
        self.fix_tree5(node)

    def fix_tree5(self, node):
        """случай балансировки 4: родитель - красный, дядя - чёрный (родитель и дед потомки одной стороны)"""
        node_g = self.get_grandparent(node)
        node.parent.red = False
        node_g.red = True
        if (node is node.parent.left) and (node.parent is node_g.left):
            if DEBUG_MODE:
                print(f"случай 5 - правый поворот от {node_g.key}({node_g.surname})")
            self.rotate_right(node_g)
        elif (node is node.parent.right) and (node.parent is node_g.right):
            if DEBUG_MODE:
                print(f"случай 5 - левый поворот от {node_g.key}({node_g.surname})")
            self.rotate_left(node_g)

    def rotate_left(self, node):
        """левый поворот поддерева"""
        tmp_node = node.right  # сохранить значение правого наследника
        node.right = tmp_node.left
        if tmp_node.left is not NIL:
            tmp_node.left.parent = node
        if tmp_node is not NIL:
            tmp_node.parent = node.parent
        # если корень поддерева не является корнем всего дерева
        if node.parent is not NIL:
            # если узел - левый потомок
            if node is node.parent.left:
                node.parent.left = tmp_node
            # узел - правый потомок
            else:
                node.parent.right = tmp_node
        # корень поддерева - корень всего дерева
        else:
            self.root = tmp_node
        tmp_node.left = node
        if node is not NIL:
            node.parent = tmp_node

    def rotate_right(self, node):
        """правый поворот поддерева"""
        tmp_node = node.left  # сохранить значение левого наследника
        node.left = tmp_node.right
        if tmp_node.right is not NIL:
            tmp_node.right.parent = node
        if tmp_node is not NIL:
            tmp_node.parent = node.parent
        # если корень поддерева не является корнем всего дерева
        if node.parent is not NIL:
            # если узел - правый потомок
            if node is node.parent.right:
                node.parent.right = tmp_node
            # узел - левый потомок
            else:
                node.parent.left = tmp_node
        # корень поддерева - корень всего дерева
        else:
            self.root = tmp_node
        tmp_node.right = node
        if node is not NIL:
            node.parent = tmp_node

    def get_grandparent(self, node):
        """получение родителя узла"""
        if (node and node.parent) is not NIL:
            return node.parent.parent
        else:
            return NIL

    def get_uncle(self, node):
        """получение дяди узла"""
        node_g = self.get_grandparent(node)
        if node_g is NIL:
            return NIL
        if node.parent is node_g.left:
            return node_g.right
        else:
            return node_g.left

    def read_file_fill_tree(self, filename):
        """Чтение файла и заполненение дерева"""
        with open(filename, "r") as f:
            for line in f:
                data = line.replace("\n", "").split(';')
                if DEBUG_MODE:
                    print(colored(data, color='green'))
                key = data[1]
                surname = data[0]
                marks = data[2:7]
                self.insert(key, surname, marks)


def main():
    rbt_tree = RBTree()
    new_rbt_tree = RBTree()
    choice = 1
    while choice != "0":
        print("\rLab 3. Binary trees.")
        print("\n\t1 - Read file and fill tree;" +
              "\n\t2 - Save tree in file;" +
              "\n\t3 - Insert element;" +
              "\n\t4 - Create new tree for excellent students;" +
              "\n\t5 - Print tree;" +
              "\n\t0 - Exit.")
        choice = input("\nYour choice:\t")
        if choice == "1":
            cprint("Tree reading from file and writing in tree", on_color='on_blue')
            rbt_tree.read_file_fill_tree(FILE_IN)
        elif choice == "2":
            cprint("Tree record in file", on_color='on_blue')
            clear_file(FILE_OUT)
            rbt_tree.root.add_record_in_file(FILE_OUT, SPEC_STR_CUR_TREE)
            rbt_tree.root.write_tree_in_file(FILE_OUT)
            new_rbt_tree.root.add_record_in_file(FILE_OUT, SPEC_STR_NEW_TREE)
            new_rbt_tree.root.write_tree_in_file(FILE_OUT)
        elif choice == "3":
            cprint("adding node", on_color='on_blue')
            grb = input("Enter grade number book:")
            surname = input("Enter surname:")
            marks = ["" for _ in range(0, 5)]
            for i,mark in enumerate(marks):
                marks[i] = input("Enter mark:")
            rbt_tree.insert(key=grb, surname=surname, marks=marks)
        elif choice == "4":
            cprint("Creating new tree", on_color='on_blue')
            rbt_tree.root.create_new_tree(new_rbt_tree)
            new_rbt_tree.root.print_tree()
        elif choice == "5":
            cprint("Tree output:", on_color='on_blue')
            if rbt_tree.root is not NIL:
                rbt_tree.root.print_tree()
            else:
                print("Tree is empty")
        # cls()


main()  # Вызов главной функции
