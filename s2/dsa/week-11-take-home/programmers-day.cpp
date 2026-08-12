#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'dayOfProgrammer' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts INTEGER year as parameter.
 */

string dayOfProgrammer(int year) {
    if (year == 1918) {
        return "26.09.1918";
    }
    string result;
    bool isLeapYear = false;
    if (year < 1918) {
        isLeapYear = (year % 4 == 0);
    } else if (year > 1918) {
        isLeapYear = (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }
    
    int februaryDays = isLeapYear ? 29 : 28;
    int daysInMonths[] = {31, februaryDays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    
    int dayCount = 0;
    int month = 1;
    while (dayCount + daysInMonths[month - 1] < 256) {
        dayCount += daysInMonths[month - 1];
        month++;
    }
    int day = 256 - dayCount;
    char buffer[11];
    sprintf(buffer, "%02d.%02d.%04d", day, month, year);
    result = buffer;
    
    return result;
}

int main()
{
    string year_temp;
    getline(cin, year_temp);

    int year = stoi(ltrim(rtrim(year_temp)));

    string result = dayOfProgrammer(year);

    cout << result << "\n";

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
