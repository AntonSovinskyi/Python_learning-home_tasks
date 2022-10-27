"""Implement append, index, pop, insert methods for UnorderedList.
Also implement a slice method, which will take two parameters `start`
and `stop`, and return a copy of the list starting at the position
and going up to but not including the stop position.

"""


from node import Node


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def front_insert(self, data):
        node = Node(data)
        node.set_next(self._head)
        self._head = node

    def insert(self, data, position):
        if self._head is not None:
            current = self._head
            for i in range(position - 1):
                current = current.get_next()
            node = Node(data)
            node.set_next(current.get_next())
            current.set_next(node)
        else:
            self._head = Node(data)

    def append(self, data):
        if self._head is not None:
            next_node = self._head
            while next_node is not None:
                previous = next_node
                next_node = next_node.get_next()
            node = Node(data)
            previous.set_next(node)
        else:
            self._head = Node(data)

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def index(self, item):
        current = self._head
        found = False
        count = 0
        while current is not None and not found:
            if current.get_data() != item:
                count += 1
                current = current.get_next()
            else:
                found = True

        if found:
            return count
        else:
            return 'No match.'

    def pop(self):
        current = self._head
        previous = None
        if current is None:
            return "List is empty."

        while current.get_next() is not None:
            previous = current
            current = current.get_next()

        previous.set_next(None)
        return current.get_data()

    def slice(self, start, stop):
        current = self._head
        slice_list = []
        if self._head is None:
            print('The list is empty.')
        else:
            while current is not None:
                slice_list.append(current.get_data())
                current = current.get_next()
        copy_ = slice(start, stop)
        return slice_list[copy_]

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.append(31)
    my_list.append(77)
    my_list.append(17)
    my_list.append(93)
    my_list.append(26)
    my_list.append(54)
    my_list.front_insert(10)
    my_list.insert(20, 3)
    print(f'Size: {my_list.size()}')
    print(f'Search: {my_list.search(17)}')
    print(my_list)
    my_list.remove(26)
    print(f'Remove 26: {my_list}')
    print(f'Index 93: {my_list.index(93)}')
    print(f'Pop: {my_list.pop()}')
    print(my_list)
    print(f'Slice: {my_list.slice(1, 4)}')
