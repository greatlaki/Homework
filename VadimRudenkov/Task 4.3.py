'''
Task 4.3
Implement a function which works the same as str.split method
(without using str.split itself, ofcourse).
'''


def as_split(street: str, m=" ") -> list:
    list_split = []
    count = 0
    for i in range(len(street)):
        if street[i] == m:
            list_split.append(street[count:i])
            count = i+1
    list_split.append(street[count:])
    return list_split


