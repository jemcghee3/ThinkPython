"""Exercise 5   Write a function called is_sorted that takes a list as a parameter
and returns True if the list is sorted in ascending order and False otherwise. For example:

>>is_sorted([1, 2, 2])
True
>>is_sorted(['b', 'a'])
False
"""


def is_sorted(input_list):
    return input_list == sorted(input_list)


t = [1, 2, 3]

print(is_sorted(t))
