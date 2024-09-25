import turtle 
 
tess=turtle.Turtle()  

def buttonclick(x,y): 
    print("You clicked at this coordinate({0},{1})".format(x,y))

turtle.onscreenclick(buttonclick,1) 
turtle.listen()
turtle.speed(10)
turtle.done()