# Given an array of n integers nums, a 132 pattern is a subsequence of three integers
#  nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
# Return true if there is a 132 pattern in nums, otherwise, return false.
# -------------------
# n == nums.length
# 1 <= n <= 2 * 10 ** 5
# -10 ** 9 <= nums[i] <= 10 ** 9
from random import randint


def find_132(nums: list[int]) -> bool:
    # working_sol (24.11%, 98.78%) -> (424ms, 36.2mb)  time: O(n) | space: O(n)
    if len(nums) < 3:
        return False
    # [0] doesn't have smallest, we don't check it.
    # But it's better to use placeholder for easier loop.
    # 'i' values.
    left_smallest: list[int] = [10 ** 9]
    for num in nums:
        left_smallest.append(
            min(
                left_smallest[-1],  # there's some left_side value which is lower.
                num,  # there's nothing lower, we will reuse it as [-1].
            )
        )
    # 'k' values.
    stack: list[int] = []
    # Search for 'j' value, to satisfy:
    # ('i' < 'j' < 'k') and (nums[i] < nums[k] < nums[j])
    for j in range(len(nums) - 1, 0, -1):
        # nums[i] == nums[j] <- not allowed.
        # Means there's no smaller value on left_side, no reasons to consider.
        if nums[j] == left_smallest[j]:
            continue
        # nums[i] < nums[k]
        while stack and not stack[-1] > left_smallest[j]:
            stack.pop()
        # nums[k] < nums[j]
        if stack and stack[-1] < nums[j]:
            return True
        stack.append(nums[j])
    return False


# Time complexity: O(n) -> traversing whole input array to get all minimum_prefixes => O(n) ->
# n - len of input array^^| -> traversing again in reverse to get value 'j' => O(n).
# Auxiliary space: O(n) -> extra array with same size as input array => O(n) -> stack with size == (n - 2) if array
#                          in descending order after [0] index, and [0] is smallest of all values ->
#                          -> we will add everything: (stack[-1] > nums[j]) and all smallest values
#                          will be equal to nums[0] => O(n) - linear anyway.
# -------------------
# Find every left side smallest for every index except 0, cuz it can have left side.
# Then find anything that have higher value than it's left_side smallest.
# Only question how to maintain right_side?
# Like we need something higher than left_side smallest, but lower than current.
# Stack? With all values on right side which higher than smallest, and lower than current.
# Should be correct.


test: list[int] = [1, 2, 3, 4]
test_out: bool = False
assert test_out == find_132(test)

test = [3, 1, 4, 2]
test_out = True
assert test_out == find_132(test)

test = [-1, 3, 2, 0]
test_out = True
assert test_out == find_132(test)

test = [randint(-10 ** 9, 10 ** 9) for _ in range(10 ** 4)]
print(test)
