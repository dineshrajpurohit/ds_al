from linked_list import Linked_List, Node

class Stack(Linked_List):

    def __init__(self):
        Linked_List.__init__(self)

    def push(self, item):
        node = Node(item)
        self.insert_front(node)

    def peek(self):
        return self.root

    def pop(self):
        return self.remove_front()

    def size(self):
        return self.count


print "Creating a new stack"
st = Stack()
print "Adding A to the stack"
st.push("A")
print "Adding B to the stack"
st.push("B")
print "Top of the stack: ", st.peek()
print "Adding C to the stack"
st.push("C")
print "Stack uptill now"
print st
print "Popping from stack"
print st.pop().item
print "Top of the stack"
print st
print "Stack Size"
print st.size()