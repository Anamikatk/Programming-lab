dict1={}

n=int(input("Enter no of items in a dictionary ; "))
for i in range(n):
    key=input("Enter keys  :  ")
    value=input("Enter values  :  ")
    dict1[key]=value
print("Dictionary 1 :  ",dict1)

dict2={}
n=int(input("Enter no. of items in a dictionary ; "))
for i in range(n):
    key=input("Enter keys  :  ")
    value=input("Enter values  :  ")
    dict2[key]=value
print("Dictionary 2 :  ",dict2)
dict1.update(dict2)
print("AFTER MERGING TWO DICTIONARY ")
print("Dictionary 1 :  ",dict1)

d3={**dict1,**dict2}
print(d3)


'''
output
-------a1 b2 a3 b4------
Enter no of items in a dictionary ; 2
Enter keys  :  a
Enter values  :  1
Enter keys  :  b
Enter values  :  2
Dictionary 1 :   {'a': '1', 'b': '2'}
Enter no. of items in a dictionary ; 2
Enter keys  :  a
Enter values  :  3
Enter keys  :  b
Enter values  :  4
Dictionary 2 :   {'a': '3', 'b': '4'}
AFTER MERGING TWO DICTIONARY 
Dictionary 1 :   {'a': '3', 'b': '4'}'''
