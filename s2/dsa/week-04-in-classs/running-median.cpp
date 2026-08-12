#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

/**
 * Reads space-separated list of numbers from standard input
 */
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

/**
 * Progressive insertion sort which assumes the first n-1 elements are sorted.
 */
void insertion_sort(vector<int> &numbers)
{
	uint currentIndex = numbers.size() - 1;
	int currentNumber = numbers[currentIndex];
	int j = currentIndex - 1;
	while (j >= 0 && currentNumber < numbers[j])
	{
		numbers[j + 1] = numbers[j];
		j--;
	}

	numbers[j + 1] = currentNumber;
}

int main()
{
	cout << fixed << setprecision(1); // to print numbers in 5.2 format
	vector<int> arr =
			get_numbers_input();
	vector<int> running_list = {};

	uint size = arr.size();
	for (uint i = 0; i < size; i++)
	{
		running_list.push_back(arr[i]);
		insertion_sort(running_list);

		double median;

		uint is_odd_number_of_elements_in_running_list = i & 1; // performant way of checking isEven
		if (is_odd_number_of_elements_in_running_list == 1)
		{
			median = (running_list[(i - 1) / 2] + running_list[(i + 1) / 2]) / 2.0;
		}
		else
		{
			median = running_list[i / 2];
		}

		cout << median << endl;
	}

	return 0;
}