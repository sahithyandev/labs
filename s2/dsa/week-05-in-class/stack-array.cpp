#include <iostream>

class Stack
{
private:
	int *memory;
	int maxSize;
	int top;

public:
	Stack(int maxSize)
	{
		this->maxSize = maxSize;
		this->memory = new int[maxSize];
		this->top = 0;
	}

	void push(int value)
	{
		if (this->isFull())
		{
			return;
		}
		this->memory[this->top++] = value;
	}
	void pop()
	{
		if (this->isEmpty())
		{
			return;
		}

		--this->top;
	}
	bool isEmpty()
	{
		return this->top == 0;
	}
	bool isFull()
	{
		return this->maxSize == this->top;
	}
	int stackTop()
	{
		if (this->isEmpty())
		{
			return -1;
		}
		return this->memory[this->top - 1];
	}
	void display()
	{
		for (int i = this->top - 1; i >= 0; i--)
		{
			std::cout << this->memory[i] << " ";
		}
		std::cout << std::endl;
	}
	~Stack()
	{
		delete[] this->memory;
	}
};