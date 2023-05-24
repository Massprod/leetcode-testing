# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.
# --------------------
# The number of nodes in the list is n.
# 1 <= n <= 500  ,  -500 <= Node.val <= 500  ,  1 <= left <= right <= n
# --------------------
# Follow up: Could you do it in one pass?


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


def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    pass


test1 = create_linked([1, 2, 3, 4, 5])
test1_left = 2
test1_right = 4
test1_out = [1, 4, 3, 2, 5]

test2 = create_linked([5])
test2_left = 1
test2_right = 1
test2_out = [5]
