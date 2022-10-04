"""Implement a class Mathematician which is a helper
class for doing math operations on lists

"""


class Mathematician:
    def square_nums(self, list_1):
        squares_list = [x**2 for x in list_1]
        return squares_list

    def remove_positives(self, list_2):
        for i in list_2:
            if i > 0:
                list_2.remove(i)
        return list_2

    def filter_leaps(self, list_3):
        list_4 = []
        for i in list_3:
            if i % 4 == 0:
                list_4.append(i)
        return list_4


m = Mathematician()

m.square_nums([7, 11, 5, 4])
m.remove_positives([26, -11, -8, 13, -90])
m.filter_leaps([2001, 1884, 1995, 2003, 2020])

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
