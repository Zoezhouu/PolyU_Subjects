#include <iostream>
using namespace std;

void swap(int &, int &);
void bubble_sort(int[], int);
void get_user_input(int *, int);

int main()
{
    const int SIZE = 5;
    int num[SIZE];
    get_user_input(num, SIZE); // 1. get input

    bubble_sort(num, 5); // 2. sort integers

    // 3. judgement
    if (num[SIZE - 1] - num[0] == SIZE - 1)
    {
        for (int i = 0; i < SIZE; i++)
        {
            cout << num[i] << " ";
        }
        cout << " The sorted array is consecutive numbers";
    }
    else
    {
        cout << " The numbers are not consecutive.";
    }

    cout << endl;
    return 0;
}

// get input
void get_user_input(int *num_array, int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << "Please input positive value " << i << ": ";
        cin >> num_array[i];
    }
}

// swapping two elements
void swap(int &a, int &b)
{
    int temp;
    temp = a;
    a = b;
    b = temp;
}

// sort the input array
void bubble_sort(int numarray[], int size)
{
    for (int i = 0; i < size - 1; i++)
    {
        for (int j = 0; j < size - 1; j++)
        {
            if (numarray[j] > numarray[j + 1])
            {
                swap(numarray[j], numarray[j + 1]);
            }
        }
    }
}