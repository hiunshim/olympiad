#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int net_force = 0;
    int force;
    int x = 0;
    int y = 0;
    int z = 0;
    while (n--) {
        cin >> force;
        x += force;
        cin >> force;
        y += force;
        cin >> force;
        z += force;
    }
    if (x == 0 && y == 0 && z == 0) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    return 0;
}

