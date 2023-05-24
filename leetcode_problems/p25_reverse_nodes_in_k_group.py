# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#   k is a positive integer and is less than or equal to the length of the linked list.
#   If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
# -------------------------------
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000  ,  0 <= Node.val <= 1000
# -------------------------------
# Follow-up: Can you solve the problem in O(1) extra memory space?


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def create_linked(to_link: list[int]) -> ListNode:
    tempo = link = ListNode()
    for index in range(len(to_link)):
        tempo.val = to_link[index]
        if index != (len(to_link) - 1):
            tempo.next = ListNode()
            tempo = tempo.next
    return link


def t_one_linked(to_test: ListNode, testout: list[int]) -> None:
    tempo: ListNode = to_test
    count: int = 0
    for _ in range(len(testout)):
        assert testout[_] == tempo.val
        tempo = tempo.next
        count += 1
    assert count == len(testout)


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    pass


test1 = create_linked([1, 2, 3, 4, 5])
test1_k = 2
test1_out = [2, 1, 4, 3, 5]

test2 = create_linked([1, 2, 3, 4, 5])
test2_k = 3
test3_out = [3, 2, 1, 4, 5]
