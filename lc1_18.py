print("------------18th PROGRAM-------------\n")

list1=list(input("Enter 1st list of colors : ").split(" "))
list2=list(input("Enter 2nd list of colors : ").split(" "))
c=[]
print("Colors from list1 not contained in list2 : ")
for i in list1:
	if i not in list2:
		print(i)
