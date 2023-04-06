# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    head_list1 = list1
    values_list = []
    while head_list1:
        val = head_list1.val
        head_list1 = head_list1.next
        values_list.append(val)
    head_list2 = list2
    while head_list2:
        val = head_list2.val
        head_list2 = head_list2.next
        values_list.append(val)
    values_list.sort()
    if len(values_list) == 0:
        return head_list1
    new_sorted = ListNode(values_list[0])
    temp = new_sorted
    for _ in values_list[1:]:
        new_node = ListNode(_)
        temp.next = new_node
        temp = new_node
    return new_sorted

test_val = [1, 2, 4]
head1 = ListNode(val=test_val[0])
temp = head1
for _ in test_val[1:]:
    new_node = ListNode(_)
    temp.next = new_node
    temp = new_node
test_val2 = [1, 3, 4]
head2 = ListNode(val=test_val2[0])
temp = head2
for _ in test_val2[1:]:
    new_node = ListNode(_)
    temp.next = new_node
    temp = new_node


print(merge_two_lists([], ListNode(val=0)))