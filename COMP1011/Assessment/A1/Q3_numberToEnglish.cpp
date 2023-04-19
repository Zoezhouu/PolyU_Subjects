#include <iostream>

using namespace std;

// Processing part (Including the output)
// This function converts numbers to the English words.

void english(int value) {

    // English of numbers that bigger than 20 is constructed by two parts:
    // English of tens and English of ones.
    if (value >= 20) {
        // English words of tens
        if (value/10 == 2){
            cout << "twenty";
        }

        else if (value/10 == 3){
            cout << "thirty";
        }

        else if (value/10 == 4){
            cout << "forty";
        }

        else if (value/10 == 5){
            cout << "fifty";
        }

        else if (value/10 == 6){
            cout << "sixty";
        }

        else if (value/10 == 7){
            cout << "seventy";
        }

        else if (value/10 == 8){
            cout << "eighty";
        }

        else {
            cout << "ninety";
        }
        
        // if value % 10 != 0
        // then add an '-' after the English word of tens
        // then value % 10 should come through function -- english() again to calculate ones.
        if (value % 10 != 0){
            cout << "-";
            english(value % 10);
        }

    }
    // English of numbers that smaller than 20 only constructed by one word.
    else {

        if (value == 1){
            cout << "one";
        }

        else if (value == 2){
            cout << "two";
        }

        else if (value == 3){
            cout <<"three";
        }

        else if (value == 4){
            cout << "four";
        }

        else if (value == 5){
            cout << "five";
        }

        else if (value == 6){
            cout << "six";
        }

        else if (value == 7){
            cout << "seven";
        }

        else if (value == 8){
            cout << "eight";
        }

        else if (value == 9){
            cout << "nine";
        }

        else if (value == 10){
            cout << "ten";
        }

        else if (value == 11){
            cout << "eleven";
        }
            
        else if (value == 12){
            cout << "twelve";
        }

        else if (value == 13){
            cout << "thirteen";
        }

        else if (value == 14){
            cout << "fourteen";
        }

        else if (value == 15){
            cout << "fifteen";
        }

        else if (value == 16){
            cout << "sixteen";
        }

        else if (value == 17){
            cout << "seventeen";
        }

        else if (value == 18){
            cout << "eighteen";
        }
        else {
            cout << "nineteen";
        }
    }
    return;

}


int main() {
    // Declare the input
    int num;
    cin >> num;

    // If user's input is -1, then terminated this program.
    // If user's input is between 1 and 99, then continues the conversion.
    while (num != -1){
        english (num);
        cout << endl;
        //because this is a loop, then input again.
        cin >> num;
        continue;
    }
    
    // Termination
    return 0;
}