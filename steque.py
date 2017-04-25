"""Excercise 1.3.32 Stack ended queue is the datatype that supports \
    push, pop and enqueue. Imeplementation using linked list"""

from __future__ import print_function
from linked_list import Linked_List, Node
import random


class Steque(Linked_List):
    """Steque implementation using Linked List."""

    def __init__(self):
        """Initializing Linked List."""
        Linked_List.__init__(self)

    def push(self, item):
        """Pushing to the from of the Steque."""
        self.insert_front(Node(item))

    def pop(self):
        """Popping from front of Steque."""
        return self.remove_front()

    def enqueue(self, item):
        """Enqueueing to end of Steque."""
        self.insert_end(Node(item))


def test_steque():
    """Testting Steque examples."""
    steque = Steque()
    for _ in range(10):
        steque.push(random.randint(0, 100))
    print(steque)
    print("Pushing in Steque")
    steque.push(77)
    print(steque)
    print("Enqueue to Steque")
    steque.enqueue(99)
    print(steque)
    print("Popping from Steque")
    print(steque.pop())
    print(steque)



if __name__ == '__main__':
    test_steque()
