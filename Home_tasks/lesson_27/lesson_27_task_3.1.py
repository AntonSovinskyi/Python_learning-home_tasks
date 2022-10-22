"""Extend the Stack to include a method called get_from_stack that
searches and returns an element e from a stack. Any other element
must remain on the stack respecting their order. Consider the case
in which the element is not found - raise ValueError with proper
info Message

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

    def get_from_stack(self, value):
        pos_id = 1
        new_stack = []

        if value not in self._items:
            raise ValueError('This item is not in the list.')

        while self._items[-1] != value:
            new_stack.append(self._items.pop())
        else:
            del self._items[-1]

        pos_id += 1

        for i in new_stack[::-1]:
            self._items.append(i)
        return self._items


s = Stack()

s.push('one')
s.push('two')
s.push('three')
s.push('four')
s.push('five')
print(s.get_from_stack('three'))
