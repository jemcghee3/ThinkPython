"""Exercise 4

If you did Exercise 7, you already have a function named has_duplicates that takes a list as a parameter
and returns True if there is any object that appears more than once in the list.

Use a dictionary to write a faster, simpler version of has_duplicates.
Solution: http://thinkpython2.com/code/has_duplicates.py.


def has_duplicates2(input_list):  # this function will consider 1 and 1.0 as duplicates
    for item in input_list:
        if input_list.count(item) > 1:
            return True
    return False"""


def has_duplicates_dict(input_list): # this doesn't work if the input list includes a list
    raw_data = dict()
    for item in input_list:
        if item in raw_data:
            return True
        raw_data.setdefault(item, 1)
    return False


test_list = ['a', 1, 1.1, 1.2, '1', 0]

print(test_list)
print(has_duplicates_dict(test_list))
print(test_list)
