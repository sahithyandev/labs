#include <iostream>

class Node
{
public:
	int data;
	Node *next;

	Node(int data)
	{
		this->data = data;
		this->next = nullptr;
	}
};

class Stack
{
private:
	Node *top;

public:
	Stack()
	{
		this->top = nullptr;
	}
	void push(int value)
	{
		if (this->isEmpty())
		{
			this->top = new Node(value);
			return;
		}

		Node *n = new Node(value);
		n->next = this->top;
		this->top = n;
	}
	void pop()
	{

		if (this->isEmpty())
		{
			return;
		}

		this->top = this->top->next;
	}
	bool isEmpty()
	{
		return this->top == nullptr;
	}
	int stackTop()
	{
		if (this->isEmpty())
		{
			return -1;
		}
		return this->top->data;
	}
	void display()
	{
		Node *n = this->top;
		while (n != nullptr)
		{
			std::cout << n->data << " ";
			n = n->next;
		}
		std::cout << std::endl;
	}
};