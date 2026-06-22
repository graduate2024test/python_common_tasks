list_1 = []
list_2 = []
N = int(input("Enter list size: "))

print("Enter ", N, " numbers: ")
for i in range(N):  
    new_element = int(input())			# считываем очередной элемент
    list_1.append(new_element)			# добавляем его в список
print(list_1)

list_length=len(list_1)
sumOfElements=0
for i in range(list_length):
    sumOfElements=sumOfElements+list_1[i]

print("Sum of all the elements in the list is:", sumOfElements)


for num in list_1:
	if num == 13:
         continue
	else:
		new_element = num
		list_2.append(new_element)
		
		
list_length=len(list_2)
sumOfElements=0
for i in range(list_length):
    sumOfElements=sumOfElements+list_2[i]

print("Sum of all the elements in the list is:", sumOfElements)
		
