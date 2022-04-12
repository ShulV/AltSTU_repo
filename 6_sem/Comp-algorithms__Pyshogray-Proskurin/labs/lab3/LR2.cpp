// LR2.cpp: ���������� ����� ����� ��� ����������� ����������.
//

#include "stdafx.h"
#include <iostream>
#include <Conio.h>
#include <Windows.h>
#include <vector>
#include <fstream>

using namespace std;
const int max_count = 100;// ������������ ����������� �������
void read(double **matrix, int *n, ifstream *fin);// ������� ������ ������� �� �����
void print(double **matrix, int *n, double *e, FILE *file, bool flag);// ������� ������ ����������� �������
bool is_diagonal_preopladanie(double **matrix, int *n);// �������, ����������� ������������ ������������
void search_nevyzka(double **matrix, int *n, FILE *file, vector<double> *X);// ������� ������ �������
void first_method(double **matrix, int *n, double *e, FILE *file);// ������� ������� �������� ��������� ������� �����
void second_method(double **matrix, int *n, double *e, FILE *file);// ������� ������� �������� ��������� ������� �������
void random(double **matrix, int *n);// ��������� ��������� �������
// ������� ������ ����������� ������� �� �����
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
// ������� ������ ����������� ������� � ������� � � ����
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
	cout << "��������: " << *e << endl;
	fprintf(file, "��������: %lf", *(e));
	cout << endl;
	fprintf(file, "\n");
}

