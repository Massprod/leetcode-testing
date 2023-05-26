# Given the head of a linked list, return the list after sorting it in ascending order.
# --------------------
# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105
# --------------------
# Follow up: Can you sort the linked list in O(n log n) time and O(1) memory (i.e. constant space)?


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


def sort_list(head: ListNode) -> ListNode:
    pass


test1 = [4, 2, 1, 3]
test1_out = [1, 2, 3, 4]

test2 = [-1, 5, 3, 4, 0]
test2_out = [-1, 0, 3, 4, 5]
