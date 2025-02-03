from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("pong")
screen.tracer(0)

score=Score()

rpaddle=Paddle((350,0))
lpaddle=Paddle((-350,0))
ball=Ball()  

screen.listen()
screen.onkeypress(rpaddle.up, "Up")
screen.onkeypress(rpaddle.down, "Down")
screen.onkeypress(lpaddle.up, "w")
screen.onkeypress(lpaddle.down, "s")


game=True
while game:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.xcor() > 320 and ball.distance(rpaddle) < 50 or ball.xcor() < -320 and ball.distance(lpaddle) < 50:
        ball.bounce_x()
        
    if ball.xcor()> 385:
        score.pnt_l_player()
        ball.game_over()

        
    if ball.xcor()< -390:
        score.pnt_r_player()
        ball.game_over()
        
screen.exitonclick()
