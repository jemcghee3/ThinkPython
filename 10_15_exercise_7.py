"""Exercise 7

Write a function called has_duplicates that takes a list and returns True
if there is any element that appears more than once. It should not modify the original list."""


def has_duplicates(input_list):  # this function will consider 1 and 1.0 as duplicates
    for item in input_list:
        t = input_list[:]
        t.remove(item)
        if item in t:
            return True
    return False


def has_duplicates2(input_list):  # this function will consider 1 and 1.0 as duplicates
    for item in input_list:
        if input_list.count(item) > 1:
            return True
    return False


test_list = ['a', 1, 1.1, 1.0, '1', []]

print(test_list)
print(has_duplicates2(test_list))
print(test_list)
