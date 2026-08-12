#include <iostream>
#include <string>

using namespace std;

/*
 * Complete the 'twoStrings' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING s1
 *  2. STRING s2
 */

string twoStrings(string s1, string s2)
{
	int s1_length = s1.length();
	int s2_length = s2.length();

	for (int i = 0; i < s1_length; i++)
	{
		for (int j = 0; j < s2_length; j++)
		{
			if (s1[i] == s2[j])
			{
				return "YES";
			}
		}
	}
	return "NO";
}

int main()
{
	string s1 = "hello";
	string s2 = "self";

	string result = twoStrings(s1, s2);
	cout << result << endl;

	return 0;
}