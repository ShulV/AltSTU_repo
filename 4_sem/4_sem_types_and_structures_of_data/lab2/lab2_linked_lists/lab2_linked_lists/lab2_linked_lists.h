#pragma once
#include "List.h"

int ReadArrayN(const std::string& filename);//чтения количества элементов массива из файла
bool SaveListInFile(List<int>& list, const std::string& filename);//сохранения массива в файл
void DisplayList(List<int>& list);
