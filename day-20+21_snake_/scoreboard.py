from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.teleport(0, 270)
        self.speed("fastest")
        
        
    def increment_score(self):
        self.score += 1
        self.update()
        
    
    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", 'w') as data:
                self.highscore = self.score
                data.write(f'{self.highscore}')
        self.score = 0
        
        self.update()
        
        