"""Exercise 5

Write a function named uses_all that takes a word and a string of required letters,
and that returns True if the word uses all the required letters at least once.
How many words are there that use all the vowels aeiou? How about aeiouy?"""


def required_check(c, word):
    for l in word:
        if c == l:
            return True
    return False


def uses_all(word, required):
    for c in required:
        if required_check(c, word) is False:
            return False
    return True


all = 'aeiou'
ally = 'aeiouy'

counter = 0

fin = open('words.txt')
for line in fin:
    line = line.rstrip()
    if uses_all(line, ally) is True:
        print(line)
        counter += 1
print('counter', counter)