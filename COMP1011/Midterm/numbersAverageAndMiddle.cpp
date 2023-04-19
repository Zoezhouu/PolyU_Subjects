#include<iostream>
#include <algorithm>

using namespace std;

int main() {
	double average;
	double accumulateValue;
	cout << "Please enter N integers (0 < N < 100) ended with -1: ";
	double n;
	double median = 0;

	while (cin >> n){
		accumulateValue += n;

		if (n == -1)
			break;

		int *a = new int[n];   //new array

		for (int i = 0; i < n; i++)    
			cin >> a[i];
			accumulateValue += a[i];
			if (a[i] == -1)
				break;
		
		average = accumulateValue / n;

		if (n % 2 != 0)    //odd
			median = a[(n / 2)-1];
		else //even
			median = (a[(n / 2)-1] + a[(n / 2 + 1)-1]) / 2;
		
		cout << "Average: " << average << endl;
		cout << "Middle: " << median << endl;
	}
	return 0;
}


