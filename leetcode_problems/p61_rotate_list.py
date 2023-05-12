# Given the head of a linked list, rotate the list to the right by k places.
#   -100 <= Node.val <= 100
#   0 <= k <= 2 * 109
#   The number of nodes in the list is in the range [0, 500].
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def create_linked(to_link: list[int]) -> ListNode:
    temp = linked = ListNode(val=to_link[0])
    for _ in to_link[1:]:
        new_node = ListNode(val=_)
        temp.next = new_node
        temp = new_node
    return linked


def rotate_right(head: ListNode, k: int) -> ListNode:
    if k == 0:
        return head
    values: list[int] = []
    tempo = head
    while tempo:
        values.append(tempo.val)
        tempo = tempo.next
    for _ in range(k):
        to_rotate = values[-1]
        values.pop()
        values.insert(0, to_rotate)
    tempo = rotated = ListNode(val=values[0])
    for _ in values[1:]:
        new_node = ListNode(val=_)
        tempo.next = new_node
        tempo = new_node
    return rotated

# Ok. First of all there's no mentioning of changing it in place, and we're returning -> ListNode.
# So, basically we can just take all values and switch [-1] to [0], k - times.
# Don't know if it is even possible to do this inplace, try this ^^ first.


test1 = [1, 2, 3, 4, 5]
test1_k = 2
test1_out = [4, 5, 1, 2, 3]
test1_linked = create_linked(test1)
assert rotate_right(test1_linked, test1_k)
print(rotate_right(test1_linked, test1_k))

test2 = [0, 1, 2]
test2_k = 4
test2_out = [2, 0, 1]
test2_linked = create_linked(test2)
assert rotate_right(test2_linked, test2_k)
print(rotate_right(test2_linked, test2_k))

test3 = [1, 2, 3]
test3_k = 0
test3_out = [1, 2, 3]
test3_linked = create_linked(test3)
assert rotate_right(test3_linked, test3_k)
print(rotate_right(test3_linked, test3_k))
