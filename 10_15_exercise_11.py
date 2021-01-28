"""Exercise 11

Two words are a “reverse pair” if each is the reverse of the other.
Write a program that finds all the reverse pairs in the word list.
Solution: http://thinkpython2.com/code/reverse_pair.py."""


import bisect


def data(file):
    fin = open(file)
    raw_data = list()
    for line in fin:
        line = line.rstrip()
        raw_data.append(line)
    return raw_data


def reverse(sorted_list, word):
    return bisect.bisect_left(sorted_list, word[::-1])


def reverse_pair(sorted_list, word):
    i = reverse(sorted_list, word)
    if i == len(sorted_list):   # this means the reverse wasn't found
        return False
    if sorted_list[i] == word:
        return False
    elif sorted_list[i] == word[::-1]:
        return True


def reverse_pair_finder(sorted_list):
    for word in sorted_list:
        if reverse_pair(sorted_list, word) is True:
            print(word, word[::-1])


data_list = data('words.txt')
reverse_pair_finder(data_list)
