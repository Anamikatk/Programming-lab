s=list(input("Enter a string :  "))
for i in range(1, len(s)):
	if s[i]==s[0]:
		s[i]='$'
#print("New string :  ",s)
x=" "
for i in s:
	x+=i
print("New String :  ",x)

