'''2.a:write program to filter positive number from list '''
n=int(input("Enter total number of list:"))
a=[]
for i in range(0,n):
	i=int(input("Enter number:"))
	a.append(i)	
pos=[]
neg=[]
for i in a:
	if(i>0):
		pos.append(i)
	else:
		neg.append(i)
print("Positive:",pos)
print("Negative:",neg)

