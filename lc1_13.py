print("------------13th PROGRAM-------------\n")
a=list(input("Enter the string : "))
a[0],a[len(a)-1]=a[len(a)-1],a[0]
x=""
for i in a:
    x+=i
print("New String : ",x)
