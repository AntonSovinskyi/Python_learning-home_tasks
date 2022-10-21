"""Write a program that reads in a sequence of characters and
prints them in reverse order, using your implementation of Stack.

"""


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def reverse(self):
        return self._items[::-1]


s = Stack()

s.push('one')
s.push('two')
s.push('three')
s.push('four')
s.push('five')
print(s._items)
print(s.reverse())
