''' Task 1.6
Write a Python program to convert a given tuple of positive integers into an integer.
Examples:
Input: (1, 2, 3, 4)
Output: 1234
'''

my_input = (1, 2, 3, 4)


def convert_int(something:tuple) -> str:
    convert = ''.join(str(x) for x in something)
    return convert


print(convert_int(my_input))
