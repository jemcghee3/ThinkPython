"""Exercise 12

Two words “interlock” if taking alternating letters from each forms a new word.
For example, “shoe” and “cold” interlock to form “schooled”. Solution: http://thinkpython2.com/code/interlock.py.
Credit: This exercise is inspired by an example at http://puzzlers.org.

    Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
    Can you find any words that are three-way interlocked; that is, every third letter forms a word,
    starting from the first, second or third?"""


import bisect


def data(file):
    fin = open(file)
    raw_data = list()
    for line in fin:
        line = line.rstrip()
        raw_data.append(line)
    return raw_data


def word_split(word3):
    word1 = ''
    word2 = ''
    for i in range(len(word3)):
        if i % 2 == 0:
            word1 = word1 + word3[i]
        else:
            word2 = word2 + word3[i]
    return word1, word2


def word_check(sorted_list, word):
    i = bisect.bisect_left(sorted_list, word)
    if i == len(sorted_list):
        return False
    return sorted_list[i] == word


def split_checker(sorted_list):
    for word3 in sorted_list:
        word1, word2 = word_split(word3)
        if word_check(sorted_list, word1) is True and word_check(sorted_list, word2) is True:
            print(word3, word1, word2)


def word_split_3way(word3):
    word1 = ''
    word2 = ''
    word4 = '' # note because I used word3 consistently for the 'interlocked' word i had to use something else
    for i in range(len(word3)):
        if i % 3 == 0:
            word1 = word1 + word3[i]
        elif i % 3 == 1:
            word2 = word2 + word3[i]
        else:
            word4 = word4 + word3[i]
    return word1, word2, word4

def split_checker_3way(sorted_list):
    for word3 in sorted_list:
        word1, word2, word4 = word_split_3way(word3)
        if word_check(sorted_list, word1) is True and word_check(sorted_list, word2) is True \
            and word_check(sorted_list, word4) is True:
            print(word3, word1, word2, word4)

data_list = data('words.txt')
split_checker_3way(data_list)