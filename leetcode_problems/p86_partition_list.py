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
    lower: list[int] = []
    higher: list[int] = []
    tempo: ListNode = head
    while tempo:
        if tempo.val >= x:
            higher.append(tempo.val)
        if tempo.val < x:
            lower.append(tempo.val)
        tempo = tempo.next
    whole: list[int] = lower + higher
    print(whole)
    tempo = new_link = ListNode()
    for index in range(len(whole)):
        tempo.val = whole[index]
        if index != (len(whole) - 1):
            tempo.next = ListNode()
            tempo = tempo.next
    return new_link


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
print(partition(linked, test1_x))

test2 = [2, 1]
test2_x = 2
test2_out = [1, 2]
linked = create_linked(test2)
print(partition(linked, test2_x))
