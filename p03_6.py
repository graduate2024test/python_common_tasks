myDictionary = { "AA":1 , "BB":2, "CC":3 }
myList = []

myList =[myDictionary[key] for key in myDictionary]

print(myList)
