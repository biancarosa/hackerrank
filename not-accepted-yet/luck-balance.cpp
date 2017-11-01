// PROBLEM: https://www.hackerrank.com/contests/w21/challenges/luck-balance

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() 
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n, k, l, t;
    vector<int> important;
    int luck = 0;

    cin >> n >> k;
    while (cin  >> l >> t) {
       if (t == 0) {
           luck += l;
       } else {
            important.push_back(l);
       }
    }
    sort(important.begin(), important.end());
    for (int i = 0; i < (important.size()-k); ++i) {
        luck -= important[i];
    }
    for (int i = (important.size()-k); i < important.size(); ++i) {
        luck += important[i];
    }
    cout << luck << endl;
    return 0;
}
