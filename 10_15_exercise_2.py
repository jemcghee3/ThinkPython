"""Exercise 2

Write a function called cumsum that takes a list of numbers and returns the cumulative sum;
that is, a new list where the ith element is the sum of the first i+1 elements from the original list. For example:

>>t = [1, 2, 3]
>>cumsum(t)
[1, 3, 6]
"""

def sum_so_far(input_list, n): # n is the number of items to sum, not position
    total = 0
    for i in range(n):
        total += input_list[i]
    return total


def cumsum(input_list):
    sum_list = list()
    for n in range(1, len(input_list)+1): # because n is the number of items to sum, not a position
        sum_list.append(sum_so_far(input_list, n))
    return sum_list

t = [1, 2, 3]

print(cumsum(t))