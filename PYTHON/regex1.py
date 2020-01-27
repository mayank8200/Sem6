#password validation
import re
p=input("Enrer Password")

sp=['!','@','#','$','%','^','&','*']
c=[]
if (re.search(r'[A-Z]+',p)):
c.append(1)
if (re.search(r'[a-z]+',p)):
c.append(1)
if (re.search(r'[0-9]+',p)):
c.append(1)
for i in p:
    if i in sp:
        a=1

if len(p)>6 and len(p)<12 and len(c)==3 and a==1:
    print("Valid")
else:
    print("Not Valid")
