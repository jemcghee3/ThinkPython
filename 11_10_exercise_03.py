"""Exercise 3   Memoize the Ackermann function from Exercise 2
and see if memoization makes it possible to evaluate the function with bigger arguments.
Hint: no. Solution: http://thinkpython2.com/code/ackermann_memo.py.


The Ackermann function, A(m, n), is defined:
A(m, n) =

              n+1	if  m = 0
        A(m−1, 1)	if  m > 0  and  n = 0
A(m−1, A(m, n−1))	if  m > 0  and  n > 0.


Here is the memoize code for Fibonacci sequence:

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res"""


known = {(0, 0): 1}
def memo_ackermann(t): # takes a tuple
    if t in known:
        return known[t]
    # if len(t) != 2:
    #     return 'This function only works with tuples formatted (m, n).'
    m, n = t
    if m < 0 or n < 0 or type(m) != int or type(n) != int or type(t) != tuple:
        return 'This function only works for tuples (m, n) where each is an integer greater than or equal to zero.'
    if m == 0:  # n+1	if  m = 0
        known[t] = n + 1
        return n + 1
    elif m > 0 and n == 0: # A(m−1, 1)	if  m > 0  and  n = 0
        t2 = (m - 1, 1)
        res = memo_ackermann(t2)
        known[t] = res
        return res
    elif m > 0 and n > 0: # A(m−1, A(m, n−1))	if  m > 0  and  n > 0
        tn = (m, n-1)
        n = memo_ackermann(tn)
        t2 = (m - 1, n)
        res = memo_ackermann(t2)
        known[t] = res
        return res


ans = memo_ackermann((3, 5))
print(ans)

# print(known)