# include <iostream>
# include <cstdlib> 
  
using namespace std;

int main(){

    int min = 2022;
    int max = 24680; //declare range of the random number
    int x, i, a;
    int rannum; //random number

    cout << "Enter a positive integer:";
    cin >> x;
  
    srand(x);  

    //generate random number
    for (i = 0; i < 1; i++){  
        rannum = min + (rand() % (max - min +1));
        cout << rannum; 
    }  
    cout << endl;

    //display factors
    cout << "Factors of " << rannum << " are: ";  

    // assume if a is number lower than random number
    // try every a and verify if a is the factor of the random number
    for (a = 1; a <= rannum; a++) {
        if (rannum % a == 0){
            if (a == 1){
                cout << "";
            }
            // print out a if a is the factor 
            else {
                cout << a << " ";
            }
        }
    }  

    // Termination
    return 0;
}   

