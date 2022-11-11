line=input("Enter a sentence :  ").split()
word={}
for x in line:
	if x not in word.keys():
		word[x]=1
	else :
		word[x]+=1
print("OCCURENCE :\n",word)


