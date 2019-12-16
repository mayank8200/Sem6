r=int(input("Enter number of row:"))
c=int(input("Enter number of column:"))
#matrix a
matrixa=[]
for i in range(r):
	a=[]
	for j in range(c):
		k=int(input("Enter number:"))
		a.append(k)
	matrixa.append(a)
print(matrixa)	
#matrix b
matrixb=[]
for i in range(r):
	a=[]
	for j in range(c):
		k=int(input("Enter number:"))
		a.append(k)
	matrixb.append(a)
print(matrixb)
matrixc=[]
for i in range(r):
	a=[]
	for j in range(c):
		k=0
		a.append(k)
	matrixc.append(a)
#print(matrixc)

for i in range(r):
	for j in range(c):
		matrixc[i][j]=matrixa[i][j] + matrixb[i][j]
print(matrixc)
