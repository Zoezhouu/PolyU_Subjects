# include <iostream>
  
using namespace std;

int main(){

    int min = 1389;
    int max = 2809; //declare range of the random number
    int i;
    int rannum; //random number
    int input;

    //generate random number
    for (i = 0; i < 1; i++){  
        rannum = rand() % max + min;
    }

    while (true) {

        cout << "Please guess this random number(between 1389 and 2809): " << endl; 
        cin >> input;

        //guess number
        if (input > rannum){
            cout << "Too Big!" << endl;
        }
        else if (input < rannum) {
            cout << "Too Small!" << endl;
        }
        else {
            cout <<"Bingo!" << endl;
            break;
        }
        
    }

    return 0;

}