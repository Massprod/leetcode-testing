# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val, and return the new head.
# -------------------
# The number of nodes in the list is in the range [0, 10 ** 4].
# 1 <= Node.val <= 50
# 0 <= val <= 50


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


def remove_elements(head: ListNode, val: int) -> ListNode:
    pass


test1 = [1, 2, 6, 3, 4, 5, 6]
test1_val = 6
test1_out = [1, 2, 3, 4, 5]

test2 = []
test2_val = 1
test2_out = None

test3 = [7, 7, 7, 7]
test3_val = 7
test3_out = None
