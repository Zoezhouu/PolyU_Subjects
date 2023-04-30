# Lab 3 Exercise Transcript
### Requirement:
Write a bash shell script called transcript to search through a list of subject files and generate the transcript for one or more given students in the argument list. 
The first part of the argument list indicates the subject files to be used. This is followed by a special marker "student". Then a list of student ID follows. The program can be run like: 
	transcript COMP101121S2.dat COMP241122S1.dat student 1234
---
### Sample Files
Filename 1: student.dat
Content 1: 
1223 bob
1224 kevin
1225 stuart
1226 otto
1234 john
1235 mary
1236 peter
1237 david
1238 alice
Filename 2: COMP101121S2.dat
Content 2:
Subject COMP1011 2021 2
1223 F
1234 B
1235 B+
1236 A
Filename 3: COMP101122S1.dat
Content 3:
Subject COMP1011 2022 1
1223 B
1224 B+
1225 B-
1238 C+
Filename 4: COMP241122S1.dat
Content 4: 
Subject COMP2411 2022 1
1223 C+
1234 B-
1235 B
1236 A
Filename 5: COMP243222S2.dat
Content 5: 
Subject COMP2432 2022 2
1223
1235
1236
1237
---
### Sample Input & Sample Output
Sample Input 1: transcript COMP101121S2.dat COMP241122S1.dat student 1234
Sample Output 1: 
Transcript for 1234 john
COMP1011 2021 Sem 2 B
COMP2411 2022 Sem 1 B-
GPA for 2 subjects 2.85

Sample Input 2: transcript COMP* student 1236 1234 1223
Sample Output 2: 
Transcript for 1236 peter
COMP1011 2021 Sem 2 A
COMP2411 2022 Sem 1 A
COMP2432 2022 Sem 2
GPA for 2 subjects 4.00

Transcript for 1234 john
COMP1011 2021 Sem 2 B
COMP2411 2022 Sem 1 B-
GPA for 2 subjects 2.85

Transcript for 1223 bob
COMP1011 2021 Sem 2 F
COMP1011 2022 Sem 1 B
COMP2411 2022 Sem 1 C+
COMP2432 2022 Sem 2
GPA for 2 subjects 2.65