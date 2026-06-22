# Написать функцию, которая принимает
# объект datetime и возвращает True,
# если год полученного значения високосный.


from datetime import datetime

myToday = datetime.today()
print(myToday, "\n", "Year is ")
if myToday.year % 4 == 0 and myToday.year % 100 != 0 or myToday.year % 400 == 0:
    print(" a leap year")
else:
    print(" not a leap year")


