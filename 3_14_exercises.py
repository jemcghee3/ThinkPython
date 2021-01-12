"""Exercise 1

Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.

>>> right_justify('monty')
                                                                 monty

Hint: Use string concatenation and repetition. Also, Python provides a built-in function called len that returns the length of a string, so the value of len('monty') is 5.
"""
def right_justify(s):
    s_len = len(s)
    print(' '*(70-s_len)+s)

right_justify('monty')
"""
Exercise 2  

A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes a function object as an argument and calls it twice:

def do_twice(f):
    f()
    f()

Here’s an example that uses do_twice to call a function named print_spam twice.

def print_spam():
    print('spam')

do_twice(print_spam)

    Type this example into a script and test it.
    Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.
    Copy the definition of print_twice from earlier in this chapter to your script.
    Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
    Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.

Solution: http://thinkpython2.com/code/do_four.py.
"""
def do_twice(f, val):
    f(val)
    f(val)

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'Spam')

def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)

do_four(print_twice, 'Spammy')

"""
Exercise 3  

Note: This exercise should be done using only the statements and other features we have learned so far.

    Write a function that draws a grid like the following:

    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +
    |         |         |
    |         |         |
    |         |         |
    |         |         |
    + - - - - + - - - - +

    Hint: to print more than one value on a line, you can print a comma-separated sequence of values:

    print('+', '-')

    By default, print advances to the next line, but you can override that behavior and put a space at the end, like this:

    print('+', end=' ')
    print('-')

    The output of these statements is '+ -' on the same line. The output from the next print statement would begin on the next line.
    Write a function that draws a similar grid with four rows and four columns.

Solution: http://thinkpython2.com/code/grid.py."""

def do_twice(f, val):
    f(val)
    f(val)

def print_twice(bruce):
    print(bruce, end = ' ')
    print(bruce, end = ' ')

def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)

def seperator(x):
    print('+', end = ' ')
    do_twice(print_twice, '-')

def empty(x):
    print('|', end = ' ')
    do_twice(print_twice, ' ')

def box(x):
    do_four(empty, 0)
    print('|')

def small_box(x):
    do_twice(empty, 0)
    print('|')

def row(x):
    do_four(seperator, 0)
    print('+')
    do_four(box, 0)

def small_row(x):
    do_twice(seperator, 0)
    print('+')
    do_four(small_box, 0)

do_twice(small_row, 0)
do_twice(seperator, 0)
print('+')

print(' ')
do_four(row, 0)
do_four(seperator, 0)
print('+')