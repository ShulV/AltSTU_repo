// LR2.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <Conio.h>
#include <Windows.h>
#include <vector>
#include <fstream>

using namespace std;
const int max_count = 100;// максимальная размерность матрицы
void read(double **matrix, int *n, ifstream *fin);// функция чтения матрицы из файла
void print(double **matrix, int *n, double *e, FILE *file, bool flag);// функция вывода расширенной матрицы
bool is_diagonal_preopladanie(double **matrix, int *n);// функция, проверяющая диагональное преобладание
void search_nevyzka(double **matrix, int *n, FILE *file, vector<double> *X);// функция поиска невязки
void first_method(double **matrix, int *n, double *e, FILE *file);// решение системы линейных уравнений методом Якоби
void second_method(double **matrix, int *n, double *e, FILE *file);// решение системы линейных уравнений методом Зейделя
void random(double **matrix, int *n);// генерация случайной матрицы
// функция чтения расширенной матрицы из файла
void read(double **matrix, int *n, ifstream *fin)
{
	for (int i = 0; i < *n; i++)
	{
		for (int j = 0; j < *n + 1; j++)
		{
			*fin >> matrix[i][j];
		}
	}
}
// функция вывода расширенной матрицы в консоль и в файл
void print(double **matrix, int *n, double *e, FILE *file, bool flag)
{
	if (!flag)
	{
		for (int i = 0; i < *n; i++)
		{
			for (int j = 0; j < *n + 1; j++)
			{
				printf("%10lf ", matrix[i][j]);
				fprintf(file, "%10lf ", matrix[i][j]);
			}
			printf("\n\n");
			fprintf(file, "\n\n");
		}
	}
	else
	{
		for (int i = 0; i < *n; i++)
		{
			for (int j = 0; j < *n; j++)
			{
				printf("%10lf ", matrix[i][j]);
				fprintf(file, "%10lf ", matrix[i][j]);
			}
			printf("\n\n");
			fprintf(file, "\n\n");
		}
	}
	cout << "Точность: " << *e << endl;
	fprintf(file, "Точность: %lf", *(e));
	cout << endl;
	fprintf(file, "\n");
}

// функция, проверяющая диагональное преобладание системы
bool is_diagonal_preopladanie(double **matrix, int *n)
{
	double sum = 0;
	for (int i = 0; i < *n; i++)// прогонка по строкам
	{
		sum = 0;
		for (int j = 0; j < *n; j++)// сложение всех элементов в строке, кроме диагонального
		{
			if (i != j)
			{
				sum += abs(matrix[i][j]);
			}
		}
		if (abs(matrix[i][i]) <= sum)// проверка на условие диагонального преобладания
		{
			cout << "Ошибка, достаточное условие сходимости не выполнятеся" << endl;
			cout << "Продолжить вычисления?\n1) да\n2) нет";
			if (_getch() == '2')
			{
				cout << "Завершение работы программы!" << endl;
				return false;// сходимость нарушена
			}
			else
			{
				cout << endl << endl;
				break;
			}
		}
	}
	return true;
}
//решение системы линейных уравнений методом Якоби
void first_method(double **matrix, int *n, double *e, FILE *file)
{
	vector<double> X(*n);// текущие корни уравнения
	vector<double> X_back(*n);// корни уравнения прошлой итерации
	bool e_flag;// флаг проверки, что необходимая точность достигнута
	double current_e;// точность в очередной итерации
	int k = 0;// кол-во итераций
	double sum;// временная переменная для нахождения корней
	cout << endl << "Метод Якоби:" << endl;
	printf("|  K  |");
	fprintf(file, "|  K  |");
	for (int i = 1; i < *n+1; i++)
	{
		printf("        X%d  |", i);
		fprintf(file, "        X%d  |", i);
	}
	for (int i = 1; i < *n + 1; i++)
	{
		printf("        e%d  |", i);
		fprintf(file, "        e%d  |", i);
	}
	printf("\n");
	fprintf(file, "\n");
	// цикл с постусловием, пока не будет найдено решение системы с заданной точностью
	do{
		e_flag = true;
		// цикл по строкам матрицы, 
		//за каждую итерацию нахождение одного корня на главной диагонали текущей строки
		for (int i = 0; i < *n; i++)
		{
			sum = matrix[i][*n];
			// цикл по столбцам
			for (int j = 0; j < *n; j++)
			{
				if (i != j)
				{
					sum -= matrix[i][j] * X_back[j];
				}
			}
			X_back[i] = X[i];// запоминание предыдущего корня
			X[i] = sum / matrix[i][i];// вычисление нового корня
		}
		// вывод номера итерации и значения корней
		printf("|%3d  |", k);
		fprintf(file, "|%3d  |", k);
		for (int i = 0; i < *n; i++)
		{
			printf("%10lf  |",X[i]);
			fprintf(file, "%10lf  |", X[i]);
		}
		if (k != 0)
		{
			// нахождение текущей точности
			for (int i = 0; i < *n; i++)
			{
				current_e = abs(X[i] - X_back[i]); // abs(X[i]);
				if (current_e >= *e)// если хотя бы одна точность не соответствует необходимой, обнуление флага
				{
					e_flag = false;
				}
				printf("%10lf  |", current_e);
				fprintf(file, "%10lf  |", current_e);

			}
		}
		else
		{
			for (int i = 0; i < *n; i++)
			{
				printf("         -  |");
				fprintf(file, "         -  |");

			}
			e_flag = false;
		}
		printf("\n");
		fprintf(file, "\n");
		k++;// переход к следуещей итерации
		if (k > 500)
		{
			cout << "k>500, решение системы расходится!" << endl;
			break;
		}
	} while (!e_flag);
	search_nevyzka(matrix, n, file, &X);// поиск невязки
}

