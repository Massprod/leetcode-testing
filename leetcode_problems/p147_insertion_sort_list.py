# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.
# The steps of the insertion sort algorithm:
#   Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
#   At each iteration, insertion sort removes one element from the input data, finds the location it belongs
#           within the sorted list and inserts it there.
# It repeats until no input elements remain.
# ------------------------
# The number of nodes in the list is in the range [1, 5000].
# -5000 <= Node.val <= 5000


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def insertion_sort_list(head: ListNode) -> ListNode:
    if not head:
        return head
    if head.next is None:
        return head
    tempo: ListNode = head
    min_node: ListNode = tempo
    max_node: ListNode = tempo
    tempo = tempo.next
    while tempo:
        current_node: ListNode = tempo
        if current_node.val >= max_node.val:
            max_node.next = current_node
            max_node = tempo
            tempo = tempo.next
            continue
        if min_node.val < current_node.val < max_node.val:
            tempo = tempo.next
            max_node.next = tempo
            between: ListNode = min_node
            while between.next.val < current_node.val:
                between = between.next
            to_place: ListNode = between.next
            between.next = current_node
            current_node.next = to_place
            continue
        if current_node.val <= min_node.val:
            tempo = tempo.next
            current_node.next = min_node
            min_node = current_node
            max_node.next = tempo
            continue
    return min_node


# Time complexity: O(n * n) -> can't see how it's not (n * (log n)), but it can't be (n * (log n)),
#                           because failing TimeLimit in p148 vs merge_sort, which is actual (n * (log n)) ->
#                           -> traversing input_list once, in the worst case each node we encounter after 3 node
#                           will search it place in between min, max nodes -> distance between min, max nodes is
#                           expanding on each step starting from 1 to n - 2 =>
#                           => so with each step we're searching (n - m), where's m is number of unchecked nodes ->
#                           => should be O((n - m1) + (n - m2) + (n - m3) + ... + (n - n - 2 )) ->
#
# ------------------------
# Won't use tests or something, because I already did this in p148.
# But in p148 my solution is ultra_slow, because it's constant space without Merge_sort and failing TimeLimit.
# And they made it, only passable with Merge_sort.
