
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <iomanip>


using namespace std;

int main() {
    int m;
    cout << fixed << setprecision(8);
    cin >> m;
    for (int i = 0; i < m; i++) {
        int r, n, theta, minutes, seconds;
        cin >> r >> n >> theta >> minutes >> seconds;

        n = min(n, 1296000);

        // Calculate angle
        int ticks = (theta * 3600 + minutes * 60 + seconds) % 1296000;
        bool cuts[1296000] = {false};

        // Algorithm
        int pos = 0;
        for (int j = 0; j < n; j++) {
            cuts[pos] = true;
            pos += ticks;
            if (pos >= 1296000) pos -= 1296000;
        }

        int largestTickGap = 0;
        int lastTick = 0;
        for (int j = 0; j < 1296000; j ++) {
          if (cuts[j]) {
            largestTickGap = max(largestTickGap, j - lastTick);
            lastTick = j;
          }
        }
        largestTickGap = max(largestTickGap, 1296000 - lastTick);


        double area = M_PI * r * r * largestTickGap / 1296000;
        cout << area << endl;
    }
}