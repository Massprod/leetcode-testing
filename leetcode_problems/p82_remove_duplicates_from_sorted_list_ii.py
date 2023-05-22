# Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# Return the linked list sorted as well.
# --------------------------
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


def delete_duplicates(head: ListNode) -> ListNode | None:
    # working_sol (38.60%, 15.26%) -> (50ms, 16.3mb)  time: O(n + m) | space: O(m + (log n))
    if not head:
        return head
    prev_val: int = head.val
    to_link: list[int] = [prev_val]
    temp = head.next
    while temp:
        if prev_val == temp.val:
            temp = temp.next
            if len(to_link) == 0:
                continue
            if len(to_link) != 0 and to_link[-1] == prev_val:
                to_link.pop()
            continue
        if prev_val != temp.val:
            prev_val = temp.val
            to_link.append(prev_val)
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
# --------------------------
# Not obliged to do this in_place, so I will just rebuild linked_list.
# ! The number of nodes in the list is in the range [0, 300] ! <- again this, returning empty head from start.
# --------------------------
# Next task with linked list, I will make universal test function, I don't like it overcomplicated like this.
# It's ok for testing just lists and I comment out something I don't need,
# but linked_lists need's to be treated better.


test1 = [1, 2, 3, 3, 4, 4, 5]
test1_linked = create_linked(test1)
test1_out = [1, 2, 5]
test = delete_duplicates(test1_linked)
print(test)
tempo = test
for _ in range(len(test1_out)):
    assert test1_out[_] == tempo.val
    tempo = tempo.next
del test

test2 = [1, 1, 1, 2, 3]
test2_linked = create_linked(test2)
test2_out = [2, 3]
test = delete_duplicates(test2_linked)
print(test)
tempo = test
for _ in range(len(test2_out)):
    assert test2_out[_] == tempo.val
    tempo = tempo.next
del test

# test3 - failed -> missed part with only duplicates...
test3 = [1, 1]
test3_linked = create_linked(test3)
test3_out = []
test = delete_duplicates(test3_linked)
print(test)
tempo = test
for _ in range(len(test3_out)):
    assert test3_out[_] == tempo.val
    tempo = tempo.next
del test

test4 = [0, 1, 2, 3, 3, 3, 3, 7, 9, 10, 10, 10]
test4_linked = create_linked(test4)
test4_out = [0, 1, 2, 7, 9]
test = delete_duplicates(test4_linked)
print(test)
tempo = test
for _ in range(len(test4_out)):
    assert test4_out[_] == tempo.val
    tempo = tempo.next
del test
