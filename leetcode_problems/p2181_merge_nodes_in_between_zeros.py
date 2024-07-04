# You are given the head of a linked list,
#  which contains a series of integers separated by 0's.
# The beginning and end of the linked list will have Node.val == 0.
# For every two consecutive 0's, merge all the nodes lying in between them into a single node
#  whose value is the sum of all the merged nodes.
# The modified list should not contain any 0's.
# Return the head of the modified linked list.
# ----------------------
# The number of nodes in the list is in the range [3, 2 * 10 ** 5].
# 0 <= Node.val <= 1000
# There are no two consecutive nodes with Node.val == 0.
# The beginning and end of the linked list have Node.val == 0.


class ListNode:
    """
    Create single Node for a linked list.
    """

    def __init__(self, x: int = 0, next: 'ListNode' = None):
        """
        :param x: value of the Node.
        :param next: Node to which it points.
        """
        self.val = x
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def create_linked(to_link: list[int]) -> ListNode | None:
    """
    Create linked list.

    :param to_link: values to put into linked list Nodes.
    """
    if not to_link:
        return None
    tempo = link = ListNode()
    for index in range(len(to_link)):
        tempo.val = to_link[index]
        if index != (len(to_link) - 1):
            tempo.next = ListNode()
            tempo = tempo.next
    return link


def t_linked(list1: ListNode | None, list2: ListNode | None) -> None:
    """
    Test two linked lists to have same values.
    :param list1: first linked list to test.
    :param list2: second linked list to test.
    :return:
    """
    if not list1 or not list2:
        assert list1 == list2
    while list1 and list2:
        assert list1.val == list2.val
        list1 = list1.next
        list2 = list2.next
    assert list1 == list2


def merge_nodes(head: ListNode) -> ListNode:
    # working_sol (78.96%, 67.77%) -> (859ms, 56.31mb)  time: O(n) | space: O(1)
    cur_zero: ListNode | None = head
    cur_node: ListNode = head.next
    # We're guaranteed to meet `0` at the end.
    # So, we can just treat every `0` as a breakpoint and summ everything between them.
    while cur_node.next is not None:
        # Collect sum in the current `0` Node.
        if 0 != cur_node.val:
            cur_zero.val += cur_node.val
            cur_node = cur_node.next
        # Update the current `0` Node and point the previous `0` Node to the NewOne.
        else:
            cur_zero.next, cur_zero, cur_node = cur_node, cur_node, cur_node.next
    # We will point `0` Node to the last `0` we meet,
    #  and we don't need it => annul it.
    cur_zero.next = None
    return head


# Time complexity: O(n) <- n - number of Nodes inside the input LinkedList `head`.
# We're always traversing whole `head`, once => O(n).
# ----------------------
# Auxiliary space: O(1)
# Only using input LinkedList Nodes, nothing new is created => O(1).


test: ListNode = create_linked([0, 3, 1, 0, 4, 5, 2, 0])
test_out: ListNode = create_linked([4, 11])
merge_nodes(test)
t_linked(test, test_out)

test = create_linked([0, 1, 0, 3, 0, 2, 2, 0])
test_out = create_linked([1, 3, 4])
merge_nodes(test)
t_linked(test, test_out)
