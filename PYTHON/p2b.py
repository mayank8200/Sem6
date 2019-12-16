'''2.b: write a program to get the maximum and minimum value from a dictionary'''
a={}
n=int(input("Enter total number:"))
for i in range(0,n):
	k=input("Enter key:")
	v=input("Enter value:")
	a[k]=v
val=[]
for i in a.values():
	val.append(i)
print("maximum:",max(val))
print("minimum:",min(val))
	
