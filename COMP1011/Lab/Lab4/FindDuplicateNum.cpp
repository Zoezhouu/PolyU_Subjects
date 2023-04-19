#include <iostream>

using namespace std;

int main(){
    int input;
    int length = 0;
    const int arraysize = 10;
    int container[arraysize];
    int i, j;
    bool duplicate = false;

    // feed into array
    do{
        //ensure the input is a number between 10 and 100
        do{
            cout << "Please enter number " << length + 1 << "[10 - 100]:";
            cin >> input;
        }
        while (!(input >= 10 && input <= 100));

        container[length] = input;
        length++;
    }
    while (length < arraysize);

    //judge whether the contains duplicate
    for (i = 0; i < arraysize ; i++){
        //whether the other value is the same as this one
        for (j = 0; j < arraysize ; j++){
            if (container[i] == container[j] && i != j){
                duplicate = true;
            }
        }

        //if no duplicate
        if (!duplicate){
            cout << container[i] << ' ';
        }

        //refresh for next one
        duplicate = false;
    }
    cout << endl;
    return 0;
}