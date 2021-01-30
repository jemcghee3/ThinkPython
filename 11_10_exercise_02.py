"""Exercise 2

Read the documentation of the dictionary method setdefault and use it to write a more concise version of invert_dict.
Solution: http://thinkpython2.com/code/invert_dict.py.

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


setdefault(key[, default])¶

    If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
"""


def better_invert(d):
    inverse = dict()
    for key in d:
        inverse.setdefault(d[key], []).append([key])
    return inverse

h = {'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}

inverse = better_invert(h)
print(inverse)
