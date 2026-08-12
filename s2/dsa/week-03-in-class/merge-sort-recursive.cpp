#include <iostream>
#include <vector>

using namespace std;

void print_vector(vector<int> arr)
{
	for (uint i = 0; i < arr.size(); i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;
}

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
void merge_recursive(vector<int> &arr, int start, int mid, int end)
{
	int left_size = mid - start + 1;
	int right_size = end - mid;

	vector<int> left(left_size, 0);
	vector<int> right(right_size, 0);

	int cursor_left = 0;
	for (; cursor_left < left_size; cursor_left++)
	{
		left[cursor_left] = arr[start + cursor_left];
	}

	int cursor_right = 0;
	for (; cursor_right < right_size; cursor_right++)
	{
		right[cursor_right] = arr[mid + 1 + cursor_right];
	}

	cursor_left = 0;
	cursor_right = 0;
	int k = start;

	int left_value = 0;
	int right_value = 0;
	while (cursor_left < left_size && cursor_right < right_size)
	{
		left_value = left[cursor_left];
		right_value = right[cursor_right];

		if (left_value <= right_value)
		{
			arr[k] = left_value;
			k++;
			cursor_left++;
		}
		else
		{
			arr[k] = right_value;
			k++;
			cursor_right++;
		}
	}

	while (cursor_left < left_size)
	{
		left_value = left[cursor_left];
		arr[k] = left_value;
		k++;
		cursor_left++;
	}
	while (cursor_right < right_size)
	{
		right_value = right[cursor_right];
		arr[k] = right_value;
		k++;
		cursor_right++;
	}
}

void merge_sort_recursive(vector<int> &arr, int left_index, int right_index)
{
	if (left_index >= right_index)
		return;
	int mid = left_index + (right_index - left_index) / 2;

	merge_sort_recursive(arr, left_index, mid);
	merge_sort_recursive(arr, mid + 1, right_index);
	merge_recursive(arr, left_index, mid, right_index);
}

int main()
{
	vector<int> arr = get_numbers_input();

	merge_sort_recursive(arr, 0, arr.size() - 1);
	print_vector(arr);

	return 0;
}