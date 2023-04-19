#include <iostream>

using namespace std;

bool isPrime(int n)
{
    for (int i = 2; i < n; i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}

int countPrime(int n)
{
    // Base case
    // n is 2, which is prime
    if (n == 2)
    {
        return 1;
    }
    // Recursive relationship
    // Number of prime of in [2, n] 
    // = number of prime in [2, n - 1] + (Is n a prime? (True = 1, False = 0))

    return countPrime(n - 1) + isPrime(n);
}

int main()
{

    int input;
    cout << "Please enter an integer: ";
    cin >> input;

    cout << "Total number of prime between 2 and " << input << " is "
         << countPrime(input) << "." << endl;
}
