# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.
# --------------------
# The number of nodes in the list is n.
# 1 <= n <= 500  ,  -500 <= Node.val <= 500  ,  1 <= left <= right <= n
# --------------------
# Follow up: Could you do it in one pass?


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


# def full_list_reverse_between(head: ListNode, left: int, right: int) -> ListNode:
#     # working_sol -> but for case if we're reverse slices on all linked_list not just indexes left and right.
#     if not head:
#         return head
#     tempo: ListNode = head
#     slice_start: bool = False
#     sliced: list[int] = []
#     new_linked: ListNode = ListNode()
#     new_tempo: ListNode = new_linked
#     while tempo:
#         if tempo.next is None:
#             sliced.append(tempo.val)
#             for x in range(len(sliced) - 1, -1, -1):
#                 new_tempo.val = sliced[x]
#                 new_tempo.next = ListNode()
#                 if x == 0:
#                     new_tempo.next = None
#                 new_tempo = new_tempo.next
#             break
#         if tempo.val == right and tempo.next is None:
#             sliced.append(tempo.val)
#             for x in range(len(sliced) - 1, -1, -1):
#                 new_tempo.val = sliced[x]
#                 new_tempo.next = ListNode()
#                 if x == 0:
#                     new_tempo.next = None
#                 new_tempo = new_tempo.next
#             break
#         if tempo.val == right and tempo.next.val != right:
#             slice_start = False
#             sliced.append(tempo.val)
#             for x in range(len(sliced) - 1, -1, -1):
#                 new_tempo.val = sliced[x]
#                 new_tempo.next = ListNode()
#                 new_tempo = new_tempo.next
#             tempo = tempo.next
#             sliced.clear()
#             continue
#         if tempo.val == right and tempo.next.val == right:
#             sliced.append(tempo.val)
#             tempo = tempo.next
#             continue
#         if slice_start:
#             sliced.append(tempo.val)
#             tempo = tempo.next
#             continue
#         if tempo.val == left and not slice_start:
#             slice_start = True
#             sliced.append(tempo.val)
#             tempo = tempo.next
#             continue
#         new_tempo.val = tempo.val
#         if tempo.next is not None:
#             new_tempo.next = ListNode()
#             new_tempo = new_tempo.next
#         tempo = tempo.next
#     return new_linked


def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    # working_sol (64.51%, 9.51%) -> (36ms, 16.5mb)  time: O(2n) | space: O(n)
    if not head:
        return head
    tempo: ListNode = head
    slice_start: bool = False
    sliced: list[int] = []
    new_linked: ListNode = ListNode()
    new_tempo: ListNode = new_linked
    step: int = 1
    while tempo:
        if tempo.next is None:
            sliced.append(tempo.val)
            for x in range(len(sliced) - 1, -1, -1):
                new_tempo.val = sliced[x]
                new_tempo.next = ListNode()
                if x == 0:
                    new_tempo.next = None
                new_tempo = new_tempo.next
            break
        if step == right:
            sliced.append(tempo.val)
            for x in range(len(sliced) - 1, -1, -1):
                new_tempo.val = sliced[x]
                new_tempo.next = ListNode()
                if x == 0:
                    new_tempo.next = tempo.next
                new_tempo = new_tempo.next
            break
        if slice_start:
            sliced.append(tempo.val)
            tempo = tempo.next
            step += 1
            continue
        if step == left:
            sliced.append(tempo.val)
            tempo = tempo.next
            step += 1
            slice_start = True
            continue
        step += 1
        new_tempo.val = tempo.val
        if tempo.next is not None:
            new_tempo.next = ListNode()
            new_tempo = new_tempo.next
        tempo = tempo.next
    return new_linked


# Time complexity: O(2n) -> worst case, we're looping once through whole l_input_list => O(n) ->
# n - length of l_input_list^^ -> and our left, right = first, last indexes of l_input_list,
#                              so we're extra looping through sliced with size of l_input_list => O(n) ->
#                              -> leaving us with 2 full loops on l_input_list => O(2n)
# Space complexity: O(2n) -> worst case, recreating full size of l_input_list into a sliced => O(n) ->
#                            -> and creating a new_linked list size of a sliced => O(n) -> O(2n)
# --------------------
# Ways to optimise:
#   - first we can store link's to a nodes inside l_input_list, not values. Same as p25.
#   - second we can ignore creating of a new linked_list with ListNode(),
#     and just made it link to already existing nodes in l_input_list,
#     just assign stored nodes like this -> new_tempo = sliced[-1] etc.
#   ! Guess I was just tired after solving p25, or didn't want to repeat it. Created something like this.
#     Not really bad, but this 2 ways already culling memory to O(n). Something new is always good. !
# --------------------
# Failed 1 commit, only because I didn't think it was such easy task, and made it work for encounter of INTs.
# Meanwhile, task description asks only about indexes...Still a fail...
# I need to be more cautions with task_descriptions.
# --------------------
# Actually why bother? We're not assigned to do this in_place, so why not just store slice from left to right values,
# and store everything else in 2 lists: before_left, after_right. Merge all 3 of them, but with reversed slice.
# Horrible on space, but simpler.
# --------------------
# For one way solution, as I understand it. We cannot traverse original linked_list more than once.
# But we can store needed slice and use it to reassign (left - 1) node and (right + 1) nodes,
# in reverse order of stored nodes, and restore path after this.
# Otherwise, I have no idea how to do this in *one_pass*. At least make this one work.
# --------------------
# Thought about using it to actually practice p25, for space O(1). But this is not going to be one_pass solution.
# So better to just do it as one_pass solution, and revisit for practice in p25 sometime else.


test1 = create_linked([1, 2, 3, 4, 5])
test1_left = 2
test1_right = 4
test1_out = [1, 4, 3, 2, 5]
test = reverse_between(test1, test1_left, test1_right)
print(test)
t_one_linked(test, test1_out)
del test

test2 = create_linked([5])
test2_left = 1
test2_right = 1
test2_out = [5]
test = reverse_between(test2, test2_left, test2_right)
print(test)
t_one_linked(test, test2_out)
del test

test3 = create_linked([1, 4, 5, 2, 1, 1, 1, 2, 2])
test3_left = 4
test3_right = 5
test3_out = [1, 4, 5, 1, 2, 1, 1, 2, 2]
test = reverse_between(test3, test3_left, test3_right)
print(test)
t_one_linked(test, test3_out)
del test

# test4 - failed -> Ok. I didn't understand task correctly, I was thinking we should reverse slice from value to value,
#                   like we encounter int == left, we're starting reversing until we hit last on a way int == right,
#                   -> my solution actually is harder, because I'm switching every possible combination on the way,
#                   like in test3. But in this task we're given POSITION, index or step from and to.
#                   So I just need to reverse slice from pos1 to pos2, not every possible option in linked_list...
test4 = create_linked([3, 5])
test4_left = 1
test4_right = 2
test4_out = [5, 3]
test = reverse_between(test4, test4_left, test4_right)
print(test)
t_one_linked(test, test4_out)
del test
