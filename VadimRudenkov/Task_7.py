''' Task 1.6
Write a Python program to convert a given tuple of positive integers into an integer.
Examples:
Input: (1, 2, 3, 4)
Output: 1234
'''


def main():
    my_input = (1, 2, 3, 4)
    convert = ''.join(str(x) for x in my_input)
    return convert


if __name__ == "__main__":
    main()