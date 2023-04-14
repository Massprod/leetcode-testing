# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def swap_pairs(head: ListNode) -> ListNode:
    counter = 0
    if not head:
        return head
    new = cursor = ListNode(val=head.val)
    while head.next:
        counter += 1
        if counter % 2 != 0:
            cursor.val = head.next.val
        cursor.next = ListNode(val=head.val)
        cursor = cursor.next
        head = head.next
    if counter % 2 == 0:
        cursor.val = head.val
    return new

test1_values = [1, 2, 3, 4, 5, 6, 8, 9, 10]
test1 = cursor = ListNode(val=test1_values[0])
for _ in test1_values[1:]:
    new_node = ListNode(val=_)
    cursor.next = new_node
    cursor = cursor.next
# print(test1)
test1_out_values = [2, 1, 4, 3]
test1_out = cursor = ListNode(val=test1_out_values[0])
for _ in test1_out_values[1:]:
    new_node = ListNode(val=_)
    cursor.next = new_node
    cursor = cursor.next
# print(test1_out)
print(swap_pairs(test1))