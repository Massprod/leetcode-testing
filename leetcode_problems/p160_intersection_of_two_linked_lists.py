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
    # working_sol (76.21%, 40.7) -> (163ms, 31.6mb)  time: O(n + m) | space: O(1)
    pointer_1: ListNode = headA
    pointer_2: ListNode = headB
    switched_A: bool = False
    switched_B: bool = False
    while pointer_1 != pointer_2:
        pointer_1, pointer_2 = pointer_1.next, pointer_2.next
        if pointer_1 == pointer_2:
            return pointer_2
        if pointer_1 is None and not switched_A:
            pointer_1 = headB
        if pointer_2 is None and not switched_B:
            pointer_2 = headA
    return pointer_2


# Time complexity: O(n + m) -> in the worst case we're traversing whole headA + inter, headB + inter,
# n - nodes of headA^^|        inter(inside headB) + inter(inside headA) -> O((n + m) + (log n + log  m)) ->
# m - nodes of headB^^|        -> we can ignore this (log n + log m) part => O(n + m).
# Auxiliary space: O(1) -> nothing extra that depends on input_lists => O(1)

# ---------------
# Ok. There's no extra math, just some logic that we can find collision point with extra travel.
# If we pass whole headA + intersection_node and after that start to move from headB once again,
# we're going to travel same distance as another pointer which started at headB
# and did the same transfer to headA -> x - headA, y - inter_node, z - headB ->
# x + y + z - distance of 1 pointer
# z + y + x - distance of 2 pointer
# x + y + z = z + y + x
# y = y + z + x - x - z -> y = y -> so we're hitting same distance after extra switch_travel.
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

test4_B = create_linked([2])
test4_both = create_linked([3])
tempo = test4_B
while tempo:
    if tempo.next is None:
        tempo.next = test4_both
        break
    tempo = tempo.next
test4_out = test4_both
assert test4_out == get_intersection_node(test4_both, test4_B)
