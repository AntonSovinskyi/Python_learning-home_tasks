"""Implement a stack using a singly linked list."""


class Node:
    def __init__(self, data):
        self.data = data
        self._next = None


class UnorderedListStack:
    def __init__(self):
        self._head = None
        self.size = 0

    def is_empty(self):
        return self._head is None

    def push(self, item):
        if self._head is None:
            self._head = Node(item)
        else:
            new_node = Node(item)
            new_node.next = self._head
            self._head = new_node

    def pop(self):
        if self._head is None:
            return None
        else:
            popped_node = self._head
            self._head = self._head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self._head is None:
            return None
        else:
            return self._head.data


if __name__ == "__main__":
    s = UnorderedListStack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s.is_empty())
    print(s.pop())
    print(s.peek())
