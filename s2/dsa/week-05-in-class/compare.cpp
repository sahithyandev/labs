#include <iostream>
#include <fstream>
#include <chrono>

using namespace std;
using namespace chrono;

const int TEST_COUNT = 1000;

class StackUsingArray
{
private:
	int *memory;
	int maxSize;
	int top;

public:
	StackUsingArray(int maxSize)
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
	~StackUsingArray()
	{
		delete[] this->memory;
	}
};

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

class StackUsingLinkedList
{
private:
	Node *top;

public:
	StackUsingLinkedList()
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

double measureStackArrayPerformance(StackUsingArray &stack)
{
	auto start = high_resolution_clock::now();

	for (int i = 1; i < TEST_COUNT; i++)
	{

		stack.push(8);
		stack.push(10);
		stack.push(5);
		stack.push(11);
		stack.push(15);
		stack.push(23);
		stack.push(6);
		stack.push(18);
		stack.push(20);
		stack.push(17);
		stack.display();
		stack.push(4);
		stack.push(30);
		stack.push(3);
		stack.push(1);
		stack.display();
	}
	auto end = high_resolution_clock::now();

	double time = duration<double, milli>(end - start).count();

	return time / TEST_COUNT;
}
double measureStackLinkedListPerformance(StackUsingLinkedList &stack)
{
	auto start = high_resolution_clock::now();

	for (int i = 1; i < TEST_COUNT; i++)
	{
		stack.push(8);
		stack.push(10);
		stack.push(5);
		stack.push(11);
		stack.push(15);
		stack.push(23);
		stack.push(6);
		stack.push(18);
		stack.push(20);
		stack.push(17);
		stack.display();
		stack.push(4);
		stack.push(30);
		stack.push(3);
		stack.push(1);
		stack.display();
	}
	auto end = high_resolution_clock::now();

	double time = duration<double, milli>(end - start).count();

	return time / TEST_COUNT;
}

int main()
{
	ofstream csvFile("stack_performance.csv");
	csvFile << "Stack Implementation,Push Time (ms),Pop Time (ms)" << endl;

	StackUsingArray *stack1 = new StackUsingArray(10);
	double time = measureStackArrayPerformance(*stack1);
	csvFile << "Using Array," << time << endl;

	StackUsingLinkedList *stack2 = new StackUsingLinkedList();
	time = measureStackLinkedListPerformance(*stack2);
	csvFile << "Using LinkedList," << time << endl;

	csvFile.close();
	cout << "Performance results written to stack_performance.csv" << endl;

	return 0;
}
