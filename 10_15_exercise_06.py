"""Exercise 6

Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams. """



def uses_only(s1, s2):
    for c in s1:
        if c not in s2 or s1.count(c) != s2.count(c):
            return False
    return True


def is_anagram(s1, s2):
    return uses_only(s1, s2) and uses_only(s2, s1)


print(is_anagram('abba', 'baab'))