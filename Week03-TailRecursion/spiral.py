import turtle
import random


def init_turtle(speed, tracer):
    """
    Initializes the turtle.
    :param speed: The speed at which the turtle should animate.
    :param tracer: Boolean to enable or disable the turtle's tracer.
    :return: None
    """
    turtle.pensize(3)
    turtle.up()
    turtle.back(200)
    turtle.left(90)
    turtle.speed(speed)
    turtle.tracer(tracer)


def random_color():
    """
    A helper function that sets the turtle's pen color to a random RGB value.
    :return: None
    """
    turtle.pencolor(random.random(), random.random(), random.random())


def spiral(length):
    """
    Recursively draws a multi-colored decagonal spiral.
    :param length: The length of the next segment of the spiral.
    :return: The total distance that the turtle travels while drawing the
             spiral
    """
    if length == 0:
        return 0
    else:
        turtle.down()
        random_color()
        turtle.forward(length)
        turtle.up()
        turtle.right(36)
        return length + spiral(length-1)


def spiral_tail(length, total_distance = 0):
    """
    A tail recursive version of the decagonal spiral drawing function.
    Accumulates the distance top-down as the turtle draws rather than bottom-up
    when the spiral is finished.
    :param length: The length of the next segment of the spiral.
    :param total_distance: The accumulated distance that the turtle has
           traveled so far.
    :return: The total accumulated distance after the spiral is complete.
    """
    if length == 0:
        return total_distance
    else:
        turtle.down()
        random_color()
        turtle.forward(length)
        turtle.up()
        turtle.right(36)
        return spiral_tail(length-1, length + total_distance)


def main():
    init_turtle(0, True)  # speed = 0, tracer on
    print(spiral_tail(150, 0))  # prints the distance traveled by the turtle
    turtle.done()


main()
