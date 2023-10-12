# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# ---------------------
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    # working_sol (98.56%, 90.89%) -> (31ms, 16.16mb)  time: O(min(m, n) | space: O(1)
    merged: ListNode = ListNode()
    tempo: ListNode = merged
    # We need merged and sorted.
    # No reasons to recreate just reassign as merged_sort.
    while list1 and list2:
        if list1.val < list2.val:
            tempo.next = list1
            tempo = list1
            list1 = list1.next
        else:
            tempo.next = list2
            tempo = list2
            list2 = list2.next
    # Reuse what's left in one of the lists.
    if list1 or list2:
        if list1:
            tempo.next = list1
        else:
            tempo.next = list2
    return merged.next


# Time complexity: O(min(m, n)) -> we're not creating a new nodes, just reassigning list1|list2 ->
# m - number of nodes in 'list1'^^| -> so it's always traverse of minimum size list and assign of leftovers =>
# n - number of nodes in 'list2'^^| => O(min(m, n))
# Auxiliary space: O(1) -> only 1 extra node 'merged' created, everything else is reassign => O(1).


test_l1: ListNode | None = create_linked([1, 2, 4])
test_l2: ListNode | None = create_linked([1, 3, 4])
test_out: ListNode | None = create_linked([1, 1, 2, 3, 4, 4])
test_t: ListNode | None = merge_two_lists(test_l1, test_l2)
while test_out or test_t:
    assert test_t.val == test_out.val
    test_t, test_out = test_t.next, test_out.next

test_l1 = None
test_l2 = None
test_out = None
test_t: ListNode | None = merge_two_lists(test_l1, test_l2)
while test_out or test_t:
    assert test_t.val == test_out.val
    test_t, test_out = test_t.next, test_out.next

test_l1 = None
test_l2 = create_linked([0])
test_out = create_linked([0])
test_t: ListNode | None = merge_two_lists(test_l1, test_l2)
while test_out or test_t:
    assert test_t.val == test_out.val
    test_t, test_out = test_t.next, test_out.next
