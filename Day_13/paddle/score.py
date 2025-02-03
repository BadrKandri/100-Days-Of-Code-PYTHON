from turtle import Turtle

class Score(Turtle):
    def __init__(self) :
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-60,190)     
        self.write(self.l_score,align="center",font=("courier",70,"normal"))
        self.goto(0,219.3)     
        self.write(":",align="center",font=("courier",40,"normal"))
        self.goto(60,190)
        self.write(self.r_score,align="center",font=("courier",70,"normal"))
    
    def pnt_l_player(self):
        self.l_score +=1
        self.update_score()
    def pnt_r_player(self):
        self.r_score +=1
        self.update_score()
        