#remove html tag from input
code=input("Enter code:")
x = re.sub('<.*?>', '', code)
print(x)
