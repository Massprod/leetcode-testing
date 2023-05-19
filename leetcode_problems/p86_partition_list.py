# Given the head of a linked list and a value x,
# partition it such that all nodes less than x come before nodes greater than or equal to x.
#
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
    # working_sol(38.83%, 13.38%) -> (44ms, 16.5mb)  time: O(n) | space: O(n)
    lower: list[int] = []
    higher: list[int] = []
    if not head:
        return head
    tempo: ListNode = head
    while tempo:
        if tempo.val >= x:
            higher.append(tempo.val)
        if tempo.val < x:
            lower.append(tempo.val)
        tempo = tempo.next
    whole: list[int] = lower + higher
    tempo = new_link = ListNode()
    for index in range(len(whole)):
        tempo.val = whole[index]
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


test1 = [1, 4, 3, 2, 5, 2]
test1_x = 3
test1_out = [1, 2, 2, 4, 3, 5]
linked = create_linked(test1)
test_tempo = test = partition(linked, test1_x)
print(test)
for _ in range(len(test1_out)):
    assert test_tempo.val == test1_out[_]
    test_tempo = test_tempo.next
    if _ == len(test1_out) == 0:
        assert test.next is None
del test

test2 = [2, 1]
test2_x = 2
test2_out = [1, 2]
linked = create_linked(test2)
test_tempo = test = partition(linked, test2_x)
print(test)
for _ in range(len(test2_out)):
    assert test_tempo.val == test2_out[_]
    test_tempo = test_tempo.next
    if _ == len(test2_out) == 0:
        assert test.next is None
del test

test3 = [0]
test3_x = 1
test3_out = [0]
linked = create_linked(test3)
test_tempo = test = partition(linked, test3_x)
print(test)
for _ in range(len(test3_out)):
    assert test_tempo.val == test3_out[_]
    test_tempo = test_tempo.next
    if _ == len(test3_out) == 0:
        assert test.next is None
del test

test4 = []
test4_x = 0
test4_out = []
test = partition(test4, test4_x)
assert test == []
