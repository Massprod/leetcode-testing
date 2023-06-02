# Given head, the head of a linked list, determine if the linked list has a cycle in it.
#
# There is a cycle in a linked list if there is some node in the list that can be reached again
#   by continuously following the next pointer. Internally, pos is used to denote the index of the node
#   that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.
# ------------------------
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
# ------------------------
# Follow up: Can you solve it using O(1) (i.e. constant) memory?


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def create_linked_with_cycle(to_link: list[int], pos: int) -> ListNode:
    tempo = link = ListNode()
    step: int = 0
    pos_node: ListNode | None = None
    for index in range(len(to_link)):
        tempo.val = to_link[index]
        if 0 < pos == step:
            pos_node = tempo
        if index != (len(to_link) - 1):
            tempo.next = ListNode()
            step += 1
            tempo = tempo.next
            continue
        tempo.next = pos_node
    return link


def has_cycle(head: ListNode) -> bool:
    pass


test1_pos = 1
test1 = create_linked_with_cycle([3, 2, 0, -4], test1_pos)
test1_out = True

test2_pos = 0
test2 = create_linked_with_cycle([1, 2], test2_pos)
test2_out = True

test3_pos = -1
test3 = create_linked_with_cycle([1], test3_pos)
test3_out = False