#columnar cipher
import math
pt=input("Enter Plain Text:")
key=input("Enter Key:")
skey=sorted(key)
mat=[]
print(list(key))
ap=len(key)-(len(pt)%len(key))
for i in range(ap):
	pt+=" "
for i in range(math.ceil(len(pt)/len(key))):
	temp=[]
	for j in range(len(key)):
		
		temp.append(pt[len(key)*i+j])
	mat.append(temp)
#print(mat)
for i in mat:
	print(i)	
ct=""
cindex=0
for i in range(len(key)):
	k=key.index(skey[cindex])
	ct+="".join([row[k] for row in mat])
	cindex+=1
print(ct)
			
	
