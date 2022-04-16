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

	//�������� ������ � �������� ������ �� �����
	void getAskFromFile(string filename);
	//����� ������� �� �����
	void displayAsk();
	//���������� �������� ������
	void shuffleAnswers();

	//������� � �������
	string getAsk();
	void setAsk(string _ask);
	vector<string> getAnswers();
	void setAnswers(vector<string> _answers);

};

