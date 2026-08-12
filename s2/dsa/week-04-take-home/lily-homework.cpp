#include <iostream>
#include <vector>
#include <map>

using namespace std;

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

int count_swaps(vector<int> &numbers, vector<int> &sorted_numbers)
{
	map<int, int> index_map;
	uint i = 0;
	for (; i < numbers.size(); i++)
	{
		index_map.insert({numbers[i], i});
	}
	vector<bool> visited(numbers.size(), false);
	int swaps = 0;
	int cycle_size = 0;
	int j;

	for (i = 0; i < numbers.size(); i++)
	{
		if (visited[i] || numbers[i] == sorted_numbers[i])
			continue;

		cycle_size = 0;
		j = i;

		while (!visited[j])
		{
			visited[j] = true;
			cycle_size += 1;
			j = index_map[sorted_numbers[j]];
		}

		if (cycle_size > 1)
		{
			swaps += cycle_size - 1;
		}
	}

	return swaps;
}
/**
 * @brief Prints a vector of integers in a line, separated by space.
 */
void print_vector(vector<int> arr)
{
	for (uint i = 0; i < arr.size(); i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;
}

int lilyHomework(vector<int> numbers)
{
	vector<int> sorted_numbers = numbers;
	recursive_quick_sort(sorted_numbers, 0, numbers.size() - 1);

	uint total_size = numbers.size();
	vector<int> reversed_numbers(total_size);

	for (uint i = 0; i < total_size; i++)
	{
		reversed_numbers[i] = sorted_numbers[total_size - 1 - i];
	}

	int sorted = count_swaps(numbers, sorted_numbers);
	int reversed =
			count_swaps(numbers, reversed_numbers);
	return min(sorted, reversed);
}

int main()
{
	vector<int> arr = {2, 5, 3, 1};
	cout << lilyHomework(arr) << endl;
	return 0;
}