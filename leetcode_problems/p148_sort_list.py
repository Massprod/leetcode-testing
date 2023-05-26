# Given the head of a linked list, return the list after sorting it in ascending order.
# --------------------
# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105
# --------------------
# Follow up: Can you sort the linked list in O(n log n) time and O(1) memory (i.e. constant space)?
from random import randint
import time


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


def t_one_linked(to_test: ListNode, testout: list[int]) -> None:
    tempo: ListNode = to_test
    count: int = 0
    for _ in range(len(testout)):
        assert testout[_] == tempo.val
        tempo = tempo.next
        count += 1
    assert count == len(testout)


def sort_list_slow(head: ListNode) -> ListNode:
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
            max_node.next = current_node.next
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


# Time complexity: O(n * n)
# Space complexity: O(1) -> only links used.
# -----------------
# I don't see how this is not constant space O(1) solution.
# But what about time?
# We're traversing once through whole linked_input => O(n) ->
# -> placing min or max values on sides which should be O(1), we're always knowing where to place and
#    changing only next links => O(1) -> placing values in between, this part is really slow,
#    because in the worst case, we're going to traverse almost whole linked_input of n - 1.
#    last value will be placed inside, and it's only lower than max_node ->
# -> leaving us with path of (n - 1) to check before we inserting it => O(n) ->
# -> should be O(n * n)
# Taking median of 92s to solve with max_constraints:
#       num_of_nodes == (5 * (10 ** 4))
#       values == (-10 ** 5 <= value <= 10 ** 5)
# -----------------
# ! dummy = cur = ListNode()
#         intMax = float('inf')
#
#         while(node1 or node2):
#             value1, value2 = node1.val if(node1) else intMax, node2.val if(node2) else intMax
#             if(value1 < value2):
#                 cur.next = node1
#                 node1 = node1.next
#             else:
#                 cur.next = node2
#                 node2 = node2.next
#             cur = cur.next
#
#         return dummy.next
#   ^^Somewhat looking like space O(1) and they claim it is. But first they're using 2 recursions,
# which is already extra, but ok. Inside this recursion above, they're creating dummy =>
# => dummy is a new ListNode() with new value = 0, ok. -> than he populates this dummy with nodes from
# original linked list, ok. We can call it links, not just copies of linked list, but it's still using space
# to store this dummy and links inside of it. I'm not sure if it's O(1) (not alone here, comments) ->
# -> Guess I will just leave my solution, which is I think is correct O(1) because I'm operating only with links,
# without creating any new lists or changing values inside input. !
# -----------------
# Dunno about solutions with O(1) space, because every one of them having either recursion, or
# rebuild it, not from scratch but still changing values saved in traversing before.
# If I see it correctly my_solution didn't take any extra space, and we're operating only with links from original.
# Working, and correctly, but really slow, because inserting in the middle traversing whole slice inside.
# -----------------
# Flow with min_node fixed, I was inserting min_node and didn't change current_node, ended in a loop.
# Now we're ending it by assigning next value as max_node.next, because we're always having tempo ->
# which is n + 1 while max_node is n.
# -----------------
# Fun part, I actually made O(1) solution, but slow af. And I have one flow with inserting min_node.
# No way I could do this by myself, and even after searching I didn't find real O(1) space solution,
# either they're rebuilding it with sort() or just sort by themselves and rebuilding anyway.
# But none of the solutions change it without recursion or rebuilding.
# -----------------
# Rebuild, too slow to cover constraints even in my tests, and failing some tests anyway.
# -----------------
# 1 obvious solution with time => O(n + n * log n + n) ->
#   -> creating list of all values, sorting with python built_in, making new one.
# Slow and space will be O(2n) => storing list of values + extra linked list created.
# 2 solution I can think of is either recursion or while loop with 2 pointers,
# to min_max values.
# 1 solution is easy and already done similar tasks, guess it's time to think about 2 solution :)


def sort_list(head: ListNode) -> ListNode:
    # working_sol (27.27%, 37.62) -> (705ms, 38.7mb)  time: O(n * log n) | space: O(1)????
    if not head:
        return head
    if head.next is None:
        return head

    def halve(whole: ListNode) -> ListNode:
        fast = prev = slow = whole
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if prev:
            prev.next = None
        return slow

    def merge(left: ListNode, right: ListNode) -> ListNode:
        new_whole = tempo = ListNode()
        while left and right:
            if left.val > right.val:
                left, right = right, left
            tempo.next = left
            tempo = tempo.next
            left = left.next
        if left:
            tempo.next = left
        if right:
            tempo.next = right
        return new_whole.next

    half: ListNode = halve(head)
    if not half or head == half:
        return head
    return merge(sort_list(head), sort_list(half))


# Rebuilding with most looking like O(1) google solution.
# Only can call this O(1) if we're not counting recursion and counting one_new node as O(1).


test1 = create_linked([4, 2, 1, 3])
test1_out = [1, 2, 3, 4]
test = sort_list(test1)
t_one_linked(test, test1_out)
print(test)
del test

test2 = create_linked([-1, 5, 3, 4, 0])
test2_out = [-1, 0, 3, 4, 5]
test = sort_list(test2)
t_one_linked(test, test2_out)
print(test)
del test

test3 = create_linked([2, 3, 5, 4])
test3_out = [2, 3, 4, 5]
test = sort_list(test3)
t_one_linked(test, test3_out)
print(test)
del test


# extra slow for leet
timed: set = set()
for _ in range(10):
    t: float = time.time()
    test_list = [randint(-10 ** 5, 10 ** 5) for _ in range(0, 5 * (10 ** 4))]
    test_linked = create_linked(test_list)
    test = sort_list(test_linked)
    test_list.sort()
    t_one_linked(test, test_list)
    t: float = time.time() - t
    timed.add(t)
median: int = 0
for _ in timed:
    median += _
print(median/len(timed))
