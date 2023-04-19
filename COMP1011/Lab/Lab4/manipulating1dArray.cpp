#include <iostream>

using namespace std;

int main(){

    int input = 0;
    int index = 0;
    const int arraysize = 1000;
    int container[arraysize];
    int i, finalresult = 0, length;
    cout << "Enter integers (-999 to end): ";

    //input sequence
    while (input != -999) {
        cin >> input;
        if (input != -999) {
            container[index] = input;
            index = index + 1;
        }
    }

    if (input == -999) {
        length = index;
        for (i = 0; i < length; i++) {
            //when index is an even number
            if (i % 2 == 0){
                finalresult += container[i];
            }
            //when index is an odd number
            else {
                finalresult-= container[i];
            }
        }
        cout << finalresult << endl;
    }
    return 0;
}