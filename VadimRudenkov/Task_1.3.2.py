''' Task 1.4
Create a program that asks the user for a number and then prints out a list
of all the [divisors] of that number.
Examples:

Input: 60
Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
'''


def main():
    my_input = 60
    list_range = list(range(1, my_input + 1))
    divisorList = []
    for number in list_range:
        if my_input % number == 0:
            divisorList.append(number)
    return divisorList


if __name__ == "__main__":
    main()

