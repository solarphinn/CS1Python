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
    """
    Draws a circle with the specified radius, and then recursively draws
    smaller circles inside of it. Continues until the recursion depth reaches
    0.
    :param radius: The radius of the circle to draw.
    :param depth: The depth at which the recursion should stop.
    :return: None
    """
    if depth <= 0:  # if the recursion depth reaches 0...
        pass        # ...do nothing.
    else:
        # if the depth is >= 1, draw the circle
        turtle.down()
        turtle.circle(radius)
        turtle.up()
        # draw inner circle 1 of 4...
        circles(radius / 2, depth - 1)
        # draw inner circle 2 of 4...
        turtle.forward(radius)
        turtle.left(90)
        turtle.forward(radius)
        circles(radius / 2, depth - 1)
        # draw inner circle 3 of 4...
        turtle.forward(radius)
        turtle.left(90)
        turtle.forward(radius)
        circles(radius / 2, depth - 1)
        # draw inner circle 4 of 4...
        turtle.forward(radius)
        turtle.left(90)
        turtle.forward(radius)
        circles(radius / 2, depth - 1)
        # position the turtle back at the start
        turtle.forward(radius)
        turtle.left(90)
        turtle.forward(radius)


def main():
    # called to initialize the turtle. change the arguments here to adjust
    # the speed and enabledisable animation of the turtle
    init_turtle(0, True, 200)
    circles(200, 3)
    turtle.done()

main()
