#include <iostream>
#include <cmath>

using namespace std;

int calculatePowerSum(int X, int N, int starting_number)
{
	int power = pow(starting_number, N); // Precompute power

	if (X == 0)
		return 1;
	if (X < 0)
		return 0;

	return calculatePowerSum(X - power, N, starting_number + 1) +
				 calculatePowerSum(X, N, starting_number + 1);
}

int powerSum(int X, int N)
{
	return calculatePowerSum(X, N, 1);
}

int main()
{
	cout << powerSum(100, 2) << endl; // Example test case
	return 0;
}
