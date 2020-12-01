import turtle


def square():
    rich_turtle = turtle.Turtle()
    rich_turtle.forward(100)
    rich_turtle.left(90)
    rich_turtle.forward(100)
    rich_turtle.left(90)
    rich_turtle.forward(100)
    rich_turtle.left(90)
    rich_turtle.forward(100)


for i in range(10):
    if i <= 10:
        square()

    i += 1
