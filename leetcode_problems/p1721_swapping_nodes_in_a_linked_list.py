# You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node from the beginning
#   and the kth node from the end (the list is 1-indexed).
# ----------------------
# The number of nodes in the list is n.
# 1 <= k <= n <= 10 ** 5  ,  0 <= Node.val <= 100


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


def swap_nodes(head: ListNode, k: int) -> ListNode:
    pass


test1 = [1, 2, 3, 4, 5]
test1_k = 2

test2 = [7, 9, 6, 6, 7, 8, 3, 0, 9, 5]
test2_k = 5
