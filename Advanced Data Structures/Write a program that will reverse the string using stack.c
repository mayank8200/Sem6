#include<stdio.h>
#include<string.h>
char a[20],st[20];
char c;
int top=-1,max=20;
void push(char a)
{
	if(top>=max)
	{
		printf("Overflow");
	}
	else
	{
		top++;
		st[top]=a;
		//printf("%c Successfully Inserted\n",a);
	}
}
char pop(char a[])
{
	if(top==-1)
	{
		printf("Underflow\n");
	}
	else
	{
		
		c=a[top];
		top--;
	}
	return c;
}
void main()
{
	printf("Enter String:");
	scanf("%s",a);
	for(int i=0;i<strlen(a);i++)
	{
		push(a[i]);
	}
	
	//printf("%s\n",st);
	for(int i=0;i<strlen(a);i++)
	{
		char d=pop(st);
		printf("%c",d);
	}	
	
	
}
	
