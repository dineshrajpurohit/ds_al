"""Queue Examples.

The example in the file are from the Exercises in
Algorithms 4th edition by Robert Sedgewick and Kevin Wayne
"""

from queue import Queue
import re

def read_dates():
    """Excercise 1.3.16.

    Based on readInt method on page 126 of the book create a similar
    function which takes dates from the input and returns array
    of dates.
    """
    date_queue = Queue()
    input_date = raw_input("Enter Date format(mm/dd/yyyy): ")
    while input_date:
        date_queue.enqueue(input_date)
        input_date = raw_input("Enter Date format(mm/dd/yyyy): ")
    date_list = []
    while not date_queue.is_empty():
        date_list.append(date_queue.dequeue())
    return date_list


def test_queue_example():
    """Testing Queue Examples."""
    print "Exercise 1.3.16 Date Queue: "
    print read_dates()
    print "\n"


if __name__ == '__main__':
    test_queue_example()
