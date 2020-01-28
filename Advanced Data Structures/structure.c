/*Write a menu driven program, with the help of functions to insert student information and display student information for the following.
-	Define a structure of student information that holds a string of 20 characters called name, a string of 50 characters called address, three integers called year of birth, month of birth and day of birth and admission number.
-	Prepare the array called 2nd year Class using the above student structure for 10 students.
-	Define a structure of subject marks in the student structure which holds internal test marks, mid semester and end semester marks for 3 subjects. */


#include<stdio.h>
struct student
{
  char name[20];
  char address[50];
  int yob,mob,dob,ad;
  struct marks
  {
    int itm,mdm,etm;  
  }m;};
void print_data(struct student s)
{
    printf("Name is %s\n",s.name);
    printf("Address is %s\n",s.address);
  printf("Year of birth is %d\n",s.yob);
  printf("Month of birth is %d\n",s.mob);
  printf("Day of birth is %d\n",s.dob);
  printf("Addmission date is %d\n",s.ad);
  printf("Internal marks is %d\n",s.m.itm);
  printf("Mid marks is %d\n",s.m.mdm);
  printf("External marks is %d\n",s.m.etm);
}
void main()
{
   struct student s[10];
  int i;
  for (i=0;i<10;i++)
  {
    printf("Insert Details\n");
      printf("Enter name:\n");
      scanf("%s",&s[i].name);
      printf("Enter Address:\n");
      scanf("%s",&s[i].address);
      printf("Enter Year of birth:\n");
      scanf("%d",&s[i].yob);
      printf("Enter Month of birth:\n");
      scanf("%d",&s[i].mob);
      printf("Enter Day of birth:\n");
      scanf("%d",&s[i].dob);
      printf("Enter Addmission date:\n");
      scanf("%d",&s[i].ad);
      printf("Enter Internal marks:\n");
      scanf("%d",&s[i].m.itm);
      printf("Enter Mid marks:\n");
      scanf("%d",&s[i].m.mdm);
      printf("Enter External marks:\n");
      scanf("%d",&s[i].m.etm);
  }
  for (i=0;i<10;i++)
  {
    printf("Displaying Details\n");
    print_data(s[i]);
  }
}
