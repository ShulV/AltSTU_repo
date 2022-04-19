#pragma once
#include "Game.h"

class MathGame : public Game {
private:
	int minNumber;
	int maxNumber;
	int curRandNum1;
	int curRandNum2;
public:

	//генерация 2 случайных чисел
	void generateRandNums();
	//подсчет суммы 2 случайных чисел
	int countRandNumsSum();
	//вывод текстового вопроса
	void displayAsk();

	//сеттеры и геттеры
	int getMinNumber();
	void setMinNumber(int _minNumber);
	int getMaxNumber();
	void setMaxNumber(int _maxNumber);
	int getCurNumber1();
	void setCurNumber1(int _curNumber1);
	int getCurNumber2();
	void setCurNumber2(int _curNumber2);

};