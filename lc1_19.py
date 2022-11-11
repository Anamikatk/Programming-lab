print("------------19th PROGRAM-------------\n")

str1=list(input("Enter 1st string : "))
str2=list(input("Enter 2nd string : "))
str1[0],str2[0]=str2[0],str1[0]
x=" "
for i in str1:
	x+=i
x+=" "
for j in str2:
	x+=j
	
print("Strings after swapping the 1st characters : ",x)
