#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    int size = n;
    int input;
    int find_even = 0;
    vector<int> numbers;
    while (n--) {
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

