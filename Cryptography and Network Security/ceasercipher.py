word=input("Enter the word : ")
key=int(input("Enter the key : "))
cipher=""
for i in word:
    x=ord(i)+key
    if(x>96 and x<123):
        print(chr(x),end="")
    elif(x>122):
        print(chr(97+(x-97)%26),end="")
print()
