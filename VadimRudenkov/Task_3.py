''' Task 1.3
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
Examples:

Input: ['red', 'white', 'black', 'red', 'green', 'black', 'red']
Output: ['black', 'green', 'red', 'white', 'red']
'''

my_input = input("Enter: ")


def unique_sorted(something:str) -> None:
    words = [word for word in something.split(",")]
    print(",".join(sorted(list(set(words)))))


print(unique_sorted(my_input))

