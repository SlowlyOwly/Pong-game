from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.sety(-605)
        self.color("white")
        self.ht()
        self.seth(90)
        for step in range(-600, 600, 20):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()