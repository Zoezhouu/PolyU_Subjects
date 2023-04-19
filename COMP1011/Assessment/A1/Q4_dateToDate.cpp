#include <iostream>

using namespace std;


// Function leapyear(int year) determines whether the year is leap year or not. 
bool leapyear (int year){  
	return (year%4==0 && year%100!=0) || year%400==0 ;
}

// Processing part
// Standard: Year 1 Jan. 1
// Function getdays(int year, int month, int day) determines the days from date 1 1 1
int getdays (int year, int month, int day){   
	
	// Declare array m with element[0]--"0" for easier indication
	int m[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};   

	// If the year is leap year, the days in February plus 1.
	if (leapyear (year)){
		m[2]++; 
	}
	
	// Declare started result = 0
    int result = 0; 

	// Calculate days from Year 1 Jan. 1 to the input data
	for (int a = 1; a < year; a++){ 
		result += 365;   

		// If the year is leap year, the result plus 1.
		if (leapyear (a)){ 
			result++;
        }
	}

	// Plus days in every month  
	for (int a = 1; a < month; a++){ 
		result += m[a]; 
	}

	// Plus day
	result += day;

	return result;
}

// This function converts result to the correct format
int dayis (int year1, int month1, int day1, int year2, int month2, int day2){
	// if the date 2 is before date 1, then the result will be negative,
	// but result should always be positive, then we need declare the absolute value between two days
	int absvalue;
	// calculate absolute value
    absvalue = abs(getdays (year2, month2, day2) - getdays (year1, month1, day1));

	// Both dates will be calculated, then the value should plus 1. 
    return absvalue + 1;
}
	
int main(){
	// Declare all variables for input 
    int day1, day2, month1, month2, year1, year2;

	// Initialization: Input date 1 and date 2
    cout << "Please input date 1 in a format of day month year." << endl;
	cin >> day1 >> month1 >> year1;
    cout << "Please input date 2 in a format of day month year." << endl;
    cin >> day2 >> month2 >> year2;

	// Output(include processing)
	cout << dayis(year1, month1, day1, year2, month2, day2);
	
	return 0;
} 