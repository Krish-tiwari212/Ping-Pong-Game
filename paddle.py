from turtle import Turtle

class UsrPaddle(Turtle):
    def __init__(self):
        super().__init__()

    def make_usr_paddle(self):
        self.setheading(90)
        self.penup()
        self.goto(-600,0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=2 , stretch_len= 8)
    def up(self):
        if self.ycor() < 260:
            self.forward(17)

    def down(self):
        if self.ycor() > -260:
            self.backward(17)

class Usr2Paddle(Turtle):
    def __init__(self):
        super().__init__()

    def make_usr2_paddle(self):
        self.setheading(90)
        self.penup()
        self.goto(600, 0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=2, stretch_len=8)

    def up(self):
        if self.ycor() < 260:
                self.forward(17)

    def down(self):
        if self.ycor() > -260:
                self.backward(17)
