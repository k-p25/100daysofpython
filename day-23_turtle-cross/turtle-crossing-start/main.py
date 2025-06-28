import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Road")

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


cars = []
game_is_on = True

while game_is_on:
    
    rand_int = random.randint(0, 10)
    
    if rand_int % 7 == 0:
        new_car = CarManager()
        cars.append(new_car)
    
    for car in cars:
        car.move()
        if car.distance(player) < 20:
            game_is_on = False
    

    
    if player.ycor() > 290:
        player.reset()
        scoreboard.increment_score()
        for car in cars:
            car.speed_up()
            
    time.sleep(0.1)
    screen.update()
        
scoreboard.game_is_over()
  

screen.exitonclick()