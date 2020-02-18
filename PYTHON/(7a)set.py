#Find the list of uncommon elements from 2 lists using set.

a=set([int(x) for x in input("Enter list 1 value(space seprated):").split()])
b=set([int(x) for x in input("Enter list 2 value(space seprated):").split()])
print((a.difference(b)).union(b.difference(a)))
#print((a|b)-(a&b))
