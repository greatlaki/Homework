''' Task 1.4
Write a Python program to sort a dictionary by key.
'''

my_dict = {44: 'a',
           33: 'of',
           55: 'poisonous',
           11:'The',
           66: 'Python',
           22:'bite',
           }


def sort_dict(something:dict) -> dict:
    asc_dict = dict(sorted(my_dict.items()))
    return asc_dict

print(sort_dict(my_dict))