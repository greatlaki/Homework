''' Task 1.4
Write a Python program to sort a dictionary by key.
Examples:
```
Input: {"b": 9, 10: 10, 9: 9, "c": 7, "a": "7", False: 7}
'''


def main():
    my_dict = {44: 'a',
               33: 'of',
               55: 'poisonous',
               11: 'The',
               66: 'Python',
               22: 'bite',
               }
    asc_dict = dict(sorted(my_dict.items()))
    return asc_dict


if __name__ == "__main__":
    main()

