#include <iostream>
#include <stdio.h>
using namespace std;

int cut(int);

int main()
{
    int n;
    cout << "Please enter the cut number (an integer): ";
    cin >> n;

    cout << "How many pieces of cakes: " << cut(n) << endl;
    return 0;
}

int cut(int x)
{
    int y;
    // base case
    if (x == 0)
        return 1;
    if (x == 1)
        return 2;
    // recursive relationship
    else
        y = cut(x - 1) + 2;

    return y;
}