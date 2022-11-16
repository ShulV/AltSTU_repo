#pragma once

#include "Scanner.h"
#include "SemTree.h"

class SyntaxAnalis
{
	Scanner scaner;
	int currentType;
	int savePoint;
	int saveLine;
	int savedType;
	int savedVarType;
	SemTree* savedMass;
	std::string currentLex;
	SemTree* root = new SemTree(NULL, NULL, NULL, new Node);

	void AnaliseSosOp();
	void AnaliseData();
	void AnaliseList();
	void AnaliseVariable();
	void AnaliseSquare(bool type);
	void AnaliseExpression();
	void AnaliseBitSave();
	void AnaliseInc();
	void AnaliseAdd();
	void AnaliseMultiply();
	void AnaliseBasicExpress();
	void AnaliseSwitch();
	void AnaliseOpAndData();
	void AnaliseFunc();
	void AnaliseOps();
	void ShowError(std::string err);
public:
	SyntaxAnalis(std::string fileName);
	void Prog();
};

