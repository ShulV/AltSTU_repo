#include "Game.h"

Game::Game() {

}
Game::~Game() {

}
//получить вопрос для викторины
void Game::performGetAsk(string filename)
{
	multiplyChoiceQuizAction->getAskFromFile(filename);
}
//вывести на экран вопрос и варианты ответа
void Game::performDisplayAsk()
{
	multiplyChoiceQuizAction->displayAsk();
}
//перемешать варианты ответа
void Game::performShuffleAnswers()
{
	multiplyChoiceQuizAction->displayAsk();
}

//вывод сообщения о резуьтате ответа на вопрос
void Game::displayAnswerResultMessage(bool isAnswerTrue) {
	if (isAnswerTrue) {
		cout << "Ваш ответ правильный!" << endl;
	}
	else {
		cout << "Ваш ответ неправильный!" << endl;
	}
}
//переход на следующий уровень
void Game::goToNextLevel() {

}
string Game::getName() {
	return name;
}
void Game::setName(string _name) {
	name = _name;
}
string Game::getPlayerAnswer() {
	return playerAnswer;
}
void Game::setPlayerAnswer(string _playerAnswer) {
	playerAnswer = _playerAnswer;
}
string Game::getCorrectAnswer() {
	return correctAnswer;
}
void Game::setCorrectAnswer(string _correctAnswer) {
	correctAnswer = _correctAnswer;
}