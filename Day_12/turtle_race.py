from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(1300,600)
finish_line=(350.0,-150.0)
#END timy2
line=Turtle()
line.pensize(5)
line.penup()
line.hideturtle()
line.goto(350.0,-150.0)
line.pendown()
line.left(90)
line.fd(250)

debut= True
while debut:
    #TURTLE 1 :
    timy1=Turtle()
    timy1.hideturtle()
    timy1.color("green4")
    timy1.penup()
    timy1.goto(-350.0,50.0)
    timy1.showturtle()
    timy1.shape("turtle")

    #TURTLE 2:
    timy2=Turtle()
    timy2.hideturtle()
    timy2.color("red")
    timy2.penup()
    timy2.goto(-350.0,0.0)
    timy2.showturtle()
    timy2.shape("turtle")

    #TURTLE 3:
    timy3=Turtle()
    timy3.hideturtle()
    timy3.color("blue")
    timy3.penup()
    timy3.goto(-350.0,-50.0)
    timy3.showturtle()
    timy3.shape("turtle")

    #TURTLE 4:
    timy4=Turtle()
    timy4.hideturtle()
    timy4.color("gray0")
    timy4.penup()
    timy4.goto(-350.0,-100.0)
    timy4.showturtle()
    timy4.shape("turtle")
    
    debut= False

def van(winner):
    if winner == "green":
        timy2.hideturtle()
        timy3.hideturtle()
        timy4.hideturtle()
    elif winner == "red":
        timy1.hideturtle()
        timy3.hideturtle()
        timy4.hideturtle() 
    elif winner == "blue":
        timy1.hideturtle()
        timy2.hideturtle()
        timy4.hideturtle() 
    elif winner == "black":
        timy1.hideturtle()
        timy2.hideturtle()
        timy3.hideturtle()   
      
restart= True
while restart:
    guess=[]
    while 'green' not in guess and 'red' not in guess and 'blue' not in guess and 'black' not in guess:

        guess.append(screen.textinput("YOUR GUESS", "\n            GREEN:\n            RED:\n            BLUE:\n            BLACK:\n"))
        
    is_end=True
    while is_end:
        timy1.fd(random.randint(10,50))
        if timy1.pos() >= finish_line:
            is_end=False
            winner=("green")
            van(winner)            
             
        timy2.fd(random.randint(10,50))
        if timy2.pos() >= finish_line:
            is_end=False
            winner=("red")
            van(winner)
            
        timy3.fd(random.randint(10,50))
        if timy3.pos() >= finish_line:
            winner=("blue")
            is_end=False
            van(winner)
            
        timy4.fd(random.randint(10,50))
        if timy4.pos() >= finish_line:
            is_end=False
            winner=("black")
            van(winner)
    again=[]        
    if guess[0] == winner:
        again.append(screen.textinput(f"YOU GOT IT RIGHT !!! ","do you wanna play again... (y/n)" ))
    else:
        result=print()
        again.append(screen.textinput(f"GAME OVER >>> {winner} ","do you wanna play again... (y/n)" ))
           
    
    if again[0]== 'y':
        timy1.showturtle()
        timy1.goto(-350.0,50.0)
        timy2.showturtle()
        timy2.goto(-350.0,0.0)
        timy3.showturtle()
        timy3.goto(-350.0,-50.0)
        timy4.showturtle()
        timy4.goto(-350.0,-100.0)
        debut= True
        restart=True
    else:
        restart=False
