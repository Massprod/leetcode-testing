# Given the head of a linked list, return the list after sorting it in ascending order.
# --------------------
# The number of nodes in the list is in the range [0, 5 * 104].
# -105 <= Node.val <= 105
# --------------------
# Follow up: Can you sort the linked list in O(n log n) time and O(1) memory (i.e. constant space)?
from random import randint


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


def sort_list(head: ListNode) -> ListNode:
    if not head:
        return head
    if head.next is None:
        return head
    tempo: ListNode = head
    min_node: ListNode = tempo
    max_node: ListNode = tempo
    tempo = tempo.next
    while tempo:
        # print(head)
        current: int = tempo.val
        current_node: ListNode = tempo
        if current >= max_node.val:
            max_node.next = current_node
            max_node = tempo
            tempo = tempo.next
            continue
        if min_node.val < current < max_node.val:
            # print(min_node, "min")
            # print(max_node, "max")
            tempo = tempo.next
            max_node.next = current_node.next
            between: ListNode = min_node
            # print(max_node, "max2")
            while between.next.val < current:
                between = between.next
            to_place: ListNode = between.next
            between.next = current_node
            current_node.next = to_place
            # print(min_node, "min2")
            continue
        if current < min_node.val:
            tempo = tempo.next
            current_node.next = min_node
            min_node = current_node
            max_node.next = tempo
            continue
    return min_node


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

test4 = create_linked([3, 4, 1])
test = sort_list(test4)
print(test)


# extra slow for this
# for _ in range(50):
#     test_list = [randint(-500, 500) for _ in range(0, 10000)]
#     test_linked = create_linked(test_list)
#     test = sort_list(test_linked)
#     test_list.sort()
#     t_one_linked(test, test_list)
#     print(test)
#     print(test_list)
