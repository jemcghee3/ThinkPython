"""Exercise 10

To check whether a word is in the word list, you could use the in operator,
but it would be slow because it searches through the words in order.

Because the words are in alphabetical order, we can speed things up with a bisection search
(also known as binary search), which is similar to what you do when you look a word up in the dictionary
(the book, not the data structure).
You start in the middle and check to see whether the word you are looking for
comes before the word in the middle of the list. If so, you search the first half of the list the same way.
Otherwise you search the second half.

Either way, you cut the remaining search space in half. If the word list has 113,809 words,
it will take about 17 steps to find the word or conclude that it’s not there.

Write a function called in_bisect that takes a sorted list and a target value and returns True
if the word is in the list and False if it’s not.

Or you could read the documentation of the bisect module and use that!
Solution: http://thinkpython2.com/code/inlist.py."""


def data_read():
    fin = open('words.txt')
    data = list()
    for line in fin:
        line = line.rstrip()
        data.append(line)
    return data


def in_bisect(sorted_list, target_value):
    if len(sorted_list) == 1:
        return target_value in sorted_list
    # print(target_value)
    i = len(sorted_list) // 2
    middle = sorted_list[i]
    # print('middle', middle)
    front = sorted_list[:i]
    # print('front', front)
    back = sorted_list[i+1:]
    # print('back', back)
    if target_value == middle:
        return True
    elif target_value < middle:
        return in_bisect(front, target_value)
    elif target_value > middle:
        return in_bisect(back, target_value)
    else:
        return 'Something went wrong.'


data = data_read()
# data = ['apple', 'banana', 'cats', 'spam', 'zebras']
print(in_bisect(data, 'zebras'))
