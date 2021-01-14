"""Exercise 2

Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.

Write a program that reads words.txt and prints only the words that have no “e”.
Compute the percentage of words in the list that have no “e”. """


def e_checker(word):
    for c in word:
        if c.lower() == 'e':
            return False
    else:
        return True


fin = open('words.txt')
no_e_counter = 0
counter = 0
for line in fin:
    line = line.rstrip()
    if e_checker(line) == True:
        no_e_counter += 1
        print(line)
    counter += 1
print('The percentage of words with no "e" is ' + str(no_e_counter/counter*100) + '%.')
