# This module inherits the Turtle class of the turtle module. It provides the code for creating a ball object

from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_position = x_pos
        self.y_position = y_pos
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.create_ball()


    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(self.x_position, self.y_position)
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_speed = 0.1
    
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    