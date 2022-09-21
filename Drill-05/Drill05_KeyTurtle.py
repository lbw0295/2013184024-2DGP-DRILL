import turtle

turtle.shape('turtle')

def Dmove():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
    
def Wmove():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def Amove():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def Smove():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def Restart():
    turtle.reset()
    

turtle.onkey(Dmove,'d')
turtle.onkey(Wmove,'w')
turtle.onkey(Amove,'a')
turtle.onkey(Smove,'s')
turtle.onkey(Restart,'Escape')
turtle.listen()
