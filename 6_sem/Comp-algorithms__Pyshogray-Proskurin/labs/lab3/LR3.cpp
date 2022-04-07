// LR3.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <Conio.h>
#include <Windows.h>
#include <vector>
#include <fstream>

using namespace std;
void read(double **matrix, double *X, int *n, ifstream *fin);// функция чтения матрицы из файла
void print(double **matrix, double *X, int *n, double *e, FILE *file);// функция вывода матрицы
void find_y(double **matrix, const double *X, int *n, double *e, FILE *file, double *X_new, double *lambda);// функция поиска наибольшей лямбды
void mul_matrix(double **matrix, double *X, double *X_previous, int *n);// умножение вектора X на матрицу А
double scalar_mul(double *vector_one, double *vector_two, int *n);// скалярное умножение векторов
void normirovanie(double *vector, int *n);// нормирование вектора
void invert_matrix(double **matrix, int *n);// поиск обратной матрицы методом Гаусса 
double** E(int* n);// формирование единичной матрицы, заданного размера
void near_lambda(double **matrix, int *n, double *X, double *lambda0, double *e, double *X_new, double *lambda, FILE *file);//поиск лямбды ближйшей к заданному числу
void mult_matrix_by_num(double** matrix, int *n, double mult);// умножение матрицы на число
void subtract_matrix_from_matrix(double** matrix1, double** matrix2, int* n);// вычиатние матриц



// функция чтения матрицы из файла
void read(double **matrix, double *X, int *n, ifstream *fin)
{
	for (int i = 0; i < *n; i++)
	{
		for (int j = 0; j < *n; j++)
		{
			*fin >> matrix[i][j];
		}
	}
	for (int i = 0; i < *n; i++)
	{
		*fin >> X[i];
	}
}
// функция вывода матрицы в консоль и в файл
void print(double **matrix, double *X, int *n, double *e, FILE *file)
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
	cout << "Произвольный вектор: ";
	fprintf(file,"Произвольный вектор: ");
	for (int i = 0; i < *n; i++)
	{
		cout << X[i] << " ";
		fprintf(file, "%lf ", X[i]);
	}
	cout << endl << "Точность: " << *e << endl;
	fprintf(file, "\nТочность: %lf", *e);
	cout << endl;
	fprintf(file, "\n");
}
// умножение матрицы на число
void mult_matrix_by_num(double** matrix, int *n, double *mult) {
	for (int i = 0; i < *n; i++)
	{
		for (int j = 0; j < *n; j++) {
			matrix[i][j] *= *mult;
		}
	}
}

// вычитание матрицы из другой матрицы
void subtract_matrix_from_matrix(double** matrix1, double** matrix2, int* n) {
	for (int i = 0; i < *n; i++)
	{
		for (int j = 0; j < *n; j++) {
			matrix2[i][j] = matrix1[i][j] - matrix2[i][j];
		}
	}
}

