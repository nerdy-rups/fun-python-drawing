import time
import turtle

def hut():
    import turtle
    from turtle import Screen, end_fill
    turtle.pensize('6')
    turtle.width(2)
    turtle.shape('arrow')
    drawing_area = turtle.Screen()
    drawing_area.title("Your hut")
    drawing_area.setup(width=1500, height=850, startx=0, starty=0)

    #the base roof 
    turtle.color("#cca300") #mud colour
    turtle.begin_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(220)
    turtle.down()
    turtle.right(90)
    turtle.forward(500)
    turtle.left(135)
    turtle.forward(250)
    turtle.left(45)
    turtle.forward(500)
    turtle.left(135)
    turtle.forward(250)
    turtle.end_fill()

    #Lines on the roof
    turtle.hideturtle()
    turtle.color("#332900")  #blackish brown
    turtle.speed(10)

    turtle.penup()
    turtle.left(180)
    turtle.fd(50)
    turtle.pendown()
    turtle.right(135)
    turtle.fd(500)
    
    turtle.penup()
    turtle.left(135)
    turtle.fd(50)
    turtle.pendown()
    turtle.left(45)
    turtle.fd(500)

    turtle.penup()
    turtle.right(45)
    turtle.fd(50)
    turtle.pendown()
    turtle.right(135)
    turtle.fd(500)
    
    turtle.penup()
    turtle.left(135)
    turtle.fd(50)
    turtle.pendown()
    turtle.left(45)
    turtle.fd(500)

    turtle.penup()
    turtle.right(45)
    turtle.fd(50)
    turtle.pendown()

    #the side roof
    turtle.color("#cca300")

    turtle.speed(3)
    turtle.left(90)
    turtle.showturtle()
    turtle.begin_fill()
    turtle.forward(250)
    turtle.left(135)
    turtle.forward(40)
    turtle.left(45)
    turtle.forward(220)
    turtle.end_fill()

    #body below main roof
    turtle.right(90)
    turtle.penup()
    turtle.forward(220)
    turtle.right(45)
    turtle.pendown()
    turtle.color("#80bfff") #sky blue colour
    turtle.begin_fill()
    turtle.forward(380)
    turtle.left(90)
    turtle.forward(470)
    turtle.left(90)
    turtle.forward(380)
    turtle.end_fill()

    #rest of the body
    turtle.hideturtle()
    turtle.left(90)
    turtle.penup()
    turtle.forward(781.13)
    turtle.pendown()
    turtle.showturtle()
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(380)
    turtle.left(90)
    turtle.forward(311.13)

    turtle.left(90)
    turtle.color("#003366") #blackish blue
    turtle.forward(380)
    
    turtle.color("#80bfff")

    turtle.left(45)
    turtle.forward(220)    
    turtle.end_fill()

    #door
    turtle.speed(10)
    turtle.left(135)
    turtle.hideturtle()
    turtle.penup()
    turtle.forward(535.5)
    turtle.right(90)
    turtle.pendown()
    turtle.showturtle()
    
    turtle.forward(30)
    turtle.right(90)

    turtle.begin_fill()
    turtle.color("#001a33")
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(180)
    turtle.end_fill()

    #window

    turtle.hideturtle()
    turtle.left(90)
    turtle.penup()
    turtle.forward(360.6)
    turtle.left(90)
    turtle.forward(200)
    turtle.pendown()
    turtle.showturtle()
    
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.end_fill()
    turtle.hideturtle()

    #Welcome text
    turtle.penup()
    turtle.backward(300)
    turtle.left(90)
    turtle.forward(180)
    turtle.pendown()
    turtle.write("Welcome", font=('castellar', 30, 'bold'), align='center')

    time.sleep(5)
    turtle.bye()
    
    turtle.Turtle._screen = None  # force recreation of singleton Screen object
    turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
    
def flower():
    import turtle
    turtle.color("#800080") #pink
    drawing_area2 = turtle.Screen()
    drawing_area2.bgcolor("#ffe6ff")
    drawing_area2.title("Small flower for you")
    turtle.left(90)
    def petal():
        turtle.circle (72, 72)
        turtle.left(72)
        turtle.circle(72, 144)
    for i in range(5):
        petal()
    
    turtle.hideturtle()
    turtle.penup()

    #bringing pointer to center
    turtle.left(135)
    turtle.circle(48, 45)
    turtle.right(90)
    turtle.pendown()


    turtle.begin_fill()    
    turtle.circle(10)
    turtle.end_fill()

    #print(turtle.pos())

    #writing
    turtle.up()
    turtle.setpos(x=-13, y=120)
    turtle.down()
    turtle.write("Good day..", font=('castellar', 30, 'bold'), align='left')
    #turtle.done()
    time.sleep(3)
    turtle.bye()
    
    turtle.Turtle._screen = None  # force recreation of singleton Screen object
    turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition

#hut()

#flower()

