import turtle


def init_turtle(speed, trace, radius):
    """
    Initializes the turtle prior to drawing the first circle.
    :param speed: The speed to which the turtle should be set.
    :param trace: The boolean value for the tracer (should the turtle animate
                  while drawing).
    :param radius: The radius of the outermost circle.
    :return: None.
    """
    turtle.speed(speed)
    turtle.tracer(trace)
    turtle.up()
    turtle.right(90)
    turtle.forward(radius)
    turtle.left(90)


def circles(radius, depth):
    if depth <= 0:
        pass
    else:
        turtle.down()
        turtle.circle(radius)
        turtle.up()
        turtle.forward(radius)
        turtle.left(90)
        turtle.forward(radius)
        circles(radius / 2, depth - 1)
        turtle.forward(radius)
        turtle.left(90)
        turtle.forward(radius)
        circles(radius / 2, depth - 1)
        turtle.forward(radius)
        turtle.left(90)
        turtle.forward(radius)
        circles(radius / 2, depth - 1)
        turtle.forward(radius)
        turtle.left(90)
        turtle.forward(radius)
        circles(radius / 2, depth - 1)


def main():
    init_turtle(0, True, 200)
    circles(200, 3)
    turtle.done()

main()
