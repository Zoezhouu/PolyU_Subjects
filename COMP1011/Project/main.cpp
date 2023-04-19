//Linear Reagression

#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <windows.h> //sleep
#include <cmath>

using namespace std;

double sum_x = 0;
double sum_y = 0;
double sum_xy = 0;
double sum_x_sq = 0;
int n = 0;
double ave_x = 0;
double ave_y = 0;
double b_ba = 0;
double a_ba = 0;
int rows;
int columns;

//Introduce concepts
void introduction(){
    fstream infile("information.txt"); //introduction
    string line;
    if (infile.is_open()){
        while (getline(infile, line)){
            cout << line << endl;
            Sleep(2000);    //allows user to read every line in the interval time
        }
        infile.close();
    }
    else{
        cout << "Unable to open file";
        introduction();
    }
}

// calculate number of point - line of the document
// calculate number of rows
// Read the file count line by line to get the number of lines in the input file
int getFileRows1(){
    ifstream file;
    string temp;
    int count = 0;// row counter
    file.open("example1_data.txt",ios::in);//ios::in - read only
    
    if(file.fail()) {
            return 0;
    }
    else {
        while(getline(file,temp,'\n')) { 
            if (temp.size() > 0 )
            count++;
        }
        file.close();
        return count;
    }
}

//calculate process(sum) for example 1
void getData1AndSum(int rowNum, int colNum) {
    int temp = 0;
    int data[rowNum][colNum];

	ifstream file;	
	file.open("example1_data.txt",ios::in);	
    for (int i = 0; i < rowNum; i++){
        for (int j = 0; j < colNum; j++){
            file >> data[i][j];
        }
    }
    for (int k = 0; k < rowNum; k++){
        int data_x = data[k][0];
        int data_y = data[k][1];

        //Calculation
        sum_x += data_x;
        sum_y += data_y;
        sum_xy += (data_x * data_y);       
        sum_x_sq += (data_x * data_x);
    }

    n = rowNum;	
}

int getFileRows2(){
    ifstream file;
    string temp;
    int count = 0;// row counter
    file.open("example2_data.txt",ios::in);//ios::in - read only
    
    if(file.fail()) {
            return 0;
    }
    else {
        while(getline(file,temp,'\n')) { 
            if (temp.size() > 0 )
            count++;
        }
        file.close();
        return count;
    }
}

//output: sums for example 2
void getData2AndSum(int rowNum, int colNum) {
    int temp = 0;
    int data[rowNum][colNum];

	ifstream file;	
	file.open("example2_data.txt",ios::in);	
    for (int i = 0; i < rowNum; i++){
        for (int j = 0; j < colNum; j++){
            file >> data[i][j];
        }
    }
    for (int k = 0; k < rowNum; k++){
        int data_x = data[k][0];
        int data_y = data[k][1];
        //Calculation
        sum_x += data_x;
        sum_y += data_y;
        sum_xy += (data_x * data_y);
        sum_x_sq += (data_x * data_x);
    }
    n = rowNum;	
}


//sub-concept 1
void subcon1(){
    fstream infile("subconcept1.txt"); //sub-concept1
    string line;
    if (infile.is_open()){
        while (getline(infile, line)){
            cout << line << endl;
            Sleep(2000);    //allows user to read every line in the interval time
        }
        infile.close();
    }
    else{
        cout << "Unable to open file";
        subcon1();
    }
}

//sub-concept 2
void subcon2(){
    fstream infile("subconcept2.txt"); //sub-concept2
    string line;
    if (infile.is_open()){
        while (getline(infile, line)){
            cout << line << endl;
            Sleep(2000);    //allows user to read every line in the interval time
        }
        infile.close();
    }
    else{
        cout << "Unable to open file";
        subcon2();
    }
}

// Input points for users
// Ask for number of point
void inputAndSum(){
    double data_x = 0;
    double data_y = 0;
    cout << "Guidelines: ";
    cout << "Please enter how many number of points would you enter:" << endl;
    cin >> n;
    cout << " " << endl;

    for ( int i = 1; i <= n; i++){
        // Ask for x-coordinate and y-coordinate for every points.
        cout << "Please enter value " << i << " for x:" << endl;
        cin >> data_x;
        cout << " " << endl;
        cout << "Please enter value " << i << " for y:" << endl;
        cin >> data_y;
        cout << " " << endl;

        //Calculation
        sum_x += data_x;
        sum_y += data_y;
        sum_xy += (data_x * data_y);   
        sum_x_sq += (data_x * data_x);

    }

}

double average(double a){
    cout << "average of " << a << " = " << a / n << endl;
    double ave = a / n;
    return ave;
}

