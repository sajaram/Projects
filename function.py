from turtle import *
side_length = 50

def squarecolor(color):
	pencolor(color)
	speed(2)
	pendown()
	for i in range(4):
		forward(side_length)
		right (90)
	penup()
	forward(60)
squarecolor('black')
squarecolor('red')
squarecolor('blue')

clear()
goto(0,0)
def tricolor(color):
	pencolor(color)
	speed(3)
	pendown()
	for i in range(3):
		forward(side_length)
		right (120)
	penup()
	forward(60)
tricolor('black')
tricolor('red')
tricolor('blue')

clear()
goto(0,0)

def reg_poly(sides, legnth, color, angle):
	pencolor(color)
	speed(3)
	pendown()
	for i in range (sides):
		forward(legnth)
		right(angle)
	penup()
	forward(legnth + 10)
reg_poly(4,5,'red', 90)		
reg_poly(3,50,'green', 120)
reg_poly(5,50,'blue',72)

clear()
goto(0,0)

def fun(color, sides, legnth):
	pencolor(color)
	speed(0)
	pendown()
	for i in range(sides):
		forward(legnth)
		right(72)
	forward(2)
for i in range (100):
	fun('red', 5, 50)
	fun('red', 5, 50)
	fun('yellow',5,50)
	fun('yellow',5,50)
	fun('green', 5,50)
	fun('green', 5,50)
	fun('blue',5,50)
	fun('blue',5,50)
	fun('purple',5,50)
	fun('purple',5,50)