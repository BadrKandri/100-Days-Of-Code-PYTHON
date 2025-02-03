from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position) :
        super().__init__()
        self.shape("square")
        self.shapesize(1,5)
        self.color("white")
        self.penup()
        self.left(90)
        self.goto(position)


    def up(self):
        self.fd(20)
        
    def down(self):
        self.bk(20)


