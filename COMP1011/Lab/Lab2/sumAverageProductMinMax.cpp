#include <iostream>

using namespace std;

int main(){
    int first, second, third;
    cout << "Input three different integer:" ;
    cin >> first >> second >> third;
    cout << "Sum is " << first + second + third << endl;
    cout << "Average is " << (first + second + third) / 3.0 << endl;
    cout << "Product is " << first * second * third  << endl;

    //smallest
    int smallest = first;
    if (second < smallest){
        smallest = second;
    }
    if (third < smallest) {
        smallest = third;
    }
    cout << "Smallest is " << smallest << endl;

    //largest
    int largest = first;
    if (second < largest){
        largest = second;
    }
    if (third < largest) {
        largest = third;
    }
    cout << "Largest is " << largest << endl;

    return 0;
}
/*
    Prompt the user to input integer1, integer2, integer3
    Calculate sum = integer1 + integer2 + integer3
    Calculate average = sum / 3
    Calculate product = integer1 * integer2 * integer3
    Set integer1 as the smallest
    If integer2 < smallest then set integer2 as the smallest
    If integer3 < smallest then set integer3 as the smallest
    Set integer1 as the largest
    If integer2 > largest then set integer2 as the largest
    If integer3 > largest then set integer3 as the largest
    Print sum, average, product, smallest and largest to the screen
*/