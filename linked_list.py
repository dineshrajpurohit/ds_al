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

    def insert(self, node, index=0):
        if self.root is None:
            self.root = node
        elif index == 0:
            node.next = self.root
            self.root = node
        elif index >= self.count:
            print "Index out of bound"
            return
        else:
            prev_pointer = None
            pointer = self.root
            counter = 0
            while pointer.next is not None and counter < index:
                prev_pointer = pointer
                pointer = pointer.next
                counter += 1
            if index == counter:
                node.next = prev_pointer.next
                prev_pointer.next = node
        self.count += 1

# Removing nodes
    def remove_front(self):
        if self.root is None:
            return
        next_node = self.root.next
        self.root = next_node
        self.count -= 1

    def remove_end(self):
        if self.root is None:
            return
        pointer = self.root
        prev_pointer = None
        while pointer.next is not None:
            prev_pointer = pointer
            pointer = pointer.next
        if prev_pointer is None:
            self.root = None
        else:
            prev_pointer.next = None
        self.count -= 1

    def remove(self, index=0):
        if self.root is None or index >= self.count:
            print "Index out of bound"
            return
        if index == 0:
            self.root = self.root.next
            self.count -= 1
        else:
            pointer = self.root
            pointer_prev = None
            counter = 0
            while pointer.next is not None and counter < index:
                counter += 1
                pointer_prev = pointer
                pointer = pointer.next
            if counter > index:
                return None
            else:
                pointer_prev.next = pointer.next
                self.count -= 1


    def remove_item(self, item):
        item_index = self.find(item)
        if item_index is not None:
            self.remove(item_index)

    # returns the index where the item is found
    def find(self, item):
        if self.root is None:
            return None
        if self.root.item == item:
            return 0
        pointer = self.root
        counter = 0
        while pointer.next is not None:
            pointer = pointer.next
            counter += 1
            if pointer.item == item:
                return counter
        else:
            return None

    def __repr__(self):
        return "Total Nodes: {} Root: {}".format(self.count, self.root)


ll = Linked_List()
print "*** Removing from end ***"
ll.remove_end()
print ll
node1 = Node("A", None)
ll.insert_front(node1)
print ll
print "*** Removing from end ***"
ll.remove_end()
print ll
node2 = Node("B", None)
node3 = Node('C')
ll.insert_front(node2)
print ll
ll.insert_end(node3)
print ll
ll.insert_end(Node("k"))
print ll
print "*** Removing from front ***"
ll.remove_front()
print ll
ll.insert_front(Node("M"))
print ll
ll.insert(Node("P"), index=2)
print ll
ll.insert(Node("X"))
print ll
print "*** Removing from end ***"
ll.remove_end()
print ll
ll.insert(Node("L"), 3)
print ll
ll.remove()
print "Finding L in the List:"
print ll.find("L")
print "Finding non existing Node item: G"
print ll.find("G")
print "Removing from index 2"
print ll
print ll.remove(2)
print ll
print "Removing from index 0"
print ll.remove(0)
print ll
print "Removing item P"
ll.remove_item("P")
print ll
