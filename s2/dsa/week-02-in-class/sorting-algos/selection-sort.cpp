#include <iostream>
#include <vector>

using namespace std;

vector<int> get_numbers_input()
{
	vector<int> numbers{};
	int currentNumber;

	do
	{
		cin >> currentNumber;
		numbers.push_back(currentNumber);
	} while (cin.peek() == ' ');

	return numbers;
}

void selectionSort(vector<int> &numbers)
{
	for (uint passIndex = 0; passIndex < numbers.size(); passIndex++)
	{
		uint smallestNumberIndex = passIndex;
		// find the index of smallest number
		for (uint currentNumberIndex = passIndex; currentNumberIndex < numbers.size(); currentNumberIndex++)
		{
			if (numbers[currentNumberIndex] < numbers[smallestNumberIndex])
			{
				smallestNumberIndex = currentNumberIndex;
			}
		}

		// swap
		int temp = numbers[smallestNumberIndex];
		numbers[smallestNumberIndex] = numbers[passIndex];
		numbers[passIndex] = temp;
	}
}

int main()
{

	vector<int> numbers = get_numbers_input();
	selectionSort(numbers);
	for (uint i = 0; i < numbers.size(); i++)
	{
		cout << numbers[i] << " ";
	}
	cout << endl;

	return 0;
}