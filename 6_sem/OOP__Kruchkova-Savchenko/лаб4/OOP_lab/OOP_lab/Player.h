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

	//������� � �������
	string getNickname();
	void setNickname(string _nickname);
};

