#Volume of Cuboid
def vol_cuboid():
    print("\n\t------VOLUME OF CUBOID------\n")
    l=int(input("Enter the length of the rectangle : "))
    b=int(input("Enter the breadth of the rectangle : "))
    h=int(input("Enter the height of the rectangle : "))
    vol=l*b*h
    print("Volume of the Cuboid : ",vol)

#Perimeter of cuboid
def peri_cuboid():
    print("\n\t------PERIMETER OF CUBOID------\n")
    l=int(input("Enter the length of the rectangle : "))
    b=int(input("Enter the breadth of the rectangle : "))
    h=int(input("Enter the height of the rectangle : "))
    peri=4*(l+b+h)
    print("Perimeter of the Cuboid : ",peri)
