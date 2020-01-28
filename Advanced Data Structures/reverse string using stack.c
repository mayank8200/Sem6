
//Write a program that will reverse the string using stack


#include<stdio.h>
#include<string.h>
char stack[100];
char str[100];
int top=-1,max=100;
void push(char x)
{
	if(top >= max)
	{
		printf("The Satck is FULL");
	}
	else
	{
		top++;
		stack[top]=x;
	}
}
char pop()
{
	char y;
	if(top == -1)
	{
		printf("The Satck is EMPTY");
	}
	else
	{
		y=stack[top];
		top--;
		return y;
	}
}
void main()
{
	int i;
	char j[100];
	printf("Enter the string: ");
	scanf("%s",&str);
	for(i=0;i<strlen(str);i++)
	{
		push(str[i]);
	}
	printf("%s\n",stack);
	for(i=0;i<strlen(str);i++)
	{
		j[i]=pop();
	}
		printf("%s\n",j);
}
