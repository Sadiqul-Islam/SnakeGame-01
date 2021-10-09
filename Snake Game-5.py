# Simple Snake Game
# By@Sadiqul Islam
# Part :-5 Keyborad Binding

import turtle
import time
import random

delay = 0.1


# Create window
wn = turtle.Screen()
wn.bgcolor("Green")
wn.title("Snake Game")
wn.setup(width=800,height=600)
#wn.tracer(0)


# Create Snake Head
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("black")
snake_head.speed(0)
snake_head.penup()
snake_head.direction = "Stop"

# Create Snake Food
snake_food = turtle.Turtle()
snake_food.shape("circle")
snake_food.color("orange")
snake_food.speed(0)
snake_food.penup()
snake_food.setposition(0,100)


# Create Function
def go_up():
    snake_head.direction = "Up"

def go_down():
    snake_head.direction = "Down"

def go_left():
    snake_head.direction = "Left"

def go_right():
    snake_head.direction = "Right"

    
def move():
    if snake_head.direction == "Up":
        y = snake_head.ycor()
        snake_head.sety(y+20)

    if snake_head.direction == "Down":
        y = snake_head.ycor()
        snake_head.sety(y-20)

    if snake_head.direction == "Left":
        x = snake_head.xcor()
        snake_head.setx(x-20)

    if snake_head.direction == "Right":
        x = snake_head.xcor()
        snake_head.setx(x+20)

# Keyborad Binding
wn.listen()
wn.onkeypress(go_up,"j")
wn.onkeypress(go_down,"f")
wn.onkeypress(go_left,"d")
wn.onkeypress(go_right,"k")

# Create Mainloop
while True:
    wn.update()
    move()
    time.sleep(delay)

    # Check for a collision with the food
    if snake_head.distance(snake_food)<20:
        x = random.randint(-390,390)
        y = random.randint(- 290,290)
        snake_food.setposition(x,y)
    
