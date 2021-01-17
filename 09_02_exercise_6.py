"""Exercise 6

Write a function called is_abecedarian that returns True
if the letters in a word appear in alphabetical order (double letters are ok). How many abecedarian words are there?"""


def is_abecedarian(word):
    prior = 0
    current = 0
    for letter in word:
        current = ord(letter)
        if current < prior:
            return False
        prior = current
    return True


fin = open('words.txt')

counter = 0
for line in fin:
    line = line.rstrip()
    if is_abecedarian(line) is True:
        counter += 1
        print(line)

print('counter', counter)