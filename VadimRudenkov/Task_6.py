'''Task 1.5
Write a Python program to print all unique values of all dictionaries in a list.
Examples:

Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

my_input = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
test_list = [{'gfg' : 1, 'is' : 2}, {'best' : 1, 'for' : 3}, {'CS' : 2}]


def unique_val_dict(something:dict) -> list:
    unique_value = set()
    for dic in something:
        for val in dic.values():
            unique_value.add(val)
    return list(unique_value)

print(f"{unique_val_dict(my_input)} function result")



