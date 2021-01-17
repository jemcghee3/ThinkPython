import math
import polygon
import turtle

bob = turtle.Turtle()

r = 0

for i in range(720):
    polygon.arc(bob, r, 10)
    r += 1

turtle.mainloop()
