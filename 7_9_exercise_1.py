"""Exercise 1

Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt that takes a as a parameter,
chooses a reasonable value of x, and returns an estimate of the square root of a.

To test it, write a function named test_square_root that prints a table like this:

a   mysqrt(a)     math.sqrt(a)  diff
-   ---------     ------------  ----
1.0 1.0           1.0           0.0
2.0 1.41421356237 1.41421356237 2.22044604925e-16
3.0 1.73205080757 1.73205080757 0.0
4.0 2.0           2.0           0.0
5.0 2.2360679775  2.2360679775  0.0
6.0 2.44948974278 2.44948974278 0.0
7.0 2.64575131106 2.64575131106 0.0
8.0 2.82842712475 2.82842712475 4.4408920985e-16
9.0 3.0           3.0           0.0

The first column is a number, a; the second column is the square root of a computed with mysqrt;
the third column is the square root computed by math.sqrt;
the fourth column is the absolute value of the difference between the two estimates. """


import math


def mysqrt(a):
    x = a / 2
    while True:
        # print(x)
        y = (x + a/x) / 2
        if y == x:
            return y
        x = y


def column_line(a):
    print(str(a/1) + ' ' * ((l1 + 1) - len(str(a/1))) + str(mysqrt(a)) + ' ' * ((l2 + 1) - len(str(mysqrt(a)))) + str(math.sqrt(a)) + ' ' * ((l3 + 1) - len(str(math.sqrt(a)))) + str(mysqrt(a) - math.sqrt(a)))
    # print(str(mysqrt(a)) + ' ')
    # print(str(math.sqrt(a)) + ' \n')
    # print(str(mysqrt(a) - math.sqrt(a)))

l1 = 1
l2 = 1
l3 = 1
group = range(2, 10)

for i in group:
    if len(str(i/1)) > l1:
        l1 = len(str(i/1))

for i in group:
    if len(str(mysqrt(i))) > l2:
        l2 = len(str(mysqrt(i)))

for i in group:
    if len(str(math.sqrt(i))) > l3:
        l3 = len(str(math.sqrt(i)))

print('a' + ' ' * (l1) + 'mysqrt(a)' + ' ' * (l2 - len('mysqrt(a)') + 1) + 'math.sqrt(a)' + ' ' * (l3 - len('math.sqrt(a)') + 1) + 'diff')
print('-' * len('a') + ' ' * (l1) + '-' * len('mysqrt(a)') + ' ' * (l2 - len('mysqrt(a)') + 1) + '-' * len('math.sqrt(a)') + ' ' * (l3 - len('math.sqrt(a)') + 1) + '-' * len('diff'))

for i in group:
    column_line(i)
# print(column_line(2))
