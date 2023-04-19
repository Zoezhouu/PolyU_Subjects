# include <iostream>
# include <fstream>
# include <cstring>
# include <iomanip>

using namespace std;

//change uppercase letter to lowercase letter
char *caseConverter(char *text, int length) {
    for (int i = 0; i <= length; i++) {
        if ((int)text[i] <= 90 && (int)text[i] >= 65) {
            text[i] += 32;
        }
    }
    return text;
}

//count word
int numOfWord(int *count, int line) {
    int total = 0;
    for (int i = 0; i < line; i++) {
        total += count[i];
    }
    return total;
}

//calculate number of lines in textfile.txt
int line_Num() {
    ifstream myfile;
    myfile.open("textfile.txt");
    myfile >> noskipws;
    int lineNum = 1;

    char tempChar;
    while (myfile >> tempChar) {
        if (tempChar == '\n') {
            ++lineNum;
        }
    }

    // cout << "lineNum" << lineNum << endl;
    return lineNum; 
}

//calculate number of lines in ignore.txt
int ignoreLine_Num() {
    ifstream myfile;
    myfile.open("ignore.txt");
    myfile >> noskipws;
    int lineNum = 1;

    char tempChar;
    while (myfile >> tempChar) {
        if (tempChar == '\n') {
            ++lineNum;
        }
    }

    return lineNum; 
}

void SelectSort(char *strings,char stringsSize){
   char min,temp;
   for(char i=0;i<stringsSize-1;i++){
        min=i;
        for(char j=i+1;j<stringsSize;j++){
            if(strings[min]>strings[j]){
                min=j;
            }
        }
        if(min!=i){
            temp=strings[min];
            strings[min]=strings[i];
            strings[i]=temp;
        }
    } 
}

char* intersection(char* strings1, char strings1Size, char* strings2, char strings2Size, char* returnSize) {
    char temp,i,j;
    char *result=(char *) malloc(strings2Size*sizeof(char));

    //selection sort
    SelectSort(strings1,strings1Size);
    SelectSort(strings2,strings2Size);

    *returnSize=0;
    temp=strings1[strings1Size-1]+1;  //Assign temp a value that cannot conflict with strings1 or strings2
    for(i=0,j=0;i<strings1Size&&j<strings2Size;){
        if(strings1[i]>strings2[j]){
            j++;
        }
        else if(strings1[i]<strings2[j]){
            i++;
        }
        else{
            if(temp!=strings1[i]){
                result[(*returnSize)++]=strings1[i];
                temp=strings1[i];
            }
            i++;
            j++;

        }
    }
    return result;
}

void core() {

    //read textfile.txt
    int wordLength;
    ifstream myfile;
    myfile.open("textfile.txt");
    myfile >> noskipws;                     //extract spaces
    
    int lineNum = line_Num();
    char textArray[lineNum][1001];
    for (int i = 0; i < lineNum; i++) {
        myfile.getline(textArray[i], 1000, '\n');
    }
    myfile.close();

    //length
    int length[lineNum];
    for (int i = 0; i < lineNum; i ++) {
        length[i] = strlen(textArray[i]);
    }

    for (int i = 0; i < lineNum; i ++) {
        *textArray[i] = *caseConverter(textArray[i], length[i]);
    }

    // split line into words
    char data[lineNum][1001][51];
    int countWord[lineNum];
    int index1 = 0;
    int index2 = 0; 

    for (int i = 0; i < lineNum; i++) {
        for (int j = 0; j < length[i]; j++) {
            if (textArray[i][j] == ' ') {
                index1++;
                index2 = 0;
            }
            else {
                if (textArray[i][j] == '-' ||
                    (97 <= (int)textArray[i][j] && (int)textArray[i][j] <= 122)) {
                    data[i][index1][index2++] = textArray[i][j];
                }
            }
        }
        countWord[i] = index1 + 1;
    }

    
    //count words
    int totalWord = numOfWord(countWord, lineNum);

    // De-duplication
    char word[totalWord][51];
    int index = 0;

    for (int i = 0; i < lineNum; i++) {
        for (int j = 0; j < countWord[i]; j++) {
            strcpy(word[index++], data[i][j]);      //copy contents of data to words
            for (int k = 0; k < index - 1; k++) {
                if (strcmp(data[i][j], word[k]) == 0)
                    index--;
            }
        }
    }
    totalWord = index;

    // sorting
    for (int i = 0; i < totalWord; i++) {
            char temp[51];     //string
            for (int j = 0, k = 0; j < totalWord; j++) {
                if (strcmp(word[i], word[j]) < 0) {
                    //swapping function
                    strcpy(temp, word[i]);
                    strcpy(word[i], word[j]);
                    strcpy(word[j], temp);    
                }
            }
        }

    // find words
    int wordPosition[totalWord + 1][lineNum];
    for (int w = 0; w < totalWord; w++) {
        for (int i = 0, index = 0; i < lineNum; i++) {
            for (int j = 0; j < countWord[i];) {
                if (strcmp(word[w], data[i][j++]) == 0) {
                    wordPosition[w][index++] = i + 1;
                    break;
                }
            }
        }
    } 

    // output
    cout << "Core Part:" << endl;
    for (int i = 0; i < totalWord; i++) {
        if (strlen(word[i]) > wordLength) {
            wordLength = strlen(word[i]) + 5;
        }
    } 
    for (int i = 0; i < totalWord; i++) {
        cout << setw(wordLength) << left << word[i];
        for (int j = 0; j < lineNum; j++) {
            if (wordPosition[i][j] != 0) {
                cout << setw(4) << wordPosition[i][j];
            }
        }
        cout << endl;
    }

}

