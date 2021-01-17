"""Exercise 3

Write a function called middle that takes a list and returns a new list
that contains all but the first and last elements. For example:

>>t = [1, 2, 3, 4]
>>middle(t)
[2, 3]
"""

def middle(input_list):
    t = input_list
    del t[0]
    del t[-1]
    return t

t = [1, 2, 3, 4]
print(middle(t))