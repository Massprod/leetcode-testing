# Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
#  leaving only distinct numbers from the original list.
# Return the linked list sorted as well.
# --------------------------
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


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


def delete_duplicates(head: ListNode) -> ListNode | None:
    # working_sol (71.21%, 92%) -> (44ms, 16.2mb)  time: O(n) | space: O(n)
    if not head or not head.next:
        return head
    nodes: list[ListNode] = [head]
    prev_node: ListNode = head
    head = head.next
    while head:
        # Ignore and delete same values.
        if prev_node.val == head.val:
            if nodes and nodes[-1].val == prev_node.val:
                nodes.pop()
            head = head.next
        # Add new values.
        else:
            nodes.append(head)
            prev_node, head = head, head.next
    if not nodes:
        return None
    # Reassign all nodes, we already stored only Nodes with unique values.
    for x in range(len(nodes) - 1):
        nodes[x].next = nodes[x + 1]
    nodes[-1].next = None
    return nodes[0]


# Time complexity: O(n) -> worst case == everything is unique -> traversing and appending all Nodes -> O(n) ->
# n - Nodes of input linked list^^| -> extra traverse of the same Nodes to reassign => O(2n).
# Auxiliary space: O(n) -> every node link is stored in a list 'nodes' => O(n).


test: ListNode = create_linked([1, 2, 3, 3, 4, 4, 5])
test_out: ListNode = create_linked([1, 2, 5])
t_linked(test_out, delete_duplicates(test))

test = create_linked([1, 1, 1, 2, 3])
test_out = create_linked([2, 3])
t_linked(test_out, delete_duplicates(test))

test = create_linked([1, 2, 2, 2])
test_out = create_linked([1])
t_linked(test_out, delete_duplicates(test))
