"""Linked List Examples.

The example in the file are from the Exercises in
Algorithms 4th edition by Robert Sedgewick and Kevin Wayne
"""


from linked_list import Linked_List, Node
import random


def delete(k):
    """Exercise 1.3.20 Delete the kth element in the linked list.

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
    print("Current Linked List ", linked_list)
    print("Removing kth: ", k, " Item:", linked_list.remove(k - 1))
    print("Updated Linked List ", linked_list)


def find(linked_list, item):
    """Excercise 1.3.21 Find function to find if item exist in linked list.

    The find function takes linked list and item and returns true if exist
    false otherwise

    The linked list implementation already has a find method which can
    be used to utilize this.
    """
    if linked_list.find(item) is not None:
        return True
    else:
        return False


def remove_after(linked_list, node=None):
    """Excercise 1.3.24 Takes a node and removes the following node.

    Takes node and removes the next node if the argument or next field in
    the argument node is null
    We can use linked list find method in combination with remove method
    in order to remove the next node if it exist
    """
    if node.item is not None:
        found = linked_list.find(node.item)
        if found is not None:
            linked_list.remove(found + 1)


def insert_after(linked_list, node1, node2):
    """Exercise 1.3.25 Takes 2 nodes and insert second after the first.

    We can utilize linked list find  method and insert method to insert
    the node after the found node
    """
    if node1.item is not None and node2.item is not None:
        found = linked_list.find(node1.item)
        if found is not None:
            linked_list.insert(node2, found + 1)


def remove(linked_list, item):
    """Excerside 1.3.26 Remove function to remove all node with the item.

    we can utilize the linked list find method along with remove to
    remove all occurence of the item"""
    item_location = linked_list.find(item)
    while item_location is not None:
        linked_list.remove(item_location)
        item_location = linked_list.find(item)


def max(linked_list):
    """Excercise 1.3.27 Find max in linked list."""
    head = linked_list.root
    if head is None:
        return
    current_node = head
    max = 0
    while current_node is not None:
        if current_node.item > max:
            max = current_node.item
        current_node = current_node.next
    return max


def max_recur(head, max):
    """Excercise 1.3.28 Find max in linked list recursively"""
    if head is None:
        return max
    if head.item > max:
        max = head.item
    head = head.next
    return max_recur(head, max)


def test_linked_list_examples():
    """Testing Linkedlist examples."""
    delete(3)
    delete(1)
    print("Find function implementation")
    ll = Linked_List()
    ll.insert_front(Node("A", None))
    ll.insert_front(Node("B", None))
    ll.insert_end(Node('C'))
    ll.insert_end(Node("K"))
    ll.insert_front(Node("M"))
    ll.insert(Node("P"), index=2)
    ll.insert(Node("X"))
    print("Current Linked List ")
    print(ll)
    print("Find C in linked list")
    print(find(ll, "C"))
    print("Find R in linked list")
    print(find(ll, "R"))
    print("Removing next to Node C")
    remove_after(ll, Node("C"))
    print(ll)
    print("Removing next Node to Node C")
    print(ll)
    print("Inserting node L after C")
    insert_after(ll, Node("C"), Node("L"))
    print(ll)
    print("Inserting node U after B")
    insert_after(ll, Node("B"), Node("U"))
    print(ll)
    ll.insert_front(Node('A'))
    print(ll)
    ll.insert(Node('A'), 3)
    print(ll)
    print("Removing all occurance of 'A' from the linked_list")
    remove(ll, 'A')
    print(ll)
    ll_nums = Linked_List()
    for _ in range(20):
        rand_num = random.randrange(1, 100)
        ll_nums.insert_front(Node(rand_num))
    print(ll_nums)
    print('MAX: ', max(ll_nums))
    print('MAX Recur: ', max_recur(ll_nums.root, 0))


if __name__ == "__main__":
    test_linked_list_examples()

