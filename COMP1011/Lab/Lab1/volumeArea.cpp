#include <iostream>

using namespace std;

int main() {
	
	double r = 11;  // radius in unit cm
	double pi  = 3.14;
	double sphere_V = (4.0/3) * pi * (r * r * r); //sphere volume
	double SA = 4 * pi * r * r; // surface area

	cout << "Volume = " << sphere_V;
	cout << "Area = " << SA;

	return 0;
}

