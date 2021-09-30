'''
Task 4.10
Implement a function that takes a number as an argument and returns a dictionary,
where the key is a number and the value is the square of that number.
'''

def gen_squares(num):
    dict = {i: i**2 for i in range(1, num+1)}
    return dict
