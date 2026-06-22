list_1 = []
list_2 = []
list_3 = []

print("Enter tree numbers")
for i in range(3):  
    new_element = int(input())			# считываем очередной элемент
    list_1.append(new_element)			# добавляем его в список
print(list_1)

print("Enter tree numbers again")
for i in range(3):  
    new_element = int(input())			# считываем очередной элемент
    list_2.append(new_element)			# добавляем его в список
print(list_2)

list_3.append(list_1[1])
list_3.append(list_2[1])
print(list_3)