// алгоритм вычиления лямбда наибольшего по модулю и собственного вектора
void find_y(double **matrix, const double *X, int *n, double *e, FILE *file, double *X_new, double *lambda)
{
	double *X_previous = new double[*n];// вектор предыдущей итерации
	double y = 0;// значение лямбда
	double y_previous;// значение лямбда предыдущей итерации
	double current_e;// текущая точность
	int k = 0;// кол-во итераций
	for (int i = 0; i < *n; i++)
	{
		X_new[i] = X[i];
	}
	//цикл с постусловием пока не найдена лямбда необходимой точности
	do{
		k++;// следующая итерация
		for (int i = 0; i < *n; i++)// запоминание текущего вектора в предыдущий
		{
			X_previous[i] = X_new[i];
		}
		y_previous = y;//запоминание текущей лямбды
		mul_matrix(matrix, X_new, X_previous, n);// умножение вектора на матрицу А
		y = scalar_mul(X_new, X_previous, n) / scalar_mul(X_previous, X_previous, n);// деление скалярного произведение векторов
		current_e = abs(y - y_previous);
		normirovanie(X_new, n);// нормирование вектора
	} while (current_e >= *e);// проверка условия выхода из цикла
	cout << "количество итераций: " << k << endl;
	fprintf(file, "количество итераций: %d", k);
	*lambda = y;
	delete[] X_previous;
}
// умножение вектора X на матрицу А
void mul_matrix(double **matrix, double *X, double *X_previous, int *n)
{
	for (int i = 0; i < *n; i++)
	{
		X[i] = 0;
		for (int j = 0; j < *n; j++)
			X[i] += matrix[i][j] * X_previous[j];
	}
}
// скалярное произведение векторов
double scalar_mul(double *vector_one, double *vector_two, int *n)
{
	double answer = 0;// сумма скалярного произведения
	for (int i = 0; i < *n; i++)
	{
		answer += vector_one[i] * vector_two[i];
	}
	return answer;
}
//нормирование вектора
void normirovanie(double *vector, int *n)
{
	double sum = 0;// норма
	for (int i = 0; i < *n; i++)
	{
		sum += vector[i];
	}
	for (int i = 0; i < *n; i++)
	{
		vector[i] /= sum;
	}
}
// получение единичной матрицы n*n
double** E(int *n) {
	double** e_matrix = new double*[*n];// выделение памяти под массив матрицы А
	for (int i = 0; i < *n; i++)
	{
		e_matrix[i] = new double[*n];
		for (int j = 0; j < *n; j++) {
			e_matrix[i][j] = (i == j) ? 1 : 0;
		}
	}
	return e_matrix;
}
// Получение обратной матрицы методом Гаусса
void invert_matrix(double **matrix, int *n) {
	
	double **matrix_e = E(n);
	double **copy_matrix = new double *[*n];// выделение памяти под массив матрицы А
	for (int i = 0; i < *n; i++)
	{
		copy_matrix[i] = new double[*n];
	}
	for (int i = 0; i < *n; i++)
	{
		for (int j = 0; j < *n; j++)
		{
			copy_matrix[i][j] = matrix[i][j];
		}
	}

	for (int i = 0; i < *n; ++i) {

		// находим главный элемент
		double maxElement = 0;
		int maxElementIndex = i;
		for (int j = i; j < *n; ++j) {
			if (maxElement < copy_matrix[j][i]) {
				maxElement = copy_matrix[j][i];
				maxElementIndex = j;
			}
		}

		// проводим цикл исключений
		for (int j = i; j < *n; ++j) {
			if (j != maxElementIndex && copy_matrix[j][i] != 0) {
				double c = copy_matrix[j][i] / maxElement;
				for (int k = 0; k < *n; ++k)
					copy_matrix[j][k] -= copy_matrix[maxElementIndex][k] * c;

				for (int k = 0; k < *n; ++k)
					matrix_e[j][k] -= matrix_e[maxElementIndex][k] * c;
			}
		}

		// замена строк
		if (i != maxElementIndex) {
			swap(copy_matrix[i], copy_matrix[maxElementIndex]);
			swap(matrix_e[i], matrix_e[maxElementIndex]);
		}
	}

	// обратный ход
	for (int k = 0; k < *n; ++k) {

		for (int i = *n - 1; i >= 0; --i) {

			// S(Aij), j > i
			double sum = 0;
			for (int j = i + 1; j < *n; ++j)
				sum += copy_matrix[i][j] * matrix[j][k];

			if (std::abs(copy_matrix[i][i]) < 0.00001)
			{
				return;
			}

			// xi = (bi - S(Aij) ) / Aii, j > i
			matrix[i][k] = (matrix_e[i][k] - sum) / copy_matrix[i][i];
		}

	}
	for (int i = 0; i < *n; i++)
	{
		delete[] copy_matrix[i];
	}
	delete[] copy_matrix;
}
void near_lambda(double **matrix, int *n, double *X, double *lambda0, double *e, double *X_new, double *lambda, FILE *file)
{
	double **matrix_B = E(n);// доп матрица B (единичная)
	mult_matrix_by_num(matrix_B, n, lambda0);// умножение матрицы B на лямбда0 
	subtract_matrix_from_matrix(matrix, matrix_B, n);// вычитание матрицы B из начальной матрицы, результат в B
	invert_matrix(matrix_B, n);// поиск обртаной матрицы B
	find_y(matrix_B, X, n, e, file, X_new, lambda);// вычисление наибольшего лямбда относительно матрицы B
	*lambda = (1. / (*lambda)) + *lambda0;// нахождение ближайшего лямбда к заданной
	// очистка памяти
	for (int i = 0; i < *n; i++)
	{
		delete[] matrix_B[i];
	}
	delete[] matrix_B;
}


