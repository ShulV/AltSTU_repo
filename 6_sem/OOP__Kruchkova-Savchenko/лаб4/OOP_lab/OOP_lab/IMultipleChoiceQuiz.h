#pragma once
#include <string>

using namespace std;

class IMultipleChoiceQuiz
{
	//�������� ������ � �������� ������ �� �����
	virtual void getAskFromFile(string filename) = 0;
	//����� ������� �� �����
	virtual void displayAsk() = 0;
	//���������� �������� ������
	virtual void shuffleAnswers() = 0;
};

