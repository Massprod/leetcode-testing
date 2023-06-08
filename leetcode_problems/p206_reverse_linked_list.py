# Given the head of a singly linked list, reverse the list, and return the reversed list.
# ---------------------
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


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


def reverse_list(head: ListNode) -> ListNode:
    pass


test1 = [1, 2, 3, 4, 5]
test1_out = [5, 4, 3, 2, 1]

test2 = [1, 2]
test2_out = [2, 1]
