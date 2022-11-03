a=[]
n=int(input("Enter no of elts in list :  "))
print("Enter the elements :  ")
for i in range (n):
    e=int(input())
    a.append(e)
print("List :  ",a)
b=[]
for i in a:
    if i>0 :
        b.append(i)
print("List of +ve numbers :  ",b)
