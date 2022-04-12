#include "Player.h"

Player::Player() {

}
Player::~Player() {

}
//геттеры и сеттеры
string Player::getNickname() {
	return nickname;
}
void Player::setNickname(string _nickname) {
	nickname = _nickname;
}
