#brut force attack
#cipher="Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly"
cipher=input("Enter the ciphered string: ")
for i in range(1,26):
	for j in cipher:
		if(j.islower()):
			if(j==" " or j==","):
		 		print(j,end="")
			elif((ord(j)+i)>122):
				print(chr(97+(((ord(j)+i)-97)%26)),end="")
			else:
				print(chr(ord(j)+i),end="")
		else:
			if(j==" " or j==","):
		 		print(j,end="")
			elif((ord(j)+i)>91):
				print(chr(65+(((ord(j)+i)-65)%26)),end="")
			else:
				print(chr(ord(j)+i),end="")
	print(" Key:",26-i)
