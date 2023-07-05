# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
# Return 0 if there is no such subarray.
# ----------------------
# 1 <= nums.length <= 10 ** 5
# nums[i] is either 0 or 1.


def longest_subarray(nums: list[int]) -> int:
    # working_sol (23.1%, 89.50%) -> (416ms, 18.8mb)  time: O(n) | space: O(1)
    # always should delete 1 element
    if len(nums) == 1:
        return 0
    zero_count: int = 0
    longest: int = 0
    left: int = 0
    right: int = 0
    while right != len(nums):
        # counting zeroes in window
        if nums[right] == 0:
            zero_count += 1
        # delete exceeding
        if zero_count > 1:
            while zero_count > 1 and left < len(nums):
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            longest = max(longest, right - left)
            right += 1
            continue
        # if only 0 zero we can delete it and calc length
        # no matter the place -> 0 1 1 1 1 or 1 0 1 1 1
        # it's always (right - left), zero indexed by default
        # no need to  extract 1 from length^^
        longest = max(longest, right - left)
        right += 1
    return longest

# Time complexity: O(n) -> in the worst case like: 1, 0, 0, 0, 1 ->
# n - len of nums^^|       -> we're going to traverse whole input once with right pointer => O(n) ->
#                          -> and to delete every exceeding zero, we're extra traversing n - 2 elements =>
#                          => O(n - 2) -> O(n) + O(n - 2) => O(2n) => O(n).
# Auxiliary space: O(1) -> only constants used, none of them depends on input_list => O(1).
# ----------------------
# Window problem?
# Window from 0 to x with counting every 0 in it and shrink only when count(0) expends 1.
# But we need to maintain 0 without count() it's too slow.


test1 = [1, 1, 0, 1]
test1_out = 3
print(longest_subarray(test1))
assert test1_out == longest_subarray(test1)

test2 = [0, 1, 1, 1, 0, 1, 1, 0, 1]
test2_out = 5
print(longest_subarray(test2))
assert test2_out == longest_subarray(test2)

test3 = [1, 1, 1]
test3_out = 2
print(longest_subarray(test3))
assert test3_out == longest_subarray(test3)

test4 = [0]
test4_out = 0
print(longest_subarray(test4))
assert test4_out == longest_subarray(test4)

test5 = [0, 1]
test5_out = 1
print(longest_subarray(test5))
assert test5_out == longest_subarray(test5)

test6 = [0, 0, 0]
test6_out = 0
print(longest_subarray(test6))
assert test6_out == longest_subarray(test6)
