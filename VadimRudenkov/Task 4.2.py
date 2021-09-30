'''
Task 4.2
Write a function that check whether a string is a palindrome or not.
Usage of any reversing functions is prohibited.
'''


def a_palyndrom(street:str) -> bool:
    street = street.lower().split()
    street = ''.join(street)
    if street == street[::-1]:
        return True
    else:
        return False



