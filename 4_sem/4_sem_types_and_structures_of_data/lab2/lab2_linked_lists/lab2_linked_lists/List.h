#pragma once
#include <fstream>
#include <iostream>
#include <string>
#include <ctime>


using namespace std;


/*
* циклический двусвязный список с головой
* реализация
*/

template<typename T>
class List
{
public:
	List();
	~List();
	//добавление элемента в конец списка
	void push_back(T data);
	//удаление элемента в списке по указанному индексу
	void removeAt(int index);
	// получить количество елементов в списке
	int GetSize() { return Size; }
	// перегруженный оператор [] 
	T& operator[](const int index);
private:
	template<typename T>
	class Node
	{
	public:
		Node *pNext, *pPrev;
		T data;
		Node(T data = T(), Node* pNext = nullptr, Node* pPrev = nullptr)
		{
			this->data = data;
			if (pNext == nullptr)
				this->pNext = this;
			else
				this->pNext = pNext;
			if (pPrev == nullptr)
				this->pPrev = this;
			else 
				this->pPrev = pPrev;
		}
	};
	int Size;
	Node<T>* head;
};


template<typename T>
List<T>::List()
{
	Size = 0;
	head = nullptr;
}

template<typename T>
List<T>::~List()
{
}

template<typename T>
void List<T>::push_back(T data)
{
	if (head == nullptr)
	{
		head = new Node<T>(data);//создание первого элемента
	}
	else
	{
		//добавление элемента в конец списка
		Node<T>* before_last = this->head->pPrev;//получаем временно последний Node (далее - предпоследний)
		Node<T>* last = new Node<T>(data);//создаем новый последний Node
		last->pNext = this->head;//следующий за последним - голова списка
		before_last->pNext = last;//следующий за предпоследним - последний
		last->pPrev = before_last;//предыдущий перед последним - бывший предпоследний
		head->pPrev = last;//предыдущий перед головой - последний
	}

	Size++;
}

template<typename T>
void List<T>::removeAt(int index)
{
	if (this->GetSize() < index || index < 0) {
		throw exception("Wrong function using");
	}
	else {
		if (index == 0)
		{
			Node<T>* previous = head->pPrev;
			//cout << "prev = " << previous->data << endl;
			Node<T>* next = head->pNext;
			previous->pNext = next;
			next->pPrev = previous;
			if (Size > 0) this->head = this->head->pNext;
			else head = nullptr;//если список стал пустым
			Size--;
			
		}
		else
		{
			Node<T>* previous = this->head;
			for (int i = 0; i < index - 1; i++)
			{
				previous = previous->pNext;
			}

			Node<T>* toDelete = previous->pNext;
			Node<T>* next = toDelete->pNext;
			previous->pNext = next;
			next->pPrev = previous;
			delete toDelete;
			Size--;
		}
	}
	
	
}

template<typename T>
T& List<T>::operator[](const int index)
{
	int counter = 0;

	Node<T>* current = this->head;

	while (current != nullptr)
	{
		if (counter == index)
		{
			return current->data;
		}
		current = current->pNext;
		counter++;
	}
}








