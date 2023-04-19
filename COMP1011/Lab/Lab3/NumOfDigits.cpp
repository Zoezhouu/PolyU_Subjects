#include <iostream>

using namespace std;

int main(){

    int input;
    cout << "Input an nteger between 1 and 9999: ";
    cin >> input;

    int temp = input;
    int i = 1;

    while (temp > 9) {
        temp = temp/10;
        i++;
    }

    cout << input << " can be expressed in " << i << " digits." << endl;

    return 0;
}