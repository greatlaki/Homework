''' Task 1.2
Write a Python program to count the number of characters (character frequency) in a string
(ignore case of letters).'''

my_input = input('Enter: ')


def char_frequency(something:str) -> dict:
    text = {}
    for char in something:
        if char in text:
            text[char] += 1
        else:
            text[char] = 1
    return text


print(char_frequency(my_input))


