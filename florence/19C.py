import turtle


def drawPolygon(sides, length):
    for i in range(sides):
        turtle.forward(length)
        turtle.left(360/sides)


drawPolygon(15,50)

