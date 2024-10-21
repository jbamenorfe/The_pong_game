# This module inherits from the Turtle class of the the turtle module. It contains the Paddle class with which paddle objects are created. It also contains functions that the objects can perform

from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_position = x_pos
        self.y_position = y_pos
        self.create_paddle()
        
    def create_paddle(self):      
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.x_position, self.y_position)

    def move_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)
        
    def move_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)