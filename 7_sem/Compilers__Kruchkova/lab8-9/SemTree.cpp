#include "SemTree.h"

SemTree* SemTree::Cur = nullptr;

SemTree::SemTree(SemTree* l, SemTree* r, SemTree* u, Node* d)
{
	n = new Node;
	Up = u; Left = l; Right = r;
	memcpy(n, d, sizeof(Node));
}

void SemTree::SetLeft(Node* Data)
// создать левого потомка от текущей вершины 
{
	SemTree* a = new SemTree(NULL, NULL, this, Data);
	Left = a; // связали с новой вершиной
}

void SemTree::SetRight(Node* Data)
// создать правого потомка от текущей вершины 
{
	SemTree* a = new SemTree(NULL, NULL, this, Data);
	Right = a; // связали с новой вершиной
}

SemTree* SemTree::FindUp(SemTree* From, std::string id)
// поиск данных от заданной вершины до корня вверх 
{
	SemTree* i = From; // текущая вершина поиска
	while ((i != NULL) && (id != i->n->id))
		i = i->Up; // поднимаемся наверх по связям
	return i;
}

SemTree* SemTree::Add(std::string* lex, int objType) {
	Node newData;
	newData.typeObject = objType;
	newData.id = *lex;
	newData.typeVar = -1;
	Cur->SetLeft(&newData);
	Cur = Cur->Left;
	return Cur;
}

SemTree* SemTree::NewBlock() {
	SemTree* sav;
	Node dat;
	dat.id = "";
	dat.typeObject = NULL;
	if (Cur->Right != NULL) {
		Cur->SetLeft(&dat);
		Cur = Cur->Left;
	}
	Cur->SetRight(&dat);
	sav = Cur;
	Cur = Cur->Right;
	return sav;
}

void SemTree::PrintError(std::string error, std::string lex) {
	std::cout << error + " " + lex << std::endl;
	exit(1);
}

void SemTree::SetTypeVar(int type) {
	n->typeVar = type;
}

void SemTree::SetCurrent(SemTree* tree) {
	Cur = tree;
}

void SemTree::AddToMass(int hgg) {
	n->hg[n->N] = hgg;
	n->N++;
}

void SemTree::Print() {
	std::cout << "ID -> " + n->id << std::endl;
	if (Up != NULL) std::cout << "Up -> " + Up->n->id << std::endl;
	if (Left != NULL) std::cout << "Left -> " + Left->n->id << std::endl;
	if (Right != NULL) std::cout << "Right -> " + Right->n->id << std::endl;
	std::cout << std::endl;
	if (Right != NULL) Right->Print();
	if (Left != NULL) Left->Print();
}

void SemTree::Check(SemTree* Start, std::string lex, bool typeFind, int IdType) {
	bool res = false;
	SemTree* tree;
	tree = FindUp(Start, lex);
	while (!res && tree != NULL) {
		if (tree->n->typeObject == IdType)
			res = true;
		tree = FindUp(tree->Up, lex);
	}
	if (res != typeFind) {
		if (typeFind) {
			if(IdType == TFunc) PrintError("Func dont exist", lex);
			else if(IdType == TVar) PrintError("Var dont exist", lex);
			else if(IdType == TConst) PrintError("Const dont exist", lex);
			else PrintError("Mass dont exist", lex);
		}
		else {
			if (IdType == TFunc) PrintError("Func already exist", lex);
			else if (IdType == TVar) PrintError("Var already exist", lex);
			else if (IdType == TConst) PrintError("Const already exist", lex);
			else PrintError("Mass already exist", lex);
		}
	}
}

