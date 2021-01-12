# 4.3  Exercises

# The following is a series of exercises using TurtleWorld. They are meant to be fun, but they have a point, too. While you are working on them, think about what the point is.

# The following sections have solutions to the exercises, so don’t look until you have finished (or at least tried).

# Write a function called square that takes a parameter named t, which is a turtle. It should use the turtle to draw a square.

import turtle


def square(t):
    print(t)
    for i in range(4):
        t.fd(100)
        t.lt(90)
    turtle.mainloop()


# Write a function call that passes bob as an argument to square, and then run the program again.

# bob = turtle.Turtle()
# square(bob)

# Add another parameter, named length, to square. Modify the body so length of the sides is length, and then modify the function call to provide a second argument. Run the program again. Test your program with a range of values for length.

def square(t, l):
    print(t)
    for i in range(4):
        t.fd(l)
        t.lt(90)
    turtle.mainloop()


bob = turtle.Turtle()


# square(bob, 100)

# Make a copy of square and change the name to polygon. Add another parameter named n and modify the body so it draws an n-sided regular polygon. Hint: The exterior angles of an n-sided regular polygon are 360/n degrees.

def polygon(t, l, n):
    angle = 360 / n
    for i in range(n):
        t.fd(l)
        t.lt(angle)
    turtle.mainloop()


# polygon(bob, 100, 10)

# Write a function called circle that takes a turtle, t, and radius, r, as parameters and that draws an approximate circle by calling polygon with an appropriate length and number of sides. Test your function with a range of values of r.
# Hint: figure out the circumference of the circle and make sure that length * n = circumference.

import math


def circle(t, r):
    cir = 2 * math.pi * r
    step = cir / 360
    angle = 1
    for i in range(360):
        t.fd(step)
        t.lt(angle)
    turtle.mainloop()

def circle2(t, r):
    cir = 2 * math.pi * r
    n = 360
    l = cir / n
    polygon(t, l, n)

def circle3(t, r):
    cir = 2 * math.pi * r
    n = int(cir / 3) + 3
    l = cir / n
    polygon(t, l, n)

# circle(bob, 100)
# circle2(bob, 100)
# circle3(bob, 100)
# Make a more general version of circle called arc that takes an additional parameter angle, which determines what fraction of a circle to draw. angle is in units of degrees, so when angle=360, arc should draw a complete circle.

def arc(t, r, a):
    cir = 2 * math.pi * r
    step = cir / 360
    angle = 1
    for i in range(a):
        t.fd(step)
        t.lt(angle)
    turtle.mainloop()

# arc(bob, 100, 360)

def polyline(t, n, l, angle):
    for i in range(n):
        t.fd(l)
        t.lt(angle)

def polygon2(t, n, l):
    angle = 360.0 / n
    polyline(t, n, l, angle)

polygon2(bob, 50, 10)

def arc2(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360 # this calculates the circumference but then only takes the length of that portion being used
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

# arc2(bob, 100, 90)