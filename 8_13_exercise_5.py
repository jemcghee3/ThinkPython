"""Exercise 5

A Caesar cypher is a weak form of encryption that involves “rotating” each letter by a fixed number of places.
To rotate a letter means to shift it through the alphabet, wrapping around to the beginning if necessary,
so ’A’ rotated by 3 is ’D’ and ’Z’ rotated by 1 is ’A’.

To rotate a word, rotate each letter by the same amount.
For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.
In the movie 2001: A Space Odyssey, the ship computer is called HAL, which is IBM rotated by -1.

Write a function called rotate_word that takes a string and an integer as parameters,
and returns a new string that contains the letters from the original string rotated by the given amount.

You might want to use the built-in function ord, which converts a character to a numeric code, and chr,
which converts numeric codes to characters. Letters of the alphabet are encoded in alphabetical order, so for example:

 ord('c') - ord('a')
2

Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes for upper case letters are different.

Potentially offensive jokes on the Internet are sometimes encoded in ROT13, which is a Caesar cypher with rotation 13.
If you are not easily offended, find and decode some of them. Solution: http://thinkpython2.com/code/rotate.py."""


def rotate(num, n):
    return num + n


def too_low(n):
    return n + 26


def too_high(n):
    return n - 26


def upper_wrap(n):
    if n < 65:
        return too_low(n)
    elif n > 90:
        return too_high(n)
    else:
        return n

def lower_wrap(n):
    if n < 97:
        return too_low(n)
    elif n > 122:
        return too_high(n)
    else:
        return n


def upper_caesar(num, n):
    num = rotate(num, n)
    num = upper_wrap(num)
    return chr(num)


def lower_caesar(num, n):
    num = rotate(num, n)
    num = lower_wrap(num)
    return chr(num)


def rotate_word(s, n):
    new_word = ''
    for c in s:
        if c.isalpha() == False:
            new_word += c
            continue
        num = ord(c)
        if 65 <= num <= 90:
            num = upper_caesar(num, n)
        elif 97 <= num <= 122:
            num = lower_caesar(num, n)
        else:
            print('something went wrong')
        new_word += num
    print(new_word)

rotate_word('IBM', -1)