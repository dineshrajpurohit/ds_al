from linked_list import Linked_List, Node
import random


class Bag(Linked_List):

    def __init__(self):
        Linked_List.__init__(self)

    def add(self, item):
        """Stores in a random location in the Linked list"""
        if self.count == 0:
            random_location = 0
        else:
            random_location = random.randint(0, self.count - 1)
        self.insert(Node(item), random_location)

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count


def test_bag():
    print "\n\nBag implementation"
    bag = Bag()
    print "Is Bag empty? ", bag.is_empty()
    bag.add("A")
    bag.add("B")
    bag.add("C")
    bag.add("X")
    print "Is Bag empty? ", bag.is_empty()
    print bag.size()
    print bag

if __name__ == '__main__':
    test_bag()
