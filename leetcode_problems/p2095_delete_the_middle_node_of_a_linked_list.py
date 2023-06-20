# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing,
#   where ⌊x⌋ denotes the largest integer less than or equal to x.
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
# --------------------------
# The number of nodes in the list is in the range [1, 10 ** 5].
# 1 <= Node.val <= 10 ** 5


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


def delete_middle(head: ListNode) -> ListNode:
    pass


test1 = create_linked([1, 3, 4, 7, 1, 2, 6])
test1_out = [1, 3, 4, 1, 2, 6]

test2 = create_linked([1, 2, 3, 4])
test2_out = [1, 2, 4]

test3 = [2, 1]
test3_out = [2]
