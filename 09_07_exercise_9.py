"""Exercise 9   Here’s another Car Talk Puzzler you can solve with a search (http://www.cartalk.com/content/puzzlers):

    “Recently I had a visit with my mom and we realized
    that the two digits that make up my age when reversed resulted in her age.
    For example, if she’s 73, I’m 37. We wondered how often this has happened over the years
    but we got sidetracked with other topics and we never came up with an answer.

    “When I got home I figured out that the digits of our ages have been reversible six times so far.
    I also figured out that if we’re lucky it would happen again in a few years,
    and if we’re really lucky it would happen one more time after that.
    In other words, it would have happened 8 times over all. So the question is, how old am I now?”

Write a Python program that searches for solutions to this Puzzler. Hint: you might find the string method zfill useful.

Solution: http://thinkpython2.com/code/cartalk3.py."""


def reverse(i, j):
    i = str(i).zfill(2)
    j = str(j).zfill(2)
    return i == j[::-1]


def mom(x, diff, counter):
    for i in range(x, 100):
        if reverse(i, i - diff) is True:
            counter += 1
            if counter == 6:
                pa = i - diff
            # print(i, i - diff, diff, counter)
    if counter == 8:
        return pa


def find_all():
    counter = 0
    for diff in range(1, 100):
        ans = mom(diff, diff, counter)
        if ans is not None:
            print('ans', ans)


find_all()