int _tmain(int argc, _TCHAR* argv[])
{
	SetConsoleCP(1251);// подключение русскоязычного ввода/вывода
	SetConsoleOutputCP(1251);
	//system("Color F0");
	int n;// размерность матрицы
	double e;// точность вычислений
	double **matrix = nullptr;// указатель на динамический массив матрицы
	double *X = nullptr;// указатель на произвольный динамический вектор
	double *X_new = nullptr;// массив для хранения собственных векторов
	double *lambda0 = new double;// заданное лямбда
	double *lambda = new double;// найденная лямбда
	// открытие файла для чтения
	ifstream fin("input.dat");
	if (fin.is_open() == false)
	{
		cout << "Ошибка открытия файла input.dat\nзавершение работы" << endl;
		_getch();
		return 1;
	}
	// чтение данных из файла
	fin >> *lambda0;// чтение заданной лямбды
	fin >> e;// чтение точности
	fin >> n;//чтение размерности
	matrix = new double *[n];// выделение памяти под массив матрицы А
	for (int i = 0; i < n; i++)
	{
		matrix[i] = new double[n];
	}
	X = new double[n];// выделение памяти под произвольный вектор
	X_new = new double[n];// собственный вектор
	read(matrix, X, &n, &fin);// заполнение матрицы
	fin.close();// закрытие файла
	FILE *file = fopen("output.dat", "w");
	if (file == NULL)
	{
		cout << "Ошибка открытия файла output.dat\nзавершение работы" << endl;
		_getch();
		return 1;
	}
	cout << "Матрица:" << endl;
	fprintf(file, "Матрица:\n");
	print(matrix, X, &n, &e, file);// вывод матрицы в консоль
	cout << "Поиск наибольшее лямбда по модулю:" << endl;
	fprintf(file, "Поиск наибольшее лямбда по модулю:\n");
	find_y(matrix, X, &n, &e, file, X_new, lambda);// поиск наибольшего лямбда
	cout << "Наибольшее лямбда по модулю: "<<*lambda << endl;
	fprintf(file, "Наибольшее лямбда по модулю: %lf\n", *lambda);
	cout << "Собственный вектор X: ";
	fprintf(file,"Собственный вектор X: ");
	for (int i = 0; i < n; i++)
	{
		cout << X_new[i] << " ";
		fprintf(file, "%lf ", X_new[i]);
	}
	cout << endl << endl;
	fprintf(file, "\n\n");
	double temp_lambda = *lambda + 0.1;
	double temp_lambda1 = -*lambda - 0.1;
	double temp_lambda2 = 0.1;
	// наибольшее лямбда
	cout << "Поиск наибольшего лямбда:" << endl;
	fprintf(file, "Поиск наибольшего лямбда:\n");
	near_lambda(matrix, &n, X, &temp_lambda, &e, X_new, lambda, file);
	cout << "Наибольшее лямбда: "<<*lambda << endl;
	fprintf(file, "Наибольшее лямбда: %lf\n", *lambda);
	cout << "Собственный вектор X: ";
	for (int i = 0; i < n; i++)
	{
		cout << X_new[i] << " ";
		fprintf(file, "%lf ", X_new[i]);
	}
	cout << endl << endl;
	fprintf(file, "\n\n");
	// наименьшее лямбда
	cout << "Поиск наименьшего лямбда:" << endl;
	fprintf(file,"Поиск наименьшего лямбда:\n");
	near_lambda(matrix, &n, X, &temp_lambda1, &e, X_new, lambda, file);
	cout << "Наименьшее лямбда: " << *lambda << endl;
	fprintf(file, "Наименьшее лямбда: %lf\n", *lambda);
	cout << "Собственный вектор X: ";
	for (int i = 0; i < n; i++)
	{
		cout << X_new[i] << " ";
		fprintf(file, "%lf ", X_new[i]);
	}
	cout << endl << endl;
	fprintf(file, "\n\n");
	// наименьшее лямбда по модулю
	cout << "Поиск наименьшего лямбда по модулю:" << endl;
	fprintf(file,"Поиск наименьшего лямбда по модулю:\n");
	near_lambda(matrix, &n, X, &temp_lambda2, &e, X_new, lambda, file);
	cout << "Наименьшее лямбда по модулю: " << abs(*lambda) << endl;
	fprintf(file, "Наименьшее лямбда по модулю: %lf\n", abs(*lambda));
	cout << "Собственный вектор X: ";
	for (int i = 0; i < n; i++)
	{
		cout << X_new[i] << " ";
		fprintf(file, "%lf ", X_new[i]);
	}
	cout << endl << endl;
	fprintf(file, "\n\n");
	//ближайшее лямбда к лямбда0
	cout << "Поиск ближайшего лямбда к " << *lambda0 << ": " << endl;
	fprintf(file, "Поиск ближайшего лямбда к &lf:\n", *lambda0);
	near_lambda(matrix, &n, X, lambda0, &e, X_new, lambda, file);
	cout << "Лямбда: " << *lambda << endl;
	fprintf(file, "Лямбда: %lf\n", *lambda);
	cout << "Собственный вектор X: ";
	for (int i = 0; i < n; i++)
	{
		cout << X_new[i] << " ";
		fprintf(file, "%lf ", X_new[i]);
	}
	cout << endl << endl;
	fprintf(file, "\n\n");
	//очистка памяти
	for (int i = 0; i < n; i++)
	{
		delete[] matrix[i];
	}
	delete[] matrix;
	delete[] X;
	delete[] X_new;
	delete lambda0;
	delete lambda;
	fclose(file);
	system("pause");
	return 0;
}

