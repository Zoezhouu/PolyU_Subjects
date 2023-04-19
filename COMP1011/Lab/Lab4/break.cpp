#include <iostream>
#include <ctime>

using namespace std;

int main(){

    srand(time(0));
    int maxoddnum = 15;
    int earlystop, curoddnum;

    for (int count = 1; count <= maxoddnum && (earlystop = rand()/100) >= (curoddnum = count *2 - 1); count++) {
        if (count == 1){
            cout << curoddnum;
        }
        else {
            cout << "," << curoddnum;
        }
    }
    return 0;
}