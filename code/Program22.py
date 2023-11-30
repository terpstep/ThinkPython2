import turtle


def draw_s():
    turtle.forward(50)
    turtle.right(90)
    turtle.circle(-25, 180)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.circle(-25, 180)
    turtle.right(90)
    turtle.forward(50)


def draw_t():
    turtle.forward(50)
    turtle.backward(25)
    turtle.right(90)
    turtle.forward(100)


def draw_e():
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)


def draw_p():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.circle(-25, 180)


turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()


draw_s()
turtle.penup()
turtle.forward(25)
turtle.pendown()
draw_t()
turtle.penup()
turtle.forward(25)
turtle.pendown()
draw_e()
turtle.penup()
turtle.forward(25)
turtle.pendown()
draw_p()
turtle.hideturtle()

turtle.done()
