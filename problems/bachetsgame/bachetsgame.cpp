
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>

using namespace std;

int main() {
  while (!cin.eof()) {

    string input;
    getline(cin, input);
    if (input == "") break;
    stringstream ss(input);

    int n, m;
    vector<int> kList = {};
    int stanWins[1000002] = {0};

    ss >> n;
    ss >> m;
    for (int i = 0; i < m; i ++) {
      int val;
      ss >> val;
      kList.push_back(val);
    }
    sort(kList.begin(), kList.end());
    
    for (int i = 1; i < n + 1; i ++) {
      for (int j = 0; j < m; j ++) {
        int k = kList[j];
        if (k > i) break;
        else if (!stanWins[i - k]) {
          stanWins[i] = 1;
          break;
        }
      }
    }

    if (stanWins[n]) {
      cout << "Stan wins" << endl;
    } else {
      cout << "Ollie wins" << endl;
    }

  }
  return 0;

}
  