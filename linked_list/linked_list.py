""" Implemenation of Linked List"""


class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __repr__(self):
        return "{} ---> {}".format(self.item, self.next)



