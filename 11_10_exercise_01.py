"""Exercise 1

Write a function that reads the words in words.txt and stores them as keys in a dictionary.
It doesn’t matter what the values are.
Then you can use the in operator as a fast way to check whether a string is in the dictionary.

If you did Exercise 10, you can compare the speed of this implementation
with the list in operator and the bisection search."""


def data(file):
    fin = open(file)
    raw_data = dict()
    for line in fin:
        line = line.rstrip()
        raw_data[line] = raw_data.get(line, 0)
    return raw_data


file = 'words.txt'
words = data(file)

print('zebra' in words)