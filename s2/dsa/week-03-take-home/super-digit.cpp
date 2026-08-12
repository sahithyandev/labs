#include <iostream>

using namespace std;

int digits_sum(int n)
{
  int sum = 0;
  while (n > 9)
  {
    sum += n % 10;
    n = n / 10;
  }
  sum += n;
  if (sum > 9)
    return digits_sum(sum);
  return sum;
}

int superDigit(string n, int k)
{
  int remainder = stoi(n) % 9;
  if (remainder == 0)
    remainder = 9;

  remainder *= k;
  return digits_sum(remainder);
}

int main()
{
  cout << superDigit("148", 3) << " must equal " << 3 << endl;
  cout << superDigit("9875", 4) << " must equal " << 8 << endl;
  cout << superDigit("123", 3) << " must equal " << 9 << endl;
  return 0;
}
