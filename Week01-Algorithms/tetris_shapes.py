# The turtle module is needed to draw shapes
import turtle


def init_turtle():
    """
    Initializes the turtle to the origin and facing east with the pen up.
    """
    turtle.up()
    turtle.home()


def draw_block():
    """
    Draws a single block filled with the current fill color.
    preconditions: The turtle is in the bottom left corner of the block.
    postconditions: The turtle is in the bottom left corner of the block.
    :return:
    """
    turtle.down()
    turtle.begin_fill()
    turtle.pensize(3)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.end_fill()
    turtle.up()


def draw_long_shape():
    """
    Draws a long shape; 4 blocks end-to-end filled with blue.
    preconditions: The turtle is in the bottom left corner of the first block.
    postconditions: The turtle is in the bottom left corner of the first
                    block.
    """
    turtle.fillcolor('blue')
    draw_block()
    turtle.forward(50)
    draw_block()
    turtle.forward(50)
    draw_block()
    turtle.forward(50)
    draw_block()
    turtle.back(150)


def main():
    """
    Main function; all of the code that should be executed in this program
    should be in this function.
    """
    init_turtle()       # initialize the turtle
    draw_long_shape()   # draw the long shape
    print("Close window to quit.")
    turtle.done()       # pause until the user closes the window


'''
Only left-justified code will be executed when the Python file is run.
Typically, this should only be a call to the main function.
'''
main()