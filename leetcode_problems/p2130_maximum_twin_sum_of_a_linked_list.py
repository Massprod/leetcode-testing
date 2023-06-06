# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known
# as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.
#   For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2.
#       These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.
# Given the head of a linked list with even length, return the maximum twin sum of the linked list.
# -----------------
# The number of nodes in the list is an even integer in the range [2, 10 ** 5].
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


def pair_sum(head: ListNode) -> int:
    # working_sol (29.71%, 30.11%) -> (968ms, 57mb)  time: O(n) | space: O(n)
    all_values: list[int] = []
    while head:
        all_values.append(head.val)
        head = head.next
    left: int = 0
    right: int = len(all_values) - 1
    max_sum: int = 0
    while left < right:
        cur_sum: int = all_values[left] + all_values[right]
        max_sum = max(max_sum, cur_sum)
        left += 1
        right -= 1
    return max_sum


# Time complexity: O(n) -> traversing input_list once to get and store all values => O(n) ->
# n - num of nodes in input_list^^| -> checking every index of created list for a sum => O(n) -> O(2n) -> O(n).
# Auxiliary space: O(n) -> extra constants and list with all values from input list => O(n)


test1 = create_linked([5, 4, 2, 1])
test1_out = 6
assert test1_out == pair_sum(test1)

test2 = create_linked([4, 2, 2, 3])
test2_out = 7
assert test2_out == pair_sum(test2)

test3 = create_linked([1, 100000])
test3_out = 100001
assert test3_out == pair_sum(test3)
