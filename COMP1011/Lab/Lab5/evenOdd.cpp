#include <iostream>
using namespace std;

bool isEven(int number){
    if(number % 2 == 0){
        return true;
    }
    return false;
}

bool isOdd(int number){
    if (number % 2 == 0){
        return false;
    }
    return true;
}

bool isOdd2(int number){
    return !isEven(number);
}

int main() {

	int input_num;
    int call_times = 3;

    for (int i = 0; i < call_times; i++){
        
        cout << "Enter an integer: ";
	    cin >> input_num;

        if (isEven(input_num)) {
            cout << input_num << " is an even integer." << endl;
        } else{
            cout << input_num << " is an odd integer."<< endl;
        }

        cout << endl;
    }

	return 0;
}
