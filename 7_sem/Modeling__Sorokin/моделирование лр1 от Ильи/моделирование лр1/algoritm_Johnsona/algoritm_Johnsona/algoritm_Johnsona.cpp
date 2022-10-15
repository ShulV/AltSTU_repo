// algoritm_Johnsona.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <Windows.h>
#include <Conio.h>
#include <vector>

using namespace std;

//чисто абстрактный класс таблицы деталей
class Table
{
protected:
	class Line_detail// вложенный класс одной строки таблицы
	{
	public:
		int detail_a;// трудоемкость детали А
		int detail_b;// трудоемкость детали В
		int detail_c;// трудоемкость детали C (для Nx2 = 0)
		int start_number;// стартовый номер строки деталей
		Line_detail(int a, int b);
		Line_detail()
		{
			detail_a = 0;
			detail_b = 0;
			detail_c = 0;
			start_number = 0;

		}
		Line_detail::Line_detail(int a, int b, int number)
		{
			detail_a = a;
			detail_b = b;
			start_number = number;
		}
	};
	ifstream *fin;// указатель на чтение из файла
	vector<Line_detail> list;// массив строк таблицы
	void find_min(int *array_comp, int &min_index);// поиск min индекса среди 4-х эл-ов
	int T;// общее время выполнения
	// сортировка таблицы для поиска оптимальной последовательности
	void sort_list(vector<Line_detail> &table);
public:
	Table(const string &path);//конструктор
	// метод нахождения оптимальной последовательности по заданному алгоритму
	virtual void work() = 0;
	virtual void print_table() = 0;// вывод таблицы и текущего маршрута
	virtual void print_Gant() = 0;// вывод диаграммы Ганта для опред таблицы
};
// класс таблицы Nx2, наследник чисто абстрактного класса Table
class nx2 : public Table
{
public:
	nx2(const string &path) :Table(path) 
	{
		if (fin->is_open())
		{
			fin->close();     // закрываем файл
		}
	}
	// переопределнные методы
	void work() override;
	void print_table() override;
	void print_Gant() override;
};
// класс таблицы Nx3, наследник чисто абстрактного класса Table
class nx3 : public Table
{
public:
	nx3(const string &path) :Table(path)
	{
		//std::ifstream fin(path); // окрываем файл для чтения
		string line;
		if (fin->is_open())
		{
			for (auto i = list.begin(); i != list.end(); i++)
			{
				*fin >> line;
				i->detail_c = atoi(line.c_str());
			}
		}
		if (fin->is_open())
		{
			fin->close();     // закрываем файл
		}
	}
	// переопределнные методы
	void work() override;
	void print_table() override;
	void print_Gant() override;
private:
	// проверка необходимого условия для работы алгоритма Джонсона для Nx3
	bool check_condition();
	void algorithm_Johnsona();// реализация алгоритма Джонсона для Nx3
	void transposition();// алгоритм перестановок
	bool next_set();// метод реализации перестановок в таблице
	// проверка что новая перестановка предпочтительней предыдущей по времени
	int check_time();
};

Table::Table(const string &path)
{
	T = 0;
	Line_detail *temp;
	string line;
	std::auto_ptr<int> count_pair(new int);// переменная, необходимая для заполнения таблицы
	fin = new ifstream(path);// открываем файл для чтения
	if (fin->is_open())
	{
		*fin >> line;
		*count_pair = atoi(line.c_str());
		//  чтение данных из файла
		for (int i = 0; i < *count_pair; i++)
		{
			temp = new Line_detail();
			*fin >> line;
			temp->detail_a = atoi(line.c_str());
			*fin >> line;
			temp->detail_b = atoi(line.c_str());
			temp->start_number = list.size() + 1;
			list.push_back(*temp);
		}
	}
	else
	{
		cout << "Ошибка открытия файла!" << endl;
		_getch();
		exit(1);
	}
}
// метод нахождения оптимальной последовательности по заданному алгоритму
void nx2::work()
{
	sort_list(list);
}
// сортировка таблицы для поиска оптимальной последовательности
void Table::sort_list(vector<Line_detail> &table)
{
	int min_index;
	int array_comp[4];// временный массив для сравнения
	// сортировка массива по алгориту Джонсона
	for (size_t i = 0; i < table.size(); i++)
	{
		for (size_t j = 0; j < table.size() - i - 1; j++)
		{
			array_comp[0] = table.at(j).detail_a;
			array_comp[1] = table.at(j + 1).detail_a;
			array_comp[2] = table.at(j + 1).detail_b;
			array_comp[3] = table.at(j).detail_b;
			find_min(array_comp, min_index);// поиск min индекса среди 4-х
			if (min_index % 2 == 1)// если требуется перестановка
			{
				swap(table.at(j), table.at(j + 1));
			}
			
		}
	}
}

