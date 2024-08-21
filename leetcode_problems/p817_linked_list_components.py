# You are given the head of a linked list containing unique integer values
#  and an integer array nums that is a subset of the linked list values.
# Return the number of connected components in nums where two values
#  are connected if they appear consecutively in the linked list.
# --------------------------
# The number of nodes in the linked list is n.
# 1 <= n <= 10 ** 4
# 0 <= Node.val < n
# All the values Node.val are unique.
# 1 <= nums.length <= n
# 0 <= nums[i] < n
# All the values of nums are unique.
from utils.linked_list import ListNode, create_linked


def num_components(head: ListNode, nums: list[int]) -> int:
    # working_sol (85.89%, 6.17%) -> (72ms, 20.81mb)  time: O(n + k) | space: O(k)
    out: int = 0
    to_use: set[int] = set(nums)
    cur_seq: int = 0
    # All we care is a CONSECUTIVE sequence with presented in `nums` numbers.
    # If it breaks == PART we need.
    # We don't care about order, or anything else, only the presence.
    while head:
        if head.val in to_use:
            cur_seq = 1
        else:
            out += cur_seq
            cur_seq = 0
        head = head.next
    return out + cur_seq


# Time complexity: O(n + k) <- n - number of Node in the input LinkedList `head`, k - length of the input array `nums`.
# Always traversing `nums` to get all unique values => O(k).
# Extra traversing every Node in `head` => O(n + k).
# --------------------------
# Auxiliary space: O(k)
# `to_use` <- allocates space for each unique num in `nums` => O(k).


test: ListNode = create_linked([0, 1, 2, 3])
test_nums: list[int] = [0, 1, 3]
test_out: int = 2
assert test_out == num_components(test, test_nums)

test = create_linked([0, 1, 2, 3, 4])
test_nums = [0, 3, 1, 4]
test_out = 2
assert test_out == num_components(test, test_nums)
