#include <iostream>
#include <ctime>

using namespace std;

int main()
{
    char random[27]="";
    srand((unsigned)time(NULL));//set random seed
    for(int i = 0; i < 20;++i){
        random[i] = rand()%26+'a';
    }
    cout<<random<<endl;
}
