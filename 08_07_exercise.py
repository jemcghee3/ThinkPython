"""
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

 As an exercise, encapsulate this code in a function named count,
 and generalize it so that it accepts the string and the letter as arguments.

Then rewrite the function so that instead of traversing the string,
it uses the three-parameter version of find from the previous section.
"""


def count(word, target_letter):
    counter = 0
    for letter in word:
        if letter == target_letter:
            counter += 1
    print(counter)


def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


def count2(word, target_letter):
    counter = 0
    start = 0
    while start <= len(word):
        mo = find(word, target_letter, start)
        if mo == -1:
            break
        counter += 1
        start = mo + 1
    print(counter)

count('Hello world!', 'o')
count2('Hello world!', 'o')
