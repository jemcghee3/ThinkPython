"""Exercise 1   Write a program that reads words.txt and prints only the words with more than 20 characters
(not counting whitespace). """

fin = open('words.txt')
for line in fin:
    line = line.rstrip()
    if len(line) > 20:
        print(line)

