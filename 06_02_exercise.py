"""As an exercise, use incremental development to write a function called hypotenuse that returns
the length of the hypotenuse of a right triangle given the lengths of the other two legs as arguments.
Record each stage of the development process as you go. """

import math


def hypotenuse(side1, side2):
    print('side1', side1)
    print('side2', side2)
    side1sq = side1 ** 2
    print('side1sq', side1sq)
    side2sq = side2 ** 2
    print('side2sq', side2sq)
    big_square = side1sq + side2sq
    print('big_square', big_square)
    side3 = math.sqrt(big_square)
    print('side3', side3)
    return side3


a = 100
b = 1000
c = hypotenuse(a, b)
print(c)
