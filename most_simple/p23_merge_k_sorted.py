# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def merge_k_sorted(lists: list[ListNode]) -> ListNode:
    values = []
    for _ in lists:
        tempor = _
        while tempor:
            values.append(tempor.val)
            tempor = tempor.next
    values.sort()
    new = ListNode(val=values[0])
    cursor = new
    for _ in values[1:]:
        new_chain = ListNode(val=_)
        cursor.next = new_chain
        cursor = new_chain
    return new


test_values = [[1, 4, 5], [1, 3, 4], [2, 6]]
test1 = []
# creating linked lists to work with
for val in test_values:
    temp = ListNode(val=val[0])
    tempo = temp
    for _ in val[1:]:
        new_node = ListNode(val=_)
        tempo.next = new_node
        tempo = new_node
    test1.append(temp)
test1_out_values = [1, 1, 2, 3, 4, 4, 5, 6]
# creating linked list to test with
test1_out = ListNode(val=test1_out_values[0])
tempo = test1_out
for _ in test1_out_values[1:]:
    new_node = ListNode(val=_)
    tempo.next = new_node
    tempo = new_node
print(test1_out)
print(merge_k_sorted(test1))
existed = test1_out
new = merge_k_sorted(test1)
while new:
    assert new.val == existed.val
    new = new.next
    existed = existed.next
