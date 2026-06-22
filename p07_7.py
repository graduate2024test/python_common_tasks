# Написать класс Point, который
# в конструкторе принимает координаты
# точки и содержит методы show(), move()
# и dist(), где первый метод возвращает
# координаты точки, второй принимает
# значения, на которые нужно сместить
# координаты точки, и последний выводит
# расстояние

import math

class Point:
	x = 0
	y = 0
	
	def __init__(self, xX, yY):
		self.x = xX
		self.y = yY
	
	def show(self):
		print("point coordinates x = ", self.x, " , y = ", self.y)
		
	def move(self, aA, bB):
		self.x += aA
		self.y += bB
		print("move point coordinates x = ", self.x, " , y = ", self.y)

	def dist(self, otherPoint):
		tempX = (self.x - otherPoint.x) * (self.x - otherPoint.x)
		tempY = (self.y - otherPoint.y) * (self.y - otherPoint.y)
		temp = math.sqrt(tempX + tempY)
		print("distance from point (0,0) = ", temp)
###############################

print ("Whole numbers are used.")
xX = int(input("Enter point coordinates x = "))
yY = int(input("Enter point coordinates y = "))

aA = int(input("Enter vector coordinates a = "))
bB = int(input("Enter vector coordinates b = "))

pointZero = Point(0,0)
pointMy = Point(xX,yY)
pointMy.show()
pointMy.move(aA,bB)
pointMy.dist(pointZero)
