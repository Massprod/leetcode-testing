# Given the head of a linked list head, in which each node contains an integer value.
# Between every pair of adjacent nodes,
#  insert a new node with a value equal to the greatest common divisor of them.
# Return the linked list after insertion.
# The greatest common divisor of two numbers is the largest positive integer
#  that evenly divides both numbers.
# -----------------------
# The number of nodes in the list is in the range [1, 5000].
# 1 <= Node.val <= 1000
from random import randint
from utils.linked_list import create_linked, t_linked, ListNode


def insert_gcd(head: ListNode) -> ListNode:
    # working_sol (97.49%, 37.02%) -> (56ms, 19.68mb)  time: O(n) | space: O(n)
    if not head:
        return head

    def gcd(higher: int, lower: int):
        if 0 == lower:
            return higher
        return gcd(lower, higher % lower)

    prev_node: ListNode = head
    cur_node: ListNode = head.next
    while cur_node:
        new_node: ListNode = ListNode(gcd(prev_node.val, cur_node.val))
        prev_node.next, new_node.next = new_node, cur_node
        prev_node, cur_node = cur_node, cur_node.next
    return head


# Time complexity: O(n) <- n - number of Nodes inside the input LinkedList `head`.
# Always using every Node of the `head` and calc `gcd` of them => O(n).
# -----------------------
# Auxiliary space: O(n)
# In the worst case there's EVEN number of odds, and we will create `n // 2` new Nodes => O(n // 2).


test: ListNode = create_linked([18, 6, 10, 3])
test_out: ListNode = create_linked([18, 6, 6, 2, 10, 1, 3])
t_linked(insert_gcd(test), test_out)

test = create_linked([7])
test_out = create_linked([7])
t_linked(insert_gcd(test), test_out)

test_leet: list[int] = [randint(1, 1000) for _ in range(5000)]
print(test_leet)
