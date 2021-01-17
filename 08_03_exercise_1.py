"""As an exercise, write a function that takes a string as an argument and displays the letters backward,
one per line."""

def reverse(string):
    l = len(string)
    i = -1
    while abs(i) <= l:
        print(string[i])
        i -= 1

reverse('test')