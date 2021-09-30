'''
Task 4.6
Implement a function get_shortest_word(s: str) -> str
which returns the longest word in the given string.
The word can contain any symbols except whitespaces ( , \n, \t and so on).
If there are multiple longest words in the string with a same length return the word that occures first.
'''


def get_shortest_word(s: str) -> str:
    lst = s.split(" ")
    ind_max = 0
    for ind in range(len(lst)):
        if len(lst[ind]) > len(lst[ind_max]):
            ind_max = ind
    return lst[ind_max]


print(get_shortest_word('Python is simple and effective!'))
# 'effective!'
