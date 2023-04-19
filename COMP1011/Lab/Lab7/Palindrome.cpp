#include <iostream>
#include <iomanip>
#include <cstring>

using namespace std;

int main()
{
	char input[101];
	// strcpy(input, "stack_cats");
	while (strcmp(input, "0") != 0)
	{
		cout << "Enter a string: ";
		cin >> input;
		//i < len / 2 && 
		if (strcmp(input, "0") != 0)
		{
			bool flag = true;
			int len = strlen(input);
			for (int i = 0, j = len - 1; i <= j; i++, j--)
			{
				if (input[i] == '_')
				{
					i++;
				}
				if (input[j] == '_')
				{
					j--;
				}
				if (i <= j && input[i] != input[j])
				{
					flag = false;
					break;
				}
			}
			if (flag)
			{
				cout << "true" << endl;
			}
			else
			{
				cout << "false" << endl;
			}
		}
	}

	cout << "Bye!" << endl;
	return 0;
}
