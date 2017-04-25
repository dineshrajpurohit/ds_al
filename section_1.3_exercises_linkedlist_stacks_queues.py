"""Stack, Queue and Linked list Examples.

The example in the file are from the Exercises from section 1.3 in
Algorithms 4th edition by Robert Sedgewick and Kevin Wayne
"""

from __future__ import print_function
from builtins import input
import random
from linked_list import Linked_List, Node
from stack import Stack
from queue import Queue
from steque import Steque


def output_string_from_stack(input_str):
    """Exercise 1.3.2.

    Given the input string print(the output
    from stack. it was - the best - of times - - - it was - the - -
    """
    str_list = input_str.split(" ")
    stack = Stack()
    for str in str_list:
        stack.push(str)
    while not stack.is_empty():
        print(stack.pop())


def check_balanced_parantheses(par_str):
    """Exercise: 1.3.4.

    Check for balanced paranthesis:
    return True for [()]{}{[()()]()} and False for [(])
    """
    stack = Stack()
    par_dict = {"}": "{", "]": "[", ")": "("}
    for par in par_str:
        if par in par_dict:
            item = stack.pop()
            if item != par_dict.get(par):
                return False
        else:
            stack.push(par)
    if stack.is_empty():
        return True
    else:
        return False


def decimal_to_binary(num):
    """Exercise: 1.3.5.

     The code given in the exercise is the logic
    to print binary representation of the decimal number
    """
    stack = Stack()
    while num > 0:
        stack.push(num % 2)
        num = num // 2
    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())
    return binary


def base_conversion(num, base):
    """Extending 1.3.5.

    More general base conversion. Converts Decimal to Binary,
    Decimal to Octal and Decimal to Hex
    """
    stack = Stack()
    num_str = "0123456789ABCDEF"
    while num > 0:
        stack.push(num % base)
        num = num // base
    conversion = ""
    while not stack.is_empty():
        print(stack.peek())
        conversion += num_str[stack.pop()]
    return conversion


def insert_left_paranthesis(expr):
    """Exercise 1.3.9.

    Given an expression without left parenthesis,
    output the expression with left paranthesis inserted
        Input:
            1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )
        Output
            ( ( 1 + 2 ) * ( ( 3 - 4 ) * ( 5 - 6 ) )
    """
    pass


def infix_to_postfix(expr):
    """Exercise 1.3.10.

    Given an infix expression convert it into postfix
         infix expression     postfix expression
          A + B * C            A B C * +
          A * B - C            A B * C -
         (A + B) * C           A B + C *
         (A + B) * (C + D)     A B + C D + *
         A + B + C + D         A B + C + D +

        # Rules for converting infix to postfix
        #   - If val is operand move to end of the output list
        #   - if val is '(' operator push to the stack
        #   - If val is ')' pop all operator from stack until we get
        #   '(' and add them to end of the output list
        #   - If val is *, +, -, / compare with the top of stack
        #       - if the val has higher precedence push to stack
        #       - if the val had lower precedence continously pop all
        #           operator with higher precedence
        #           and add it to the end of the output list
    """
    expr = expr.split(" ")
    stack = Stack()
    postfix_list = []
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    for ch in expr:
        # If ch is operand we move it to the list
        if ch not in "()*+-/^":
            postfix_list.append(ch)
        elif ch == '(':
            stack.push(ch)
        elif ch == ")":
            item = stack.pop()
            while item != "(":
                postfix_list.append(item)
                item = stack.pop()
        else:
            item = stack.peek()
            while not stack.is_empty() and precedence[item] >= precedence[ch]:
                item = stack.pop()
                postfix_list.append(item)
            stack.push(ch)
    while not stack.is_empty():
        postfix_list.append(stack.pop())
    return postfix_list


def evaluate_expr(op1, op2, operator):
    """Operation helper function.

    Assuming the only operation we will do is addition, substration,
    multiplication and division
    """
    if operator == '*':
        return op1 * op2
    elif operator == "/":
        return op1 / op2
    elif operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2
    elif operator == "%":
        return op1 % op2


def evaluate_postfix(expr):
    """Exercise 1.3.11.

    Evaluate the given the postfix expression
    """
    stack = Stack()
    for ex in expr:
        if ex not in "-+*/%":
            stack.push(int(ex))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.push(evaluate_expr(operand1, operand2, ex))
    return stack.pop()


