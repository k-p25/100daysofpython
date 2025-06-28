from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time 

WIDTH = 800
HEIGHT = 600
TS_FACTOR = 10/11

# Setting up the main screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Setting up the paddles 
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
ts = 0.1


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    if ball.xcor() > 320: 
        if ball.distance(r_paddle) < 50:
            ball.bounce_x()
            ts *= TS_FACTOR
            
        elif ball.xcor() > 400:      
            ball.reset()
            scoreboard.l_point()
            
    if ball.xcor() < -320:
        if ball.distance(l_paddle) < 50:
            ball.bounce_x()
            ts *= TS_FACTOR
        elif ball.xcor() < -400: 
            ball.reset()
            scoreboard.r_point()
    

screen.exitonclick()