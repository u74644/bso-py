import turtle
turtle.speed(5)
def drawTriange(side):
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)

for i in range(20):
    drawTriange(100)
    turtle.left(18)
