m=int(input("Enter the current year :  "))
n=int(input("Enetr the final year :  "))
c=[]
for i in range(m,n+1):
    if i%4==0:
        if i%100==0:
            if i%400==0:
                c.append(i)
        else:
            c.append(i)
print("The future leap years from ",m," to ",n," :  \n",c)
