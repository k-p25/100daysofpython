from turtle import Turtle
import time

class Ball(Turtle): 
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.x_move = 10 
        self.y_move = 10
        self.move_speed = 0.1
        
    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        
        
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        
    def reset(self):
        self.goto(0, 0)
        time.sleep(0.5)
        self.move_speed = 0.1
        self.bounce_x()
    