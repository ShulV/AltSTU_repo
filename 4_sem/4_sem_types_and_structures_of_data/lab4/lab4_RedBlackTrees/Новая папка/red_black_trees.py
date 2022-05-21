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


def cls():
    """Очистка консоли"""
    os.system('cls')
    print('\r')


def color_print(text, red=False):
    if red:
        print(Back.BLACK, Fore.RED + text)

    else:
        print(Back.BLACK, Fore.LIGHTBLACK_EX + text)
    print(Style.RESET_ALL, end='')


class Node:
    """класс узла студент для КЧД"""
    def __init__(self, key, surname, marks):
        self.key = key  # номер зачетной книжки
        self.surname = surname
        self.marks = marks
        self.red = True
        self.left = None
        self.right = None
        self.parent = None

    def print_tree(self, indent=0):
        if self is not None:
            if self.left is not None:
                self.left.print_tree(indent + 4)
            color_print(f"{' '*indent} {self.surname}", self.red)
            if self.right is not None:
                self.right.print_tree(indent + 4)


def write_tree_in_file(filename):
    """Запись дерева в файл"""
    pass


class RBTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        """поиск места для вставки"""
        current_node = self.root
        while current_node is not None and key != current_node.key:
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return current_node

    def insert(self, key, surname, marks):
        """вставка узла"""
        node = Node(key, surname, marks)
        # СЛУЧАЙ 1 - дерево пустое
        if self.root is None:
            node.red = False
            self.root = node
            print(f"Вставка в корень {self.root.key}")
            return  # Конец случая 1 (выход)
        # Поиск None-узла (места для вставки) и его предка
        last_node = self.root
        while last_node is not None:
            potential_parent = last_node
            if node.key < last_node.key:
                last_node = last_node.left
            else:
                last_node = last_node.right
        # Назначить родителей и братьев новому узлу
        node.parent = potential_parent
        print(f"Новый узел - {node.key} его родитель - {node.parent.key}")
        if node.key < node.parent.key:
            node.parent.left = node
            print(f"Вставляемый узел - левый потомок узла {node.parent.key}")
        else:
            node.parent.right = node
            print(f"Вставляемый узел - правый потомок узла {node.parent.key}")
        node.left = None
        node.right = None
        self.fix_tree(node)

    def fix_tree(self, node):
        print(f"Родитель узла - ", end='')
        if not node.parent.red:
            print("чёрный (свойства не нарушены)")  # СЛУЧАЙ 2 - предок чёрный
            return
        else:
            print("красный (свойства нарушены)")
        # ---------------------------------------------------------------------
        cur_parent = node.parent  # текущий родитель
        cur_grandfather = cur_parent.parent  # текущий дедушка

        # # определение, является ли текущий узел левым потомком?
        # if node == cur_parent.left:
        #     node_is_left = True
        # else:
        #     node_is_left = False

        # определение, является ли родитель текущего узла левым потомком?
        if cur_grandfather.left == cur_parent:
            parent_is_left = True
        else:
            parent_is_left = False
        # поиск дяди текущего узла
        if parent_is_left:
            cur_uncle = node.parent.parent.right
        else:
            cur_uncle = node.parent.parent.left
        # ---------------------------------------------------------------------
        # Далее родитель всегда красный
        # СЛУЧАЙ 3 - родитель и дядя красные
        if cur_uncle is None:
            print(f"Родитель {node.key} красный, дяди нет")
        elif cur_uncle.red:
            print(f"Родитель {node.key} красный и дядя {cur_uncle.key} красный")
        else:
            print(f"Родитель {node.key} красный и дядя {cur_uncle.key} чёрный")

    def read_file_fill_tree(self, filename):
        """Чтение файла и заполненение дерева"""
        with open(filename, "r") as f:
            for line in f:
                data = line.replace("\n", "").split(';')
                print(colored(data, color='green'))
                key = data[1]
                surname = data[0]
                marks = data[2:7]
                self.insert(key, surname, marks)


def main():
    rbt_tree = RBTree()
    choice = 1
    while choice != "0":
        print("\rLab 3. Binary trees.")
        print("\n\t1 - Read file and fill tree;" +
              "\n\t2 - Save tree in file;" +
              "\n\t3 - Insert element;" +
              "\n\t4 - Delete tree;" +
              "\n\t5 - Print tree;" +
              "\n\t0 - Exit.")
        choice = input("\nYour choice:\t")
        if choice == "1":
            print(1)
            rbt_tree.read_file_fill_tree(FILE_IN)
        elif choice == "2":
            print(2)
        elif choice == "3":
            grb = input("Enter grade number book:")
            surname = input("Enter surname:")
            marks = [None for _ in range(0, 5)]
            for mark in marks:
                mark = input("Enter mark:")
            rbt_tree.insert(key=grb, surname=surname, marks=marks)
        elif choice == "4":
            print(4)
        elif choice == "5":
            print("Tree output:")
            if rbt_tree.root is not None:
                rbt_tree.root.print_tree()
            else:
                print("Tree is empty")
        # cls()


main()  # Вызов главной функции