// �������, ����������� ������������ ������������ �������
bool is_diagonal_preopladanie(double **matrix, int *n)
{
	double sum = 0;
	for (int i = 0; i < *n; i++)// �������� �� �������
	{
		sum = 0;
		for (int j = 0; j < *n; j++)// �������� ���� ��������� � ������, ����� �������������
		{
			if (i != j)
			{
				sum += abs(matrix[i][j]);
			}
		}
		if (abs(matrix[i][i]) <= sum)// �������� �� ������� ������������� ������������
		{
			cout << "������, ����������� ������� ���������� �� �����������" << endl;
			cout << "���������� ����������?\n1) ��\n2) ���";
			if (_getch() == '2')
			{
				cout << "���������� ������ ���������!" << endl;
				return false;// ���������� ��������
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
//������� ������� �������� ��������� ������� �����
void first_method(double **matrix, int *n, double *e, FILE *file)
{
	vector<double> X(*n);// ������� ����� ���������
	vector<double> X_back(*n);// ����� ��������� ������� ��������
	bool e_flag;// ���� ��������, ��� ����������� �������� ����������
	double current_e;// �������� � ��������� ��������
	int k = 0;// ���-�� ��������
	double sum;// ��������� ���������� ��� ���������� ������
	cout << endl << "����� �����:" << endl;
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
	// ���� � ������������, ���� �� ����� ������� ������� ������� � �������� ���������
	do{
		e_flag = true;
		// ���� �� ������� �������, 
		//�� ������ �������� ���������� ������ ����� �� ������� ��������� ������� ������
		for (int i = 0; i < *n; i++)
		{
			sum = matrix[i][*n];
			// ���� �� ��������
			for (int j = 0; j < *n; j++)
			{
				if (i != j)
				{
					sum -= matrix[i][j] * X_back[j];
				}
			}
			X_back[i] = X[i];// ����������� ����������� �����
			X[i] = sum / matrix[i][i];// ���������� ������ �����
		}
		// ����� ������ �������� � �������� ������
		printf("|%3d  |", k);
		fprintf(file, "|%3d  |", k);
		for (int i = 0; i < *n; i++)
		{
			printf("%10lf  |",X[i]);
			fprintf(file, "%10lf  |", X[i]);
		}
		if (k != 0)
		{
			// ���������� ������� ��������
			for (int i = 0; i < *n; i++)
			{
				current_e = abs(X[i] - X_back[i]); // abs(X[i]);
				if (current_e >= *e)// ���� ���� �� ���� �������� �� ������������� �����������, ��������� �����
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
		k++;// ������� � ��������� ��������
		if (k > 500)
		{
			cout << "k>500, ������� ������� ����������!" << endl;
			break;
		}
	} while (!e_flag);
	search_nevyzka(matrix, n, file, &X);// ����� �������
}

// ������� ������� �������� ��������� ������� �������
void second_method(double **matrix, int *n, double *e, FILE *file)
{
	vector<double> X(*n);// ������� ����� ���������
	vector<double> X_back(*n);// ����� ��������� ������� ��������
	bool e_flag;// ���� ��������, ��� ����������� �������� ����������
	double current_e;// �������� ��� ��������� �������� �����
	int k = 0;// ���-�� ��������
	double sum;// ��������� ���������� ��� ���������� ������������� ���������
	cout << endl << "����� �������:" << endl;
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
	// ���� � ������������, ���� �� ����� ���������� ����������� ��������
	do{
		e_flag = true;
		// ���� �� ������� �������
		//�� ������ �������� ���������� ������ ����� �� ������� ��������� ������� ������
		for (int i = 0; i < *n; i++)
		{
			sum = 0;
			for (int j = 0; j < *n; j++)
			{
				if (i != j)
				{
					sum -= matrix[i][j] * X[j];// �������� ������������ ��������� ������ �� ��������������� ������
				}
			}
			sum += matrix[i][*n];
			X_back[i] = X[i];// ����������� ����������� ����� ��� ������ ��������
			X[i] = sum / matrix[i][i];// ���������� ���������� �����
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
			// ���������� �������
			for (int i = 0; i < *n; i++)
			{
				current_e = abs(X[i] - X_back[i]); // abs(X[i]);
				if (current_e >= *e)// ���� ���� �� ���� �������� �� ������������� �����������, ��������� �����
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
		k++;// ������� � ��������� ��������
		if (k > 500)
		{
			cout << "k>500, ������� ������� ����������!" << endl;
			break;
		}
	} while (!e_flag);
	search_nevyzka(matrix, n, file, &X);// ����� �������
}

// ������� ������ ������� � ����� �������
void search_nevyzka(double **matrix, int *n, FILE *file, vector<double> *X)
{
	//���������� � ����� �������
	double *nevyzka = new double;// �������� �������
	double *max = new double;
	cout << endl << "������� �����:" << endl;
	fprintf(file, "������� �����:\n");
	// ���� �� ������� �������, �� ������ �������� ���������� ������� ��� ������� ������
	for (int i = 0; i < *n; i++)
	{
		*nevyzka = 0;
		for (int j = 0; j < *n; j++)
		{
			*nevyzka += matrix[i][j] * X->at(j);
		}
		*nevyzka -= matrix[i][*n];
		// ���������� ����� �������
		if (i == 0)
		{
			*max = abs(*nevyzka);// ��������� �������� �����
		}
		else if (*max < abs(*nevyzka))// ���� ������� ������� ��������
		{
			*max = abs(*nevyzka);
		}
		// ����� ������� � ������� � � ����
		cout << "������ " << i + 1 << " = " << *nevyzka << endl;
		fprintf(file, "������ %d = %lf\n", i + 1, *nevyzka);
	}
	cout << "����� �������: " << *max << endl;
	delete nevyzka;
	delete max;
}

// ��������� ��������� �������
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
	SetConsoleCP(1251);// ����������� �������������� �����/������
	SetConsoleOutputCP(1251);
	system("Color F0");
	int n;// ����������� �������
	double e;// �������� ����������
	double **matrix = nullptr;// ��������� �� ������������ ������ ����������� �������
	cout << "�������� ������ ����� ������:" << endl;
	cout << "1) �� ����� input.dat" << endl;
	cout << "2) ������������� �������������" << endl;
	char c = _getch();
	if (c == '1')
	{
		system("cls");
		ifstream fin("input.dat");
		if (fin.is_open() == false)
		{
			cout << "������ �������� ����� input.dat\n���������� ������" << endl;
			_getch();
			return 1;
		}
		// ������ ������ �� �����
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
		cout << "������� ����������� �������: ";
		cin >> n;
		cout << "������� ����������� ��������: ";
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
		cout << "������ �������� ����� output.dat\n���������� ������" << endl;
		_getch();
		return 1;
	}
	cout << "����������� �������:" << endl;
	fprintf(file, "����������� �������:\n");
	print(matrix, &n, &e, file, 0);// ����� ����������� ������� � �������
	// �������� �� ������������ ������������
	if (!is_diagonal_preopladanie(matrix, &n))
	{
		system("pause");
		return 1;
	}
	// ������� ������� ������� �����
	first_method(matrix, &n, &e, file);
	cout << endl;
	fprintf(file, "\n");
	// ������� ������� ������� �������
	second_method(matrix, &n, &e, file);
	fclose(file);
	system("pause");
	return 0;
}

