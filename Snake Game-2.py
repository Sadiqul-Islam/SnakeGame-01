# Simple Snake Game
# By@Sadiqul Islam
# Part :-2 Snake Head

import turtle



# Create window
wn = turtle.Screen()
wn.bgcolor("Green")
wn.title("Snake Game")
wn.setup(width=800,height=600)
wn.tracer(0)


# Create Snake Head
snake_head = turtle.Turtle()
snake_head.shape("square")
snake_head.color("black")
snake_head.speed(0)
snake_head.penup()
snake_head.setposition(0,0)
snake_head.direction = "Stop"

# Create Mainloop
while True:
    wn.update()

turtle.mainloop()
