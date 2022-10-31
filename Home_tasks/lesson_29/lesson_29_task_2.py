"""Read about the Fibonacci search and implement it using python.
Explore its complexity and compare it to sequential, binary searches.

"""


def fibonacci_search(search_list, item):
    size_list = len(search_list)
    start = -1

    pos0 = 0
    pos1 = 1
    pos2 = 1
    while pos2 < size_list:
        pos0 = pos1
        pos1 = pos2
        pos2 = pos1 + pos0

    while pos2 > 1:
        index = min(start + pos0, size_list - 1)
        if search_list[index] < item:
            pos2 = pos1
            pos1 = pos0
            pos0 = pos2 - pos1
            start = index
        elif search_list[index] > item:
            pos2 = pos0
            pos1 = pos1 - pos0
            pos0 = pos2 - pos1
        else:
            return index
    if pos1 and (search_list[size_list - 1] == item):
        return size_list - 1
    return None


search_list = [0, 1, 2, 3, 4, 10, 15, 17, 22, 37]

print(fibonacci_search(search_list, 37))
