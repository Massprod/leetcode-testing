# You are given an integer array nums.
# You must repeatedly apply the following merge operation
#  until no more changes can be made:
# If any two adjacent elements are equal, choose the leftmost such adjacent pair
#  in the current array and replace them with a single element equal to their sum.
# After each merge operation, the array size decreases by 1.
# Repeat the process on the updated array until no more changes can be made.
# Return the final array after all possible merge operations.
# --- --- --- ---
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 5​​​​


def merge_adjacent(nums: list[int]) -> list[int]:
    # working_solution: (42.04%, 36.29%) -> (157ms, 32.79mb)  Time: O(n) Space: O(n)
    stack: list[int] = []

    for num in nums:
        stack.append(num)
        while 1 < len(stack) and stack[-1] == stack[-2]:
            stack.append(stack.pop() + stack.pop())

    return stack


# Time complexity: O(n)
# n - length of the input array `nums`
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [3, 1, 1, 2]
test_out: list[int] = [3, 4]
assert test_out == merge_adjacent(test)

test = [2, 2, 4]
test_out = [8]
assert test_out == merge_adjacent(test)

test = [3, 7, 5]
test_out = [3, 7, 5]
assert test_out == merge_adjacent(test)