// решение системы линейных уравнений методом Зейделя
void second_method(double **matrix, int *n, double *e, FILE *file)
{
	vector<double> X(*n);// текущие корни уравнения
	vector<double> X_back(*n);// корни уравнения прошлой итерации
	bool e_flag;// флаг проверки, что необходимая точность достигнута
	double current_e;// точность при вычилении текущего корня
	int k = 0;// кол-во итераций
	double sum;// временная переменная для нахождения промежуточных вычилений
	cout << endl << "Метод Зейделя:" << endl;
	printf("|  K  |");
	fprintf(file, "|  K  |");
	for (int i = 1; i < *n + 1; i++)
	{
		printf("        X%d  |", i);
		fprintf(file, "        X%d  |", i);
	}
	for (int i = 1; i < *n + 1; i++)
	{
		printf("        e%d  |", i);
		fprintf(file, "        e%d  |", i);
	}
	printf("\n");
	fprintf(file, "\n");
	// цикл с постусловием, пока не будет достигнута необходимая точность
	do{
		e_flag = true;
		// цикл по строкам системы
		//за каждую итерацию нахождение одного корня на главной диагонали текущей строки
		for (int i = 0; i < *n; i++)
		{
			sum = 0;
			for (int j = 0; j < *n; j++)
			{
				if (i != j)
				{
					sum -= matrix[i][j] * X[j];// разность произведения элементов строки на соответствующий корень
				}
			}
			sum += matrix[i][*n];
			X_back[i] = X[i];// запоминания предыдущего корня для поиска точности
			X[i] = sum / matrix[i][i];// вычисление очередного корня
		}
		printf("|%3d  |", k);
		fprintf(file, "|%3d  |", k);
		for (int i = 0; i < *n; i++)
		{
			printf("%10lf  |", X[i]);
			fprintf(file, "%10lf  |", X[i]);
		}
		if (k != 0)
		{
			// вычисление невязки
			for (int i = 0; i < *n; i++)
			{
				current_e = abs(X[i] - X_back[i]); // abs(X[i]);
				if (current_e >= *e)// если хотя бы одна точность не соответствует необходимой, обнуление флага
				{
					e_flag = false;
				}
				printf("%10lf  |", current_e);
				fprintf(file, "%10lf  |", current_e);

			}
		}
		else
		{
			for (int i = 0; i < *n; i++)
			{
				printf("         -  |");
				fprintf(file, "         -  |");

			}
			e_flag = false;
		}
		printf("\n");
		fprintf(file, "\n");
		k++;// переход к следующей итерации
		if (k > 500)
		{
			cout << "k>500, решение системы расходится!" << endl;
			break;
		}
	} while (!e_flag);
	search_nevyzka(matrix, n, file, &X);// поиск невязки
}

