"""Queue implementation using Linked list."""

from __future__ import print_function
from linked_list import Linked_List, Node


class Queue(Linked_List):

    def __init__(self):
        Linked_List.__init__(self)

    def enqueue(self, item):
        node = Node(item)
        self.insert_front(node)

    def dequeue(self):
        return self.remove_end()

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count


def test_queue():
    print("\n\n QUEUE TESTING")
    queue = Queue()
    print("Queue Empty?", queue.is_empty())
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    print("Queue Size:", queue.size())
    print(queue)
    print("DEQUEUEING 1")
    print(queue.dequeue())
    print(queue)
    print("Queue Size:", queue.size())
    print("DEQUEUEING 2")
    print(queue.dequeue())
    print(queue)
    print("Queue Size:", queue.size())
    print("Queue Empty?", queue.is_empty())
    print("DEQUEUEING 3")
    print(queue.dequeue())
    print(queue)
    print("Queue Size:", queue.size())
    print("Queue Empty?", queue.is_empty())
    print(queue)
    print("DEQUEUEING 4")
    print(queue.dequeue())

if __name__ == '__main__':
    test_queue()
