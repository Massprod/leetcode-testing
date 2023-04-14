# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def swap_pairs(head: ListNode) -> ListNode:
    # working_sol (56.93%, 10.33%) 14mb
    counter = 0
    if not head:
        return head
    new = cursor = ListNode(val=head.val)
    while head.next:
        counter += 1
        if counter % 2 != 0:
            cursor.val = head.next.val
        cursor.next = ListNode(val=head.val)
        cursor = cursor.next
        head = head.next
    if counter % 2 == 0:
        cursor.val = head.val
    return new
    # ------------------------
    # working_googled_sol (38.79%, 95.17%) 0.3 mb winning against mine 13.7mb
    # if not head or head.next is None:
    #     return head
    # new = head.next
    # cursor = head
    # to_switch = None
    # while cursor and cursor.next:
    #     pair = cursor.next
    #     if to_switch:
    #         to_switch.next = pair
    #     cursor.next = pair.next
    #     pair.next = cursor
    #     to_switch = cursor
    #     cursor = cursor.next
    # return new



# Don't have enough practice with LinkedLists, but we're evolving :)
# Solution is working, but I'm sure there's way to change next to prev without counter.
# Googled solution more confusing and switching links inside a list instead of values like mine.
# In my solution we can just change counter and skip another Number of values but in googled.
# We just switch next-to-prev until we reach One with no NEXT pair to switch. Not really better than mine.
# Maybe after I learn more about linked_lists, will try to rebuild it.
# !without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)!
# Correct answer but I failed this condition. I'm not modifying values, but switching them.
# Still it's changing values not nodes. GG

test1_values = [1, 2, 3, 4, 5, 6, 8, 9, 10]
test1 = cursor = ListNode(val=test1_values[0])
for _ in test1_values[1:]:
    new_node = ListNode(val=_)
    cursor.next = new_node
    cursor = cursor.next
# print(test1)
test1_out_values = [2, 1, 4, 3]
test1_out = cursor = ListNode(val=test1_out_values[0])
for _ in test1_out_values[1:]:
    new_node = ListNode(val=_)
    cursor.next = new_node
    cursor = cursor.next
# print(test1_out)
print(swap_pairs(test1))