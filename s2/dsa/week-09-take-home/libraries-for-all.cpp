#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'roadsAndLibraries' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER c_lib
 *  3. INTEGER c_road
 *  4. 2D_INTEGER_ARRAY cities
 */

long roadsAndLibraries(int n, int c_lib, int c_road,
                       vector<vector<int>> cities) {
  if (c_lib <= c_road) {
    // If building a library is cheaper than a road, build a library in every
    // city
    return (long)n * c_lib;
  }

  // Adjacency list for graph
  // Adjacency list is used as it's a sparse graph
  vector<vector<int>> adj(n);
  for (const auto &edge : cities) {
    int u = edge[0] - 1;
    int v = edge[1] - 1;
    adj[u].push_back(v);
    adj[v].push_back(u);
  }

  vector<bool> visited(n, false);
  long total_cost = 0;

  for (int i = 0; i < n; i++) {
    if (visited[i]) {
      continue;
    }
    // For every new connected component, we need 1 library
    // and (number of nodes in component - 1) roads
    
    // Traverse the connected component using DFS
    stack<int> s;
    s.push(i);
    visited[i] = true;
    int component_size = 1;

    while (!s.empty()) {
      int u = s.top();
      s.pop();

      for (int v : adj[u]) {
        if (visited[v]) {
          continue;
        }
        visited[v] = true;
        s.push(v);
        component_size++;
      }
    }

    total_cost += c_lib + (long)(component_size - 1) * c_road;
  }

  return total_cost;
}

int main() {
  string q_temp;
  getline(cin, q_temp);

  int q = stoi(ltrim(rtrim(q_temp)));

  for (int q_itr = 0; q_itr < q; q_itr++) {
    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input =
        split(rtrim(first_multiple_input_temp));

    int n = stoi(first_multiple_input[0]);

    int m = stoi(first_multiple_input[1]);

    int c_lib = stoi(first_multiple_input[2]);

    int c_road = stoi(first_multiple_input[3]);

    vector<vector<int>> cities(m);

    for (int i = 0; i < m; i++) {
      cities[i].resize(2);

      string cities_row_temp_temp;
      getline(cin, cities_row_temp_temp);

      vector<string> cities_row_temp = split(rtrim(cities_row_temp_temp));

      for (int j = 0; j < 2; j++) {
        int cities_row_item = stoi(cities_row_temp[j]);

        cities[i][j] = cities_row_item;
      }
    }

    long result = roadsAndLibraries(n, c_lib, c_road, cities);

    cout << result << "\n";
  }

  return 0;
}

string ltrim(const string &str) {
  string s(str);

  s.erase(s.begin(),
          find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

  return s;
}

string rtrim(const string &str) {
  string s(str);

  s.erase(
      find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
      s.end());

  return s;
}

vector<string> split(const string &str) {
  vector<string> tokens;

  string::size_type start = 0;
  string::size_type end = 0;

  while ((end = str.find(" ", start)) != string::npos) {
    tokens.push_back(str.substr(start, end - start));

    start = end + 1;
  }

  tokens.push_back(str.substr(start));

  return tokens;
}
