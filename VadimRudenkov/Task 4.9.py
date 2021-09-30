'''
Task 4.9
Implement a bunch of functions which receive a changeable number of strings and return next parameters:

    characters that appear in all strings

    characters that appear in at least one string

    characters that appear at least in two strings

    characters of alphabet, that were not used in any string

'''


import string
test_strings = ["hello", "world", "python"]

def test_1_1(*strings):
    result = set()
    for char in strings[0]:
        flags = []
        for string in strings:
            if char in string:
                flag = True
            else:
                flag = False
            flags.append(flag)
        if all(flags):
            result.add(char)
    return result


def test_1_2(*strings):
    result = set()
    for string in strings:
        for char in string:
            result.add(char)
    return result


def test_1_3(*strings):
    result = set()
    for char in strings[0]:
        flags = []
        for string in strings:
            if char in string:
                flag = True
            else:
                flag = False
            flags.append(flag)
        if flags.count(True) >= 2:
            result.add(char)
    return result



def test_1_4(*strings):
    alph = list(string.ascii_lowercase)
    for word in strings:
        for char in word:
            if char in alph:
                alph.remove(char)
    return set(alph)

