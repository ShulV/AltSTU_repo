// LR3.cpp: ���������� ����� ����� ��� ����������� ����������.
//

#include "stdafx.h"
#include <iostream>
#include <Conio.h>
#include <Windows.h>
#include <vector>
#include <fstream>

using namespace std;
void read(double **matrix, double *X, int *n, ifstream *fin);// ������� ������ ������� �� �����
void print(double **matrix, double *X, int *n, double *e, FILE *file);// ������� ������ �������
void find_y(double **matrix, const double *X, int *n, double *e, FILE *file, double *X_new, double *lambda);// ������� ������ ���������� ������
void mul_matrix(double **matrix, double *X, double *X_previous, int *n);// ��������� ������� X �� ������� �
double scalar_mul(double *vector_one, double *vector_two, int *n);// ��������� ��������� ��������
void normirovanie(double *vector, int *n);// ������������ �������
void invert_matrix(double **matrix, int *n);// ����� �������� ������� ������� ������ 
double** E(int* n);// ������������ ��������� �������, ��������� �������
void near_lambda(double **matrix, int *n, double *X, double *lambda0, double *e, double *X_new, double *lambda, FILE *file);//����� ������ �������� � ��������� �����
void mult_matrix_by_num(double** matrix, int *n, double mult);// ��������� ������� �� �����
void subtract_matrix_from_matrix(double** matrix1, double** matrix2, int* n);// ��������� ������



// ������� ������ ������� �� �����
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
// ������� ������ ������� � ������� � � ����
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
	cout << "������������ ������: ";
	fprintf(file,"������������ ������: ");
	for (int i = 0; i < *n; i++)
	{
		cout << X[i] << " ";
		fprintf(file, "%lf ", X[i]);
	}
	cout << endl << "��������: " << *e << endl;
	fprintf(file, "\n��������: %lf", *e);
	cout << endl;
	fprintf(file, "\n");
}
// ��������� ������� �� �����
void mult_matrix_by_num(double** matrix, int *n, double *mult) {
	for (int i = 0; i < *n; i++)
	{
		for (int j = 0; j < *n; j++) {
			matrix[i][j] *= *mult;
		}
	}
}

// ��������� ������� �� ������ �������
void subtract_matrix_from_matrix(double** matrix1, double** matrix2, int* n) {
	for (int i = 0; i < *n; i++)
	{
		for (int j = 0; j < *n; j++) {
			matrix2[i][j] = matrix1[i][j] - matrix2[i][j];
		}
	}
}

