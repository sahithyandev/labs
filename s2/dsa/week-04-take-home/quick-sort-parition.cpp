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

/**
 * @brief Merges multiple vectors into one.
 *
 * This function takes a vector of vectors and merges them into a single vector.
 *
 * @param vectors A vector of vectors to be merged.
 * @return vector<int> A single vector containing all the elements of the input vectors.
 */
vector<int> merge_vectors(const vector<vector<int>> &vectors)
{
	vector<int> merged;
	for (const auto &vec : vectors)
	{
		merged.insert(merged.end(), vec.begin(), vec.end());
	}
	return merged;
}

/**
 * @brief Only does partitioning for quick sort. Named `quickSort` because the lab said so.
 */
vector<int> quickSort(vector<int> arr)
{

	int pivot_value = arr[0];
	vector<vector<int>> memory = {
			{},						 // left
			{pivot_value}, // equal
			{}};					 // right

	for (uint i = 1; i < arr.size(); i++)
	{
		int current_value = arr[i];
		if (current_value < pivot_value)
		{
			memory[0].push_back(current_value);
		}
		else if (current_value == pivot_value)
		{
			memory[1].push_back(current_value);
		}
		else
		{
			memory[2].push_back(current_value);
		}
	}
	return merge_vectors(memory);
}

int main()
{
	int length;
	cin >> length;

	vector<int> arr = get_numbers_input(length);
	vector<int> partitioned = quickSort(arr);
	print_vector(partitioned);

	return 0;
}