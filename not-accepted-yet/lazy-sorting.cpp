// PROBLEM: https://www.hackerrank.com/contests/w21/challenges/lazy-sorting

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

int fact(int n) {
    if (n == 1) {
        return 1;
    }
    return n * fact(n-1);
}
int main() {
    double n, p;
    cin >> n;
    set<int> numbers;
    while (cin>>p) {
        numbers.insert(p);
    }
    n = numbers.size();
    double sum = 0;
    double new_sum; 
    bool found = false;
    int i = 1;
    int eq = 0;
    while (!found) {
        new_sum = sum + i * pow(fact(n),-i);
        if (new_sum == sum) {
            eq++;
        } else {
            eq = 0;
            sum = new_sum;
        }
        ++i;
        if (eq == 10) found = true;
    }
    cout << fixed << sum << endl;

    return 0;
}
