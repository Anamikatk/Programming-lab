'''
d={'k1':'abc'}
print(d)
print(d['k1'])
car={'company':'BMW','model':'M3','year':'1999','year':'2000'}
print(d1['year'])
car={'company':'BMW','model':'M3','year':'1999'}
car['year']=2000
print(car)

d1={'1':'a1','2':'b1'}
d2={'1':'a2','2':'b2','3':'c2'}
d3={**d1,**d2}
for k,v in d3.items():
    if k in d1 and k in d2:
        d3[k]=[v,d1[k]]
print(d3)
'''



dict1={}
n=int(input("enter no of items:"))
for i in range(n):
    key=input("enter key:")
    value=input("enter value:")
    dict1[key]=value
print("DICTIONARY 1:  ",dict1)

dict2={}
n=int(input("enter no of items:"))
for i in range(n):
    key=input("enter key:")
    value=input("enter value:")
    dict2[key]=value
print("DICTIONARY 2:  ",dict2)
d3={**dict1,**dict2}
for k,v  in d3.items():
    if k in dict1 and k in dict2:
        d3[k]=[v,dict1[k]]
print("MERGED DICTIONARY :  ",d3)

