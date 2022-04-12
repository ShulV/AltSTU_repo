#include "IGame.h"
#include "ITextAsk.h"
#include "IMultipleChoiceQuiz.h"
#include <iostream>
#include <string>

using namespace std;

#pragma once
class Game : IGame, IMultipleChoiceQuiz
{
private:
    string name; //название игры
    string playerAnswer; //ответ игрока
    string correctAnswer; //правильный ответ
public:
    Game();
    ~Game();
    //вывод сообщения о резуьтате ответа на вопрос
    void displayAnswerResultMessage(bool isAnswerTrue);
    //переход на следующий уровень
    void goToNextLevel();

    //геттеры и сеттеры
    string getName();
    void setName(string _name);
    string getPlayerAnswer();
    void setPlayerAnswer(string _playerAnswer);
    string getCorrectAnswer();
    void setCorrectAnswer(string _correctAnswer);
};

