"""Write a Python program to detect the number of local
variables declared in a function.

"""


def num_loc_var():
    num_ = 1
    float_ = 5,25
    str_ = 'GeeksForGeeks'
    list_ = [1, 2, 3, 4]

print(num_loc_var.__code__.co_nlocals)
