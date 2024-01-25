# There is a singly-linked list head and we want to delete a node node in it.
# You are given the node to be deleted node. You will not be given access to the first node of head.
# All the values of the linked list are unique,
#  and it is guaranteed that the given node node is not the last node in the linked list.
# Delete the given node.
# Note that by deleting the node, we do not mean removing it from memory. We mean:
#  - The value of the given node should not exist in the linked list.
#  - The number of nodes in the linked list should decrease by one.
#  - All the values before node should be in the same order.
#  - All the values after node should be in the same order.
# ------------------
# The number of the nodes in the given list is in the range [2, 1000].
# -1000 <= Node.val <= 1000
# The value of each node in the list is unique.
# The node to be deleted is in the list and is not a tail node.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f'{self.val} -> {self.next}'


def delete_node(node: ListNode):
    # working_sol (91.79%, 72.78%) -> (34ms, 16.76mb)  time: O(n) | space: O(1)
    # We can't access previous Nodes, so only way is to reassign everything from given `node`.
    # We guaranteed that we don't get LAST node, so we always have something after given `node`.
    # All we need is to get all values from next node to previous node and delete LAST node of the LinkedList.
    while node.next.next:
        node.val = node.next.val
        node = node.next
    node.val = node.next.val
    node.next = None


# Time complexity: O(n) <- n - number of Nodes in LinkedList.
# Worst case: we're given first Node of the LinkedList, so we're just traversing whole list => O(n).
# ------------------
# Auxiliary space: O(1).
# Nothing extra.

# Testcases longer than actual task.
