"""Create your own implementation of a built-in function range,
named in_range(), which takes three parameters: `start`, `end`,
and optional step.

"""


def in_range(start, end, step):
    if step is None and end is None:
        start, end, step = 0, start, 1
        while start < end:
            yield start
            start += step
    elif end is None:
        start, end, step = start, step, 1
        while start < end:
            yield start
            start += step
    while start < end:
        yield start
        start += step


a = in_range(11, 44, 4)

for i in a:
    print(i)
