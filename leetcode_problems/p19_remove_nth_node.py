# Given the head of a linked list, remove the nth node from the end of the list
# and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def remove_node(head: ListNode, n: int) -> ListNode:
    # working_sol (30.30%, 55.77%)
    length = 0
    tempo = head
    while tempo:
        tempo = tempo.next
        length += 1
    position = length - n
    tempo = ListNode()
    cursor = tempo
    for x in range(position + 1):
        if x == position:
            cursor.next = head.next
            break
        cursor.next = head
        head, cursor = head.next, head
    return tempo.next

# I'm sure there's no need to get length, but I have no idea how for now.
# There's a lot of linked_list tasks in a future, just revisit it later.
# Really need more practice with linked_lists. 2 tasks isn't enough to get them straight.


test_val = [1, 2, 3, 4, 5]
test1 = ListNode(val=test_val[0])
temp = test1
for _ in test_val[1:]:
    new_node = ListNode(val=_)
    temp.next = new_node
    temp = new_node
remove_node(test1, n=2)
