#include <iostream>

using namespace std;

int main(){
    int input = 0;
    int counter = 0;
    double total = 0;
    double average;

    cout << "Enter integers(999 to end): " << endl;

    while (input != 999){
        cin >> input;

        if (input != 999) {
            total += input;
            counter++;
        }
    }
    
    if (counter !=0){
        average = total / counter;
        cout <<"The average number is:" << average << endl;
    }
    else {
        cout << "No input!" << endl;
    }


    return 0;
}