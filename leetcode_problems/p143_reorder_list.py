# You are given the head of a singly linked-list. The list can be represented as:
#       L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#       L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# ------------------------
# The number of nodes in the list is in the range [1, 5 * 10 ** 4].
# 1 <= Node.val <= 1000


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


def reorder_list(head: ListNode) -> None:
    pass


test1 = [1, 2, 3, 4]
test1_out = [1, 4, 2, 3]

test2 = [1, 2, 3, 4, 5]
test2_out = [1, 5, 2, 4, 3]
