# Given the head of a singly linked list and an integer k, split the linked list
#  into k consecutive linked list parts.
# The length of each part should be as equal as possible:
#  no two parts should have a size differing by more than one. This may lead to some parts being null.
# The parts should be in the order of occurrence in the input list,
#  and parts occurring earlier should always have a size greater than or equal to parts occurring later.
# Return an array of the k parts.
# ----------------
# The number of nodes in the list is in the range [0, 1000].
# 0 <= Node.val <= 1000
# 1 <= k <= 50
from math import ceil
from random import randint


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


def split_to_parts(head: ListNode, k: int) -> list[ListNode]:
    # working_sol (94.59%, 97.75%) -> (37ms, 16.6mb)  time: O(n + k) | space: O(k)
    # Save every Node to split.
    all_nodes: list[ListNode | None] = []
    tempo: ListNode = head
    while tempo:
        all_nodes.append(tempo)
        tempo = tempo.next
    # If we need more than we have then:
    #  every node is a part, and extra None to fill the gap.
    if k >= len(all_nodes):
        index: int = 0
        # Just break all links.
        while index != len(all_nodes):
            all_nodes[index].next = None
            index += 1
        # And append extras.
        while index != k:
            all_nodes.append(None)
            index += 1
        return all_nodes
    split_parts: list[ListNode] = []
    length: int = len(all_nodes)
    # Head of a list after split.
    start: int = 0
    # Taking one part at a time, until we have smth to split.
    while length > 0:
        # We can use only whole, and we need maximum of k parts.
        # So we always take ceil() from length(nodes) we still have,
        #  and parts we need to split this length into.
        end: int = start + ceil(length / k)
        # Array is 0-indexed, extra -1 to get correct index.
        all_nodes[end - 1].next = None
        # Delete used nodes.
        length -= end - start
        split_parts.append(all_nodes[start])
        start = end
        # Decrease by part used.
        k -= 1
    return split_parts


# Time complexity: O(n + k) -> traversing whole linked list to save every node => O(n) -> if we have k >= n, then we
# n - nodes of linked_list^^| will break links at every index and append extra None's to fill gap k - n => O(k) ->
#                             actually this ^^ should be the worst case, otherwise we're checking only part of
#                             original indexes, and it can even be 1 operation when k == 1 => O(log n).
#                             Should be smth: O(n + n + k) <- (n + k) every index + extras, can cull to O(n + k).
#                             In cases when n > k => O(n + log n) <- cuz only part of the indexes will be used.
# Auxiliary space: O(k) -> same worst case, we will expand original list of nodes with extra Nones to fill => O(k) ->
#                         -> and if n > k, we will just split original Node links without creating extra => O(n).
# ----------------
# Most basic way I see is that store every node in a list and just split like:
# length <- number of nodes left, K <- parts to split =>
# => start == 0, end == start + ceil(length / k), and all we need is to maintain start point like:
# start = end, cuz end is limit Node and k - 1 cuz we take 1 part at a time.
# Working with random max constraints, let's fail. All correct.


test: ListNode = create_linked([1, 2, 3])
test_k: int = 5
test_out: list[ListNode] = [
    create_linked([1]), create_linked([2]), create_linked([3]), create_linked([]), create_linked([]),
]
c_test: list[ListNode] = split_to_parts(test, test_k)
for y in range(len(test_out)):
    t_linked(test_out[y], c_test[y])

test = create_linked([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
test_k = 3
test_out = [
    create_linked([1, 2, 3, 4]), create_linked([5, 6, 7]), create_linked([8, 9, 10]),
]
c_test = split_to_parts(test, test_k)
for y in range(len(test_out)):
    t_linked(test_out[y], c_test[y])

test_copy: list[int] = [randint(0, 1000) for _ in range(1000)]
print(test_copy)
