import turtle

count1 = 6
count2 = 6
turtle.penup()
turtle.goto(-200,200)
while (count1 > 0):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.backward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    count1 = count1 - 1

turtle.penup()
turtle.goto(-200,200)
while(count2 > 0):
    turtle.pendown()
    turtle.right(90)
    turtle.forward(500)
    turtle.penup()
    turtle.backward(500)
    turtle.left(90)
    turtle.forward(100)
    count2 = count2 - 1

turtle.exitonclick()
