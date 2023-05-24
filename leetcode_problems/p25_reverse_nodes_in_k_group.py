# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
#   k is a positive integer and is less than or equal to the length of the linked list.
#   If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.
# -------------------------------
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000  ,  0 <= Node.val <= 1000
# -------------------------------
# Follow-up: Can you solve the problem in O(1) extra memory space?


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


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    if not head:
        return head
    if k == 1:
        return head
    steps: int = k
    step: int = 1
    tempo: ListNode = head
    path: list[ListNode] = [tempo]
    to_assign: ListNode = head
    complete: ListNode | None = None
    multiplier: int = 1
    while to_assign and to_assign.next:
        if tempo.next is None:
            break
        if tempo.next and step < steps:
            step += 1
            tempo = tempo.next
            path.append(tempo)
        if step == steps:
            to_assign: ListNode | None = None
            if tempo.next:
                to_assign = tempo.next
            reverse: ListNode = path[-1]
            to_link = reverse
            for x in range(len(path) - 2, -1, -1):
                to_link.next = path[x]
                to_link = to_link.next
            path.clear()
            step = 1
            to_link.next = to_assign
            tempo = to_assign
            path.append(tempo)
            if complete is None:
                complete = reverse
            else:
                temp: ListNode = complete
                for x in range(0, ((steps * multiplier) - 1)):
                    temp = temp.next
                temp.next = reverse
                multiplier += 1
    if complete:
        return complete
    if not complete:
        return head

# Space complexity: O(n) -> worst cas
#
# -------------------------------
# Pff. actually made it in 1 commit. Well experience with all this tasks didn't go to waste,
# already can see limit_cases and made count of problems like *not_complete* before failing commits.
# -------------------------------
# Monstrous solution to read, but I made it work...
# Really slow, because we're traversing in complete every time to insert at certain position,
# maybe I can somehow save last position in complete and insert on it, but still we would need to traverse it.
# -------------------------------
# Without trying to this in_place, we can just count steps and memorize state of list on 1 step,
# like: 1->2->3->4->5 , k = 2 => memorizing 1 with 1 step, doing k - 1 steps, stops at 2, memorizing 2.next =>
# every node we visit on step we're storing in a list and assigning them backwards ->
# [1, 2] <- list of nodes we walk through -> memorized node 2.next gives us what need to be next after first index ->
# 2.next == 3->4->5 -> assigning list backwards -> 2->1 and assign first index to memorized 2.next =>
# 2->1->3->4->5 and now we need to make steps * 2.
# ! steps-1 first point to reverse, steps+1 point to assign !
# -------------------------------
# No idea about O(1). First let's try to make at least something working.
# Comeback to this task after having some experience with linked_lists,
# but doing this in_place with O(1) still hard.


test1 = create_linked([1, 2, 3, 4, 5])
test1_k = 2
test1_out = [2, 1, 4, 3, 5]
test = reverse_k_group(test1, test1_k)
print(test)
t_one_linked(test, test1_out)
del test

test2 = create_linked([1, 2, 3, 4, 5])
test2_k = 3
test2_out = [3, 2, 1, 4, 5]
test = reverse_k_group(test2, test2_k)
print(test)
t_one_linked(test, test2_out)
del test

test3 = create_linked([2, 2, 3, 4, 5, 6, 8, 9, 10, 12, 11, 5, 4, 3])
test3_k = 3
test3_out = [3, 2, 2, 6, 5, 4, 10, 9, 8, 5, 11, 12, 4, 3]
test = reverse_k_group(test3, test3_k)
print(test)
t_one_linked(test, test3_out)
del test

test4 = create_linked([1, 2, 3, 4])
test4_k = 5
test4_out = [1, 2, 3, 4]
test = reverse_k_group(test4, test4_k)
print(test)
t_one_linked(test4, test4_out)
del test
