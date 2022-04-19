#pragma once
#include <string>

using namespace std;

class IMultipleChoiceQuiz
{
public:
	//получить вопрос и варианты ответа из файла
	virtual void getAskFromFile(string filename) = 0;
	//вывод вопроса на экран
	virtual void displayAsk() = 0;
	//перемешать варианты ответа
	virtual void shuffleAnswers() = 0;
};

