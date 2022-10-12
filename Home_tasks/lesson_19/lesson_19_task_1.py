"""Create your own implementation of a built-in function enumerate,
named `with_index`, which takes two parameters: `iterable` and `start`,
default is 0.

"""


def with_index(iterable_, start=0):
    st = start
    for elem in iterable_:
        yield st, elem
        st += 1


wi = with_index(['a', 'b', 'c', 'd'])
for i in wi:
    print(i)
