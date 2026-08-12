#include <iostream>
#include <vector>
#include <stack>

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

int partition(vector<int> &arr, int start_index, int end_index)
{
	int pivot = arr[end_index];
	int small_element_index = start_index;

	for (int i = start_index; i < end_index; i++)
	{
		if (arr[i] > pivot)
			continue;
		swap(arr[i], arr[small_element_index++]);
	}

	swap(arr[small_element_index], arr[end_index]);
	return small_element_index;
}

void iterative_quick_sort(vector<int> &arr)
{
	/**
	 * to store the subarray indices that needs to be quick-sorted
	 * start is pushed first
	 * end is pushed next
	 */
	stack<int> memory;

	int start = 0;
	int end = arr.size() - 1;
	memory.push(start);
	memory.push(end);

	while (!memory.empty())
	{
		end = memory.top();
		memory.pop();
		start = memory.top();
		memory.pop();

		int pivot = partition(arr, start, end);

		if (pivot - 1 > start)
		{
			memory.push(start);
			memory.push(pivot - 1);
		}
		if (pivot + 1 < end)
		{
			memory.push(pivot + 1);
			memory.push(end);
		}
	}
}

int main()
{
	vector<int> arr = get_numbers_input();

	iterative_quick_sort(arr);

	for (uint i = 0; i < arr.size(); i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;

	return 0;
}