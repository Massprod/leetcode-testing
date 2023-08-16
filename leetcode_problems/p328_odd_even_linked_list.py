# Given the head of a singly linked list, group all the nodes with odd indices together
#   followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.
# ------------------
# The number of nodes in the linked list is in the range [0, 10 ** 4].
# -10 ** 6 <= Node.val <= 10 ** 6
from random import randint


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


def odd_even_list(head: ListNode) -> ListNode:
    # working_sol (89.61%, 88.88%) -> (45ms, 18.8mb)  time: O(n) | space: O(1)
    # Empty list, or list with 1 value insta return.
    if not head or not head.next:
        return head
    # Using last possible node to reassign every even index,
    # after this node.
    last_node: ListNode = head
    # Depending on Even|Odd list, we need to assign either
    # on last_node, or PRE last_node.
    count: int = 1
    # Count every node until PRE last.
    while last_node.next.next:
        last_node = last_node.next
        count += 1
    even_node: ListNode | None = None
    # If PRE last node is ODD index, then last_node is
    # EVEN, and we should reassign it as well.
    if (count + 1) % 2 != 0:
        # Otherwise, we can use last_node as endpoint.
        last_node = last_node.next
    else:
        # Remember EVEN last_node to reassign it later.
        even_node: ListNode = last_node.next
    # We need to stop at last_node, so we need extra link
    # to assign everything one by one and use last_node as a breakpoint.
    use_last: ListNode = last_node
    # Starting from head ->
    cur_node: ListNode = head
    while cur_node != last_node:
        # -> cur_node.next is always EVEN index,
        # assigning it correctly into EVEN group after last_node ->
        use_last.next = cur_node.next
        # -> cur_node.next is used, and we need to assign all ODD nodes
        # to another ODD nodes, and next ODD node is next.next ->
        cur_node.next = cur_node.next.next
        # -> break inf_loop from reassigned EVEN node ->
        use_last.next.next = None
        # -> repeat for every ODD node possible.
        cur_node = cur_node.next
        use_last = use_last.next
    # Even node is last_node and points -> None,
    # so we can just assign it as last EVEN node.
    if even_node:
        use_last.next = even_node
    return head


# Time complexity: O(n) -> traversing whole input_list once, to get pre_last Node and decide Even|Odd => O(n) ->
# n - node if input_list^^| -> extra using every node, once to reassign them to correct groups => O(2n).
# Auxiliary space: O(1) -> only 1 constant INT used, everything else is operating with links of original => O(1).


test: ListNode = create_linked([1, 2, 3, 4, 5])
test_out: list[int] = [1, 3, 5, 2, 4]
t_one_linked(odd_even_list(test), test_out)

test = create_linked([2, 1, 3, 5, 6, 4, 7])
test_out = [2, 3, 6, 7, 1, 5, 4]
t_one_linked(odd_even_list(test), test_out)

test = create_linked([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
test_out = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
t_one_linked(odd_even_list(test), test_out)

print([randint(-100, 100) for _ in range(10 ** 4)])