// поиск min индекса среди 4-х эл-ов
void Table::find_min(int *array_comp, int &min_index)
{
	int min = array_comp[0];
	min_index = 0;
	for (int i = 1; i < 4; i++)
	{
		if (min>array_comp[i])
		{
			min = array_comp[i];
			min_index = i;
		}
	}
}

void nx2::print_table()
{
	printf("************************************\n");
	printf("*     №     *     A     *     B    *\n");
	printf("************************************\n");
	int index = 1;
	for (auto i = list.begin(); i != list.end(); i++)
	{
		printf("*%5d(%d)   *%8d   *%8d  *\n", index, i->start_number, i->detail_a, i->detail_b);
		printf("************************************\n");
		index++;
	}
	cout << endl << "S -> ";
	for (size_t i = 0; i < list.size(); i++)
	{
		cout << i + 1 << "(" << list.at(i).start_number << "), ";
	}
	cout << endl;
}

void nx2::print_Gant()
{
	cout << "Диаграмма Ганта" << endl;
	cout << "A: ";
	for (auto i = list.begin(); i != list.end(); i++)
	{
		for (int j = 1; j <= i->detail_a; j++)
		{
			cout << i->start_number;
		}
	}

	cout << endl <<  "B: ";
	int X = list.begin()->detail_a;
	T = 0;
	int sum_a = X;
	int sum_b = 0;
	int sum_X = 0;
	for (auto i = list.begin(); i != list.end(); i++)
	{
		for (int j = 1; j <= X; j++)
		{
			cout << "x";
			T++;
		}
		for (int j = 1; j <= i->detail_b; j++)
		{
			T++;
			cout << i->start_number;
		}
		if (i + 1 != list.end())
		{
			sum_a += (i + 1)->detail_a;
			sum_b += (i)->detail_b;
			sum_X += X;
			X = sum_a - sum_b - sum_X;
			if (X < 0) X = 0;
		}
	}
	cout << endl << "T = " << T << endl;
}

void nx3::print_table()
{
	printf("***********************************************\n");
	printf("*     №     *     A     *     B    *     C    *\n");
	printf("***********************************************\n");
	int index = 1;
	for (auto i = list.begin(); i != list.end(); i++)
	{
		printf("*%5d(%d)   *%8d   *%8d  *%8d  *\n", index, i->start_number, i->detail_a, i->detail_b, i->detail_c);
		printf("***********************************************\n");
		index++;
	}
	cout << endl << "S -> ";
	for (size_t i = 0; i < list.size(); i++)
	{
		cout << i + 1 << "(" << list.at(i).start_number << "), ";
	}
	cout << endl;
}

void nx3::work()
{
	// проверка необходимого условия для работы алгоритма Джонсона для Nx3
	if (check_condition())
	{
		cout << "Условие (min_a >= max_b) || (min_c >= max_b) выполняется" << endl;
		cout << "Задача решается методом Джонсона" << endl;
		algorithm_Johnsona();
	}
	else
	{
		// решение через метод перестановок
		cout << "Условие (min_a >= max_b) || (min_c >= max_b) не выполняется" << endl;
		cout << "Задача решается методом перебора" << endl;
		transposition();
	}
}

// проверка необходимого условия для работы алгоритма Джонсона для Nx3
bool nx3::check_condition()
{
	int min_a = list.begin()->detail_a;
	int max_b = list.begin()->detail_b;
	int min_c = list.begin()->detail_c;

	for (auto i = list.begin() + 1; i != list.end(); i++)
	{
		if (min_a > i->detail_a)
		{
			min_a = i->detail_a;
		}
		if (max_b < i->detail_b)
		{
			max_b = i->detail_b;
		}
		if (min_c > i->detail_c)
		{
			min_c = i->detail_c;
		}
	}
	if (min_a >= max_b || min_c >= max_b)
	{
		//условие выполняется
		return true;
	}
	else
	{
		//условие не выполняется
		return false;
	}
}

// реализация алгоритма Джонсона для Nx3
void nx3::algorithm_Johnsona()
{
	//формирования новой таблицы через суммирование эл-ов
	vector<Line_detail> list_1 = list;
	for (auto i = list_1.begin(); i != list_1.end(); i++)
	{
		i->detail_a += i->detail_b;
		i->detail_b += i->detail_c;
	}
	sort_list(list_1);
	for (size_t i = 0; i < list.size(); i++)
	{
		if (list_1.at(i).start_number>i + 1)
		{
			swap(list.at(i), list.at(list_1.at(i).start_number - 1));
		}
	}
}