void task2_output() {
    
    // read textfile.txt
    int wordLength;
    ifstream myfile;
    myfile.open("textfile.txt");
    myfile >> noskipws;

    int lineNum = line_Num();
    char textArray[lineNum][1001];
    for (int i = 0; i < lineNum; i++) {
        myfile.getline(textArray[i], 1000, '\n');
    }
    myfile.close();

    //length
    int length[lineNum];
    for (int i = 0; i < lineNum; i ++) {
        length[i] = strlen(textArray[i]);
    }

    for (int i = 0; i < lineNum; i ++) {
        *textArray[i] = *caseConverter(textArray[i], length[i]);
    }

    //split line into words
    char data[lineNum][1001][51];
    int countWord[lineNum];
    for (int i = 0; i < lineNum; i++) {
        int index1 = 0, index2 = 0;
        for (int j = 0; j < length[i]; j++) {
            if (textArray[i][j] == ' ') {
                index1 ++;
                index2 = 0;
            }
            else {
                if (textArray[i][j] == '-' || (97 <= (int)textArray[i][j] && (int)textArray[i][j] <= 122)) {
                    data[i][index1][index2++] = textArray[i][j];
                }
            }
        }
        countWord[i] = index1 + 1;
    }

    //count words
    int totalWord = numOfWord(countWord, lineNum);

    //De-duplication
    char word[totalWord][51];
    int index = 0;
    for (int i = 0; i < lineNum; i++) {
        for (int j = 0; j < countWord[i]; j++) {
            strcpy(word[index++], data[i][j]);      //copy contents of data to words
            for (int w = 0; w < index - 1; w++) {
                if (strcmp(data[i][j], word[w]) == 0)
                    index--;
            }
        }
    }
    totalWord = index;

    //sorting
    for (int i = 0; i < totalWord; i++) {
        char temp[51];
        for (int j = 0, k = 0; j < totalWord; j++) {
            if (strcmp(word[i], word[j]) < 0) {
                strcpy(temp, word[i]);
                strcpy(word[i], word[j]);
                strcpy(word[j], temp);
            }
        }
    }

    //find words
    int wordPosition[totalWord + 1][lineNum];
    for (int w = 0; w < totalWord; w++) {
        for (int i = 0, index = 0; i < lineNum; i++) {
            for (int j = 0; j < countWord[i];) {
                if (strcmp(word[w], data[i][j++]) == 0) {
                    wordPosition[w][index++] = i + 1;
                    break;
                }
            }
        }
    }     

    int ignoreLine;
    ignoreLine = ignoreLine_Num();

    ifstream file;
    file.open("ignore.txt");
    file >> noskipws;
    char ignoreWord[ignoreLine][51];
    for (int i = 0; i < ignoreLine; i++) {
        file.getline(ignoreWord[i], 51, '\n');
    }
    file.close();

    //word length
    int wordlength[ignoreLine];
    for (int i = 0; i < ignoreLine; i++) {
        wordlength[i] = strlen(ignoreWord[i]);
    }
    for (int i = 0; i < ignoreLine; i++) {
        *ignoreWord[i] = *caseConverter(ignoreWord[i], wordlength[i]);
    }


    


    

    
    int choice;
    cout << "Task 2: " << endl;
    cout << "Please select one: "<< endl;
    cout << "(1) Display concordance with the words in \"ignore.txt\" " << endl;
    cout << "(2) Display concordance without the words in \"ignore.txt\"  ";
    cout << "(3) quit" << endl;
    cin >> choice;

    char intersectionList = intersection(ignoreLine, ignoreWord, totalWord, word);

    for (int i = 0; i < ignoreLine; i++){
        for (int j = 0; j < totalWord;j++)
            if (strcmp(intersectionList[i], word[j++]) != 0) {
                char temp[i] = word[j++]
            }
        }
    }
    while (true){
        if (choice == 1) {
            
            cout << intersectionList << endl;
            continue;
        }
        else if (choice == 2){
            cout << temp[i] << endl;
            continue;

        }
        else if(choice == 3) {
            break;
        }

    }               
}


int main() {

    // Display Student ID & Task number
    cout << "Name: ZHOU Siyu" << endl;
    cout << "Student ID: 21094655D" << endl;
    cout << "Additional Part: Task "<< 21094655 % 3 << endl;

    core();
    cout << endl;
    task2_output();

    return 0;
}