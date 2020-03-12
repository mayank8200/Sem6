P=int(input("Enter Prime number P:"))


mat=[]
for i in range(1,P):
	temp=[]
	for j in range(1,P):
		temp.append(i**j%P)
	mat.append(temp)
#print(mat)
op=[]
c=1
for i in mat:
	k=list(set(i))
	if(len(k)==P-1):
		op.append(c)
	c+=1
print("Primitive root of P is :",op)

G=int(input("Enter G(Primitive root of P):"))
a=int(input("Enter Alice Private Key a:"))
b=int(input("Enter Bob Private Key b:"))
X=(G**a)%P
Y=(G**b)%P
print("Alice Recieved: {}".format((G**b)%P))
print("Bob Recieved: {}".format((G**a)%P))
ka=(Y**a)%P
kb=(X**b)%P
print("Alice Secret key: {}".format((Y**a)%P))
print("Bob Secret key: {}".format((X**b)%P))
'''
if ka==kb:
	print("Secure Connection Establish")
else:
	print("Secure Connection is not Establish")
'''
