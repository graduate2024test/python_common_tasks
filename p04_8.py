# Написать функцию, которая принимает
# целое число x и возвращает список из
# 20 объектов datetime с интервалами
# между днями равными x. За первоначальное
# значение datetime следует принять текущую дату.

from datetime import datetime, timedelta

myToday = datetime.today()
daysDelta = int(input("Enter interval between days: "))
print(myToday)
for i in range(0,20):
	myToday = myToday + timedelta(days=daysDelta)
	print(myToday)
