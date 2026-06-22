myList = ["alpha", "beta", "gama", "delta"]
myNewList = []

print(myList)

for word in myList:
	#print(word)
	#print(list(word))
	myNewList.append(list(word))
	
print(myNewList)
