def facto():
    a=int(input("Enter a no. : "))
    p=1
    for i in range(1,a+1):
        p=p*i
    print("factorial of ",a," : ",p)

facto()
