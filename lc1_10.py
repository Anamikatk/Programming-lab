list1=list(map(int,input("Enter list elements :  ").split()))
for i in range(0,len(list1)):
	if(list1[i]>100):
		list1[i]="over"
print(list1)
