"""Implement binary search using recursion."""


def binary_search(search_list, first, last, element):
    if last >= first:
        middle = (last + first) // 2
        if search_list[middle] == element:
            return middle
        elif search_list[middle] > element:
            return binary_search(search_list, first, middle - 1, element)
        else:
            return binary_search(search_list, middle + 1, last, element)
    else:
        return -1


search_list = [3, 7, 9, 14, 21, 22, 54, 70, 99]
element = 21

result = binary_search(search_list, 0, len(search_list) - 1, element)

if result != -1:
    print("Index element: ", str(result))
else:
    print("Element not in the list!")
