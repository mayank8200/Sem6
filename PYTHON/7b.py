'''Find out the list of subjects of a particular semester from the
input provided as a list of dictionaries using lambda map and
filter together.
i/p:-
[{'sem':6,'sub':'python'},
{'sem':6,'sub':'cns'},
{'sem':5,'sub':'java'},
{'sem':5,'sub':'daa'}]
o/p:- sem 6 subjects:['python','cns']'''

d=[]
n=int(input("Enter total num entries:"))
for i in range(n):
	temp={}
	temp['sem']=int(input("Enter sem:"))
	temp['sub']=input("Enter sub:")
	d.append(temp)

s=int(input("Enter sem to see subject:"))
ans=list(map(lambda x:x['sub'],list(filter(lambda x:x['sem']==s,d))))
print("sem {} subjects:{}".format(s,ans))
