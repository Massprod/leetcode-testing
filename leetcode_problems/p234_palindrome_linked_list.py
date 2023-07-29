# Given the head of a singly linked list, return true if it is a palindrome
#  or false otherwise.
# --------------
# The number of nodes in the list is in the range [1, 10 ** 5].
# 0 <= Node.val <= 9


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


def is_palindrome(head: ListNode) -> bool:
    # working_sol (99.93%, 99.35%) -> (477ms, 33.4mb)  time: O(n) | space: O(1)
    # There's only 1 node.
    if head.next is None:
        return True
    # There's only 2 nodes.
    if head.next.next is None:
        return head.val == head.next.val
    # Standard Floyd algorithm, to find a middle.
    slow: ListNode = head
    # Node == pre_slow.
    prev: ListNode = head
    fast: ListNode = head.next
    # We need to know if it's ODD/EVEN list,
    # cuz we need to either skip of check middle Node.
    count: int = 2
    # Switching nodes inplace, so we're using same head.
    # We're switching START -> MIDDLE into MIDDLE -> START,
    # so basically we need to reverse half of the list.
    # First node obviously need to have next == None to escape infinite_loop.
    first: bool = True
    while fast and fast.next is not None:
        # Standard case with 2 nodes skipped.
        count += 2
        fast = fast.next.next
        # Not standard case with 2 nodes skipped, but we landed
        # on empty spot, so it's not Node, and we need to decrease count by 1.
        if fast is None:
            count -= 1
        # Saving current slow node, before stepping further.
        tempo: ListNode = slow
        slow = slow.next
        # Didn't think about better swap with 1 node,
        # but we need it only once, and we can't switch before slow.next is taken.
        if first:
            head.next = None
            first = False
            continue
        # We reassign them like: 1 -> 2 -> 3 -> 4 -> 5 -> 6
        # We're saving 2 into tempo and slow is stepping further,
        # PREV is holding all nodes before current SLOW is saved in tempo.
        # PREV == [1] , TEMPO == [2] , SLOW == [3]
        # tempo.next -> should point to all previous nodes, which holds in prev.
        # PREV == [1] <- [2], TEMPO == [3] , SLOW =[4] etc.
        tempo.next = prev
        prev = tempo

    # Failed to make correct FAST break, so we need extra step
    # to take middle, with slow.
    tempo = slow
    slow = slow.next
    tempo.next = prev
    prev = tempo
    # And if it's ODD we don't need a MIDDLE Node.
    if count % 2 != 0:
        prev = prev.next
    # Standard traverse for 2 Halves:
    # MIDDLE -> END
    # MIDDLE -> START
    while slow:
        if slow.val != prev.val:
            return False
        slow = slow.next
        prev = prev.next
    return True

# Time complexity: O(n) -> traversing once to get the middle, then we're extra traversing both halves ->
# n - nodes of input_list^^| -> so it's should be O(2n), cuz we're using every Node twice.
# Auxiliary space: O(1) -> switching nodes in place -> count, first used as extras, both doesn't depend on input => O(1)
# --------------
# Ok a little robust, but it's working. Only part I don't understand how to skip it's
# how we can know if it's ODD or EVEN list. Because if it's ODD I need to extra skip middle value,
# and if it's not we need this value considered. Only way I come up with is extra traverse to count
# number of nodes, which is slow. Don't know, maybe there's a way to do this while checking?
# No way to do this while looking for a middle, cuz we're not always skipping 2 nodes, sometimes
# it's just landing on None. Hmm. Actually worked -> start from 2 cuz we already head.next
# and +2 for every loop until fast.next.next is None and we landed on None, so it should be +1.
# If we're landing on Node then it's still +2.
# Nice practice to remember nodes, and with follow up it's actually at least Medium task.
# --------------
# Follow up: Could you do it in O(n) time and O(1) space?
# TurtleHare and switch all nodes before middle?


test1 = create_linked([1, 2, 2, 1])
test1_out = True
assert test1_out == is_palindrome(test1)

test2 = create_linked([1, 2])
test2_out = False
assert test2_out == is_palindrome(test2)

test3 = create_linked([1, 2, 3, 4, 3, 2, 1])
test3_out = True
assert test3_out == is_palindrome(test3)

test4 = create_linked([1, 2, 3])
test4_out = False
assert test4_out == is_palindrome(test4)

test5 = create_linked([1])
test5_out = True
assert test5_out == is_palindrome(test5)
