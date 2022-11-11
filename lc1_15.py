print("------------15th PROGRAM-------------\n")
file=list(input("Enter a file name : "))
x=" "
for i in range(0,len(file)):
	if file[i]=='.':
		break
for j in range(i+1,len(file)):
	x+=file[j]

		
print("The file extension is ",x)
