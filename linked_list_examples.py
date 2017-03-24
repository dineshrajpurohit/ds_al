"""Linked List Examples.

The example in the file are from the Exercises in
Algorithms 4th edition by Robert Sedgewick and Kevin Wayne
"""


from linked_list import Linked_List, Node


def delete(k):
    """Exercise 1.3.10 Delete the kth element in the linked list

    The delete() function takes k as an Integer and deletes the kth
    element in the Linked List.
    Solution:
    The implementation has already been done as part of Linked List
    code.
        method:
        remove(self, index=0)
    """
    linked_list = Linked_List()
    linked_list.insert(Node(1))
    linked_list.insert(Node(2))
    linked_list.insert(Node(3))
    linked_list.insert(Node(4))
    print "Current Linked List ", linked_list
    print "Removing kth: ", k, " Item:", linked_list.remove(k - 1)
    print "Updated Linked List ", linked_list


def test_linked_list_examples():
    """Testing Linkedlist examples"""
    delete(3)
    delete(1)


if __name__ == "__main__":
    test_linked_list_examples()

