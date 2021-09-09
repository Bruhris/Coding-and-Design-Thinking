def spiralPlayer(spiral_type,sprialRGB):
	screen = Screen()
	screen.bgcolor(0,0,0)
	t1 = Turtle()
	t2 = Turtle()
	t3 = Turtle()
	t4 = Turtle()
	turtles = [t1,t2,t3,t4]
	turtle_width = 4
	for turtle in turtles:
		turtle.ht()# your own code
		turtle.pencolor(sprialRGB[0],sprialRGB[1],sprialRGB[2])
		turtle.width(turtle_width)
		turtle.speed(0)
	if spiral_type.lower() == "circle":
		for q in range(300):
			t4.circle(q, 20)
		time.sleep(5)
		t4.clear()# your own code
		del turtles[3]# your own code
	elif spiral_type.lower() == "square":
		side = 0
		for j in range(120):
			t2.forward(side)
			t2.right(270)
			side -= 4
		time.sleep(5)
		t2.clear()# your own code
		del turtles[1]# your own code
	elif spiral_type.lower() == "triangle":
		for k in range(100):
			t3.forward(k * 10)
			t3.left(120)
		time.sleep(5)
		t3.clear()# your own code
		del turtles[2]# your own code
	else:
		side = 0
		for i in range(420):
			t1.forward(side)
			t1.left(48)
			side -= 0.5
		time.sleep(5)
		t1.clear()# your own code
		del turtles[0]# your own code
def main():
	print("Welcome to Boris' Colorful Spiral Creator!")
	spirals = ["circle","square","octagon","triangle"]
	while True:
		spiralRGB = []
		spiral_type = input("What type of spiral would you like? (Circle, Square, Octagon or Triangle): ")
		while spiral_type.lower() not in spirals:
			print("That is an invalid input!")
			spiral_type = input("What type of spiral would you like? (Circle, Square, Octagon or Triangle): ")
		print("Please enter the RGB values of the color you want the spiral to be in order (Red -> Green -> Blue) or type 'random' in order to randomize the color")
		for i in range(3):
			rgbValue = input("Value:")
			while rgbValue.isdigit() == False and rgbValue.lower() != "random":
				print("That is an invalid input!")
				rgbValue = input("Value:")
			if rgbValue.lower() == "random":
				rgbValue = random.randint(0,256)
			else:
				while int(rgbValue) > 255 or int(rgbValue) < 0:
					print("That is an invalid input!")
					rgbValue = input("Value:")
			spiralRGB.append(int(rgbValue))
		spiralPlayer(spiral_type,spiralRGB)
		again = input("Do you want to run the program again? (Y or N)")
		while again.lower() != "y" and again.lower() != "n" :
			print("That is an invalid input!")
			again = input("Do you want to run the program again? (Y or N)")
		if again.lower() == "n":
			print("Thanks for running my program!")
			break
import random
import time
from turtle import *
main()
