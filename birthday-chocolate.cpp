// PROBLEM: https://www.hackerrank.com/contests/womens-codesprint-3/challenges/the-birthday-bar
#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> squares(n);
    for(int squares_i = 0; squares_i < n; squares_i++){
       cin >> squares[squares_i];
    }
    int d;
    int m;
    cin >> d >> m;
    int ct = 0;
    int sum = 0;
    int max = n - m;
    int j;
    for (int i = 0; i <= max; ++i) {
        sum = 0;
        j = i;
        for (int k = 0; k < m; ++k) {
            sum += squares[j];
            ++j;
        }
        if (sum == d) {
            ct++;
        }
    }
    cout << ct << endl;
    return 0;
}
