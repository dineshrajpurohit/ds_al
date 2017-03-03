""" Implemenation of Linked List"""


class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __repr__(self):
        return "{} ---> {}".format(self.item, self.next)


class Linked_List:

    def __init__(self):
        self.root = None
        self.count = 0

    def size(self):
        return self.count

    # Insertions
    def insert_front(self, node):
        if self.root is None:
            self.root = node
        else:
            node.next = self.root
            self.root = node
        self.count += 1

    def insert_end(self, node):
        pointer = self.root
        if pointer is None:
            self.root = node
        while pointer.next  is not None:
            pointer = pointer.next
        pointer.next = node
        self.count += 1

    def __repr__(self):
        return "Total Nodes: {} Root: {}".format(self.count, self.root)


ll = Linked_List()
print ll
node1 = Node("A", None)
ll.insert_front(node1)
print ll
node2 = Node("B")
ll.insert_front(node2)
print ll
node3 = Node("C")
ll.insert_end(node3)
print ll
