"""Exercise 3

Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn’t use any of the forbidden letters.

Write a program that prompts the user to enter a string of forbidden letters
and then prints the number of words that don’t contain any of them.
Can you find a combination of 5 forbidden letters that excludes the smallest number of words?"""

def forbidden_checker(c, forbidden):
    for l in forbidden:
        if l == c:
            return False
    return True

def avoids(word, forbidden):
    ans = False
    for c in word:
        if forbidden_checker(c, forbidden) == False:
            return False
    return True


forbidden_list = input('Please input the forbidden letters: ')
excluded_counter = 0
valid_counter = 0

fin = open('words.txt')
for line in fin:
    line = line.rstrip()
    if avoids(line, forbidden_list) == True:
        valid_counter += 1
    else:
        excluded_counter += 1
print('valid_counter', valid_counter)
print('excluded_counter', excluded_counter)
