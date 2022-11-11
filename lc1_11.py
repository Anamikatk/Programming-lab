l=input("Enter list of first name : ").split()
c=0
for i in l:
	#print(i)
	for j in i:	
		#print(j)
		if j=='a':
			c+=1
print("Occurence of a :  ",c)
