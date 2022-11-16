#pragma once
#include <string>
#include <iostream>
#define MAX_N 50

enum TypeObj {
	TVar = 1,
	TFunc,
	TConst,
	TMass
};

enum TypeVar {
	TInt = 200,
	TShort,
	TLong,
	TBool,
	TVoid,
	TypeDef = 100
};

struct Node {
	std::string id;
	int typeObject = -1;
	int typeVar = -1;
	int N = 0;
	int hg[MAX_N];
};

class SemTree
{
public:
	Node* n;
	SemTree* Left, * Right, * Up;
	static SemTree* Cur;
	SemTree(SemTree* l, SemTree* r, SemTree* u, Node* Data);
	void SetLeft(Node* Data);
	void SetRight(Node* Data);
	SemTree* FindUp(SemTree* From, std::string id);
	SemTree* Add(std::string* lex, int objType);
	SemTree* NewBlock();
	void PrintError(std::string error, std::string lex);
	void SetTypeVar(int type);
	static void SetCurrent(SemTree* tree);
	void AddToMass(int hgg);
	std::string GetId() { return n->id; };
	int GetTypeObject() { return n->typeObject; };
	int GetTypeVar() { return n->typeVar; };
	int GetN() { return n->N; };
	int* GetHG() { return n->hg; };
	void Print();

	void Check(SemTree* Start, std::string lex, bool typeFind, int IdType);
};

