import random
from turtle import *
turtle = Turtle()
turtle.color("blue")
turtle.speed(0)
turtle.penup()
turtle.goto(-200,-150)
turtle.pendown()
def temple(layers, length):
	if layers <= 1:
		blue = random.randint(0,255)
		red = random.randint(0,255)
		green = random.randint(0,255)
		turtle.color(red,green,blue)
		turtle.begin_fill()# your own code
		turtle.forward(length)
		turtle.left(90)
		turtle.forward(length)
		turtle.left(90)
		turtle.forward(length)
		turtle.left(90)
		turtle.forward(length)
		turtle.right(90)
		turtle.end_fill()# your own code
	else:
		for i in range(layers):
			blue = random.randint(0,255)
			red = random.randint(0,255)
			green = random.randint(0,255)
			turtle.color(red,green,blue)
			turtle.begin_fill()# your own code
			turtle.forward(length)
			turtle.left(90)
			turtle.forward(length)
			turtle.left(90)
			turtle.forward(length)
			turtle.left(90)
			turtle.forward(length)
			turtle.left(90)
			turtle.forward(length)
			turtle.end_fill()# your own code
		turtle.penup()
		turtle.backward(length*(layers-1))
		turtle.left(90)
		turtle.forward(length)
		turtle.right(90)
		turtle.pendown()
		temple(layers-2,length)
		turtle.ht()# your own code
temple(17, 22)
