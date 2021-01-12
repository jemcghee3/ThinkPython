"""def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

As an exercise, modify find so that it has a third parameter, the index in word where it should start looking."""

def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

position = find('Hello world!', 'o', 5)
print(position)