#include <iostream>
using namespace std;

int fib(int x)
{
    if (x == 1 || x == 0)
    {
        return x;
    }
    return fib(x - 1) + fib(x - 2);

}

int main()
{
    // Testing N = 20
    for(int i = 1; i <= 20; i++)
    {
        cout << fib(i) << " ";
    }
    cout << endl;

    return 0;
}