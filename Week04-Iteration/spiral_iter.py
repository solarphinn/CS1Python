import turtle
import random

def spiral(length):
    total = 0
    while length > 0:
        turtle.down()
        turtle.pencolor(random.random(), random.random(),random.random())
        turtle.forward(length)
        turtle.right(36)
        turtle.up()
        total = total + length
        length = length - 1

    return total


def spiral_rec(length, total=0):
    if length <= 0:
        return total
    else:
        turtle.down()
        turtle.pencolor(random.random(), random.random(), random.random())
        turtle.forward(length)
        turtle.right(36)
        turtle.up()
        total = total + length
        length = length - 1
        return spiral_rec(length, total)


turtle.up()
turtle.back(200)
turtle.left(90)
turtle.speed(0)
spiral_rec(100)
turtle.done()
