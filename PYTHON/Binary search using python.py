#implement binary seach using python
import timeit
a=[]
l=int(input("Enter size of list:"))
for i in range(l):
	e=int(input("Enter Element:"))
	a.append(e)
b=int(input("Enter Element to search:"))
a.sort()
start = timeit.default_timer()
def bin_search(a,s,e,b):
	m=(s+e)//2
	if s==e:
		return m		
	if a[m]==b:
		return m
	if a[m] > b:
		return (bin_search(a,s,m+1,b))
	else:
		return (bin_search(a,m+1,l,b))
stop = timeit.default_timer()
print(bin_search(a,0,l-1,b))
print('Time: ', stop - start)  
		
	

