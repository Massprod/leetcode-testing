# You are given two non-empty linked lists representing two non-negative integers.
# The most significant digit comes first and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# ---------------------
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


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


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    # working_sol (82.70%, 94.82%) -> (77ms, 16.26mb)  time: O(n + k) | space: O(n + k)
    first: str = ""
    second: str = ""
    # read first
    while l1:
        first += str(l1.val)
        l1 = l1.next
    # read second
    while l2:
        second += str(l2.val)
        l2 = l2.next
    # summarize
    summ: str = str(int(first) + int(second))
    # rebuild
    new: ListNode = ListNode()
    tempo: ListNode = new
    for _ in range(len(summ)):
        # type change
        tempo.val = int(summ[_])
        if _ != len(summ) - 1:
            tempo.next = ListNode()
            tempo = tempo.next
    return new


# Time complexity: O(n + k) -> traversing both input_linked_lists => O(n + k) -> creating new linked_list with size of
# n - nodes of input_l1^^| maximum length of both input_linked_lists => O(max(n, k)) -> O(n + k) + O(max(n, k)).
# k - nodes of input_L2^^|
# Auxiliary space: O(n + k) -> creating 2 extra strings of sizes n and k => O(n + k) ->
#                           -> creating extra linked_list with size of max(n, k) => O(max(n, k) ->
#                           -> O(n + k) + O(max(n, k) => O(n + k).
# ---------------------
# In case of reversing, it's same double walk, with recording of length and switching every node value on the way.
# And after this 2 walks to summarize reversed nodes for _ in range(max(lengths)) => return head of max(lengths) list.
# But it's actually harder cuz there's going to be cases with 6 + 5, and we need to transfer extras between nodes.
# ---------------------
# Follow up: Could you solve it without reversing the input lists?
# Rebuild after reading? Well it's not reversing, so it should be correct.


test1_l1 = create_linked([7, 2, 4, 3])
test1_l2 = create_linked([5, 6, 4])
test1_out = create_linked([7, 8, 0, 7])
test = add_two_numbers(test1_l1, test1_l2)
while test1_out:
    assert test1_out.val == test.val
    test1_out = test1_out.next
    test = test.next
del test

test2_l1 = create_linked([2, 4, 3])
test2_l2 = create_linked([5, 6, 4])
test2_out = create_linked([8, 0, 7])
test = add_two_numbers(test2_l1, test2_l2)
while test2_out:
    assert test2_out.val == test.val
    test2_out = test2_out.next
    test = test.next
del test

test3_l1 = create_linked([0])
test3_l2 = create_linked([0])
test3_out = create_linked([0])
test = add_two_numbers(test3_l1, test3_l2)
while test3_out:
    assert test3_out.val == test.val
    test3_out = test3_out.next
    test = test.next
del test
