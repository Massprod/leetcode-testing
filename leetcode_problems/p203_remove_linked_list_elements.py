# Given the head of a linked list and an integer val,
# remove all the nodes of the linked list that has Node.val == val, and return the new head.
# -------------------
# The number of nodes in the list is in the range [0, 10 ** 4].
# 1 <= Node.val <= 50
# 0 <= val <= 50
from random import randint, choice


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


def remove_elements(head: ListNode, val: int) -> ListNode | None:
    # working_sol (62.26%, 7.17%) -> (79ms, 21.9mb)  time: O(n) | space: O(n)
    if not head:
        return None
    new_full: ListNode | None = ListNode(-1)
    if head.val != val:
        new_full.val = head.val
        head = head.next
    new = new_full
    while head:
        if head.val != val:
            # if first value isn't correct
            if new.val == -1:
                new.val = head.val
                head = head.next
                continue
            new.next = ListNode(head.val)
            new = new.next
        head = head.next
    if new_full.val == -1:
        return None
    return new_full


# Time complexity: O(n) -> traversing whole input_list once => O(n)
# n - num of nodes in input_list^^|
# Auxiliary space: O(n) -> no values to delete, returning same list but recreated => O(n)
#                  Θ(log n) -> part of the original input_list will be returned as a new one => Θ(log n)
# -------------------
# There's no limits on space, so I can just rebuild original list, without doing this in_place.


test1 = create_linked([1, 2, 6, 3, 4, 5, 6])
test1_val = 6
test1_out = [1, 2, 3, 4, 5]
print(remove_elements(test1, test1_val))
t_one_linked(remove_elements(test1, test1_val), test1_out)

test2 = []
test2_val = 1
test2_out = []
print(remove_elements(test2, test2_val))
t_one_linked(remove_elements(test2, test2_val), test2_out)

test3 = create_linked([7, 7, 7, 7])
test3_val = 7
test3_out = []
print(remove_elements(test3, test3_val))
t_one_linked(remove_elements(test3, test3_val), test3_out)

test: list[int] = []
for x in range(0, 100):
    test.append(randint(1, 50))
test_link: ListNode = create_linked(test)
test_val: int = choice(test)
tested: ListNode = remove_elements(test_link, test_val)
print(test)
print(test_val, "val")
print(tested)
for _ in test:
    if _ == test_val:
        test.remove(_)
t_one_linked(tested, test)
