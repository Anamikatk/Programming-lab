s=list(input("Enter a string :  "))
s[0],s[len(s)-1]=s[len(s)-1],s[0]
x=" "
for i in s:
	x+=i
print("New String :  ",x)
