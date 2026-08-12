#include <iostream>
#include <vector>

using namespace std;

void insertion_sort(vector<int> &numbers)
{
	for (uint currentIndex = 1; currentIndex < numbers.size(); currentIndex++)
	{
		int currentNumber = numbers[currentIndex];
		int j = currentIndex - 1;
		while (j >= 0 && currentNumber < numbers[j])
		{
			numbers[j + 1] = numbers[j];
			j--;
		}

		numbers[j + 1] = currentNumber;
	}
}

/*
 * Complete the 'cookies' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY A
 */

int cookies(int k, vector<int> A)
{
	int iterations_count = 0;

	while (true)
	{
		if (A.size() < 2)
		{
			return -1;
		}

		int min1 = A[0];
		if (min1 >= k)
		{
			return iterations_count;
		}
		int min2 = A[1];
		int x = min1 + 2 * min2;
		A[0] = x;
		swap(A[A.size() - 1], A[1]);
		A.pop_back();

		iterations_count++;
		insertion_sort(A);
	}
}
int main()
{
	int n, k;
	n = 6;
	k = 7;

	// cin >> n;
	// cin >> k;

	vector<int> arr = {1, 2, 3, 9, 10, 12};

	cout << cookies(k, arr) << endl;
	return 0;
}