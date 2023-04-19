# include <iostream>
# include <cmath>

using namespace std;

int main(){
    int choice;
    double num1;
    double num2;
    double x; //result

    cout << "MENU\n";
    cout << "           1. Divide. a/b\n";
    cout << "           2. Multiply. a*b\n";
    cout << "           3. Power. a^b\n";
    cout << "           4. Square root. sqrt(a)\n";

    cout << "Enter your choice:";
    cin >> choice;

    // selection calculation method
    // for choice 1,2,3, there's two input number
    // for choice 4, there's only one input number

    if (choice <= 3){ 
        cout << "Enter two numbers(integers):";
        cin >> num1 >> num2;

        if (choice == 1){
            x = num1 / num2;
            cout << num1 << "/" << num2 <<"=" << x << endl;
            }
        else if (choice == 2){
            x = num1 * num2;
            cout << num1 << "*" << num2 <<"=" << x << endl;
            }
        else {
            x = pow(num1, num2);
            cout << num1 << "^" << num2 <<"=" << x << endl;
            }
        } 
    else {
        cout << "Enter a number(integer):";
        cin >> num1;
        x = sqrt(num1);
        cout << "sqrt(" << num1 << ")" << "=" << x << endl;
        }
    return 0;
}