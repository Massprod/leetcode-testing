# Given the heads of two singly linked-lists headA and headB, return the node
#   at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.
# ---------------
# The number of nodes of listA is in the m.
# The number of nodes of listB is in the n.
# 1 <= m, n <= 3 * 10 ** 4  ,  1 <= Node.val <= 10 ** 5
# ---------------
# Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?


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


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    # working_sol (73.7%, 7.71%) -> (164ms, 32.4mb)  time: O(n + m) | space: O(n)
    met: set[ListNode] = set()
    while headA:
        met.add(headA)
        headA = headA.next
    while headB:
        if headB in met:
            return headB
        headB = headB.next


# Time complexity: O(n + m) -> traversing both input_lists once => O(n + m).
# n - nodes in headA^^|
# m - nodes in headB^^|
# Auxiliary space: O(n) -> only node links from headA will be saved into a set() => O(n)
# ---------------
# No idea how to make this in O(1) memory, but we can make this in O(n + m) and O(n) memory.
# Guess there's something like tasks with Floyd_algorithm, if you don't know it you just can't do this.
# First commit with O(n) and search for extra_info after.

# Could change it into a function, but w.e. Easy task and no reasons to.
test1_A = create_linked([4, 1])
test1_B = create_linked([5, 6, 1])
test1_both = create_linked([8, 4, 5])
tempo = test1_A
while tempo:
    if tempo.next is None:
        tempo.next = test1_both
        break
    tempo = tempo.next
tempo = test1_B
while tempo:
    if tempo.next is None:
        tempo.next = test1_both
        break
    tempo = tempo.next
test1_out = test1_both
assert test1_out == get_intersection_node(test1_A, test1_B)

test2_A = create_linked([1, 9, 1])
test2_B = create_linked([3])
test2_both = create_linked([2, 4])
tempo = test2_A
while tempo:
    if tempo.next is None:
        tempo.next = test2_both
        break
    tempo = tempo.next
tempo = test2_B
while tempo:
    if tempo.next is None:
        tempo.next = test2_both
        break
    tempo = tempo.next
test2_out = test2_both
assert test2_out == get_intersection_node(test2_A, test2_B)

test3_A = create_linked([2, 6, 4])
test3_B = create_linked([1, 5])
test3_both = None
tempo = test3_A
while tempo:
    if tempo.next is None:
        tempo.next = test3_both
        break
    tempo = tempo.next
tempo = test3_B
while tempo:
    if tempo.next is None:
        tempo.next = test3_both
        break
    tempo = tempo.next
test3_out = test3_both
assert test3_out == get_intersection_node(test3_A, test3_B)
