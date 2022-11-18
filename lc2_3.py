def sumlist():
    x=0
    list1=input("Enter a list").split()
    list1=list(map(int,list1))
    for i in list1:
        x=x+i
    print(x)

sumlist()
