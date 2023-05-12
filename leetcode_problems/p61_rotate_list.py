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
    pass


test1 = [1, 2, 3, 4, 5]
test1_k = 2
test1_out = [4, 5, 1, 2, 3]
test1_linked = create_linked(test1)
print(test1_linked)

test2 = [0, 1, 2]
test2_k = 4
test2_out = [2, 0, 1]
test2_linked = create_linked(test2)
print(test2_linked)
