import time
from turtle import *
screen = Screen()
screen.bgcolor("white")
turtle = Turtle()
turtle.shape("turtle")
turtle.pencolor(0,0,0)
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
def make_Face():
	#Create face# your own code
	turtle.begin_fill()# your own code
	turtle.circle(100)
	turtle.color(255,255,0)
	turtle.end_fill()# your own code
def make_Nose(noseType):
	if noseType == "yes":
		turtle.penup()
		turtle.goto(0,0)
		turtle.begin_fill()# your own code
		turtle.circle(7)
		turtle.color(0,0,0)
		turtle.end_fill()# your own code
def make_Mouth(mouthType):
	if mouthType.lower() == "sad":
		turtle.color("black")
		turtle.penup()
		turtle.goto(-40,-60)
		turtle.pendown()
		turtle.right(90)
		turtle.circle(40, -180)
		turtle.left(90)
	elif mouthType.lower() == "happy":
		turtle.color("black")
		turtle.penup()
		turtle.goto(-40,-40)
		turtle.pendown()
		turtle.right(90)
		turtle.circle(40, 180)
		turtle.left(90)
def make_Eye(eyeType):
	if eyeType == "big":
		turtle.color(0,0,0)
		turtle.penup()
		turtle.goto(-50,15)
		turtle.pendown()
		turtle.begin_fill()# your own code
		turtle.circle(25)
		turtle.color("white")
		turtle.end_fill()# your own code
		turtle.penup()
		turtle.goto(-50,30)
		turtle.pendown()
		turtle.begin_fill()# your own code
		turtle.circle(10)
		turtle.color("black")
		turtle.end_fill()# your own code
		turtle.color("black")
		turtle.penup()
		turtle.goto(50,15)
		turtle.pendown()
		turtle.begin_fill()# your own code
		turtle.circle(25)
		turtle.color("white")
		turtle.end_fill()# your own code
		turtle.penup()
		turtle.goto(50,30)
		turtle.pendown()
		turtle.begin_fill()# your own code
		turtle.circle(10)
		turtle.color("black")
		turtle.end_fill()# your own code
	elif eyeType == "small":
		turtle.color(0,0,0)
		turtle.penup()
		turtle.goto(-50,30)
		turtle.pendown()
		turtle.begin_fill()# your own code
		turtle.circle(7)
		turtle.color("white")
		turtle.end_fill()# your own code
		turtle.penup()
		turtle.goto(-50,33)
		turtle.pendown()
		turtle.begin_fill()# your own code
		turtle.circle(3)
		turtle.color("black")
		turtle.end_fill()# your own code
		turtle.color("black")
		turtle.penup()
		turtle.goto(50,30)
		turtle.pendown()
		turtle.begin_fill()# your own code
		turtle.circle(7)
		turtle.color("white")
		turtle.end_fill()# your own code
		turtle.penup()
		turtle.goto(50,33)
		turtle.pendown()
		turtle.begin_fill()# your own code
		turtle.circle(3)
		turtle.color("black")
		turtle.end_fill()# your own code
def make_Antenna(antennaType):
	if antennaType.lower() == "antenna":
		turtle.penup()
		turtle.goto(-50,85)
		turtle.color("black")
		turtle.pendown()
		turtle.right(-90)
		turtle.forward(90)
		turtle.begin_fill()# your own code
		turtle.circle(15)
		turtle.color("blue")
		turtle.end_fill()# your own code
		turtle.color("black")
		turtle.penup()
		turtle.goto(50,85)
		turtle.pendown()
		turtle.forward(90)
		turtle.left(180)
		turtle.begin_fill()# your own code
		turtle.circle(15)
		turtle.color("blue")
		turtle.end_fill()# your own code
		turtle.left(90)
	elif antennaType == "horn":
		turtle.penup()
		turtle.goto(-60,80)
		turtle.pendown()
		turtle.color("grey")
		turtle.begin_fill()# your own code
		turtle.left(60)
		turtle.forward(120)
		turtle.left(-120)
		turtle.forward(120)
		turtle.left(60)
		turtle.goto(-60,80)
		turtle.end_fill()# your own code
while True:
	print("Let's create your own emoji face!")
	make_Face()
	time.sleep(2)
	antennaType = input("Do you want a horn or antenna? : ")
	while antennaType.lower() != "horn" and antennaType.lower() != "antenna":
		print("Invalid input!")
		antennaType = input("Do you want a horn or antenna? : ")
	make_Antenna(antennaType.lower())
	eyeType = input("What type of eyes do you want? (Big or small): ")
	while eyeType.lower() != "big" and eyeType.lower() != "small" :
		print("Invalid input!")
		eyeType = input("What type of eyes do you want? (Big or small): ")
	make_Eye(eyeType.lower())
	noseType = input("Do you want a nose? (Yes or no): ")
	while noseType.lower() != "no" and noseType.lower() != "yes" :
		print("Invalid input!")
		noseType = input("Do you want a nose? (Yes or no): ")
	make_Nose(noseType.lower())
	mouthType = input("What type of expression do you want? (Happy or sad): ")
	while mouthType.lower() != "happy" and mouthType.lower() != "sad":
		print("Invalid input!")
		mouthType = input("What type of expression do you want? (Happy or sad): ")
	make_Mouth(mouthType.lower())
	print("That is a nice looking emoji!")
	again = input("Do you want to create another emoji?")
	while again.lower() != "y" and again.lower() != "n":
		print("Invalid input!")
		again = input("Do you want to create another emoji? (Y or N)")
	if again.lower() == "n":
		print("Thanks for using my program!")
		break
	else:
		turtle.reset()# your own code
		turtle.shape("turtle")
		turtle.pencolor(0,0,0)
		turtle.penup()
		turtle.goto(0,-100)
		turtle.pendown()
