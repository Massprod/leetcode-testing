# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again
#  by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list.
# Otherwise, return false.
# ------------------------
# The number of the nodes in the list is in the range [0, 10 ** 4].
# -10 ** 5 <= Node.val <= 10 ** 5
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
    # We're given linked_list with TAIL connected to some Node.
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
        # So we assign only TAIL to this saved node.
        tempo.next = pos_node
    return link


def has_cycle(head: ListNode) -> bool:
    # working_sol (91.52%, 87.61%) -> (62ms, 20.2mb)  time: O(n) | space: O(1)
    if not head:
        return False
    # Standard Floyd.
    slow: ListNode = head
    # Even if one Node present, we're still entering While.
    fast: ListNode = head.next
    while slow != fast:
        slow = slow.next
        # If fast or fast.next IS None.
        # Then there's no Loop.
        if not fast or not fast.next:
            return False
        fast = fast.next.next
    # Otherwise, they collide and it's a cycle.
    return True


# Time complexity: O(n) -> worst case with cycle placed on 0 Node slow will traverse list twice, still linear => O(n).
# n - len of input_list^^|
# Auxiliary space: O(1) -> extra STR doesn't depend on input, and only changing stored input Nodes => O(1).
# ------------------------
# Guess it should actually be done with Floyd turtle-hare algorithm, but if we're not blocked from changing values.
# It should be faster to just change them and check for last node pointing to changed value. Fewer nodes to visit.
# And both constant space anyway. But it's better to rebuild for correct way.
# ------------------------
# Getting recursion Error, means creating of cycled_linked is correct.
# Task is easy we're not obligated to save original state of linked_list, and there's no rule for that.
# I see 2 ways at least for now, is change every value from 0 - n and just check if we encounter changed value =>
# => O(1) for space, we're just changing linked list.
# Or just save whole linked_list nodes links into a dict() and check if we meet them twice, this one is O(n) space.


test_pos: int = 1
test: ListNode = create_linked_with_cycle([3, 2, 0, -4], test_pos)
test_out: bool = True
assert test_out == has_cycle(test)

test_pos = 0
test = create_linked_with_cycle([1, 2], test_pos)
test_out = True
assert test_out == has_cycle(test)

test_pos = -1
test = create_linked_with_cycle([1], test_pos)
test_out = False
assert test_out == has_cycle(test)

test_pos = -1
test = create_linked_with_cycle([1, 2, 3, 4, 5, 6, 7], test_pos)
test_out = False
assert test_out == has_cycle(test)
