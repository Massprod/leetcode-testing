# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again
#   by continuously following the next pointer. Internally, pos is used to denote the index of the node
#   that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle.
# Note that pos is not passed as a parameter.
# Do not modify the linked list.
# ---------------------
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
# ---------------------
# Follow up: Can you solve it using O(1) (i.e. constant) memory?


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def create_linked_with_cycle(to_link: list[int], pos: int) -> tuple[ListNode, ListNode]:
    tempo = link = ListNode()
    step: int = 0
    pos_node: ListNode | None = None
    for index in range(len(to_link)):
        tempo.val = to_link[index]
        if 0 <= pos == step:
            pos_node = tempo
        if index != (len(to_link) - 1):
            tempo.next = ListNode()
            step += 1
            tempo = tempo.next
            continue
        tempo.next = pos_node
    return link, pos_node


def detect_cycle(head: ListNode) -> ListNode:
    pass


test1_pos = 1
test1 = create_linked_with_cycle([3, 2, 0, -4], test1_pos)
test1_out = test1[1]
print(detect_cycle(test1[0]))
assert test1_out == detect_cycle(test1[1])

test2_pos = 0
test2 = create_linked_with_cycle([1, 2], test2_pos)
test2_out = test2[1]
print(detect_cycle(test2[1]))
assert test2_out == detect_cycle(test2[0])

test3_pos = -1
test3 = create_linked_with_cycle([1], test3_pos)
test3_out = False
print(detect_cycle(test3[0]))
assert test3_out == detect_cycle(test3[0])
