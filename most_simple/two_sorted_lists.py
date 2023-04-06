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


def merge_two_lists(list1: ListNode, lis2: ListNode) -> ListNode:
    pass




test_val = [1, 2 , 4]
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

print(head1, head2)