// �������� ��������� ������ ����������� �� ������ � ������������ �������
void find_y(double **matrix, const double *X, int *n, double *e, FILE *file, double *X_new, double *lambda)
{
	double *X_previous = new double[*n];// ������ ���������� ��������
	double y = 0;// �������� ������
	double y_previous;// �������� ������ ���������� ��������
	double current_e;// ������� ��������
	int k = 0;// ���-�� ��������
	for (int i = 0; i < *n; i++)
	{
		X_new[i] = X[i];
	}
	//���� � ������������ ���� �� ������� ������ ����������� ��������
	do{
		k++;// ��������� ��������
		for (int i = 0; i < *n; i++)// ����������� �������� ������� � ����������
		{
			X_previous[i] = X_new[i];
		}
		y_previous = y;//����������� ������� ������
		mul_matrix(matrix, X_new, X_previous, n);// ��������� ������� �� ������� �
		y = scalar_mul(X_new, X_previous, n) / scalar_mul(X_previous, X_previous, n);// ������� ���������� ������������ ��������
		current_e = abs(y - y_previous);
		normirovanie(X_new, n);// ������������ �������
	} while (current_e >= *e);// �������� ������� ������ �� �����
	cout << "���������� ��������: " << k << endl;
	fprintf(file, "���������� ��������: %d", k);
	*lambda = y;
	delete[] X_previous;
}
// ��������� ������� X �� ������� �
void mul_matrix(double **matrix, double *X, double *X_previous, int *n)
{
	for (int i = 0; i < *n; i++)
	{
		X[i] = 0;
		for (int j = 0; j < *n; j++)
			X[i] += matrix[i][j] * X_previous[j];
	}
}
// ��������� ������������ ��������
double scalar_mul(double *vector_one, double *vector_two, int *n)
{
	double answer = 0;// ����� ���������� ������������
	for (int i = 0; i < *n; i++)
	{
		answer += vector_one[i] * vector_two[i];
	}
	return answer;
}
//������������ �������
void normirovanie(double *vector, int *n)
{
	double sum = 0;// �����
	for (int i = 0; i < *n; i++)
	{
		sum += vector[i];
	}
	for (int i = 0; i < *n; i++)
	{
		vector[i] /= sum;
	}
}
// ��������� ��������� ������� n*n
double** E(int *n) {
	double** e_matrix = new double*[*n];// ��������� ������ ��� ������ ������� �
	for (int i = 0; i < *n; i++)
	{
		e_matrix[i] = new double[*n];
		for (int j = 0; j < *n; j++) {
			e_matrix[i][j] = (i == j) ? 1 : 0;
		}
	}
	return e_matrix;
}
// ��������� �������� ������� ������� ������
void invert_matrix(double **matrix, int *n) {
	
	double **matrix_e = E(n);
	double **copy_matrix = new double *[*n];// ��������� ������ ��� ������ ������� �
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

		// ������� ������� �������
		double maxElement = 0;
		int maxElementIndex = i;
		for (int j = i; j < *n; ++j) {
			if (maxElement < copy_matrix[j][i]) {
				maxElement = copy_matrix[j][i];
				maxElementIndex = j;
			}
		}

		// �������� ���� ����������
		for (int j = i; j < *n; ++j) {
			if (j != maxElementIndex && copy_matrix[j][i] != 0) {
				double c = copy_matrix[j][i] / maxElement;
				for (int k = 0; k < *n; ++k)
					copy_matrix[j][k] -= copy_matrix[maxElementIndex][k] * c;

				for (int k = 0; k < *n; ++k)
					matrix_e[j][k] -= matrix_e[maxElementIndex][k] * c;
			}
		}

		// ������ �����
		if (i != maxElementIndex) {
			swap(copy_matrix[i], copy_matrix[maxElementIndex]);
			swap(matrix_e[i], matrix_e[maxElementIndex]);
		}
	}

	// �������� ���
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
	double **matrix_B = E(n);// ��� ������� B (���������)
	mult_matrix_by_num(matrix_B, n, lambda0);// ��������� ������� B �� ������0 
	subtract_matrix_from_matrix(matrix, matrix_B, n);// ��������� ������� B �� ��������� �������, ��������� � B
	invert_matrix(matrix_B, n);// ����� �������� ������� B
	find_y(matrix_B, X, n, e, file, X_new, lambda);// ���������� ����������� ������ ������������ ������� B
	*lambda = (1. / (*lambda)) + *lambda0;// ���������� ���������� ������ � ��������
	// ������� ������
	for (int i = 0; i < *n; i++)
	{
		delete[] matrix_B[i];
	}
	delete[] matrix_B;
}


