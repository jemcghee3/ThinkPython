"""As an exercise, write a function is_between(x, y, z) that returns True if x ≤ y ≤ z or False otherwise."""


def is_between(x, y, z):
    return x <= y <= z


a = 1
b = 2
c = 3

print(is_between(b, a, c))
