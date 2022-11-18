'''
def nochar():
    count=0
    n=input("Enter a string : ")
    for i in n:
        count=0
        for j in n:
            if i==j:
                count+=1
        print(i ," = ",count)
nochar()
'''


def nochar():
    d={}
    n=input("Enter a string : ")
    for i in n:
        count=0
        for j in n:
            if i==j:
                count+=1
        d[i]=count
    print(d)
nochar()
