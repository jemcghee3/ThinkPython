"""Exercise 1

Draw a stack diagram for the following program. What does the program print?

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))
"""


def b(z):
    print('function b')
    print('z -->', z)
    prod = a(z, z)
    print(z, prod)
    return prod


def a(x, y):
    print('function a')
    print('x -->', x)
    print('y -->', y)
    x = x + 1
    print('x -->', x)
    print('returning x * y', x * y)
    return x * y


def c(x, y, z):
    print('function c')
    print('x -->', x)
    print('y -->', y)
    print('z -->', z)
    total = x + y + z
    print('total -->', total)
    square = b(total)**2
    print('square -->', square)
    return square


print('__main__')
x = 1
print('x -->', x)
y = x + 1
print('y -->', y)
print(c(x, y+3, x+y))