int _tmain(int argc, _TCHAR* argv[])
{
	SetConsoleCP(1251);// ����������� �������������� �����/������
	SetConsoleOutputCP(1251);
	//system("Color F0");
	int n;// ����������� �������
	double e;// �������� ����������
	double **matrix = nullptr;// ��������� �� ������������ ������ �������
	double *X = nullptr;// ��������� �� ������������ ������������ ������
	double *X_new = nullptr;// ������ ��� �������� ����������� ��������
	double *lambda0 = new double;// �������� ������
	double *lambda = new double;// ��������� ������
	// �������� ����� ��� ������
	ifstream fin("input.dat");
	if (fin.is_open() == false)
	{
		cout << "������ �������� ����� input.dat\n���������� ������" << endl;
		_getch();
		return 1;
	}
	// ������ ������ �� �����
	fin >> *lambda0;// ������ �������� ������
	fin >> e;// ������ ��������
	fin >> n;//������ �����������
	matrix = new double *[n];// ��������� ������ ��� ������ ������� �
	for (int i = 0; i < n; i++)
	{
		matrix[i] = new double[n];
	}
	X = new double[n];// ��������� ������ ��� ������������ ������
	X_new = new double[n];// ����������� ������
	read(matrix, X, &n, &fin);// ���������� �������
	fin.close();// �������� �����
	FILE *file = fopen("output.dat", "w");
	if (file == NULL)
	{
		cout << "������ �������� ����� output.dat\n���������� ������" << endl;
		_getch();
		return 1;
	}
	cout << "�������:" << endl;
	fprintf(file, "�������:\n");
	print(matrix, X, &n, &e, file);// ����� ������� � �������
	cout << "����� ���������� ������ �� ������:" << endl;
	fprintf(file, "����� ���������� ������ �� ������:\n");
	find_y(matrix, X, &n, &e, file, X_new, lambda);// ����� ����������� ������
	cout << "���������� ������ �� ������: "<<*lambda << endl;
	fprintf(file, "���������� ������ �� ������: %lf\n", *lambda);
	cout << "����������� ������ X: ";
	fprintf(file,"����������� ������ X: ");
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
	// ���������� ������
	cout << "����� ����������� ������:" << endl;
	fprintf(file, "����� ����������� ������:\n");
	near_lambda(matrix, &n, X, &temp_lambda, &e, X_new, lambda, file);
	cout << "���������� ������: "<<*lambda << endl;
	fprintf(file, "���������� ������: %lf\n", *lambda);
	cout << "����������� ������ X: ";
	for (int i = 0; i < n; i++)
	{
		cout << X_new[i] << " ";
		fprintf(file, "%lf ", X_new[i]);
	}
	cout << endl << endl;
	fprintf(file, "\n\n");
	// ���������� ������
	cout << "����� ����������� ������:" << endl;
	fprintf(file,"����� ����������� ������:\n");
	near_lambda(matrix, &n, X, &temp_lambda1, &e, X_new, lambda, file);
	cout << "���������� ������: " << *lambda << endl;
	fprintf(file, "���������� ������: %lf\n", *lambda);
	cout << "����������� ������ X: ";
	for (int i = 0; i < n; i++)
	{
		cout << X_new[i] << " ";
		fprintf(file, "%lf ", X_new[i]);
	}
	cout << endl << endl;
	fprintf(file, "\n\n");
	// ���������� ������ �� ������
	cout << "����� ����������� ������ �� ������:" << endl;
	fprintf(file,"����� ����������� ������ �� ������:\n");
	near_lambda(matrix, &n, X, &temp_lambda2, &e, X_new, lambda, file);
	cout << "���������� ������ �� ������: " << abs(*lambda) << endl;
	fprintf(file, "���������� ������ �� ������: %lf\n", abs(*lambda));
	cout << "����������� ������ X: ";
	for (int i = 0; i < n; i++)
	{
		cout << X_new[i] << " ";
		fprintf(file, "%lf ", X_new[i]);
	}
	cout << endl << endl;
	fprintf(file, "\n\n");
	//��������� ������ � ������0
	cout << "����� ���������� ������ � " << *lambda0 << ": " << endl;
	fprintf(file, "����� ���������� ������ � &lf:\n", *lambda0);
	near_lambda(matrix, &n, X, lambda0, &e, X_new, lambda, file);
	cout << "������: " << *lambda << endl;
	fprintf(file, "������: %lf\n", *lambda);
	cout << "����������� ������ X: ";
	for (int i = 0; i < n; i++)
	{
		cout << X_new[i] << " ";
		fprintf(file, "%lf ", X_new[i]);
	}
	cout << endl << endl;
	fprintf(file, "\n\n");
	//������� ������
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

