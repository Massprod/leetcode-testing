# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
# ----------------------
# n == nums.length
# 1 <= n <= 5 * 10 ** 4
# -10 ** 9 <= nums[i] <= 10 ** 9
# ----------------------
# Follow-up: Could you solve the problem in linear time and in O(1) space?


def majority_element(nums: list[int]) -> int:
    # working_sol (56.50%, 55.22%) -> (174ms, 17.8mb)  time: O(n) | space: O(1)
    major_element: int = 0
    counter: int = 0
    for num in nums:
        if counter == 0:
            major_element = num
            counter = 1
        elif major_element == num:
            counter += 1
        elif major_element != num:
            counter -= 1
    return major_element


# Time complexity: O(n) -> traversing whole input_list once => O(n).
# n - len of input_list^^|
# Auxiliary space: O(1) -> 2 extra INTs, doesn't depends on input => O(1)
# ----------------------
# Yeah, correct -> https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
# Without knowing this Boyer_Moore algorithm, I couldn't do this in O(1) space.
# !
# It can be shown by way of negation that the algorithm can't output a non majority element. !
# ----------------------
# O(n) + space O(n) is easy with dictionary, but it's not O(1) space, and I have no idea how it can be done.
# This task marked as easy, so I guess it's just some math_theory you need to know otherwise,
# almost impossible to come up with by yourself.


test1 = [3, 2, 3]
test1_out = 3
assert test1_out == majority_element(test1)

test2 = [2, 2, 1, 1, 1, 2, 2]
test2_out = 2
assert test2_out == majority_element(test2)
