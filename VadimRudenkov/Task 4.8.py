'''
Task 4.8
Implement a function get_pairs(lst: List) -> List[Tuple] which returns
 a list of tuples containing pairs of elements. Pairs should be formed as in the example.
If there is only one element in the list return None instead.
'''


def get_pairs(lst: List) -> list[Tuple]:
    lst_out = []
    first_num = lst[0]
    for num in lst[1:]:
        lst_out.append((first_num, num))
        first_num = num
    return lst_out