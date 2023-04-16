# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
#
# For example, for arr = [1,2,3], the following are all the permutations of arr:
# [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
# More formally, if all the permutations of the array are sorted in one container
# according to their lexicographical order, then the next permutation of that array
# is the permutation that follows it in the sorted container.
# If such arrangement is not possible,
# the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
#
# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3]
# because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.
#
# The replacement must be in place and use only constant extra memory.


def next_perm(nums: list[int]) -> None:
    # working_sol (87.24%, 97.43%)
    length = len(nums)
    x = length - 1  # max_index
    while x >= 1 and nums[x - 1] >= nums[x]:  # largest value index
        x -= 1
    if x <= 0:
        nums.sort()
        return
    y = length - 1
    while nums[y] <= nums[x - 1]:
        y -= 1
    nums[x - 1], nums[y] = nums[y], nums[x - 1]
    nums[x:] = nums[len(nums) - 1: x - 1: -1]  # reversing nums[x:] slice
    # len(nums) - 1 - last index
    # x - 1 - cuz stop - excluded
    # -1 - step, reverse read

test1 = [1, 2, 3]
test1_out = [1, 3, 2]
next_perm(test1)
print(test1)
assert test1 == test1_out

test2 = [3, 2, 1]
test2_out = [1, 2, 3]
next_perm(test2)
print(test2)
assert test2 == test2_out

test3 = [1, 1, 5]
test3_out = [1, 5, 1]
next_perm(test3)
print(test3)
assert test3 == test3_out

test4 = [2, 3, 1]
test4_out = [3, 1, 2]
next_perm(test4)
print(test4)
assert test4 == test4_out


# Condensed mathematical description:
#
# Find the largest index i such that array[i − 1] < array[i].
# (If no such i exists, then this is already the last permutation.)
#
# Find the largest index j such that j ≥ i and array[j] > array[i − 1].
#
# Swap array[j] and array[i − 1].
#
# Reverse the suffix starting at array[i].
#
# Overall, this algorithm to compute the next
# lexicographical permutation has Θ(n) worst-case time complexity,
# and Θ(1) space complexity. Thus, computing every permutation requires Θ(n! × n) run time.
