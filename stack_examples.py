"""The examplse in the file comes from the Exercises in Algorithms 4th edition by Robert Sedgewick and Kevin Wayne """

from stack import Stack


def output_string_from_stack(input_str):
    """ Exercise 1.3.2: Given the input string print the output from stack.
    it was - the best - of times - - - it was - the - -"""
    str_list = input_str.split(" ")
    stack = Stack()
    for str in str_list:
        stack.push(str)
    while not stack.is_empty():
        print stack.pop()

def check_balanced_parantheses(par):




def test_stack_examples():
    output_string_from_stack("it was - the best - of times - - - it was - the - -")

if __name__ == '__main__':
    test_stack_examples()
