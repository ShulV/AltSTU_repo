#include "IGame.h"
#include "ITextAsk.h"
#include "IMultipleChoiceQuiz.h"
#include <iostream>
#include <string>

using namespace std;

#pragma once
class Game : IGame, IMultipleChoiceQuiz
{
    //����������� ����� ����������
private:
    string name; //�������� ����
    string playerAnswer; //����� ������
    string correctAnswer; //���������� �����
public:
    //
    IMultipleChoiceQuiz* multiplyChoiceQuizAction;
    //
    Game();
    ~Game();
    //�������� ������ � �������� ������ ��� ���������
    void performGetAsk(string filename);
    //������� �� ����� ������ � �������� ������
    void performDisplayAsk();
    //���������� �������� ������
    void performShuffleAnswers();
    //����� ��������� � ��������� ������ �� ������
    void displayAnswerResultMessage(bool isAnswerTrue);
    //������� �� ��������� �������
    void goToNextLevel();

    //������� � �������
    string getName();
    void setName(string _name);
    string getPlayerAnswer();
    void setPlayerAnswer(string _playerAnswer);
    string getCorrectAnswer();
    void setCorrectAnswer(string _correctAnswer);
};