class StackClient(Stack):
    def __init__(self):
        pass

    @staticmethod
    def copy(self, stack):
        pass

    def __iter__(self):
        pass


def stack_client():
    """Excercise 1.3.12.

    Iterable stack client which implement static method copy which
    returns the copy of the stack which was supplied as an argument.
    """
    client = StackClient()
    stack = Stack()
    stack.push("A")
    stack.push("B")
    stack.push("C")

    print(client.copy(stack))


def read_dates():
    """Excercise 1.3.16.

    Based on readInt method on page 126 of the book create a similar
    function which takes dates from the input and returns array
    of dates.
    """
    date_queue = Queue()
    input_date = input("Enter Date format(mm/dd/yyyy): ")
    while input_date:
        date_queue.enqueue(input_date)
        input_date = raw_input("Enter Date format(mm/dd/yyyy): ")
    date_list = []
    while not date_queue.is_empty():
        date_list.append(date_queue.dequeue())
    return date_list


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
    remove all occurence of the item
    """
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
    """Excercise 1.3.28 Find max in linked list recursively."""
    if head is None:
        return max
    if head.item > max:
        max = head.item
    head = head.next
    return max_recur(head, max)


def queue_with_circular_linked_list():
    """Excercise 1.3.29 Create an implementation of a Queue using a
        circular linked list."""
    pass


def reverse_linked_list(head):
    """Excercise 1.3.30 reverse a linked list."""
    linked_list_rev = Linked_List()
    stack = Stack()
    current_node = head
    while current_node is not None:
        stack.push(current_node.item)
        current_node = current_node.next
    while not stack.is_empty():
        item = stack.pop()
        linked_list_rev.insert_end(Node(item))
    return linked_list_rev.root


def reverse_linked_list_recursive(head):
    """Excercise 1.3.30 Recursively reverese a linked list."""
    if head is None:
        return
    if head.next is None:
        return head
    second = head.next
    rest = reverse_linked_list_recursive(second)
    second.next = head
    head.next = None
    return rest


def test_stack_examples():
    """Testing Stack Examples."""
    print("Output string from stack (reverser)")
    print("it was - the best - of times - - - it was - the - -")
    output_string_from_stack("it was - the best - of times - - -\
     it was - the - -")
    print("\n")
    print("Valid Paranthesis", check_balanced_parantheses("[()]{}{[()()]()}"))
    print("Invalid Paranthesis", check_balanced_parantheses("[(])"))
    print("Valid Paranthesis:", check_balanced_parantheses("{{([][])}()}"))
    print("Valid Paranthesis: ", check_balanced_parantheses(""))
    print("Invalid Paranthesis", check_balanced_parantheses("[{()]"))
    print("\n")
    print("Binary representation of 50: ", decimal_to_binary(50))
    print("Binary representation of 275", decimal_to_binary(275))
    print("\n")
    print("Base conversion: To Binary (275): ", base_conversion(233, 2))
    print("Base conversion: To Oct (275): ", base_conversion(233, 8))
    print("Base conversion: To Hex (275): ", base_conversion(233, 16))
    print("\n")
    print("Testing Infix to Postfix conversion")
    print("Infix: A*B-C Postfix:", infix_to_postfix("A * B - C"))
    print("Infix: (A+B)*(C+D) Postfix:")
    print(infix_to_postfix("( A + B ) * ( C + D )"))
    # print("Infix: 1+2)*3-4)*5-6))) Postfix:",\
    # infix_to_postfix("1+2)*3-4)*5-6)))")
    print("\n")
    print("Evaluating Postfix expression: 2+3*5: ")
    print(evaluate_postfix(infix_to_postfix("2 + 3 * 5")))
    print("Evaluating Postfix expression: (25+30)*(30+10): ")
    print(evaluate_postfix(infix_to_postfix("( 25 + 30 ) * ( 30 + 10 )")))
    print("\n")


def test_queue_example():
    """Testing Queue Examples."""
    print("Exercise 1.3.16 Date Queue: ")
    print(read_dates())
    print("\n")


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
    print("\n")
    print("Destructively reverse a linked list")
    print("Current Linked list")
    print(ll_nums)
    print("Reverse linked list")
    print(reverse_linked_list(ll_nums.root))
    print("Reverse linked list recursively")
    print(reverse_linked_list_recursive((ll_nums.root)))


if __name__ == '__main__':
    test_stack_examples()
    #test_queue_example()
    test_linked_list_examples()
