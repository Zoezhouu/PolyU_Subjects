#include <iostream>
#include <cstring>

using namespace std;

void rotate(char*, int*);

int main() {

    char characters[51];

    cout << "Please enter a series of characters (Max. 50 characters): ";
    cin.getline(characters, 51, '\n');

    // check the length of the input characters
    int noOfChar = strlen(characters);

    // do the rotation
    for(int i = 0; i < noOfChar; i++) {
        rotate(characters, &noOfChar);
        cout << characters << endl;
    }
    return 0;
}

void rotate(char *charArray, int *size) {
    // save the last character first
    char lastChar = *(charArray + *size - 1);

    // start from the ending character
    // overwrite it by its previous character
    for(int i = *size - 1; i > 0; i--) {
        *(charArray + i) = *(charArray + i - 1);
    }

    // overwrite the first character
    *charArray = lastChar;
}
