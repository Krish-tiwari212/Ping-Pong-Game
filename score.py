from turtle import Turtle

class Scoreboard_player1(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0

    def make_score1(self):
        self.color("blue")
        self.penup()
        self.goto(-100, 390)
        self.hideturtle()

    def increase_score(self):
        self.score1 += 1

    def count_score1(self):
        self.clear()
        self.write(f'Score : {self.score1}', font=("normal", 30, "bold"))


class Scoreboard_player2(Turtle):
    def __init__(self):
        super().__init__()
        self.score2 = 0

    def make_score1(self):
        self.color("blue")
        self.penup()
        self.goto(80, 390)
        self.hideturtle()

    def increase_score(self):
        self.score2 += 1

    def count_score1(self):
        self.clear()
        self.write(f'| {self.score2}', font=("normal", 30, "bold"))

class Border(Turtle):
    def __init__(self):
        super().__init__()

    def make_border(self):
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0,290)
        self.setheading(270)
        self.speed("fastest")
        for i in range(40):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.setheading(0)
        for i in range(50):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.goto(0, -290)
        for i in range(50):
            self.color("red")
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.goto(0 ,290)
        for i in range(50):
            self.color("red")
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.goto(0 ,290)
        self.setheading(180)
        for i in range(50):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.goto(0, -290)
        for i in range(50):
            self.color("red")
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        self.goto(0, 290)
        for i in range(50):
            self.color("red")
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)




