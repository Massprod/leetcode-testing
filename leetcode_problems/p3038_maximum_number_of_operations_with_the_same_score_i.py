# You are given an array of integers nums. Consider the following operation:
#  - Delete the first two elements nums and define the score of the operation
#    as the sum of these two elements.
# You can perform this operation until nums contains fewer than two elements.
# Additionally, the same score must be achieved in all operations.
# Return the maximum number of operations you can perform.
# -------------------------
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 1000


def max_operations(nums: list[int]) -> int:
    # working_sol (100.00%, 97.85%) -> (0ms, 17.55mb)  time: O(n) | space: O(1)
    out: int = 1
    operation: int = nums[0] + nums[1]
    for index in range(3, len(nums), 2):
        new_operation: int = nums[index] + nums[index - 1]
        if operation == new_operation:
            out += 1
        else:
            break

    return out


# Time complexity: O(n) <- n - length of the input array `nums`
# Always traversing whole input array `nums`, once => O(n).
# -------------------------
# Auxiliary space: O(1)
# Only two constant INTs used, none of them depends on input => O(1).


test: list[int] = [3, 2, 1, 4, 5]
test_out: int = 2
assert test_out == max_operations(test)

test = [1, 5, 3, 3, 4, 1, 3, 2, 2, 3]
test_out = 2
assert test_out == max_operations(test)

test = [5, 3]
test_out = 1
assert test_out == max_operations(test)
