# Написать функцию, которая
# принимает Json строку и
# конвертирует её в словарь.
 
import json
 
with open('p05_1.json') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(data))
 
    # Print the data of dictionary
    print("\nPeople1:", data['people1'])
    print("\nPeople2:", data['people2'])
