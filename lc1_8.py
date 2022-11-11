'''
#list comprehension
#generate positive list of numbers from a given list of integers
a=[]
n=int(input("Enter no of elts in list :  "))
print("Enter ",n," elements : ")
for i in range (n):
    e=int(input())
    a.append(e)
print("List :  ",a)
b=[x for x in a if x>0]
print("List of Positive numbers:  ",b)

#square of elements in the list
c=[x*x for x in a ]
print("List of Square of the list elements  :  ",c)
'''

#list comprehension
#generate positive list of numbers from a given list of integers
l=input("Enter list :  ")
l=l.split(" ")
l=list(map(int,l))
print("Original List :  ",l)

#generate positive list of numbers from a given list of integers
b=[x for x in l if x>0]
print("List of Positive numbers:  ",b)

#square of elements in the list
c=[x*x for x in l ]
print("List of Square of the list elements  :  ",c)

#select vowels from word
l=input("Enter the word :  ")
#l=list(map(int,l))
#print("Original List :  ",l)
v=['a','e','i','o','u']
m=[x for x in l if x in v]
print("List of vowels :  ",m)


#ordinal
l=list(input("Enter the word :  "))
h=[ord(i) for i in l ]
print("Ordinal :  ",h)
