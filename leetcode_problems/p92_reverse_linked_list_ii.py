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


# Actually why bother? We're not assigned to do this in_place, so why not just store slice from left to right values,
# and store everything else in 2 lists: before_left, after_right. Merge all 3 of them, but with reversed slice.
# Horrible on space, but simpler.
# --------------------
# For one way solution, as I understand it. We cannot traverse original linked_list more than once.
# But we can store needed slice and use it to reassign (left - 1) node and (right + 1) nodes,
# in reverse order of stored nodes, and restore path after this.
# Otherwise, I have no idea how to do this in *one_pass*. At least make this one work.
# --------------------
# Thought about using it to actually practice p25, for space O(1). But this is not going to be one_pass solution.
# So better to just do it as one_pass solution, and revisit for practice in p25 sometime else.


test1 = create_linked([1, 2, 3, 4, 5])
test1_left = 2
test1_right = 4
test1_out = [1, 4, 3, 2, 5]

test2 = create_linked([5])
test2_left = 1
test2_right = 1
test2_out = [5]