double B_ba(double calc1, double calc2){
    double square_ave_x = calc1 * calc1; //square of average x
    cout << "sqaure of average x = " << square_ave_x << endl;
    
    double calc3;
    calc3 = (sum_xy - n * calc1 * calc2) / (sum_x_sq - n * square_ave_x);
    cout << "Value of b = " << calc3 << endl;
    return calc3;
}

void A_ba(){
    cout << "Value of a = " << ave_y - b_ba * ave_x << endl;
    a_ba = ave_y - b_ba * ave_x;
}

//Calculation for only one variables
void calc1Var(){
    
    ave_x = average(sum_x);
    ave_y = average(sum_y);
    b_ba = B_ba(ave_x,ave_y);
    A_ba();         // calculate a_ba

    cout << "value of n: " << n << endl;
    cout << "sum of all x value: " << sum_x << endl;
    cout << "sum of all y value: " << sum_y << endl;
    cout << "sum of all x multiply all y: " << sum_x_sq << endl;
    cout << "sum of all x squared: " << sum_xy << endl;
    cout << "average of x: " << ave_x << endl;
    cout << "average of y: " << ave_y << endl;
    cout << "a: " << a_ba << endl;
    cout << "b: " << b_ba << endl;
    cout << "linear regression equation is: y = " << b_ba << "x + " << "(" << a_ba << ")" << endl;
    //system("pause");

}

int getFileRows3(){
    ifstream file;
    string temp;
    int count = 0;// row counter
    file.open("example3_data.txt",ios::in);//ios::in - read only
    
    if(file.fail()) {
            return 0;
    }
    else {
        while(getline(file,temp,'\n')) { 
            if (temp.size() > 0 )
            count++;
        }
        file.close();
        return count;
    }
}


void resultFor3(int rowNum){
    int distance_a[rowNum];
    int distance_b[rowNum];
    int distance_c[rowNum];

    int temp = 0;
    int data[rowNum][2];

	ifstream file;	
	file.open("example3_data.txt",ios::in);	
    for (int i = 0; i < rowNum; i++){
        for (int j = 0; j < 2; j++){
            file >> data[i][j];
        }
    }
    
    cout << "----------------------------------------------------------------------------------------------------"<< endl;
    cout << "Firstly, we should calculate the distance between every data points and (0,100), (50,50) and (100,0)" << endl;
    
    // (0,100)
    for (int i = 0; i < rowNum; i++) { 
        int xa = 0;
        int ya = 100;
        int data_x = data[i][0];
        int data_y = data[i][1];
        double da = sqrt( (data_x - xa) ^ 2 + (data_y - ya) ^ 2);
        distance_a[i] = da;
    }

    //(50,50)
    for (int j = 0; j < rowNum; j++) { 
        int xb = 50;
        int yb = 50;
        int data_x = data[j][0];
        int data_y = data[j][1];
        double db = sqrt( (data_x - xb) ^ 2 + (data_y - yb) ^ 2);
        distance_b[j] = db;
    }

    // (100, 0)
    for (int k = 0; k < rowNum; k++) { 
        int xc = 100;
        int yc = 0;
        int data_x = data[k][0];
        int data_y = data[k][1];
        double dc = sqrt( (data_x - xc) ^ 2 + (data_y - yc) ^ 2);
        distance_c[k] = dc;
    }

    // compare distance
    cout << "Then we compare distance between every point and point (0,100),(50,50) and (100,0)."<< endl;
    int count_c = 0;
    int c_array[rowNum][2];
    int count_b = 0;
    int b_array[rowNum][2];
    int count_a = 0;
    int a_array[rowNum][2];

    for(int i = 0; i < rowNum; i++) {
        if (distance_a[i] > distance_b[i]) {
            if (distance_b[i] > distance_c[i]) {
                c_array[i][0] = data[i][0];
                c_array[i][1] = data[i][1];
            } 
            else if (distance_b[i] < distance_c[i]) {
                b_array[i][0] = data[i][0];
                b_array[i][1] = data[i][1];
            }
        } 
        else if (distance_a[i] < distance_b[i]){
            if (distance_a[i] > distance_c[i]) {
                c_array[i][0] = data[i][0];
                c_array[i][1] = data[i][1];
            } 
            else if (distance_a[i] < distance_c[i]) {
                a_array[i][0] = data[i][0];
                a_array[i][1] = data[i][1];
            }
        }  
    }

    // For a
    cout << "--------------------------------------------------------------------------------------" << endl;
    cout << "Data Summary for the first point(0,100), the points near it is calculated as follows:" << endl;
    for (int i = 0; i < rowNum; i++){
        int data_x = a_array[i][0];
        int data_y = a_array[i][1];

        //Calculation
        sum_x += data_x;
        sum_y += data_y;
        sum_xy += (data_x * data_y);        
        sum_x_sq += (data_x * data_x);
        count_a++;
    }
    {
        n = count_a;
        calc1Var();
        cout << endl;
        Sleep(5000);
    }

    //for b
    cout << "-------------------------------------------------------------------------------------"<< endl;
    cout << "Data Summary for the first point(50,50), the points near it is calculated as follows:" << endl;
    for (int i = 0; i < rowNum; i++){
        int data_x = b_array[i][0];
        int data_y = b_array[i][1];

        //Calculation
        sum_x += data_x;
        sum_y += data_y;
        sum_xy += (data_x * data_y);        
        sum_x_sq += (data_x * data_x);
        count_b++;
    }
    {
        n = count_b;
        calc1Var();
        cout << endl;
        Sleep(5000);
    }
    
    //for c
    cout << "-------------------------------------------------------------------------------------"<< endl;
    cout << "Data Summary for the first point(100,0), the points near it is calculated as follows:" << endl;
    for (int i = 0; i < rowNum; i++){
        int data_x = c_array[i][0];
        int data_y = c_array[i][1];

        //Calculation
        sum_x += data_x;
        sum_y += data_y;
        sum_xy += (data_x * data_y);        
        sum_x_sq += (data_x * data_x);
        count_c++;
    }
    {
        n = count_c;
        calc1Var();  
        cout << endl;
        Sleep(5000);  
    }

    cout << "-------------------------------------------------------------------------------------"<< endl;




}



