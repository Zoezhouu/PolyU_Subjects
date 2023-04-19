#include <iostream>
#include <iomanip>
#include <cstring>
using namespace std;

int main()
{
    char input_string[10][11];
    const int ARRAY_SIZE = 10;
    int unique_indx[ARRAY_SIZE], repeat_num[ARRAY_SIZE];

    for (int i = 0; i < ARRAY_SIZE; i++)
    {
        cout << "Please enter string " << (i + 1) << ": ";
        cin.getline(input_string[i], 11, '\n');
    }

    // 1. judge whether unique string
    for (int j = 0; j < ARRAY_SIZE; j++)
    {
        unique_indx[j] = 0;
        repeat_num[j] = 0;
    }

    // unique_indx, if the string has appeared, value=1; otherwise, value=0
    for (int i = 1; i < ARRAY_SIZE; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (strcmp(input_string[i], input_string[j]) == 0)
            {
                unique_indx[i] = 1;
            }
        }
    }
    cout << endl;
    cout << setw(10) << "String" << setw(15) << "Frequency" << endl;
    cout << "--------------------------\n";

    // 2. count number for unique string
    for (int i = 0; i < ARRAY_SIZE; i++)
    {
        if (unique_indx[i] == 0)
        {
            for (int j = 0; j < ARRAY_SIZE; j++)
            {
                if (strcmp(input_string[i], input_string[j]) == 0)
                {
                    repeat_num[i] += 1;
                }
            }
            cout << setw(10) << input_string[i] << setw(15) << repeat_num[i] << '\n';
        }
    }
    return 0;        
}