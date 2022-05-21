#pragma once
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>
#include <fstream>
#include <iostream>
#include <string>
#include <Windows.h>
#include <ctime>

using namespace std;

// Структура узла
struct tnode {// Узел дерева
    int key;// Ключ
    int level;//уровень
    struct tnode* left;// Левый потомок
    struct tnode* right;// Правый потомок
    
};

// Сравнение чисел
int numcmp(int a, int b)
{
    if (a > b) return 1;
    if (a < b) return -1;
    if (a == b) return 0;
}

// Функция добавления узла к дереву
struct tnode* addNode(struct tnode* node, int key) {
    int cond;
    if (node == NULL) {
        node = new tnode();
        node->key = key;
        node->level = 0;
        node->left = node->right = NULL;

    }
    else 
    {
        cond = numcmp(key, node->key);
        if (cond < 0) {
            node->left = addNode(node->left, key);
            node->left->level = node->level + 1;
        }
        else {
            node->right = addNode(node->right, key);
            node->right->level = node->level + 1;
        }
    }

    return node;
}

// Добавление N узлов к дереву с рандомным значением
void randomAdd_N_Nodes(struct tnode** node, int quantity) {
    int number;
    
    
    for (int i = 0; i < quantity; i++) {
        number = rand() % 100 - 50;
        *node=addNode(*node, number);
    }

    
}

// Функция удаления поддерева
void deleteSubTree(tnode* node) {
    if (node != NULL) {
        deleteSubTree(node->left);
        deleteSubTree(node->right);
        delete node;
    }
}

// Функция вывода дерева
void printTree(tnode* node) {
    if (node != NULL) {
        printTree(node->left);
        printf("ключ: %10d\tуровень: %10d\n", node->key, node->level);
        printTree(node->right);
    }

}

// Функция графического вывода дерева
void printTreeGraphics(tnode* node, int level)
{
    if (node)
    {
        printTreeGraphics(node->left, level + 1);
        for (int i = 0; i < level; i++) cout << "   ";
        cout << node->key << endl;
        printTreeGraphics(node->right, level + 1);
    }
}

// Изменить уровень (node-level) каждого узла
void changeLevel(tnode* node, int x) {
    if (node != NULL) {
        node->level += x;
        changeLevel(node->left, x);
        changeLevel(node->right, x);
    }
}

// Удаление корня поддерева
tnode* deleteRootSubTree(tnode* node) {
    if (node != NULL) {
        cout << "removing from root" << endl;

        if (node->left == NULL && node->right == NULL) {
            return NULL;
        }
        if (node->left != NULL && node->right == NULL) {
            node = node->left;// Присваиваем корню левую часть дерева (от корня)
            changeLevel(node, -1);
        }
        if (node->left == NULL && node->right != NULL) {
            node = node->right;// Присваиваем корню правую часть дерева (от корня)
            changeLevel(node, -1);
        }
        if (node->left != NULL && node->right != NULL) {
            int height = 0; // Высота, на которую опустится левое поддерево
            tnode* left_node = node->left;// Сохраняем левую часть дерева (от корня)
            node = node->right;// Присваиваем корню правую часть дерева (от корня)
            //нужно левую часть дерева вставить после наименьшего элемента в дереве 
            
            tnode* tmp = node;// Временный узел для прохода по ветке
            while (tmp->left != NULL) {
                tmp = (tmp)->left;
                height++;
            }
            changeLevel(node, -1);
            changeLevel(left_node, height);
            tmp->left = left_node;// <последний наименьший элмент в правом дереве>->left = бывшее левое дерево

        }
        
        return node;
    }
    else node;
}

// Поиск в бинарном дереве и удаление узла
tnode* deleteNode(tnode* node, int key, int level) {
    tnode *ptr;// Указатель для прохода по дереву
    tnode* ptr2;// Указатель для хранения поддерева, в котором удалена вершина
    tnode* prev_ptr = node;// Указатель на предыдущий элемент (инициализация для компилятора, позже затрётся)
    if (node != NULL) {// Если дерево имеет хотя бы 1 элемент
        if (node->key == key && node->level==level) return deleteRootSubTree(node);// Если вершина дерева - то, что мы ищем,
        else {// Иначе ищём этот элемент, двигаясь по узлам по единственному пути
            ptr = node;
            while (ptr != NULL)
                if (ptr->level == level && ptr->key == key) { 
                    ptr2 = deleteRootSubTree(ptr); 
                    if (prev_ptr->key > key) prev_ptr->left = ptr2;
                    else prev_ptr->right = ptr2;
                    return node;
                }
                else {
                    prev_ptr = ptr;
                    if (ptr->key > key) ptr = ptr->left;
                    else ptr = ptr->right;
                    if (ptr == NULL) return node;// Если узел пуст
                    if (ptr->level > level) return node;// Если прошли нужный уровень
                }
                    
        }
    }
    return node;
}

// Чтения количества элементов массива из файла
int readArrayN(const std::string& filename)// Чтения количества элементов массива из файла
{
    ifstream in;
    string str_n;
    int n = 0;
    // Open the file.
    in.open(filename, std::ios::in | std::ios::binary);
    if (in.is_open()) {
        getline(in, str_n);
    }
    else
    {
        throw exception("Exception: file did't open");
    }
    try {
        n = stoi(str_n);
    }
    catch (exception exc) {
        throw exception("Exception: convert failure");
    }
    return n;
}

// Сохранения числа в файл
bool SaveNumberInFile(const std::string& filename, int key)
{
    ofstream out;
    // Open the file.
    out.open(filename, ios::app | std::ios::binary);
    // Validate that the file is open.
    if (!out.is_open())
        return false;
    out << key << endl;
    out.close();
    return true;
}

// Сохранить дерево в файл
void SaveTreeInFile(struct tnode* node, const std::string& filename)
{
    if (node != NULL) {
        SaveTreeInFile(node->left, filename);
        SaveNumberInFile(filename, node->key);// Сохранить 1 значение в файл
        SaveTreeInFile(node->right, filename);
    }
}

// Очистить файл
void clearFile(const std::string& filename) {
    ofstream out;
    // Open the file.
    out.open(filename, ios::trunc);// Пересоздать файл (сделать пустым)
    out.close();
}