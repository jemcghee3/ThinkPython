"""Exercise 3

Write an appropriately general set of functions that can draw shapes as in Figure 4.2.

Solution: http://thinkpython2.com/code/pie.py."""

import turtle, math

def line(t, l):
    t.fd(l)

def triangle(t, a, b, c, angle, other_angle):
    turn_angle = 180-other_angle
    line(t, a)
    t.lt(turn_angle)
    # this is too long! but it's right!
    line(t, c)
    t.lt(turn_angle)
    line(t, b)

def shape(t, a, b, c, angle, other_angle, n):
    for i in range(n):
        triangle(t, a, b, c, angle, other_angle)
        t.rt(180)

bob = turtle.Turtle()

n = 6
a = 90
b = a
angle = 360/n
rad = math.radians(angle)
c = (a ** 2 + b ** 2 - (2 * a * b * math.cos(rad)))**0.5
other_angle = (180-angle) / 2
print(math.cos(angle))

shape(bob, a, b, c, angle, other_angle, n)

turtle.mainloop()