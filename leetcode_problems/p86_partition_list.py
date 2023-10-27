# Given the head of a linked list and a value x,
#   partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# ------------------------
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200


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


def partition(head: ListNode, x: int) -> ListNode:
    # working_sol(97.27%, 88.85%) -> (34ms, 16.19mb)  time: O(n) | space: O(n)
    # Store everything lower and higher than x.
    lower: list[ListNode] = []
    higher: list[ListNode] = []
    # Empty list -> insta return.
    if not head:
        return head
    tempo: ListNode = head
    while tempo:
        # Higher|Equal than x => right_side.
        if tempo.val >= x:
            higher.append(tempo)
        # Lower than x => left_side.
        if tempo.val < x:
            lower.append(tempo)
        tempo = tempo.next
    # Recombine with correct order.
    for x in range(len(lower) - 1):
        lower[x].next = lower[x + 1]
    for x in range(len(higher) - 1):
        higher[x].next = higher[x + 1]
    if higher:
        higher[-1].next = None
    if lower:
        if higher:
            lower[-1].next = higher[0]
        else:
            lower[-1].next = None
        return lower[0]
    return higher[0]


# Time complexity: O(n) -> traversing whole input LinkedList to get all Nodes, once => O(n) ->
# n - Node of linked_list ^^| -> recombining original Nodes in correct order => O(2n).
# Space complexity: O(n) -> two extra lists with all Node links stored, summarized == 'n' => O(n).


test: ListNode = create_linked([1, 4, 3, 2, 5, 2])
test_x: int = 3
test_out: ListNode = create_linked([1, 2, 2, 4, 3, 5])
t_linked(partition(test, test_x), test_out)

test = create_linked([2, 1])
test_x = 2
test_out = create_linked([1, 2])
t_linked(partition(test, test_x), test_out)

test = create_linked([0])
test_x = 1
test_out = create_linked([0])
t_linked(partition(test, test_x), test_out)
