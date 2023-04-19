#include <iostream>
#include <cmath>

using namespace std;

int main(){
    double a, b, c, x1, x2, discriminant;

    cout << "Please enter a:";
    cin >> a;

    cout << "Please enter b:";
    cin >> b;

    cout << "Please enter c:";
    cin >> c;

    discriminant = b * b - 4.0 *a * c;

    if (a==0){
        cout << "a cannot be 0.";
    }
    else {
        if (discriminant > 0) {
            x1 = (-b + sqrt(discriminant)) / (2.0 * a);
            x2 = (-b - sqrt(discriminant)) / (2.0 * a);

            cout << "Two real roots:";
            cout << "x = " << x1 << " or " << x2 << endl;
        }
        else if (discriminant == 0){
            cout << "Repeated root: ";
            x1 = (-b + sqrt(discriminant)) / (2.0 * a);
            cout << "x = " << x1 << endl;
        }
        else {
            cout << "No real root." << endl;
        }
    }
    return 0;
}