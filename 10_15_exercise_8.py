"""Exercise 8

This exercise pertains to the so-called Birthday Paradox, which you can read about at
http://en.wikipedia.org/wiki/Birthday_paradox.

If there are 23 students in your class, what are the chances that two of you have the same birthday?
You can estimate this probability by generating random samples of 23 birthdays and checking for matches.
Hint: you can generate random birthdays with the randint function in the random module.

You can download my solution from http://thinkpython2.com/code/birthday.py."""

import math

def birthday_chance(n):  # n is the number of people in the class
    return 1 - math.factorial(365) / (365 ** n * math.factorial(365 - n))

print(str(birthday_chance(23) * 100) + '%')