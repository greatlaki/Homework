'''
Task 4.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa.
'''


def re_quotes(street: str) -> str:
    result = ""
    for char in street:
        if char == "\"":
            result += "\'"
        elif char == "\'":
            result += "\""
        else:
            result += char
    return result

