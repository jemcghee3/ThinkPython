"""Exercise 2

The Ackermann function, A(m, n), is defined:
A(m, n) =
⎧
⎪
⎨
⎪
⎩
              n+1	if  m = 0
        A(m−1, 1)	if  m > 0  and  n = 0
A(m−1, A(m, n−1))	if  m > 0  and  n > 0.

See http://en.wikipedia.org/wiki/Ackermann_function. Write a function named ack that evaluates the Ackermann function.
Use your function to evaluate ack(3, 4), which should be 125. What happens for larger values of m and n?
Solution: http://thinkpython2.com/code/ackermann.py. """


def ack(m, n):
    if m < 0:
        print('This function cannot evaluate m < 0.')
    if n < 0:
        print('This function cannot evaluate n < 0.')
    elif m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))


print(ack(3,4))