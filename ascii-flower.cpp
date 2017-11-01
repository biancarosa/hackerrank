// PROBLEM: https://www.hackerrank.com/contests/womens-codesprint-3/challenges/ascii-flower
#include <bits/stdc++.h>

using namespace std;

int main(){
    int r;
    int c;
    cin >> r >> c;
    
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            cout << "..O..";
        }
        cout << endl;
        for (int j = 0; j < c; ++j) {
            cout << "O.o.O";
        }
        cout << endl;
        for (int j = 0; j < c; ++j) {
            cout << "..O..";
        }
        cout << endl;
    }
    
    return 0;
}
