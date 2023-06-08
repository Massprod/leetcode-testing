# You are given the head of a singly linked-list. The list can be represented as:
#       L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#       L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
# ------------------------
# The number of nodes in the list is in the range [1, 5 * 10 ** 4].
# 1 <= Node.val <= 1000


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


def reorder_list(head: ListNode) -> None:
    # working_sol (93.67%, 37.8%) -> (86ms, 26.2mb)  time: O(n + m) | space: O(n)
    all_nodes: list[ListNode] = []
    while head:
        all_nodes.append(head)
        head = head.next
    switches: int = (len(all_nodes) - 1) // 2
    left: int = 1
    right: int = -1
    start_node: ListNode = all_nodes[0]
    if (len(all_nodes) - 1) % 2 == 0:
        even: bool = True
    else:
        even: bool = False
    while switches:
        left_node: ListNode = all_nodes[left]
        right_node: ListNode = all_nodes[right]
        start_node.next = right_node
        right_node.next = left_node
        start_node = left_node
        if switches == 1 and not even:
            all_nodes[left + 1].next = None
        if switches == 1 and even:
            start_node.next = None
        left += 1
        right -= 1
        switches -= 1


# Time complexity: O(n + m) -> traversing input_list once to create list with all node_links => O(n) ->
# n - nodes in input_list^^| -> switching nodes for (n - 1 // 2) times => O(m) -> O(n + m).
# m - number of switches^^ |
# Auxiliary space: O(n) -> creating extra list with links of every node in input_list => O(n)
# ------------------------
# No limits on space, so just store every node in a list and reassign them?
# 0 index always stays, -1 to 1, -2 to 2, -3 to 3, etc.


test1 = create_linked([1, 2, 3, 4])
test1_out = [1, 4, 2, 3]
reorder_list(test1)
t_one_linked(test1, test1_out)

test2 = create_linked([1, 2, 3, 4, 5])
test2_out = [1, 5, 2, 4, 3]
reorder_list(test2)
t_one_linked(test2, test2_out)

test3 = create_linked([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
test3_out = [1, 14, 2, 13, 3, 12, 4, 11, 5, 10, 6, 9, 7, 8]
reorder_list(test3)
t_one_linked(test3, test3_out)
