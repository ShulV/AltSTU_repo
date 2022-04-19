#include "IGame.h"
#include "ITextAsk.h"
#include "IMultipleChoiceQuiz.h"
#include <iostream>
#include <string>

using namespace std;

#pragma once
class Game : IGame, IMultipleChoiceQuiz
{
    //абстрактный класс устройства
private:
    string name; //название игры
    string playerAnswer; //ответ игрока
    string correctAnswer; //правильный ответ
public:
    //
    IMultipleChoiceQuiz* multiplyChoiceQuizAction;
    //
    Game();
    ~Game();
    //получить вопрос и варианты ответа для викторины
    void performGetAsk(string filename);
    //вывести на экран вопрос и варианты ответа
    void performDisplayAsk();
    //перемешать варианты ответа
    void performShuffleAnswers();
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

