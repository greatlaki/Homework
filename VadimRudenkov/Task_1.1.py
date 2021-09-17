''' Task 1.1
Write a Python program to calculate the length of a string without using the `len` function.
Examples:

Input: Oh, it is python
Output: 16
'''

def main():
    my_input = 'Oh, it is python'
    counter = 0
    for i in my_input:
        counter += 1
    return counter

if __name__ == "__main__":
    main()
