"""Exercise 4

A number, a, is a power of b if it is divisible by b and a/b is a power of b.
Write a function called is_power that takes parameters a and b and returns True if a is a power of b.
Note: you will have to think about the base case."""


def is_power(a, b):
    if a < 0 and b < 0: # to take care of negative numbers
        a = -a
        b = -b
    if b == 1 or b == -1: # to end infinite recursion if b == 1
        return False
    if a % b != 0 and a >= 1 and b >= 1: # if a is not divisible by b
        return False
    if -1 < a < 1 or -1 < b < 1:
        if b < a:
            return False
    if a == b:
        return True
    return is_power(a/b, b)

print(is_power(-8, -2))