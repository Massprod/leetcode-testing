# You are given an integer array nums.
# You may delete any number of elements from nums.
# The remaining elements keep their original order.
# The resulting array a is sharp if the bitwise XOR of every pair of adjacent elements
#  is non-zero.
# That is, a[i] XOR a[i + 1] != 0 for every index i such that 0 <= i < a.length - 1.
# An array with at most one element is sharp.
# Return the minimum number of deletions needed to make nums sharp.
# Bitwise XOR compares the corresponding bits of two integers.
# A bit in the result is 1 if the corresponding bits differ, and 0 otherwise.
# --- --- --- ---
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 100


def min_deletions(nums: list[int]) -> int:
    # working_solution: (100%, 27.76%) -> (0ms, 19.22mb)  Time: O(n) Space: O(n)
    stack: list[int] = []
    for num in nums:
        if stack and stack[-1] == num:
            continue
        stack.append(num)

    return len(nums) - len(stack)


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [1, 1, 2, 2, 2, 3]
test_out: int = 3
assert test_out == min_deletions(test)

test = [4, 4, 9, 4]
test_out = 1
assert test_out == min_deletions(test)
