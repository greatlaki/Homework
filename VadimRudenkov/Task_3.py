''' Task 1.3
Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
Examples:

Input: ['red', 'white', 'black', 'red', 'green', 'black', 'red']
Output: ['black', 'green', 'red', 'white', 'red']
'''


def main():
    my_input = 'red, white, black, red, green, black, red'
    words = [word for word in my_input.split(",")]
    print(",".join(sorted(list(set(words)))))


if __name__ == "__main__":
    main()
