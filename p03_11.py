myList = []

lLength = int(input("Enter list size: "))
for i in range(0,lLength):  
    myList.append(i)
    
print(myList)

a = int(input("Enter A: "))
b = int(input("Enter B: "))

if a < b & b < lLength:
	for i in range(a, b):
		print(myList[i])
else:
	print("out of range")
