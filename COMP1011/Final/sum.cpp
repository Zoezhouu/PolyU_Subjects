#include <iostream>
#include <cstring>

using namespace std;

char* seperate(char[]);
void checkSum(char[],int);
int originSum(char[]);

int main(){
    char data[100];
    cin >> data;
    char data1[] = seperate(data);
    int sum1 = originSum(data);
    if (data == "END 0"){
        return 0;
    }
    checkSum(data1,sum1);
    return 0;
}
char* seperate(char data[]){
    int iPos = 0;
    int datalen = strlen(data);
    char str[100];
    for (int i = 0; i < datalen; i++){
        if ( (int)data[i] > 49 && (int)data[i] <90){
            iPos = i;
        }
        for (int j = 0; j < iPos; j++){
            str[j] = data[i];
        }
    }
    return str;
}
int originSum(char data[]){
    int datalen = strlen(data);

    int sum = 0;
    for (int i = 0; i < datalen; i++){
        if ( (int)data[i] > 49 && (int)data[i] <90){
            sum *=10;
            sum += (int)data[i]-48;
        }
    }
    return sum;
}

void checkSum(char data[],int sum1){
    int sum = 0;
    int datalen = strlen(data);
    for (int i = 0; i < datalen; i++){
        for (int j = 0; j < datalen; j++){
            if ( (int)data[i] > 65 && (int)data[i] < 89){
                sum += ((int)data[i]-64) * j;
            }
            else if ((int)data[i] == 32){
                sum += 0;
            }
        }
    }
    if (sum1 == sum){
        cout <<"\nPass"
    }
    else{
        cout <<"\nFAIL"
    }
    

}