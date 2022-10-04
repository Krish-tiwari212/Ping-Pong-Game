from turtle import Turtle, Screen
from paddle import  UsrPaddle, Usr2Paddle
from ball import Ball
from score import Scoreboard_player1, Scoreboard_player2, Border
import time
import random
screen = Screen()
screen.setup(height=900, width=1280)
screen.bgcolor("black")
screen.tracer(0)
paddle = UsrPaddle()
paddle1 = Usr2Paddle()
paddle.make_usr_paddle()
paddle1.make_usr2_paddle()
ball=Ball()
score1 = Scoreboard_player1()
score1.make_score1()
border = Border()
score2 = Scoreboard_player2()
score2.make_score1()
screen.listen()
screen.onkeypress(paddle.up,"w")
screen.onkeypress(paddle.down,"s")
screen.onkeypress(paddle1.up,"Up")
screen.onkeypress(paddle1.down,"Down")
game_is_on = True
ball.make_ball()
border.make_border()
while game_is_on:
    time.sleep(0.015)
    screen.update()
    score1.count_score1()
    score2.count_score1()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle) < 66 and ball.xcor() < -580 or ball.distance(paddle1) <66 and ball.xcor() > 580:
        ball.bounce_x()
    if ball.xcor() < -600:
        ball.speed("fastest")
        ball.goto_center()
        ball.speed("normal")
        score2.increase_score()
    elif ball.xcor() > 600:
        ball.speed("fastest")
        ball.goto_center()
        ball.speed("normal")
        score1.increase_score()
    else:
        ball.move()
screen.exitonclick()