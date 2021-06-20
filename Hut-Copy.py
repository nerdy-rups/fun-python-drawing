def hut():
    import turtle
    turtle.pensize('6')
    turtle.width(2)
    turtle.shape('arrow')
    drawing_area = turtle.Screen()
    drawing_area.title("Your hut")
    drawing_area.setup(width=1500, height=850, startx=0, starty=0)
    turtle.color("#cca300")
    turtle.begin_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(200)
    turtle.down()
    turtle.right(90)
    turtle.forward(200)
    turtle.done()
    
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
    turtle.done()
#hut()
#flower()


