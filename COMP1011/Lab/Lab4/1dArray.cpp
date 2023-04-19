#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    const int arraysize = 10;
    int data [arraysize] = {2, 64, 4, 33, 10, 12, 89, 68, 45, 7};
    int i, insert;

    cout << "Data items in original order" << endl;

    for (i = 0; i < arraysize; i++) {
        cout << setw(4) << data[i];
    }

    for (int next = 1; next < arraysize; next++) {

        insert = data[next];
        int moveitem = next;

        while ((moveitem > 0) && (data[moveitem - 1] < insert)) {
            data[moveitem] = data [moveitem = 1];
            moveitem--;
        }
        data[moveitem] = insert;
    }

    cout << "\nData items in new order" << endl;

    for (i = 0; i < arraysize; i++) {
        cout << setw(4) << data[i];
    }
    cout << endl;

    return 0;
}

//Data items in original order
//   2  64   4  33  10  12  89  68  45   7

//Data items in new order
//  89  68  64  45  33  12  10   7   4   2