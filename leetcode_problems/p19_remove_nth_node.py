# Given the head of a linked list,
#  remove the nth node from the end of the list and return its head.
# ----------------
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# ----------------
# Follow up: Could you do this in one pass?


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


def remove_node(head: ListNode, n: int) -> ListNode:
    # working_sol (77.53%, 96.58%) -> (37ms, 16.08mb)  time: O(n) | space: O(n)
    nodes: list[ListNode] = []
    tempo: ListNode = head
    while tempo:
        nodes.append(tempo)
        tempo = tempo.next
    # First node for deletion, we can't return 'head'.
    if -n == -len(nodes):
        if len(nodes) == 1:
            return head.next
        return nodes[1]
    # Delete 'n' Node == reassign neighbours.
    # And we know there's something before it, cuz it's not [0] index.
    nodes[-n - 1].next = nodes[-n].next
    return head


# Time complexity: O(n) -> traversing whole input linked_list once => O(n).
# n - Nodes of input linked_list^^|
# Auxiliary space: O(n) -> every link to a Node is saved => O(n).
#                       Actually might be called constant, because we're saving only Links and they always mention.
#                       That recursions using only links to a Nodes are constant space, but I will stick to Linear.
# ----------------
# Follow up == One pass.
# We're not limited by space, so it can be just safe everything in a list and reassign indexes.
# But can it be done in constant space and one pass?
# Don't see it, cuz we have no idea how many nodes left we can't just use some buffer.
# And we can't reassign without second pass in this case, because we need to know how many Nodes left on right side.


test: ListNode = create_linked([1, 2, 3, 4, 5])
test_n: int = 2
test_out: ListNode = create_linked([1, 2, 3, 5])
t_linked(test_out, remove_node(test, test_n))

test = create_linked([1])
test_n = 1
test_out = create_linked([])
t_linked(test_out, remove_node(test, test_n))

test = create_linked([1, 2])
test_n = 1
test_out = create_linked([1])
t_linked(test_out, remove_node(test, test_n))
