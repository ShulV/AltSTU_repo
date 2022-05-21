#pragma once

#include <fstream>
#include <iostream>
#include <string>
#include <ctime>

using namespace std;
//функция, сливающая массивы
void Merge(int* A, int first, int last) {
    int middle, start, final, j;
    int* mas = new int[last + 1];
    middle = (first + last) / 2;  //вычисление среднего элемента (округляется в меньшую сторону)
    start = first;                //начало левой части
    final = middle + 1;           //начало правой части
    for (j = first; j <= last; j++)  //выполнять от начала до конца
        if ((start <= middle) && ((final > last) || (A[start] < A[final]))) {
            mas[j] = A[start];
            start++;
        }
        else {
            mas[j] = A[final];
            final++;
        }
    //возвращение результата в список
    for (j = first; j <= last; j++)
        A[j] = mas[j];
    delete[] mas;
};

//рекурсивная процедура сортировки
void MergeSort(int* A, int first, int last) {
    if (first < last) {
        int middle = (first + last) / 2;
        MergeSort(A, first, middle);  //сортировка левой части
        MergeSort(A, middle + 1, last);  //сортировка правой части
        Merge(A, first, last);  //слияние двух частей
    }
}

//получить максимальное отриц число массива
int GetMaxNegative(int* A, int first, int last) {
    int maxNegative=1;
    int flag = 0;
    for (int i = 1; i <= last; i++) {
        if (A[i] < 0 && (flag == 0 || maxNegative < A[i])) {
            maxNegative = A[i];
            flag = 1;

        }
    }
    if (flag == 0) throw exception("Exception: no negative numbers");
    else return maxNegative;
}

//сохранения массива в файл
bool SaveArrayInFile(int* A, int first, int last, const std::string& filename)
{
    /*
    Первое число в файле будет N, остальные - элементы массива
    */
    ofstream out;

    // Open the file.
    out.open(filename, std::ios::out | std::ios::binary);

    // Validate that the file is open.
    if (!out.is_open())
        return false;

    out << last << "\n\n";
    for (int i = first; i <= last; i++) {
        out << A[i] << endl;
    }

    out.close();

    return true;
}

//чтения количества элементов массива из файла
int ReadArrayN(const std::string& filename) {
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

//вывод массива
void DisplayArray(int* A, int first, int last) {
    for (int i = first; i <= last; i++) {
        cout << A[i] << " ";
    }
}