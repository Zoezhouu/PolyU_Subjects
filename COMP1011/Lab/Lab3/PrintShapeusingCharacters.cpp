#include <iostream>

using namespace std;

int main(){

    int n = 0;
    char thechar;

    cout << "How many rows?";
    cin >> n;

    cout << "The character to be print: ";
    cin >> thechar;

    int i=0;

    while (i < n) {
        int j = 0;

        while (i>= j){
            cout << thechar;
            j++;
        }

        cout << endl;
        i++;
    }
    return 0;
}