#include "Game.h"

Game::Game() {

}
Game::~Game() {

}
//�������� ������ ��� ���������
void Game::performGetAsk(string filename)
{
	multiplyChoiceQuizAction->getAskFromFile(filename);
}
//������� �� ����� ������ � �������� ������
void Game::performDisplayAsk()
{
	multiplyChoiceQuizAction->displayAsk();
}
//���������� �������� ������
void Game::performShuffleAnswers()
{
	multiplyChoiceQuizAction->displayAsk();
}

//����� ��������� � ��������� ������ �� ������
void Game::displayAnswerResultMessage(bool isAnswerTrue) {
	if (isAnswerTrue) {
		cout << "��� ����� ����������!" << endl;
	}
	else {
		cout << "��� ����� ������������!" << endl;
	}
}
//������� �� ��������� �������
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