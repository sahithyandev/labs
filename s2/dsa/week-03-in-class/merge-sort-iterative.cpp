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

/**
 * A = the array to be sorted
 * L1 = the start of the first part
 * R1 = the end of the first part
 * L2 = the start of the second part
 * R2 = the end of the second part
 */
vector<int> merge_iterative(vector<int> arr, uint L1, uint R1, uint L2, uint R2)
{

	vector<int> temp(arr.size(), 0);
	int index = 0;

	while (L1 <= R1 and L2 <= R2)
	{
		int first_start = arr[L1];
		int second_start = arr[L2];

		if (first_start <= second_start)
		{
			temp[index++] = first_start;
			L1++;
		}
		else
		{
			temp[index++] = second_start;
			L2++;
		}
	}

	while (L1 <= R1)
	{
		temp[index++] = arr[L1++];
	}
	while (L2 <= R2)
	{
		temp[index++] = arr[L2++];
	}
	return temp;
}

vector<int> merge_sort_iterative(vector<int> arr)
{
	uint size_of_arr = arr.size();
	uint current_length = 1;
	uint i = 0;
	uint L1 = 0;
	uint L2 = 0;
	uint R1 = 0;
	uint R2 = 0;

	vector<int> temp;
	while (current_length < size_of_arr)
	{
		i = 0;
		while (i < size_of_arr)
		{
			L1 = i;
			R1 = i + current_length - 1;
			L2 = i + current_length;
			R2 = i + 2 * current_length - 1;

			if (L2 >= size_of_arr)
				break;
			if (R2 >= size_of_arr)
				R2 = size_of_arr - 1;

			temp = merge_iterative(arr, L1, R1, L2, R2);
			for (uint j = 0; j < R2 - L1 + 1; j++)
			{
				arr[i + j] = temp[j];
			}
			i = i + 2 * current_length;
		}
		current_length *= 2;
	}
	return arr;
}

int main()
{
	vector<int> input = get_numbers_input();
	vector<int> sorted = merge_sort_iterative(input);
	print_vector(sorted);
	return 0;
}