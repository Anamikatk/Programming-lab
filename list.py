'''
a=[1,2,3,4]
for i in a:
    print(i)
b = int (input("enter a no : "))
a.append(b)
print(a)



a=[]
n=int(input("Enter no of elts in list :  "))
for i in range (n):
    e=int(input())
    a.append(e)
print("List :  ",a)
'''



#Two list

l1=input("Enter 1st list :  ")
l1=l1.split(" ")
l1=list(map(int,l1))
l2=input("Enter 1st list :  ")
l2=l2.split(" ")
l2=list(map(int,l2))
'''
n1=int(input("Enter no of elts in list1 :  "))
print("Enter the elts : ")
for i in range (n1):
    e=int(input())
    l1.append(e)
n2=int(input("Enter no of elts in list2 :  "))
print("Enter the elts : ")
for i in range (n2):
    f=int(input())
    l2.append(f)'''
print("List 1 :  ",l1)
print("List 2 :  ",l2)


#1
m=len(l1)
n=len(l2)
if(n==m):
    print("Both list have the same length ")
else:
    print("Both list have different length ")
#2
s1=s2=0
'''
for i in l1:
    s1+=i'''
print("sum of list1 :  ",sum(l1))
'''for i in l2:
    s2+=i
    '''
print("sum of list2 :  ",sum(l2))
if (sum(l1)==sum(l2)):
    print("Sum of both list values are same")
else :
    print("Sum of both list values are different")
    

#3
p=0
for i in l1:
    if (i in l2):
        p=1
        break
if(p==1):
    print("Atleast one elt in both list are the same")
else:
    print("no same elt")
    
