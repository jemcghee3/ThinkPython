"""Exercise 4

The following functions are all intended to check whether a string contains any lowercase letters,
but at least some of them are wrong. For each function, describe what the function actually does
(assuming that the parameter is a string).

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
"""


def any_lowercase1(s):
    print('any_lowercase1 takes a string')
    for c in s:
        print('for character in string)')
        if c.islower():
            print('if the character is lower case, return true and end the function.')
            return True
        else:
            print('if the character is not lower case, return false and end the function.')
            return False

def any_lowercase2(s):
    print('any_lowercase2 takes a string')
    for c in s:
        print('for character in string')
        if 'c'.islower():
            print('if the string "c" is lower case (which it is), end the function and return the string "True".')
            return 'True'
        else:
            print('if the string "c" is not lower case (but it is), end the function and return the string "False".')
            return 'False'

def any_lowercase3(s):
    print('any_lowercase3 takes a string')
    for c in s:
        print('for character in string')
        print('pass whether c is lower case to a variable called flag')
        flag = c.islower()
    print('return the variable flag, which will return the value for the last character in the string')
    return flag

def any_lowercase4(s):
    print('any_lowercase4 takes a string')
    print('a variable called "flag" is set to False')
    flag = False
    for c in s:
        print('for character in string')
        flag = flag or c.islower()
        print('flag is set to flag or the truth value of c.islower')
        print('once c.islower is true, flag is true, then flag stays true because true or false is true')
        print(flag)
    return flag

def any_lowercase5(s):
    print('any_lowercase5 takes a string')
    for c in s:
        print('for character in string')
        print('if c is not lower case (first upper case character), return false and end the function')
        if not c.islower():
            return False
    print('if no upper case characters found, return true')
    return True