int main(){
    // Introduce concept
    introduction(); //**

    // example 1 - beginner level
    cout << "For beginner level, let's only sees few points and calculate step by step." << endl;
    cout << "Let's see the example 1 for our beginner level.\n Here are the coordinators of points in example 1:" << endl;

    ifstream file1 ("example1_data.txt");
    string line1;
    if (file1.is_open()){
        while (getline(file1,line1)){
        cout << line1 << '\n';
        }
    }
    else {
        cout <<"unable to open file";
    }
    file1.close();

    {
        rows = getFileRows1();
        columns = 2;
        getData1AndSum(rows, columns);
        cout << "---------------------------------" << endl;
        cout << "Data Summary for example 1: " << endl;
        calc1Var();
        cout << endl;
        Sleep(5000);
    }

    
    // example 2 - intermediate level
    cout << "For intermediate level, let's see more points and calculate step by step." << endl;
    cout << "Let's see the example 2 for our intermediate level.\n Here are the coordinators of points in example 1:" << endl;

    ifstream file2 ("example2_data.txt");
    string line2;
    if (file2.is_open()){
        while (getline(file2,line2)){
        cout << line2 << '\n';
        }
    }
    else {
        cout <<"Unable to open file";
    }
    file2.close();

    {
        rows = getFileRows2();
        columns = 2;
        getData2AndSum(rows, columns);
        cout << "---------------------------------" << endl;
        cout << "Data Summary for example 3: " << endl;
        calc1Var();
        cout << endl;
        Sleep(5000);
    }

    
    //example 3 - advanced level
    cout << "For advanced level, let's only sees more points with segmentation and calculate step by step." << endl;
    cout << "Let's see the example 3 for our advanced level.\n Here are the coordinators of points in example 3:" << endl;
    cout << "also the data in example 3 is same as those in example 2.\nBut the only difference is there should be three clusters to model the linear regression." <<endl;
    cout << "That is to say, there are three lines here for three clusters. \nThese three clusters can be classified by three points here: (0,100) , (50,50), and (100,00)" << endl;
    {
        rows = getFileRows3();
        columns = 2;
        resultFor3(rows);
    }




    //interactivity
    //choose sub-concepts to learn
    cout << "Aftergiving you an introduction and showing you few example, I believe you must know something about Linear Regression." << endl;
    cout << "If you want to know more sub-concept about Linear Regression." << endl;
    cout << "Here are few sub-concepts for you." << endl;
    cout << "(1) Sub-concept 1 - R value - correlation index for Linear Regression" << endl;
    cout << "(2) Sub-concept 2 - Multiple Linear Regression" << endl;

    int input;
    cout << "Please enter a number(enter -1 to quit, 1 for sub-concept 1, 2 for sub-concept 2): ";
    cin >> input;
    char yorn;
    while (input != -1){
        if (input = 1){
            subcon1();
            break;
        }
        else if (input = 2){
            subcon2();
            break;
        }
        else {
            cout << "Please enter number again(enter -1 to quit, 1 for sub-concept 1, 2 for sub-concept 2)" << endl;
            cin >> input;
            continue;
        }      

    }    

    // inputting data(guidelines by the program)
    cout << "You can input the point coordinates for calculation now" << endl;
    inputAndSum(); //one variable **
    calc1Var(); //**

    cout << "Thanks for your learning progress!";


    return 0;
}