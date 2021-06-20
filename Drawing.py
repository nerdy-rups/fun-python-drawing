
#import turtle


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
    turtle.forward(20)
    
    turtle.right(90)
    turtle.forward(180)
    #turtle.right(90)
    #turtle.forward(40)
    #turtle.right(90)
    #turtle.forward(180)

    turtle.color("#001a33")


    turtle.bye()
    
def flower():
    import turtle
    turtle.color("#cca300")
    turtle.begin_fill()
    turtle.up()
    turtle.right(90)
    turtle.forward(200)
    turtle.down()
    turtle.right(90)
    turtle.forward(200)
    turtle.bye()
#hut()
#flower()


