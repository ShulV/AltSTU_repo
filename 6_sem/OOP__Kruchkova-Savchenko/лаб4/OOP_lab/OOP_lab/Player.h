#include <string>

using namespace std;

#pragma once
class Player
{
private:
	string nickname;
public:
	Player();
	~Player();

	//геттеры и сеттеры
	string getNickname();
	void setNickname(string _nickname);
};

