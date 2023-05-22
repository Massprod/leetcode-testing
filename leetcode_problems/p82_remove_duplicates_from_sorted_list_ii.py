# Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# Return the linked list sorted as well.
# ---------------------------
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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


def delete_duplicates(head: ListNode) -> ListNode:
    pass


test1 = [1, 2, 3, 3, 4, 4, 5]
test1_out = [1, 2, 5]

test2 = [1, 1, 1, 2, 3]
test2_out = [2, 3]
