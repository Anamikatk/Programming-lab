

d={}
n=int(input("Enter the no. of items :  "))
for i in range(n):
    key=input("Enter key : ")
    value=input("Enter value : ")
    d[key]=value
d3=sorted(d.items())
print("SORTED DICTIONARY IN ASCENDING ORDER :  ",d3)
d3=sorted(d.items(),reverse=True)
print("SORTED DICTIONARY IN DECENDING ORDER :  ",d3)









'''
--------OUTPUT----------
Enter the no. of items :  3
Enter key : g
Enter value : 4
Enter key : u
Enter value : 3
Enter key : b
Enter value : 2
SORTED DICTIONARY IN ASCENDING ORDER :   [('b', '2'), ('g', '4'), ('u', '3')]
SORTED DICTIONARY IN DECENDING ORDER :   [('u', '3'), ('g', '4'), ('b', '2')]
----------------------------
'''
