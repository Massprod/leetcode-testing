# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"[{self.val}] -> {self.next}"

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode] = None) -> Optional[ListNode]:
    print(l1)
    print(l2)










val1 = 2
val2 = 4
val3 = 3
val11 = 5
val22 = 6
val33 = 4

l1 = ListNode(val=val1,
              next=ListNode(val2,
                            next=ListNode(val3)
                            )
              )
l2 = ListNode(val=val11,
              next=ListNode(val22,
                            next=ListNode(val33)
                            )
              )


add_two_numbers(l1, l2)
