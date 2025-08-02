FONT = ("Courier", 24, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.update()
        
        
    def increment_score(self):
        self.clear()
        self.score += 1
        self.update()
        
    def game_is_over(self):
        self.goto(0, 160)
        self.write("GAME OVER!", align="center", font=FONT)
        
    def update(self):
        self.write(f"Level: {self.score}", align="center", font=FONT)
        
