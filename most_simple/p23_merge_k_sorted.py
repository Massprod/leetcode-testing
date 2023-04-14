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
    # 100% sure it's working solution, may be slow. But working.
    # and there's either bug or I don't know leetcode Raises IndexError
    # on any index call on values list. But prints every index and value....
    # like !for _ in values: print(_)! is executing no problem
    # !len(values)! - same, correct len and printed
    # !but values[0]! == index error. WHAT????
    # ------------------
    # values = []
    # for _ in lists:
    #     tempor = _
    #     while tempor:
    #         values.append(tempor.val)
    #         tempor = tempor.next
    # values.sort()
    # new = ListNode(val=values[0])
    # cursor = new
    # for _ in values[1:]:
    #     new_chain = ListNode(val=_)
    #     cursor.next = new_chain
    #     cursor = new_chain
    # return new
    # ------------------
    # Same solution but without calling indexes of a values list
    # working_sol (98.40%, 13.43%)
    values = []
    for _ in lists:
        while _:
            values.append(_.val)
            _ = _.next
    values.sort()
    new = cursor = ListNode(val=0)
    for _ in values:
        cursor.next = ListNode(val=_)
        cursor = cursor.next
    return new.next  # don't like this part of returning NEXT in created list. This is why I wanted to add values[0]


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
