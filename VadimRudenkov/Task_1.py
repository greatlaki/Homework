''' Task 1.1
Write a Python program to calculate the length of a string without using the `len` function.
'''

my_input = input('Enter: ')


def calculate_len(something:str) -> int:
    counter = 0
    for i in something:
        counter += 1
    return counter


print(calculate_len(my_input))
