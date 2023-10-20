# Given the head of a linked list, rotate the list to the right by k places.
# -----------------
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10 ** 9
# The number of nodes in the list is in the range [0, 500].


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


def rotate_right(head: ListNode, k: int) -> ListNode:
    # working_sol (76.62%, 88.80%) -> (40ms, 16.2mb)  time: O(n) | space: O(n)
    if not head:
        return head
    if k == 0:
        return head
    nodes: list[ListNode] = []
    while head:
        nodes.append(head)
        head = head.next
    # We only care about remainder, full rotations is irrelevant.
    # (k % len(nodes)) == what's left.
    for _ in range(k % len(nodes)):
        nodes = [nodes.pop()] + nodes
    # Reassign in the new order.
    for x in range(len(nodes) - 1):
        nodes[x].next = nodes[x + 1]
    nodes[-1].next = None
    return nodes[0]


# Time complexity: O(n) -> traversing whole input linked list once to get all nodes => O(n) ->
# n - nodes of input linked list^^|-> worst case == rotate by (n - 1) -> rebuild array for (n - 1) times => O(n - 1) ->
#                                  -> reassigning them in the new order => O(n).
# Auxiliary space: O(n) -> all Node links stored in 'nodes' => O(n).


test: ListNode = create_linked([1, 2, 3, 4, 5])
test_k: int = 2
test_out: ListNode = create_linked([4, 5, 1, 2, 3])
t_linked(test_out, rotate_right(test, test_k))

test = create_linked([0, 1, 2])
test_k = 4
test_out = create_linked([2, 0, 1])
t_linked(test_out, rotate_right(test, test_k))
