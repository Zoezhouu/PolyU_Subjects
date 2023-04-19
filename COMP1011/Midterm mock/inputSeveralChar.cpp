#include<iostream>

using namespace std;
 
int main() {
    
    char input;
    cout << "Please enter a character.('n' to quit)" << endl;
    cin >> input;
    for (char input =' '; input != 'n'; input++) {
        cout << "Please enter a character.('n' to quit)" << endl;
        cin >> input;
        cout <<"The input is " << input << endl;
        input =' ';
    }
    return 0;
}