// функция поиска невязки и нормы невязки
void search_nevyzka(double **matrix, int *n, FILE *file, vector<double> *X)
{
	//нахождение и вывод невязки
	double *nevyzka = new double;// значение невязки
	double *max = new double;
	cout << endl << "Невязка равна:" << endl;
	fprintf(file, "Невязка равна:\n");
	// цикл по строкам матрицы, за каждую итерацию нахождения невязки для текущей строки
	for (int i = 0; i < *n; i++)
	{
		*nevyzka = 0;
		for (int j = 0; j < *n; j++)
		{
			*nevyzka += matrix[i][j] * X->at(j);
		}
		*nevyzka -= matrix[i][*n];
		// нахождение нормы невязки
		if (i == 0)
		{
			*max = abs(*nevyzka);// начальное значение нормы
		}
		else if (*max < abs(*nevyzka))// если найдено большее значение
		{
			*max = abs(*nevyzka);
		}
		// вывод невязки в консоль и в файл
		cout << "Строка " << i + 1 << " = " << *nevyzka << endl;
		fprintf(file, "Строка %d = %lf\n", i + 1, *nevyzka);
	}
	cout << "Норма невязки: " << *max << endl;
	delete nevyzka;
	delete max;
}

// генерация случайной матрицы
void random(double **matrix, int *n)
{
	for (int i = 0; i < *n; i++)
	{
		for (int j = 0; j < *n + 1; j++)
		{
			matrix[i][j] = (rand() % 50) + 1;
		}
	}
}



int _tmain(int argc, _TCHAR* argv[])
{
	SetConsoleCP(1251);// подключение русскоязычного ввода/вывода
	SetConsoleOutputCP(1251);
	system("Color F0");
	int n;// размерность матрицы
	double e;// точность вычислений
	double **matrix = nullptr;// указатель на динамический массив расширенной матрицы
	cout << "Выберите откуда брать данные:" << endl;
	cout << "1) из файла input.dat" << endl;
	cout << "2) сгенерировать автоматически" << endl;
	char c = _getch();
	if (c == '1')
	{
		system("cls");
		ifstream fin("input.dat");
		if (fin.is_open() == false)
		{
			cout << "Ошибка открытия файла input.dat\nзавершение работы" << endl;
			_getch();
			return 1;
		}
		// чтение данных из файла
		fin >> e;
		fin >> n;
		matrix = new double *[n];
		for (int i = 0; i < n; i++)
		{
			matrix[i] = new double[n + 1];
		}
		read(matrix, &n, &fin);
		fin.close();
	}
	else
	{
		system("cls");
		cout << "Введите размерность матрицы: ";
		cin >> n;
		cout << "Введите необходимую точность: ";
		cin >> e;
		matrix = new double *[n];
		for (int i = 0; i < n; i++)
		{
			matrix[i] = new double[n + 1];
		}
		random(matrix, &n);
	}
	FILE *file = fopen("output.dat", "w");
	if (file == NULL)
	{
		cout << "Ошибка открытия файла output.dat\nзавершение работы" << endl;
		_getch();
		return 1;
	}
	cout << "Расширенная матрица:" << endl;
	fprintf(file, "Расширенная матрица:\n");
	print(matrix, &n, &e, file, 0);// вывод расширенной матрицы в консоль
	// проверка на диагональное преобладание
	if (!is_diagonal_preopladanie(matrix, &n))
	{
		system("pause");
		return 1;
	}
	// решение системы методом Якоби
	first_method(matrix, &n, &e, file);
	cout << endl;
	fprintf(file, "\n");
	// решение системы методом Зейделя
	second_method(matrix, &n, &e, file);
	fclose(file);
	system("pause");
	return 0;
}

