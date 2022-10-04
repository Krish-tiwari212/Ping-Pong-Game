from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.a = 0
        self.x = 12
        self.y = 12

    def make_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)

    def goto_center(self):
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1




