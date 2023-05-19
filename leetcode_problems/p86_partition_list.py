# Given the head of a linked list and a value x,
# partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
# ------------------------
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100  ,  -200 <= x <= 200


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def partition(head: ListNode, x: int) -> ListNode:
    pass


test1 = [1, 4, 3, 2, 5, 2]
test1_x = 3
test1_out = [1, 2, 2, 4, 3, 5]

test2 = [2, 1]
test2_x = 2
test2_out = [1, 2]
