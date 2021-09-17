''' Task 1.4
Create a program that asks the user for a number and then prints out a list
of all the [divisors] of that number.
Examples:

Input: 60
Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
'''

my_input = int(input("Enter: "))


def divisor_list(something:int) -> list:
    list_range = list(range(1, something + 1))
    divisorList = []
    for number in listRange:
        if something % number == 0:
            divisorList.append(number)
    return divisorList


print(divisor_list(my_input))