#pragma once
#include "Game.h"

class MathGame : public Game {
private:
	int minNumber;
	int maxNumber;
	int curRandNum1;
	int curRandNum2;
public:

	//��������� 2 ��������� �����
	void generateRandNums();
	//������� ����� 2 ��������� �����
	int countRandNumsSum();
	//����� ���������� �������
	void displayAsk();

	//������� � �������
	int getMinNumber();
	void setMinNumber(int _minNumber);
	int getMaxNumber();
	void setMaxNumber(int _maxNumber);
	int getCurNumber1();
	void setCurNumber1(int _curNumber1);
	int getCurNumber2();
	void setCurNumber2(int _curNumber2);

};