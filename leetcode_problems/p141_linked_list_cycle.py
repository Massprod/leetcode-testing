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
        if 0 <= pos == step:
            pos_node = tempo
        if index != (len(to_link) - 1):
            tempo.next = ListNode()
            step += 1
            tempo = tempo.next
            continue
        tempo.next = pos_node
    return link


def has_cycle(head: ListNode) -> bool:
    # working_sol (69.69%, 50.15%) -> (62ms, 20.2mb)  time: O(n) | space: O(1)
    placeholder: str = "p"
    temp: ListNode = head
    while temp:
        if temp.val == placeholder:
            return True
        temp.val = placeholder
        temp = temp.next
    return False


# Time complexity: O(n) -> traversing linked list only once => O(n)
# n - len of input_list^^|
# Space complexity: o(1) -> extra STR doesn't depend on input, and only changing input itself => O(1)
# ------------------------
# Getting recursion Error, means creating of cycled_linked is correct.
# Task is easy we're not obligated to save original state of linked_list, and there's no rule for that.
# I see 2 ways at least for now, is change every value from 0 - n and just check if we encounter changed value =>
# => O(1) for space, we're just changing linked list.
# Or just save whole linked_list nodes links into a dict() and check if we meet them twice, this one is O(n) space.


test1_pos = 1
test1 = create_linked_with_cycle([3, 2, 0, -4], test1_pos)
test1_out = True
print(has_cycle(test1))
assert test1_out == has_cycle(test1)

test2_pos = 0
test2 = create_linked_with_cycle([1, 2], test2_pos)
test2_out = True
print(has_cycle(test2))
assert test2_out == has_cycle(test2)

test3_pos = -1
test3 = create_linked_with_cycle([1], test3_pos)
test3_out = False
print(has_cycle(test3))
assert test3_out == has_cycle(test3)
