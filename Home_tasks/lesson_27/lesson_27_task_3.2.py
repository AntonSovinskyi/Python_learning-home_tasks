"""Extend the Queue to include a method called get_from_queue that
searches and returns an element e from a queue. Any other element
must remain in the queue respecting their order. Consider the case
in which the element is not found - raise ValueError with proper
info Message.

"""


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def size(self):
        return len(self._items)

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        return self._items.pop(0)

    def front(self):
        if self._items:
            return self._items[0]
        else:
            return None

    def rear(self):
        try:
            return self._items[-1]
        except IndexError:
            return None

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def get_from_queue(self, value):
        pos_id = 1
        new_queue = []

        if value not in self._items:
            raise ValueError('This item is not in the list.')

        while self._items[0] != value:
            new_queue.append(self._items.pop(0))
        else:
            del self._items[0]

        pos_id += 1

        for i in new_queue[::-1]:
            self._items.insert(0, i)
        return self._items


if __name__ == "__main__":
    q = Queue()
    q.enqueue('one')
    q.enqueue('two')
    q.enqueue('three')
    q.enqueue('four')
    q.enqueue('five')
    print(q.get_from_queue('four'))
