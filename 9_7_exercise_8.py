"""Exercise 8   Here’s another Car Talk Puzzler (http://www.cartalk.com/content/puzzlers):

    “I was driving on the highway the other day and I happened to notice my odometer.
    Like most odometers, it shows six digits, in whole miles only.
    So, if my car had 300,000 miles, for example, I’d see 3-0-0-0-0-0.

    “Now, what I saw that day was very interesting. I noticed that the last 4 digits were palindromic;
    that is, they read the same forward as backward. For example, 5-4-4-5 is a palindrome,
    so my odometer could have read 3-1-5-4-4-5.

    “One mile later, the last 5 numbers were palindromic.
    For example, it could have read 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic.
    And you ready for this? One mile later, all 6 were palindromic!

    “The question is, what was on the odometer when I first looked?”

Write a Python program that tests all the six-digit numbers and prints any numbers that satisfy these requirements.
Solution: http://thinkpython2.com/code/cartalk2.py."""


def is_palindromic(n, i):
    return str(n)[-i:] == str(n)[-1:-i-1:-1]


n = 100000
while n <1000000:
    if is_palindromic(n, 4) is True:
        if is_palindromic(n+1, 5) is True:
            if is_palindromic(((n+2) % 100000) // 10, 4) is True:
                if is_palindromic(n+3, 6) is True:
                    print(n)
    n += 1
print('done')