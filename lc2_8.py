def l_word():
    h=0
    l=input("Enter a list : ")
    l=l.split(" ")
    for i in l:
        c=0
        for j in i:
            c=c+1
        if h<c:
            h=c
    print("Length of the longest word is : ",h)


l_word()        
