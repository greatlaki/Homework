'''
Task 4.5
Implement a function get_digits(num: int) -> Tuple[int]
which returns a tuple of a given integer's digits.
'''


def get_digits(num: int) -> tuple:
    result = []
    for i in str(num):
        result.append(int(i))
    return tuple(result)
