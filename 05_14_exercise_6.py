"""Exercise 6

The Koch curve is a fractal that looks something like Figure 5.2.
To draw a Koch curve with length x, all you have to do is

    Draw a Koch curve with length x/3.
    Turn left 60 degrees.
    Draw a Koch curve with length x/3.
    Turn right 120 degrees.
    Draw a Koch curve with length x/3.
    Turn left 60 degrees.
    Draw a Koch curve with length x/3.

The exception is if x is less than 3: in that case, you can just draw a straight line with length x.

    Write a function called koch that takes a turtle and a length as parameters,
    and that uses the turtle to draw a Koch curve with the given length.
    Write a function called snowflake that draws three Koch curves to make the outline of a snowflake.

    Solution: http://thinkpython2.com/code/koch.py.
    The Koch curve can be generalized in several ways.
    See http://en.wikipedia.org/wiki/Koch_snowflake for examples and implement your favorite."""

import turtle

def koch(t, x):
    if x < 3:
        t.fd(x)
    else:
        koch(t, x/3)
        t.lt(60)
        koch(t, x/3)
        t.rt(120)
        koch(t, x/3)
        t.lt(60)
        koch(t, x/3)


def snowflake(t, x):
    for i in range(3):
        koch(t, x)
        t.rt(120)


bob = turtle.Turtle()

snowflake(bob, 300)

turtle.mainloop()