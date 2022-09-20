""" Write a function called oops that explicitly raises
 an IndexError exception when called. Then write another
 function that calls oops inside a try/except statement
 to catch the error. What happens if you change oops to
 raise KeyError instead of IndexError?

"""


def oops(list_):
    print(oops)
    list_[4] = 5
    print(oops)


oops([1, 2, 3, 4])


def oops(list_1):
    try:
        list_1[4] = 5
        print(list_1)
    except IndexError:
        print('Index out of range')


oops([1, 2, 3, 4])

# Якщо замість IndexError написати KeyError, то не знайшовши цього виключення
# интерпритатор видасть те виключення, яке знайшов у блоці try.
