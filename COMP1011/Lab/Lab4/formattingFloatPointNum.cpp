#include <iostream>
#include <iomanip>

using namespace std;

int main(){

    float temp = 1;
    float save;
    int iteration = 0;

    while (temp >= 0.0001){
        save = temp;
        temp = temp / 2;
        iteration++;
        cout << setprecision(16) << fixed << temp << endl;
    }

    cout << endl;
    cout << save << " is just greater than 0.0001" << endl;
    cout << "It needs " << iteration - 1 << " divisions." << endl;

    return 0;
}