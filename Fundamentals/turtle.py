import turtle
def draw_square():
    window = turtle.screensize(4,4,"red")

    brad = turtle.Turtle()

    for i in range(0,4):
        brad.forward(100)
        brad.right(90)

    window.exitonclick()
draw_square()
