"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/

Exercise 2

Write an appropriately general set of functions that can draw flowers as in Figure 4.1.

Solution: http://thinkpython2.com/code/flower.py, also requires http://thinkpython2.com/code/polygon.py.

"""


from __future__ import print_function, division

import math
import turtle


def square(t, length):
    """Draws a square with sides of the given length.
    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    print('polyline function')
    print('t: ', t)
    print('n: ', n)
    print('length: ', length)
    print('angle: ', angle)
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.
    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.
    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    print('arc function')
    print(f't: , {t}')
    print(f'r: , {r}')
    print(f'angle: , {angle}')
    arc_length = 2 * math.pi * r * abs(angle) / 360
    print(f'arc_length: {arc_length}')
    n = int(arc_length / 4) + 3
    print(f'n: {n}')
    step_length = arc_length / n
    print(f'step_length: {step_length}')
    step_angle = float(angle) / n
    print(f'step_angle: {step_angle}')

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.
    t: Turtle
    r: radius
    """
    print('circle function')
    print(f't: {t}')
    print('r:', r)
    arc(t, r, 360)

def flower(t, r, p): # p is number of petals
    print('flower function')
    for i in range(p):
        arc(t, 2*r, 360*2/p)
        t.lt(360/p)
# this draws 'fat' flowers, like a rose. turn is based on regular polygon, with arc angle twice as long

def flower2(t, r, p): # p is number of petals
    print('flower function')
    for i in range(2*p): # note 2p used to make complete
        arc(t, r, 180+360/p)
        t.lt(360/p)
# This gets closer but I'm not sure why. Petals too fat and too many.

def flower3(t, r, p): # p is number of petals
    print('flower function')
    for i in range(2*p): # note 2p used to make complete
        arc(t, r, 2*360/p)
        t.lt(180-360/p)
# This makes the right kind of petals, but 2*p instead of p

def flower4(t, r, p): # p is number of petals
    print('flower function')
    for i in range(2*p): # note 2p used to make complete
        arc(t, r, 180-360/p)
        t.lt(180-360/p)
# This makes the right kind of petals, and the right number, but they don't meet at a point in the middle.

def flower5(t, r, p): # p is number of petals
    print('flower function')
    for i in range(2*p): # note 2p used to make complete
        arc(t, r, (360/(p-2))) #when p= 4 need this to be 180, when p = 3, 120, p = 5,? This works for p = 4 but that's it.
        t.lt((180*(p-2)/p)) # when p = 3, angle = 120, p = 4, angle = 90, p = 5, angle = 72
# This makes the right kind of petals, and the right number, but they don't meet at a point in the middle.

def flower6(t, r, p): # p is number of petals
    print('flower function')
    for i in range(2*p): # note 2p used to make complete
        arc(t, r, (360/p)) # this works for p = 3 #(180*(p-2)/p))
        t.lt(180-180*(p-2)/p)
# this works for p = 4 but nothing else

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

def petal(t, r, a):
    print('petal function')
    for i in range(2):
        arc(t, r, a)
        t.lt(180-a)


def flower7(t, r, n):
    print('flower function')
    angle = 360/n
    print('angle: ', angle)
    for i in range(n):
        petal(t, r, angle)
        t.lt(angle)


if __name__ == '__main__':
    print('__main__')
    bob = turtle.Turtle()
    print('bob: ', bob)

    # draw a circle centered on the origin
    radius = 500
    print('radius: ', radius)
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()

    flower7(bob, radius, 21)



    # wait for the user to close the window
    turtle.mainloop()