void nx3::print_Gant()
{
	cout << "Диаграмма Ганта" << endl;
	cout << "A: ";
	for (auto i = list.begin(); i != list.end(); i++)
	{
		for (int j = 1; j <= i->detail_a; j++)
		{
			cout << i->start_number;
		}
	}

	cout << endl << "B: ";
	int X = list.begin()->detail_a;
	T = 0;
	int sum_a = X;
	int sum_b = 0;
	int sum_X = 0;
	for (auto i = list.begin(); i != list.end(); i++)
	{
		for (int j = 1; j <= X; j++)
		{
			cout << "x";
		}
		for (int j = 1; j <= i->detail_b; j++)
		{
			cout << i->start_number;
		}
		if (i + 1 != list.end())
		{
			sum_a += (i + 1)->detail_a;
			sum_b += (i)->detail_b;
			sum_X += X;
			X = sum_a - sum_b - sum_X;
			if (X < 0) X = 0;
		}
	}
	cout << endl << "C: ";
	int Ta = list.at(0).detail_a;
	X = Ta;
	int Tb = list.at(0).detail_b + X;
	int Y = Tb;
	T = 0;
	for (auto i = list.begin(); i != list.end(); i++)
	{
		for (int j = 0; j < Y; j++)
		{
			cout << "Y";
			T++;
		}
		for (int j = 0; j < i->detail_c; j++)
		{
			T++;
			cout << i->start_number;
		}
		if (i + 1 != list.end())
		{
			Ta += (i + 1)->detail_a;
			X = Ta - Tb;
			if (X < 0)X = 0;
			Tb += X + (i + 1)->detail_b;
			Y = Tb - T;
			if (Y < 0)Y = 0;
		}
	}
	cout << endl << "T = " << T << endl;
}

// метод реализации перестановок в таблице
bool nx3::next_set()
{
	int j = list.size() - 2;
	while (j != -1 && list.at(j).start_number >= list.at(j+1).start_number) j--;
	if (j == -1)
		return false; // больше перестановок нет
	int k = list.size() - 1;
	while (list.at(j).start_number >= list.at(k).start_number) k--;
	swap(list.at(j), list.at(k));
	int l = j + 1, r = list.size() - 1; // сортируем оставшуюся часть последовательности
	while (l < r)
		swap(list.at(l++), list.at(r--));
	return true;
}
// проверка что новая перестановка предпочтительней предыдущей по времени
int nx3::check_time()
{
	int Ta = list.at(0).detail_a;
	int X = Ta;
	int Tb = list.at(0).detail_b + X;
	int Y = Tb;
	int Tc = Y + list.at(0).detail_c;
	// подсчет текущего времени выполнения
	for (auto i = list.begin(); i != list.end(); i++)
	{
		if (i + 1 != list.end())
		{
			Ta += (i + 1)->detail_a;
			X = Ta - Tb;
			if (X < 0)X = 0;
			Tb += X + (i + 1)->detail_b;
			Y = Tb - Tc;
			if (Y < 0)Y = 0;
			Tc += Y + (i + 1)->detail_c;
		}
	}
	return Tc;
}
// метод перестановок
void nx3::transposition()
{
	int T = check_time();
	int current_T;
	vector<Line_detail> temp_table = list;
	while (next_set())
	{
		current_T = check_time();
		if (T>current_T)
		{
			T = current_T;
			temp_table = list;
		}
	}
	list = temp_table;
}
//////////////////nx2//////////////////////
void count_nx2()
{
	system("cls");
	auto_ptr<Table> table_nx2(new nx2("date_nx2.txt"));
	cout << "Исходные данные:" << endl;
	table_nx2->print_table();
	table_nx2->print_Gant();
	table_nx2->work();
	cout << endl << "Оптимальная последовательность:" << endl;
	table_nx2->print_table();
	table_nx2->print_Gant();
}

//////////////////nx3//////////////////////
void count_nx3()
{
	system("cls");
	auto_ptr<Table> table_nx3(new nx3("date_nx3.txt"));
	cout << "Исходные данные:" << endl;
	table_nx3->print_table();
	table_nx3->print_Gant();
	table_nx3->work();
	cout << endl << "Оптимальная последовательность:" << endl;
	table_nx3->print_table();
	table_nx3->print_Gant();
}

int _tmain(int argc, _TCHAR* argv[])
{
	SetConsoleCP(1251);// подключение русскоязычного ввода/вывода
	SetConsoleOutputCP(1251);
	system("Color F0");
	char choise;	
	//int b = 2;
	//int a[4] = { b = 1, 2, 3, 4 };
	do{
		system("cls");
		cout << "Выберите кол-во станков:" << endl;
		cout << "1.   nx2" << endl;
		cout << "2.   nx3" << endl;
		cout << "3.   Выход" << endl;
		choise = _getch();
		switch (choise)
		{
		case '1':
			count_nx2(); 
			_getch(); break;
		case '2':
			count_nx3(); 
			_getch(); break;
		default:
			break;
		}
	} while (choise != '3');
	return 0;
}

