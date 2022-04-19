#pragma once
#include "Game.h"
#include "IMultipleChoiceQuiz.h"
#include <string>
#include <vector>

using namespace std;

class RusLangGame : public Game
{
private:
	string ask;
	vector<string> answers;
public:
	RusLangGame();
	~RusLangGame();

	//получить вопрос и варианты ответа из файла
	void getAskFromFile(string filename);
	//вывод вопроса на экран
	void displayAsk();
	//перемешать варианты ответа
	void shuffleAnswers();

	//сеттеры и геттеры
	string getAsk();
	void setAsk(string _ask);
	vector<string> getAnswers();
	void setAnswers(vector<string> _answers);

};

