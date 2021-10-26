#include <iostream>
#include <vector>

using namespace std;

int main() {
    int tt;
    cin >> tt;
    int size = tt;
    int input;
    int find_even = 0;
    vector<int> numbers;
    while (tt--) {
        cin >> input;
        numbers.push_back(input);
        find_even += input % 2;
    }
    if (find_even > 1) {
        for (int k = 0; k < size; k++) {
            if (numbers[k] % 2 == 0) {
                cout << k + 1 << "\n";
                return 0;
            }
        }
    } else {
        for (int k = 0; k < size; k++) {
            if (numbers[k] % 2 == 1) {
                cout << k + 1 << "\n";
                return 0;
            }
        }
    }
    return 0;
}

