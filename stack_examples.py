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

def check_balanced_parantheses(par_str):
    """ Exercise: 1.3.4 Check for balanced paranthesis:
        return True for [()]{}{[()()]()} and False for [(])"""
    stack = Stack()
    par_dict = {"}": "{", "]": "[", ")": "("}
    for par in par_str:
        if par_dict.has_key(par):
            item = stack.pop()
            if item != par_dict.get(par):
                return False
        else:
            stack.push(par)
    if stack.is_empty():
        return True
    else:
        return False



def test_stack_examples():
    print "Output string from stack (reverser)"
    print "it was - the best - of times - - - it was - the - -"
    output_string_from_stack("it was - the best - of times - - - it was - the - -")
    print "\n"
    print "Valid Paranthesis", check_balanced_parantheses("[()]{}{[()()]()}")
    print "Invalid Paranthesis", check_balanced_parantheses("[(])")
    print "Valid Paranthesis:", check_balanced_parantheses("{{([][])}()}")
    print "Valid Paranthesis: ", check_balanced_parantheses("")
    print "Invalid Paranthesis", check_balanced_parantheses("[{()]")

if __name__ == '__main__':
    test_stack_examples()

