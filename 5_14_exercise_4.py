"""Exercise 4   What is the output of the following program?
Draw a stack diagram that shows the state of the program when it prints the result.

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

    What would happen if you called this function like this: recurse(-1, 0)?
    Write a docstring that explains everything someone would need to know
    in order to use this function (and nothing else)."""

def recurse(n, s): # takes an integer n and is recursive n times, adding n to integer s each time before giving final s.
    print('recurse')
    print('n', n)
    print('s', s)
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

print('__main__')

recurse(3, 0)

# recurse(-1, 0) This causes infinite recursion.