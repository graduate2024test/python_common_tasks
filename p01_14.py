myDictionary = {"AA" : "True"}

dLength = int(input("Enter dictionary size: "))
for element in range(0,dLength):
    myDictionary[input("Enter string name ")] = input("Enter bool status ")

print(myDictionary)

myList = []

lLength = int(input("Enter list size: "))
for i in range(0,lLength):  
    new_element = myDictionary
    myList.append(new_element)

print(myList)

lResult = []

for i in range(0,lLength): 
	tempDictionary = myList[i]
	for key in tempDictionary:
		print(key, '->', tempDictionary[key])
	
myNewList = []	
for i in range(0,lLength): 
	tempDictionary = myList[i]
	for key in tempDictionary:
		tempStatus = tempDictionary[key]
		print(tempStatus)
		if  tempDictionary[key] == "True":
			myNewList.append(key)
			
print(myNewList)
