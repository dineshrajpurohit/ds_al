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


def decimal_to_binary(num):
    """ Exercise: 1.3.5 The code given in the exercise is the logic to print binary representation of the decimal number"""
    stack = Stack()
    while num > 0:
        stack.push(num % 2)
        num = num / 2
    binary = ""
    while not stack.is_empty():
        binary += str(stack.pop())
    return binary

def base_conversion(num, base):
    """Extending 1.3.5: More general base conversion. Converts Decimal to Binary, Decimal to Octal and Decimal to Hex"""
    stack = Stack()
    num_str = "0123456789ABCDEF"
    while num > 0:
        stack.push(num % base)
        num = num / base
    conversion = ""
    while not stack.is_empty():
        conversion += num_str[stack.pop()]
    return conversion


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
    print "\n"
    print "Binary representation of 50: ", decimal_to_binary(50)
    print "Binary representation of 275", decimal_to_binary(275)
    print "\n"
    print "Base conversion: To Binary (275): ", base_conversion(233, 2)
    print "Base conversion: To Oct (275): ", base_conversion(233, 8)
    print "Base conversion: To Hex (275): ", base_conversion(233, 16)

if __name__ == '__main__':
    test_stack_examples()

