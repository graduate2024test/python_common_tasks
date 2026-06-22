# Написать функцию, которая
# принимает Json строку и
# конвертирует её в словарь.
 
import json
 
with open('demo_rowarrays.js') as json_file:
    data = json.load(json_file)
 
    # Print the type of data variable
    print("Type:", type(data))
 
    # Print the data of dictionary
    print(data[0])
    print(data[1])
    print(data[2])

