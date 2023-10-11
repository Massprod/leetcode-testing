# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# ----------------
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"[{self.val}] -> {self.next}"


def create_linked(to_link: list[int]) -> ListNode:
    tempo = link = ListNode()
    for index in range(len(to_link)):
        tempo.val = to_link[index]
        if index != (len(to_link) - 1):
            tempo.next = ListNode()
            tempo = tempo.next
    return link


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    # working_sol (55.79%, 96.44%) -> (65ms, 16.2mb)  time: O(m + n) | space: O(m + n + max(m, n))
    # Get both numbers to summarize.
    number1: str = ''
    while l1:
        number1 += str(l1.val)
        l1 = l1.next
    number2: str = ''
    while l2:
        number2 += str(l2.val)
        l2 = l2.next
    # Reverse to get correct number and summarize.
    number3: str = str(int(number1[::-1]) + int(number2[::-1]))
    # Reverse summ and create a new list.
    l3: ListNode = ListNode(int(number3[-1]))
    temp: ListNode = l3
    for x in range(len(number3) - 2, -1, -1):
        temp.next = ListNode(int(number3[x]))
        temp = temp.next
    return l3


# Time complexity: O(m + n) -> traversing both input lists to get their numbers => O(m + n) ->
# m - nodes of l1^^|        -> reversing them => O(m + n) -> recreating list with sum => O(max(m, n) + 1).
# n - nodes of l2^^|
# Auxiliary space: O(m + n + max(m, n)) -> two string with numbers from l1, l2 and their sum number3 ->
#                           -> which should be close to max(m, n) + 1, even if we get overflow it's still +1 digit.


test_l1: ListNode = create_linked([2, 4, 3])
test_l2: ListNode = create_linked([5, 6, 4])
test_out: ListNode = create_linked([7, 0, 8])
test_t: ListNode = add_two_numbers(test_l1, test_l2)
while test_out or test_t:
    assert test_t.val == test_out.val
    test_t, test_out = test_t.next, test_out.next

test_l1 = create_linked([0])
test_l2 = create_linked([0])
test_out = create_linked([0])
test_t = add_two_numbers(test_l1, test_l2)
while test_out or test_t:
    assert test_t.val == test_out.val
    test_t, test_out = test_t.next, test_out.next

test_l1 = create_linked([9, 9, 9, 9, 9, 9, 9])
test_l2 = create_linked([9, 9, 9, 9])
test_out = create_linked([8, 9, 9, 9, 0, 0, 0, 1])
test_t = add_two_numbers(test_l1, test_l2)
while test_out or test_t:
    assert test_t.val == test_out.val
    test_t, test_out = test_t.next, test_out.next
