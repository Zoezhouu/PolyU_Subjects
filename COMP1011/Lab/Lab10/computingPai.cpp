#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;

long double function_Q(int);
long double function_R(int);

int main()
{
    
    long double pi;
    
    for(int n = 1; n <= 30; n++) {
        pi = 2 * sqrt(2) / function_R(n);
        cout << "(n = " << n << ") pi = " << setprecision(20) << pi << endl;
    }
    return 0;
}

long double function_Q(int x)
{
    long double y;
    // base case
    if (x == 1)
        return sqrt((0.5 + 0.5 * sqrt(0.5)));
    // recursive relationship
    else
        y = sqrt((0.5 + 0.5 * function_Q(x - 1)));

    return y;
}

long double function_R(int x)
{
    long double y;
    // base case
    if (x == 1)
        return function_Q(1);
    // recursive relationship
    else
        y = function_R(x - 1) * function_Q(x);

    return y;
}