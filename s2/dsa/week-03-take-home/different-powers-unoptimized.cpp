#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int powerSum(int X, int N)
{
	int possible_different_ways = 0;
	int max_number_to_check = 1;
	while (pow(max_number_to_check, N) <= X)
	{
		max_number_to_check++;
	}
	max_number_to_check--;

	cout << "max= " << max_number_to_check << endl;

	vector<int> powers(max_number_to_check - 1, 0);

	for (int i = 1; i <= max_number_to_check; i++)
	{
		powers[i - 1] = pow(i, N);
	}

	uint32_t total_permutations = 1 << (max_number_to_check);
	cout << "total_permutations= " << total_permutations << endl;

	uint32_t minimum_permutation_id = 0;
	int sum = 0;
	for (int i = 1; i <= max_number_to_check; i++)
	{
		sum += pow(i, N);
		if (sum > X)
		{
			minimum_permutation_id = 1 << (i - 1);
			break;
		}
	}
	cout << "minimal_permutation= " << minimum_permutation_id << endl;

	uint32_t permutation_id = minimum_permutation_id;
	while (permutation_id <= total_permutations)
	{
		sum = 0;
		for (int i = max_number_to_check; i >= 1; i--)
		{
			bool should_include = (permutation_id & (1 << (i - 1)));
			if (!should_include)
				continue;
			sum += powers[i - 1];
			// cout << "perm " << permutation_id << ": sum=" << sum << " (" << i << ")" << endl;
			if (sum > X)
				break;
		}
		cout << "perm " << permutation_id << ": sum=" << sum << endl;
		// if (sum > X)
		// {
		// 	// find the 1 from the left
		// 	int one_index = ceil(log2(permutation_id));
		// 	cout << "one_index=" << one_index << endl;
		// 	permutation_id = 1 << one_index;
		// 	continue;
		// }

		if (sum == X)
		{
			possible_different_ways++;
			// cout << "possible: " << permutation_id << endl;
		}
		permutation_id++;
	}

	return possible_different_ways;
}

int main()
{

	cout << powerSum(1000, 2) << endl;
	return 0;
}