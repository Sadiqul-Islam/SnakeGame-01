# Simple Snake Game
# By@Sadiqul Islam
# Part :-4 Time module


import turtle
import time

delay = 0.1


# Create Window
wn = turtle.Screen()
wn.bgcolor("Green")
wn.title("Snake Game")
wn.setup(width=800,height=600)

# Create Snake Head
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("black")
snake_head.speed(0)
snake_head.penup()
snake_head.setposition(0,0)
snake_head.direction = "Stop"

# Create Move Function
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

    

# Create Mainloop
while True:
    
    wn.update()
    move()
    time.sleep(delay)
    
