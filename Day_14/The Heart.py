from turtle import Turtle,Screen

myscreen= Screen()
myscreen.title("THE HEART")
pen = Turtle() 
pen.shape("turtle")

# Method to draw curve 
def curve(): 
	for _ in range(200): 
		pen.right(1) 
		pen.forward(1) 

# Method to draw a full heart 
def heart():
	pen.fillcolor('red')  
	pen.begin_fill() 
	pen.left(140)
	pen.speed("slow")
	pen.forward(113) 
	curve()	
	pen.left(120) 
	pen.speed('slow')
	curve() 
	pen.forward(112) 
	pen.end_fill() 

# Method to write text 
def txt(): 
	pen.speed('slow')
	pen.up() 
	pen.setpos(-68, 95) 
	pen.down() 
	pen.color('black') 
	pen.write("BADR", font=( "Black", 40, "bold"))

heart()
txt() 
# hide turtle 
pen.ht() 
myscreen.exitonclick()
#the end
