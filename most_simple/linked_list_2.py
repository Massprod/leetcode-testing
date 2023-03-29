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
    head = l1
    values_l1 = []
    values_l2 = []
    while head:
        val = head.val
        head = head.next
        values_l1.append(val)
    head = l2
    while head:
        val = head.val
        head = head.next
        values_l2.append(val)
    print(values_l1)
    print(values_l2)
    values_l1.reverse()
    values_l2.reverse()
    print(values_l1)
    print(values_l2)
    values_l1 = [str(_) for _ in values_l1]
    values_l2 = [str(_) for _ in values_l2]
    number_1 = int("".join(values_l1))
    number_2 = int("".join(values_l2))
    print(number_1)
    print(number_2)
    number_3 = number_1 + number_2
    print(number_3)
    new_list_value = list(str(number_3))
    new_list_value.reverse()
    print(new_list_value)
    new_list = ListNode(val=new_list_value[0],
                        next=ListNode(val=new_list_value[1],
                                      next=new_list_value[2]))
    print(new_list)







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
