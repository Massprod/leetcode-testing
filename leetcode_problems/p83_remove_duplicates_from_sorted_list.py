# Given the head of a sorted linked list,
# delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.
# ---------------------
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


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


def delete_duplicates(head: ListNode) -> ListNode | None:
    # working_sol (23.43%, 34.50%) -> (57ms, 16.3mb)  time: O(n + m) | space: O(2(log n))
    if not head:
        return head
    to_link: list[int] = [head.val]
    temp = head.next
    while temp:
        if temp.val != to_link[-1]:
            to_link.append(temp.val)
        if temp.next is None:
            break
        temp = temp.next
    if len(to_link) == 0:
        return None
    temp = new_linked = ListNode()
    for x in range(len(to_link)):
        temp.val = to_link[x]
        if x != (len(to_link) - 1):
            temp.next = ListNode()
            temp = temp.next
    return new_linked


# Time complexity: O(n + m) -> looping once through whole input linked_list
#                              and creating list without duplicates => O(n) ->
#                              -> looping once through created no_duplicates list and creating new linked_list => O(m).
#
# Space complexity: O(2(log n)) -> list to store path_values, with size of == part of the input => O(log n) ->
#                                     -> creating linked list of the same size => O(log n) -> O(2(log n)).
# n - size of input l_list ^^
# m - size of no_duplicates list ^^
# ---------------------
# ! Maybe it's more correct to say time: O(n + n) and space O(2n) -> because in a worst case ->
#   there's no duplicates, and we're looping through whole input + created list of the same size => O(n + n)
#   space to store this is same as input, because we're just copying it => O(2n)
#   Not sure. !
# ---------------------
# Reusing problem 82, because it's a mirror and no reasons to create something from a scratch.
# Just need to rebuild duplicate_check part.


test1 = [1, 1, 2]
test1_linked = create_linked(test1)
test1_out = [1, 2]
test = delete_duplicates(test1_linked)
print(test)
t_one_linked(test, test1_out)
del test

test2 = [1, 1, 2, 3, 3]
test2_linked = create_linked(test2)
test2_out = [1, 2, 3]
test = delete_duplicates(test2_linked)
print(test)
t_one_linked(test, test2_out)
del test

test3 = [0, 0, 1, 1, 1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5]
test3_linked = create_linked(test3)
test3_out = [0, 1, 2, 3, 4, 5]
test = delete_duplicates(test3_linked)
print(test)
t_one_linked(test, test3_out)
del test
