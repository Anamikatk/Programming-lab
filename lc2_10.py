def fact():
    a=[]
    n=int(input("Enter a number : "))
    print("All the factors of ",n," : ")
    for i in range(1,n):
        if n%i==0:
            print(i,end=" ")

fact()
