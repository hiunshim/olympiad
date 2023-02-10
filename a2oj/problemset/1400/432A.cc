#include <iostream>

using namespace std;

int main() {
    int n, k;
    int student;
    int count = 0;
    cin >> n >> k;
    while (n--) {
        cin >> student;
        if (student + k <= 5) {
            count++;
        }
    }
    cout << count / 3 << "\n";
    return 0;
}

