#include <iostream>
#include <cstring>

using namespace std;

void find(char[], char[]);
int main()
{
	char data[50];
	char text[] = "xyz";
    cin >> data;
	find(data,text);
	return 0;
}

void find(char data[], char text[])
{
    //length
    int datal = strlen(data);
	int textl = strlen(text);
    //compare text and str
    for (int i = 0; i <= datal - textl; i++)
    {
        char str[textl + 1];
        // copy string
        for (int j = i, k = 0; j < textl + i; j++, k++)
        {
            str[k] = data[j];
        }
        bool e = 1;//same = true
        //compare str and text
        for (int i = 0; i < textl; i++)
        {
            //one character is different
            if (!(str[i] == text[i]))
            {
                e = 0;//same = false
            }
        }
        if(e)
        {
            cout << i+1;
            return;
        }
    }
    cout << "Not Found"<<endl;
	return;
}

