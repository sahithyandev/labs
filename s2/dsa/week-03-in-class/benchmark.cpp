#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <chrono>

using namespace std;
using namespace std::chrono;

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

// Function to parse a line of space-separated numbers
vector<int> parseInput(const string &line)
{
	vector<int> numbers;
	stringstream ss(line);
	int num;
	while (ss >> num)
	{
		numbers.push_back(num);
	}
	return numbers;
}

int main()
{
	ifstream inputFile("inputs.txt");
	ofstream outputFile("benchmark_results.csv");

	if (!inputFile.is_open())
	{
		cerr << "Error: Could not open inputs.txt" << endl;
		return 1;
	}
	if (!outputFile.is_open())
	{
		cerr << "Error: Could not create benchmark_results.csv" << endl;
		return 1;
	}

	// Write CSV header
	outputFile << "Input Size,Input,Program,Execution Time (seconds)\n";

	string line;

	auto start = high_resolution_clock::now();
	auto end = start;
	duration<double> elapsed;
	double elapsed_time;

	while (getline(inputFile, line))
	{
		vector<int> numbers = parseInput(line);
		int size = numbers.size();

		// Benchmark iterative merge sort
		start = high_resolution_clock::now();
		merge_sort_iterative(numbers);
		end = high_resolution_clock::now();
		elapsed = end - start;
		elapsed_time = elapsed.count();

		outputFile << size << "," << line << ",merge-sort-iterative," << elapsed_time << "\n";

		// Benchmark recursive merge sort
		start = high_resolution_clock::now();
		merge_sort_recursive(numbers, 0, numbers.size() - 1);
		end = high_resolution_clock::now();
		elapsed = end - start;
		elapsed_time = elapsed.count();

		outputFile << size << "," << line << ",merge-sort-recursive," << elapsed_time << "\n";

		// cout << "Benchmarked input size " << size << endl;
	}

	inputFile.close();
	outputFile.close();

	cout << "Benchmarking complete. Results saved in benchmark_results.csv" << endl;
	return 0;
}
