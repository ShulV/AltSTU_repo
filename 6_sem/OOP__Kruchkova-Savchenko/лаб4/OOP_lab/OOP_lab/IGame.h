#pragma once
class IGame
{
public:
    virtual void displayAnswerResultMessage(bool isAnswerTrue) = 0;
    virtual void goToNextLevel() = 0;
};

