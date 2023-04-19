#include <iostream>
using namespace std;

double average(double *, int);

int main() {

    double data[] = {1, 2, 3, 4, 5};
    double* aPtr = data;
    int array_size = sizeof(data) / sizeof(data[0]); 

    cout << "average: " << average(data, array_size);

    return 0;
}

double average(double *aPtr, int size){
    
    double avg_result;

    for(int offset1 = 0; offset1 < size; offset1++){
            avg_result += *(aPtr + offset1);
    }

    return (avg_result / size);
}