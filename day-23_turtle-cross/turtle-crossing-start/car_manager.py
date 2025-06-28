COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.5


from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(180)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(random.randint(330, 360), random.randint(-250, 250))
        self.shapesize(stretch_len=2, stretch_wid=1)
        
    
    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
        
    def speed_up(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        
