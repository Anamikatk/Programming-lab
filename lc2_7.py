def last():
    c="ing"
    d="ly"
    n=input("Enter a string : ")
    b=n[-3:]
    if b=="ing":
        n=n+d
    else:
        n=n+c
    print("string : ",n)

last()
        
