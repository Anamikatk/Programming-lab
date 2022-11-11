print("------------20th PROGRAM-------------\n")

a=input("Enter a list of numbers : ").split()
a=list(map(int, a))
b=[]
for i in a:
	if i%2!=0:
		b.append(i)
print("List containing elements other than even numbers :",b)
