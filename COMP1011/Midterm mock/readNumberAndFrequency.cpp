#include<iostream>

using namespace std;

int main() {

	int currVal = 0, val = 0;

	if (cin >> currVal) {
        //ensure number can be read
		//read first number(currVal)
		
        int counter = 1; //read only 1 number

        //this loop is used for reading left numbers
		while (cin >> val) { 
			if (val == currVal)
				++counter;//if same to the last number, then counter +1
			
            else {//otherwise, print frequence of last value
				cout << currVal << " occurs " << counter << " times " << endl;
				currVal = val; //update currVal to new number
				counter = 1; //renew counter
			}
		}
        //when read to the last number, while loop will be stopped, this sentence for termination
		cout << currVal << " occurs " << counter << " times " << endl;//print frequence of last number
	}
	return 0;
}

