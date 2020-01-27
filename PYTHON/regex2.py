#remove html tag from input
import re
code=input("Enter code:")
x = re.sub('<.*?>', '', code)
print(x)
