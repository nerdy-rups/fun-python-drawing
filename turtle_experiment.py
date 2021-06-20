import turtle

# Rups = turtle.Turtle() <---- can be used if we want to create an object of the class before using it
turtle.color('red')
turtle.pensize('6')
turtle.shape('arrow')

turtle.forward(100)
turtle.penup()
turtle.left(80)
turtle.pendown()
turtle.left(45)
turtle.forward(100)
turtle.right(270)
turtle.forward(500)
turtle.color('green')
turtle.left(45)
turtle.forward(40)
turtle.hideturtle()

turtle.clear()

turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()

turtle.done()