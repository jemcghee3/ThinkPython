"""Exercise 5

Two words are “rotate pairs” if you can rotate one of them and get the other (see rotate_word in Exercise 5).

Write a program that reads a wordlist and finds all the rotate pairs.
Solution: http://thinkpython2.com/code/rotate_pairs.py."""


def data(file):
    fin = open(file)
    raw_data = dict()
    for line in fin:
        line = line.rstrip()
        raw_data.setdefault(line, None)
    return raw_data


def rotate(num, n):
    return num + n


def too_low(n):
    return n + 26


def too_high(n):
    return n - 26


def upper_wrap(n):
    if n < 65:
        return too_low(n)
    elif n > 90:
        return too_high(n)
    else:
        return n


def lower_wrap(n):
    if n < 97:
        return too_low(n)
    elif n > 122:
        return too_high(n)
    else:
        return n


def upper_caesar(num, n):
    num = rotate(num, n)
    num = upper_wrap(num)
    return chr(num)


def lower_caesar(num, n):
    num = rotate(num, n)
    num = lower_wrap(num)
    return chr(num)


def rotate_word(s, n):
    new_word = ''
    for c in s:
        if not c.isalpha():
            new_word += c
            continue
        num = ord(c)
        if 65 <= num <= 90:
            num = upper_caesar(num, n)
        elif 97 <= num <= 122:
            num = lower_caesar(num, n)
        else:
            print('something went wrong')
        new_word += num
    return new_word


def find_all_rotate_pairs(d):
    rotated_list = list()
    for word in d:
        for i in range(1, 14):  # will rotate 13 times to get each pair just once instead of twice
            rotated_word = rotate_word(word, i)
            if rotated_word in d:
                rotated_list.append((word, rotated_word))
    print(rotated_list)
    print(len(rotated_list))


word_dict = data('words.txt')

find_all_rotate_pairs(word_dict)
