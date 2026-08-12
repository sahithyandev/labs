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

void recursive_quick_sort(vector<int> &arr, int start_index, int end_index)
{
	if (start_index >= end_index)
		return;

	int pivot_index = partition(arr, start_index, end_index);

	recursive_quick_sort(arr, start_index, pivot_index - 1);
	recursive_quick_sort(arr, pivot_index + 1, end_index);
}

int main()
{
	vector<int> arr = get_numbers_input();
	recursive_quick_sort(arr, 0, arr.size() - 1);

	for (uint i = 0; i < arr.size(); i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;

	return 0;
}