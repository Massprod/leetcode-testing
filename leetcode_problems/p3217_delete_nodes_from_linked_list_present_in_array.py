# You are given an array of integers nums and the head of a linked list.
# Return the head of the modified linked list after removing all nodes
#  from the linked list that have a value that exists in nums.
# --------------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 5
# All elements in nums are unique.
# The number of nodes in the given list is in the range [1, 10 ** 5].
# 1 <= Node.val <= 10 ** 5
# The input is generated such that there is at least one node in the linked list
#  that has a value not present in nums.
from utils.linked_list import ListNode, create_linked, t_linked


def modified_list(nums: list[int], head: ListNode) -> ListNode:
    # working_sol (84.36%, 70.63%) -> (701ms, 55.00mb)  time: O(n + k) | space: O(k)
    fast_nums: set[int] = set(nums)
    # We can't have `prev_node` before `head`.
    # So, we just delete everything before.
    while head.val in fast_nums:
        head = head.next
    prev_node: ListNode = head
    cur_node: ListNode = head
    while cur_node:
        # We delete and stay at the same spot.
        if cur_node.val in fast_nums:
            prev_node.next = cur_node.next
        # We just move to the next spot.
        else:
            prev_node = cur_node
        cur_node = cur_node.next
    return head


# Time complexity: O(n + k) <- n - number of Nodes inside the input linked list `head`, k - length of the `nums`.
# Creating `fast_nums` with equal size to `nums` => O(k).
# Always traversing every Node of the `head`, once => O(n + k).
# --------------------------
# Auxiliary space: O(k).
# `fast_nums` <- allocates space for each unique value from `nums` => O(k).


test: ListNode = create_linked([1, 2, 3, 4, 5])
test_list: list[int] = [1, 2, 3]
test_out: ListNode = create_linked([4, 5])
t_linked(modified_list(test_list, test), test_out)

test = create_linked([1, 2, 1, 2, 1, 2])
test_list = [1]
test_out = create_linked([2, 2, 2])
t_linked(modified_list(test_list, test), test_out)

test = create_linked([1, 2, 3, 4])
test_list = [5]
test_out = create_linked([1, 2, 3, 4])
t_linked(modified_list(test_list, test), test_out)

test = create_linked([3, 7, 1, 8, 1])
test_list = [1, 7, 6, 2, 4]
test_out = create_linked([3, 8])
t_linked(modified_list(test_list, test), test_out)
