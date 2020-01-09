m=int(input("Enter number of row:"))
n=int(input("Enter number of column:"))
a = [[int(input("Enter Element")) for x in range (n)] for y in range(m)]
print(a)
t=[[x[i] for x in a] for i in range(n)]
print(t)
