# Given the head of a sorted linked list,
# delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.
# ---------------------
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


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


def delete_duplicates(head: ListNode) -> ListNode | None:
    if not head:
        return head
    prev_val: int = head.val
    to_link: list[int] = [prev_val]
    temp = head.next
    while temp:
        if prev_val == temp.val:
            temp = temp.next
            if len(to_link) == 0:
                continue
            if len(to_link) != 0 and to_link[-1] == prev_val:
                to_link.pop()
            continue
        if prev_val != temp.val:
            prev_val = temp.val
            to_link.append(prev_val)
            if temp.next is None:
                break
            temp = temp.next
    if len(to_link) == 0:
        return None
    temp = new_linked = ListNode()
    for x in range(len(to_link)):
        temp.val = to_link[x]
        if x != (len(to_link) - 1):
            temp.next = ListNode()
            temp = temp.next
    return new_linked


# Reusing problem 82, because it's a mirror and no reasons to create something from a scratch.
# Just need to rebuild duplicate_check part.


test1 = [1, 1, 2]
test1_linked = create_linked(test1)
test1_out = [1, 2]

test2 = [1, 1, 2, 3, 3]
test2_linked = create_linked(test2)
test2_out = [1, 2, 3]
