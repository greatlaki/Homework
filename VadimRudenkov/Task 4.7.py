'''
Task 4.7
Implement a function foo(List[int]) -> List[int] which, given a list of integers,
return a new list such that each element at index i of the new list is
the product of all the numbers in the original array except the one at i.
'''


def foo(List: int) -> list:
    lst_out = []
    for i in range(len(List)):
        result = 1
        for ind, num in enumerate(List):
            if ind == i:
                continue
            result *= num
        lst_out.append(result)
    return lst_out

