'''Task 1.5
Write a Python program to print all unique values of all dictionaries in a list.
Examples:

Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''


def main():
    my_input = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                {"VIII": "S007"}]
    unique_value = set()
    for dic in my_input:
        for val in dic.values():
            unique_value.add(val)
    return list(unique_value)


if __name__ == "__main__":
    main()


