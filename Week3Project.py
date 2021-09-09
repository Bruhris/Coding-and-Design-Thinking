from turtle import *
import time
import random
def create_pattern(turtles):
	screen = Screen()
	screen.bgcolor("white")
	shapes = 5
	sides = 4
	for amt in range(len(turtles)):
		red = random.randint(0,254)
		blue = random.randint(0,254)
		green = random.randint(0,254)
		turt = turtles[amt]
		if turt == turtles[0]:
			turt.color(red,blue,green)
			turt.shape("turtle")
			turt.penup()
			turt.goto(-200,200)
			turt.pendown()
		else:
			turt.shape("turtle")
			turt.color(red,blue,green)
			turt.penup()
			turt.goto(-200,200-amt*80)
			turt.pendown()
	for turtle in turtles:
		turtle.st()# your own code
		for shape in range(shapes):
			if shape == 0:
				turtle.forward(40)
			else:
				turtle.forward(80)
			for side in range(sides):
				red = random.randint(0,254)
				blue = random.randint(0,254)
				green = random.randint(0,254)
				turtle.begin_fill() # your own code
				turtle.color(red,blue,green)
				turtle.pendown()
				turtle.forward(40)
				turtle.left(-90)
				turtle.forward(40)
				turtle.penup()
				turtle.end_fill()   # your own code
		turtle.ht()# your own code
def main():
	print("Welcome to Boris' Square Color Pattern Creator!")
	time.sleep(3)
	t1 = Turtle()
	t2 = Turtle()
	t3 = Turtle()
	t4 = Turtle()
	t5 = Turtle()
	turtles = [t1,t2,t3,t4,t5]
	while True:
		print("Lets make you a funky square pattern!")
		create_pattern(turtles)
		again = input("Do you want to create another funky pattern? (Y or N)")
		while again.lower() != "y" and again.lower() != "n":
			print("That is an invalid option!")
			again = input("Do you want to create another funky pattern? (Y or N)")
		if again.lower() == "n":
			print("Thanks for creating patterns with this program!")
			break
		else:
			for turtle in turtles:
				turtle.clear()# your own code
main()
