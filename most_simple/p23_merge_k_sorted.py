# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def merge_k_sorted(lists: list[ListNode]) -> ListNode:
    pass


test1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
test1_out = [1, 1, 2, 3, 4, 4, 5, 6]
