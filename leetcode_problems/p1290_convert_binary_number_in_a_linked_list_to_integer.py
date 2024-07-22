# Given head which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.
# The most significant bit is at the head of the linked list.
# -----------------------
# The Linked List is not empty.
# Number of nodes will not exceed 30.
# Each node's value is either 0 or 1.
from utils.linked_list import create_linked, t_linked, ListNode


def get_decimal_value(head: ListNode) -> int:
    # working_sol (73.41%, 89.25%) -> (33ms, 16.36mb)  time: O(n) | space: O(1)
    out: int = 0
    while head:
        out <<= 1
        out += head.val
        head = head.next
    return out


# Time complexity: O(n) <- n - number of Nodes inside the input LinkedList `head`.
# We're always traversing whole input LinkedList `head`, once => O(n).
# -----------------------
# Auxiliary space: O(1).
# Only one constant INT used, doesn't depend on input => O(1).


test: ListNode = create_linked([1, 0, 1])
test_out: int = 5
assert test_out == get_decimal_value(test)

test = create_linked([0])
test_out = 0
assert test_out == get_decimal_value(test)
