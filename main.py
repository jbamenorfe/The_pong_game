# TODO 1: Import necessary modules and classes
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# TODO 2: create a screen object and Setup the screen

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

# TODO 3: Create a paddle
r_paddle = Paddle(380,0)
l_paddle = Paddle(-380, 0)

ball = Ball(0, 0)
scoreboard = Scoreboard()

# Listen to key events
screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

# Detect collision withtop and bottom walls

game_is_on = True
while game_is_on:       # You need a while loop to update the screen
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -275:
        ball.bounce_y()
        
    # Detect collision with r_padel
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()
        ball.increase_speed()
    
    # Detect when the right paddle misses the ball
    if ball.xcor() > 390:
        scoreboard.increase_l_point()
        

    
    # Detect when the left paddle misses the ball
    if ball.xcor() < -390:
        scoreboard.increase_r_point()
        ball.reset_position()


screen.exitonclick()