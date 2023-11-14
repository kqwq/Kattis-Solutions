
#include <iostream>

using namespace std;

int main() {
    
    int n;
    cin >> n;
    if (n % 2) {
        cout << "still running";
        return 0;
    }
    int sum = 0;
    int last = 0;
    bool stopped = true;
    
    for (int i = 0; i < n; i ++) {
        int x;
        cin >> x;
        if (stopped) {
            last = x;
        } else {
            sum += x - last;
        }
        stopped = !stopped;
    }
    cout << sum;
}