// GPA.c
/*
In this lab, we are required to print out grade, and grade point for the subject, 
then the GPA in PolyU System & Other System
Sample Input: GPA A B+
Sample output: 
Grade for subject 1 is A, GP 4.0
Grade for subject 2 is B+, GP 3.3
Your GPA for 2 subjects is 3.65
*/

#include <stdio.h>

int main(int argc, char *argv[]) 
{
  // argv[0] is the name of the program
  printf("This program is %s\n",argv[0]);
  printf("There are %d subjects\n",argc-1);

  polyU(argc-1, argv+1);
  otherSystem(argc-1, argv+1); 
  return 0;
}

// PolyU System
void polyU(int num_subj, char *argv[]){
  int   validSubject = 0;
  float in_gp, sum_gp = 0.0;
  int   i;
    
  printf("PolyU System:\n");
  for (i = 0; i < num_subj; i++) {
    char  in_grade = argv[i][0]; // get first character
    int   bool = 1; // boolean of correct input
    switch (in_grade) {
      case 'A': in_gp = 4.0; break;
      case 'B': in_gp = 3.0; break;
      case 'C': in_gp = 2.0; break;
      case 'D': in_gp = 1.0; break;
      case 'F': in_gp = 0.0; break;
      default: 
        printf("Wrong grade %s\n", argv[i]);
        bool--;
    }

    if (bool == 0) continue;

    printf("Grade for subject %d is %c%c, ", i+1, in_grade, argv[i][1]);
    
    if (in_grade == 'F' && (argv[i][1] == '+'|| argv[i][1] == '-')) {
      printf("invalid\n");
    } 
    else if (in_grade == 'D' && (argv[i][1] == '-')){
      printf("invalid\n");
    }
    else{
      if (argv[i][1] == '+') in_gp += 0.3;
      else if(argv[i][1] == '-'){
        in_gp -= 0.3;
      }
      sum_gp += in_gp;
      validSubject++;
      printf("GP%5.1f\n",in_gp);
    }
  }
  printf("Your GPA for %d valid subjects is%5.2f\n\n", validSubject, sum_gp/validSubject);
   
}


// Other System
void otherSystem(int num_subj, char *argv[]){
  int   validSubject = 0;
  float in_gp, sum_gp = 0.0;
  int   i;
    
  printf("Other System:\n");
  for (i = 0; i < num_subj; i++) {
    char  in_grade = argv[i][0]; // get first character
    int   bool = 1; // boolean of correct input
    switch (in_grade) {
      case 'A': in_gp = 11; break;
      case 'B': in_gp = 8; break;
      case 'C': in_gp = 5; break;
      case 'D': in_gp = 2; break;
      case 'F': in_gp = 0; break;
      default: 
        printf("Wrong grade %s\n", argv[i]);
        bool--;
    }

    if (bool == 0) continue;

    printf("Grade for subject %d is %c%c, ", i+1, in_grade, argv[i][1]);
    
    if (in_grade == 'F' && (argv[i][1] == '+'|| argv[i][1] == '-')) {
      printf("invalid\n");
    }
    else{
      if (argv[i][1] == '+') in_gp += 1;
      else if(argv[i][1] == '-'){
        in_gp -= 1;
      }
      sum_gp += in_gp;
      validSubject++;
      printf("GP%5.0f\n",in_gp);
    }
  }
  printf("Your GPA for %d valid subjects is%5.2f\n\n", validSubject, sum_gp/validSubject);
}
