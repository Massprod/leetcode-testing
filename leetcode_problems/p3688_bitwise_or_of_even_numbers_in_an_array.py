# You are given an integer array nums.
# Return the bitwise OR of all even numbers in the array.
# If there are no even numbers in nums, return 0.
# --- --- --- ---
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


def even_number_bitwise_or(nums: list[int]) -> int:
    # working_solution: (100%, 93.84%) -> (0ms, 17.68mb)  Time: O(n) Space: O(1)
    out: int = 0
    for num in nums:
        if num % 2:
            continue
        out = out | num

    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing the whole input array `nums`, once => O(n).
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, 2, 3, 4, 5, 6]
test_out: int = 6
assert test_out == even_number_bitwise_or(test)

test = [7, 9, 11]
test_out = 0
assert test_out == even_number_bitwise_or(test)

test = [1, 8, 16]
test_out = 24
assert test_out == even_number_bitwise_or(test)
