print("------------21th PROGRAM-------------\n")

n1=int(input("Enter 1st number : "))
n2=int(input("Enter 2nd number : "))
a=[]
b=[]
c=[]
for i in range(1,n1+1):
	if(n1%i==0):
		a.append(i)
for i in range(1,n2+1):
	if(n2%i==0):
		b.append(i)
for i in a:
	if i in b:
		c.append(i)
for i in range(0,len(c)-1):
	if c[i+1]>c[i]:
		gcd=c[i+1]
print("GCD : ",gcd)

