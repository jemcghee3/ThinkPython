"""Exercise 9

Write a function that reads the file words.txt and builds a list with one element per word.
Write two versions of this function, one using the append method and the other using the idiom t = t + [x].
Which one takes longer to run? Why?

Solution: http://thinkpython2.com/code/wordlist.py. """


def list_builder2():
    t = list()
    fin = open('words.txt')
    for line in fin:
        line = line.rstrip()
        t.append(line)
    print('list_builder2 done!')


def list_builder1():
    t = list()
    fin = open('words.txt')
    for line in fin:
        line = line.rstrip()
        t = t + [line]
    print('list_builder1 done!')

list_builder2()
list_builder1()

"""the t = t + [x] method is a lot longer, presumably becauseit makes a new list each time instead
of just adding to an existing list"""
