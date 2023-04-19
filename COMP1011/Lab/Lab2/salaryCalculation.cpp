#include <iostream>
#include <cmath>

using namespace std;

int main(){

    double x, origin_salary, output;

    cout << "What is your salary?";
    cin >> origin_salary;

    x = pow(1.05,10); // After 10 years
    output = origin_salary * x;

    cout << "After 10 years, your salary is: " << output << endl;

    return 0;


}