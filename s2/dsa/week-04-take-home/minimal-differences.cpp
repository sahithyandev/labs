#include <iostream>
#include <vector>

using namespace std;

/**
 * @brief Reads a specified number of integers from standard input and returns them as a vector.
 *
 * This function prompts the user to input a series of integers. It reads the integers one by one
 * until the specified length is reached or a non-space character is encountered in the input stream.
 *
 * @param length The number of integers to read from the input.
 * @return vector<int> A vector containing the integers read from the input.
 */
vector<int> get_numbers_input(int length)
{
	vector<int> numbers{};
	int currentNumber;

	do
	{
		cin >> currentNumber;
		numbers.push_back(currentNumber);
		length--;
	} while (length > 0 && cin.peek() == ' ');

	return numbers;
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

/**
 * @brief Finds pairs of numbers in the input vector that have the minimal absolute difference.
 *
 * This function takes a vector of integers and returns a vector containing pairs of numbers
 * that have the smallest absolute difference between them. If the input vector has fewer than
 * two elements, an empty vector is returned.
 *
 * @param numbers A vector of integers to be analyzed.
 * @return A vector of integers containing pairs of numbers with the minimal absolute difference.
 */
vector<int> close_numbers(vector<int> numbers)
{
	vector<int> close_numbers_vector = {};
	if (numbers.size() < 2)
		return close_numbers_vector;

	double minimal_difference = (numbers[1] - numbers[0]);
	double current_difference;
	for (int i = 0; i < numbers.size() - 1; i++)
	{
		current_difference = abs(numbers[i + 1] - numbers[i]);
		if (current_difference < minimal_difference)
		{
			minimal_difference = current_difference;
			close_numbers_vector.clear();

			close_numbers_vector.push_back(numbers[i]);
			close_numbers_vector.push_back(numbers[i + 1]);
		}
		else if (current_difference == minimal_difference)
		{
			close_numbers_vector.push_back(numbers[i]);
			close_numbers_vector.push_back(numbers[i + 1]);
		}
	}

	return close_numbers_vector;
}

int main()
{
	vector<int> arr = {-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854};
	recursive_quick_sort(arr, 0, arr.size() - 1);
	print_vector(arr);
	print_vector(close_numbers(arr));
	return 0;
}