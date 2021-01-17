"""Exercise 7

This question is based on a Puzzler that was broadcast on the radio program Car Talk
(http://www.cartalk.com/content/puzzlers):

    Give me a word with three consecutive double letters.
    I’ll give you a couple of words that almost qualify, but don’t.
    For example, the word committee, c-o-m-m-i-t-t-e-e. It would be great except for the ‘i’ that sneaks in there.
    Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i’s it would work.
    But there is a word that has three consecutive pairs of letters
    and to the best of my knowledge this may be the only word.
    Of course there are probably 500 more but I can only think of one. What is the word?

Write a program to find it. Solution: http://thinkpython2.com/code/cartalk1.py."""


def letter_checker(c1, c2, c3, c4, c5, c6):
    return c1 == c2 and c3 == c4 and c5 == c6

def word_reader(word):
    if len(word) < 6:
        return False
    i = 0
    while i <= len(word) - 6:
        if letter_checker(word[i], word[i+1], word[i+2], word[i+3], word[i+4], word[i+5]) is True:
            return True
        i += 1
    return False

fin = open('words.txt')

for line in fin:
    line = line.rstrip()
    if word_reader(line) is True:
        print(line)