#include <iostream>
//use sort function
#include<bits/stdc++.h>

using namespace std;

struct student{//define students' structure
	int score;
	char name[50];
};
student stu[1010];
int cmp(student a,student b)
{
	if(a.score!=b.score)
	return a.score>b.score;//if different, better grades, print first
	else if(strcmp(a.name,b.name)!=0)
	return strcmp(a.name,b.name)<0;//if same, but different name, using dictonary sequence
}
int main()
{
	int n;
    cout << "Please input number of students"<< endl;
	cin >> n;//set number of students
	for(int i=0;i<n;i++)
	{
		cin>>stu[i].score>>stu[i].name;
	}
	sort(stu,stu+n,cmp);//sorting number
	cout<<"result after sorting"<<endl;
	for(int i=0;i<n;i++)
	{
		cout<<stu[i].score<<" "<<stu[i].name<<endl;
	}
	return 0;
}
