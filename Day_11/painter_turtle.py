from turtle import Turtle,Screen

timy = Turtle()

screen = Screen()



def move_forwards():
    timy.fd(50)
    
def move_back():
    timy.bk(50)
    
def move_right():
    timy.right(10)

def move_left():
    timy.left(10)

def clear_screen():
    timy.clear()
    timy.penup()
    timy.home()
    timy.pendown()
    
screen.listen()    
screen.onkey(fun=move_forwards,key="w")
screen.onkey(fun=move_back,key="s")
screen.onkey(fun=move_right,key="d")
screen.onkey(fun=move_left,key="a")
screen.onkey(fun=clear_screen,key="c")
screen.exitonclick()
