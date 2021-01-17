"""Exercise 4

Write a function named uses_only that takes a word and a string of letters,
and that returns True if the word contains only letters in the list.
Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa”?"""


def letter_checker(c, letters):
    for l in letters:
        if c == l:
            return True
    return False


def uses_only(word, letters):
    for c in word:
        if letter_checker(c, letters) is False:
            return False
    return True


fin = open('words.txt')

allowed_letters = 'acefhlo'

for line in fin:
    line = line.rstrip()
    if uses_only(line, allowed_letters) is True:
        print(line)
