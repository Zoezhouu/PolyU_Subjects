#include <iostream>
using namespace std;

int main()
{
    int h;
    cin >> h;

    char letter = 'A';
    // i: height
    // j: number of space
    // k: letter number

    for (int i = 0; i < h; i++)
    {
        for (int j = i; j < h; j++)
            cout << " ";
        
        for (int k = 1; k <= i * 2 + 1; k++)
        {
            cout << letter;
            if (letter == 'Z')
                letter = 'A';
            else
                letter++;
        }
        cout << endl;
    }

    // i: height
    // j: number of space
    for (int i = 0; i < h / 2; i++)
    {
        for (int j = 0; j < h - 1; j++)
            cout << " ";
        cout << letter << " " << letter << endl;
        if (letter == 'Z')
            letter = 'A';
        else
            letter++;
    }

    return 0;
}
