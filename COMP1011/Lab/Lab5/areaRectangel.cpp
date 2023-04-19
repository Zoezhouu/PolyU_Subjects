#include <iostream>
using namespace std;

float rectangleArea(float width, float height) {
    float area;
    area = width * height;
    return area;
}

int main() {
	float width, height;

	cout << "Please enter rectangle width: ";
	cin >> width;

    cout << "Please enter rectangle height: ";
	cin >> height;

    if (width > 0 && height > 0) {
        cout << "Area: " << rectangleArea(width, height) << endl;
    }
    else {
        cout << "invalid input number, please enter them again" << endl;
    }

	return 0;
}
