'''
Task 4.4
Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
which splits the `s` string by indexes specified in `indexes`.
Wrong indexes must be ignored.
'''


def split_by_index(s: str, indexes: list) -> list:
    s = s.replace(' ', '')
    result = []
    end_indexes = 0
    for i in indexes:
        result.append(s[end_indexes:i])
        end_indexes = i
    if s[i:]:
        result.append(s[i:])
    return result

