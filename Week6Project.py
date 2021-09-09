import turtle
import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
screen.setup(width = 800, height = 800, startx = None, starty = None)
t = Turtle("turtle")
t.pensize(5)
t.speed(-1)

def drag(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(drag)

def colorRed():
    t.color('red')

def colorGreen():
    t.color('green')

def colorBlue():
    t.color('blue')

def colorPink():
    t.color('pink')

def colorTurquoise():
    t.color('turquoise')

def colorPurple():
    t.color('purple')

def colorWhite():
    t.color('white')

def colorRandom():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    t.color(color)

def clickZ():
    t.clear()

def clickRight(x, y):
    t.penup()

def clickmiddle(x,y):
    t.pendown()

def end():
    screen.bye()

  
def main():
    turtle.listen()
    t.ondrag(drag)
    turtle.onscreenclick(clickRight, 3)
    turtle.onscreenclick(clickmiddle, 2)
    turtle.onkey(colorRandom, 'n')
    turtle.onkey(clickZ, 'z')
    turtle.onkey(colorRed, 'r')
    turtle.onkey(colorPurple, 'i')
    turtle.onkey(colorBlue, 'b')
    turtle.onkey(colorGreen, 'g')
    turtle.onkey(colorPink, 'p')
    turtle.onkey(colorTurquoise, 't')
    turtle.onkey(colorWhite, 'w')
    turtle.onkey(end, 'x')


    screen.mainloop()

main()