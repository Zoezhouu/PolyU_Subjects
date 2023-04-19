#include <iostream>
#include <iomanip>
using namespace std;

int main() {

    int num[5][5];
    // row
    for (int i = 0; i < 5; i++) { 
        // col
        for (int j = 0; j < 5; j++) { 
            num[i][j] = (i + 1) * (j + 1);  // find the pattern
            cout << (i + 1) * (j + 1) << setw(5); // display
        }

        cout << '\n' ;
    }

    return 0;
}
