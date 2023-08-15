# Given the head of a linked list and a value x,
#   partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# ------------------------
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100  ,  -200 <= x <= 200


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


def partition(head: ListNode, x: int) -> ListNode:
    # working_sol(97.27%, 55.72%) -> (34ms, 16.38mb)  time: O(n) | space: O(n)
    # Store everything lower and higher than x.
    lower: list[int] = []
    higher: list[int] = []
    # Empty list -> insta return.
    if not head:
        return head
    tempo: ListNode = head
    while tempo:
        # Higher|Equal than x => right_side.
        if tempo.val >= x:
            higher.append(tempo.val)
        # Lower than x => left_side.
        if tempo.val < x:
            lower.append(tempo.val)
        tempo = tempo.next
    # Combine and recreate with correct order.
    whole: list[int] = lower + higher
    tempo = new_link = ListNode()
    for index in range(len(whole)):
        tempo.val = whole[index]
        # Last index should always point to None.
        if index != (len(whole) - 1):
            tempo.next = ListNode()
            tempo = tempo.next
    return new_link


# Time complexity: O(n) -> traversing once through whole input linked_list of n size O(n) ->
#                          -> creating new_linked_list of same size => O(n) --> O(n)
# Space complexity: O(n) -> creating lists with summary size of input linked_list ->
#                           -> merging them together and getting list of input_n size => O(n)
# n - number of values inside linked_list ^^
# ---------------------------
# Ok. I should have been considered incorrect input of None and make it return None.
# I was correct with thinking this is through but, I didn't think about incorrect input of None.
# ---------------------------
# ! The number of nodes in the list is in the range [0, 200] !
# How we return ListNode if there's NO input? Cuz any ListNode by default having val == 0, always should be [1, 200]?
# WTF? We given input -> HEAD type of ListNode -> ListNode() object by default having val=0 ->
# we just can't even start function without correct input how it can be 0?
# Even if ListNode_input will be 1 length, still going to have at least 1 value of 0 by default,
# and if ListNode_input length is 0 => means it doesn't exist, and we can't call a function?
# Ok.w.e. Let's try to fail.
# ---------------------------
# Most basic way and slowest (guess), is just recreate linked list from scratch.
# Loop once to take all values inside nodes ->
# -> create 2 lists of values: first => all values lower than x
#                              second => all values higher or equal than x
# first + second -> correct list of values -> creating a new linked_list with values from this list.
# There's no word about doing this in_place, so I will try this one first.


test: ListNode = create_linked([1, 4, 3, 2, 5, 2])
test_x: int = 3
test_out: list[int] = [1, 2, 2, 4, 3, 5]
test_tempo: ListNode = partition(test, test_x)
for _ in range(len(test_out)):
    assert test_tempo.val == test_out[_]
    test_tempo = test_tempo.next
    if _ == len(test_out) == 0:
        assert test.next is None

test = create_linked([2, 1])
test_x = 2
test_out = [1, 2]
test_tempo = partition(test, test_x)
for _ in range(len(test_out)):
    assert test_tempo.val == test_out[_]
    test_tempo = test_tempo.next
    if _ == len(test_out) == 0:
        assert test.next is None

test = create_linked([0])
test_x = 1
test_out = [0]
test_tempo = partition(test, test_x)
for _ in range(len(test_out)):
    assert test_tempo.val == test_out[_]
    test_tempo = test_tempo.next
    if _ == len(test_out) == 0:
        assert test.next is None
