from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

#Set up screen 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    scoreboard.update()
    time.sleep(0.1)

    snake.move()
    
    if snake.head.distance(food) <  15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
         
        
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10: 
            scoreboard.reset()
    
    


screen.exitonclick()