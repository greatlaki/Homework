'''
Task 4.11
Implement a function, that receives changeable number of dictionaries
(keys - letters, values - numbers) and combines them into one dictionary.
Dict values should be summarized in case of identical keys
'''


def combines_dicts(*args):
    result_dict = {}
    for arg in args:
        for key, value in arg.items():
            if key not in result_dict:
                result_dict[key] = value
            else:
                result_dict[key] += value
    return result_dict
