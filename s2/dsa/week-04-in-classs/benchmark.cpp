#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <stack>
#include <chrono>

using namespace std;
using namespace std::chrono;

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

void iterative_quick_sort(vector<int> &arr)
{
	stack<int> memory; // stores the subarray indices that needs to be quick-sorted

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
		recursive_quick_sort(numbers, 0, size - 1);
		end = high_resolution_clock::now();
		elapsed = end - start;
		elapsed_time = elapsed.count();

		outputFile << size << "," << line << ",quick-sort-recursive," << elapsed_time << "\n";

		// Benchmark recursive merge sort
		start = high_resolution_clock::now();
		iterative_quick_sort(numbers);
		end = high_resolution_clock::now();
		elapsed = end - start;
		elapsed_time = elapsed.count();

		outputFile << size << "," << line << ",quick-sort-iterative," << elapsed_time << "\n";

		// cout << "Benchmarked input size " << size << endl;
	}

	inputFile.close();
	outputFile.close();

	cout << "Benchmarking complete. Results saved in benchmark_results.csv" << endl;
	return 0;
}
