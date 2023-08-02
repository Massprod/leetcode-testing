# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# ------------------
# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100


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


def middle_node(head: ListNode) -> ListNode:
    # working_sol (99.49%, 94.18%) -> (29ms, 16.2mb)  time: O(n) | space: O(1)
    # Only one node is present.
    if head.next is None:
        return head
    # Standard Floyd method.
    slow: ListNode = head
    fast: ListNode = head.next
    # Counting nodes, we already checked if there's >= 2 nodes.
    # So it's insta +2.
    count: int = 2
    while fast and fast.next is not None:
        # Fast is always skipping 2 nodes.
        count += 2
        fast = fast.next.next
        # But it can land on either LAST node, or EMPTY spot.
        # If it's landing on EMPTY spot we need to delete 1 Node.
        # If it's lading on LAST node we're just breaking,
        #   and it's correct node to count.
        if fast is None:
            count -= 1
        slow = slow.next
    # By default, we asked:
    # if odd => return middle
    # if even => return middle + 1
    if count % 2 != 0:
        return slow
    return slow.next


# Time complexity: O(n) -> standard Floyd method is used, so we're just traversing whole input_list once => O(n) ->
# n - nodes of input_list^^| -> actually we're not using every Node with fast, but slow is still using other half,
#                            so it's still use of every Node at least once.
# Auxiliary space: O(1) -> only 1 extra INT is used, doesn't depend on input => O(1).
# ------------------
# Solved this in p234, while I wanted to switch nodes in_place and needed middle for it.


test_head: ListNode = create_linked([1, 2, 3, 4, 5])
test_out: list[int] = [3, 4, 5]
test: ListNode = middle_node(test_head)
t_one_linked(test, test_out)

test_head: ListNode = create_linked([1, 2, 3, 4, 5, 6])
test_out: list[int] = [4, 5, 6]
test: ListNode = middle_node(test_head)
t_one_linked(test, test_out)
