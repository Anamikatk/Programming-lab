def fib():
    n=int(input("Enter a number : "))
    t1=0
    t2=1
    t=t1+t2
    print(t1)
    print(t2)
    print(t)
    for i in range(2,n-1):
        t1=t2
        t2=t
        t=t1+t2
        print(t)
fib()
