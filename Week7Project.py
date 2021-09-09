import turtle
import time
import random

wn = turtle.Screen()
wn.setup(width = 600, height= 600)
wn.tracer(1)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('green')
head.penup()
head.goto(0,0)
head.direction = 'Stop'

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)
food.direction = 'Stop'

scoreTxt = turtle.Turtle()
scoreTxt.speed(0)
scoreTxt.shape('square')
scoreTxt.color('white')
scoreTxt.penup()
scoreTxt.hideturtle()
scoreTxt.goto(0, 280)
scoreTxt.write("Score: 0 | High Score: 0", align= 'center', font = ('Helvetica', 24, 'normal'))

def go_up():
    if head.direction != 'down':
        head.direction = 'up'

def go_down():
    if head.direction != 'up':
        head.direction = 'down'

def go_right():
    if head.direction != 'left':
        head.direction = 'right'

def go_left():
    if head.direction != 'right':
        head.direction = 'left'

def foodgo_up():
    if food.direction != 'down':
        food.direction = 'up'

def foodgo_down():
    if food.direction != 'up':
        food.direction = 'down'

def foodgo_right():
    if food.direction != 'left':
        food.direction = 'right'

def foodgo_left():
    if food.direction != 'right':
        food.direction = 'left'



wn.listen()
wn.onkey(go_up,'Up')
wn.onkey(go_down,'Down')
wn.onkey(go_right,'Right')
wn.onkey(go_left,'Left')
wn.onkey(foodgo_up,'w')
wn.onkey(foodgo_down,'s')
wn.onkey(foodgo_right,'d')
wn.onkey(foodgo_left,'a')

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

def foodmove():
    if food.direction == "up":
        y = food.ycor()
        food.sety(y+10)
    elif food.direction == "down":
        y = food.ycor()
        food.sety(y-10)
    elif food.direction == "right":
        x = food.xcor()
        food.setx(x+10)
    elif food.direction == "left":
        x = food.xcor()
        food.setx(x-10)

def main():
    delay = 0.1
    score = 0
    highScore = 0
    segments = []
    snakeC = ['red','green','blue','yellow']
    bgC = ['purple','pink','sandybrown','black']
    foodC = ['turquoise', 'light green', 'teal', 'grey']

    print("Welcome to Boris' Snake Game!")
    snake = input("What color do you want the snake to be? (Red, Green, Blue or Yellow) ")
    while snake.lower() not in snakeC:
        print("That is an invalid input!")
        snake = input("What color do you want the snake to be? (Red, Green, Blue or Yellow) ")
    head.color(snake.lower())
    background = input("What color do you want the background to be? (Purple, Pink, Sandybrown, Black) ")
    while background.lower() not in bgC:
        print("That is an invalid input!")
        background = input("What color do you want the background to be? (Purple, Pink, Sandybrown, Black) ")
    wn.bgcolor(background.lower())
    foodColor = input("What color do you want the background to be? (Turquoise, Light Green, Teal, Grey) ")
    while foodColor.lower() not in foodC:
        print("That is an invalid input!")
        foodColor = input("What color do you want the food to be? (Turquoise, Light Green, Teal, Grey) ")
    food.color(foodColor.lower())


    while True:
        wn.update()
        if head.xcor() < -290 or head.xcor() > 290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.direction = 'stop'
            food.goto(x,y)

            for segment in segments:
                segment.goto(1000,1000)

            segments[:] = []

            score = 0
            delay = 0.1

            scoreTxt.clear()
            scoreTxt.write('Score: {} | High Score: {}'.format(score, highScore),align= 'center', font=("Helvetica", 24, 'normal'))
        
        if food.xcor() < -290 or food.xcor() > 290 or food.ycor() > 290 or food.ycor() < -290:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.direction = 'stop'
            food.goto(x,y)
        
        if head.distance(food) < 20:

            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            redV = random.randint(0, 254)
            greenV = random.randint(0, 254)
            blueV = random.randint(0, 254)
            food.direction = 'stop'
            food.goto(x,y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color(redV, greenV, blueV)
            new_segment.penup()
            segments.append(new_segment)

            delay -= 0.002
            score += 10

            if score > highScore:
                highScore = score
            
            scoreTxt.clear()
            scoreTxt.write('Score: {} | High Score: {}'.format(score, highScore),align= 'center', font=("Helvetica", 24, 'normal'))

        
        for index in range(len(segments)-1,0,-1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x,y)

        
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)


        move()
        foodmove()
        time.sleep(delay)

main()
