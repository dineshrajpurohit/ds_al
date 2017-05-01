"""Excercise 1.3.33 Deque: a doublie ended queue which allows adding
    and removing items from both end."""

from linked_list import Linked_List, Node
import random


class Deque(Linked_List):
    """Deque implementation using linked list."""

    def __init__(self):
        """Initialize the linked list."""
        Linked_List.__init__(self)

    def is_empty(self):
        """Check whether the deque is empty by checking the linked list
         has 0 items/node."""
        return self.count == 0

    def size(self):
        """Return the total nodes in the linked list."""
        return self.count

    def push_left(self, item):
        """Insert node to the start of the linked list."""
        self.insert_front(Node(item))

    def push_right(self, item):
        """Insert node to the end of the linked list."""
        self.insert_end(Node(item))

    def pop_left(self):
        """Remove the first element of the linked list."""
        return self.remove_front()

    def pop_right(self):
        """Remove the last element of the linked list."""
        return self.remove_end()


def test_deque():
    """Testing Deque implementation."""
    deque = Deque()
    print("Deque empty? ", deque.is_empty())
    for _ in range(10):
        deque.push_left(random.randint(0, 100))
    for _ in range(10):
        deque.push_right(random.randint(0, 100))
    print("Deque empty? ", deque.is_empty())
    print("Testing push left: 77")
    deque.push_left(77)
    print(deque)
    print("Testing push right: 44")
    deque.push_right(44)
    print(deque)
    print("Testing pop left")
    print(deque.pop_left())
    print("Testing pop right")
    print(deque.pop_right())
    print('Deque size: ', deque.size())


if __name__ == '__main__':
    test_deque()
