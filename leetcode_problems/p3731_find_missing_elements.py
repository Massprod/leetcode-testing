# You are given an integer array nums consisting of unique integers.
# Originally, nums contained every integer within a certain range.
# However, some integers might have gone missing from the array.
# The smallest and largest integers of the original range are still present in nums.
# Return a sorted list of all the missing integers in this range.
# If no integers are missing, return an empty list.
# --- --- --- ---
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 100


def find_missing_elements(nums: list[int]) -> list[int]:
    # working_solution: (100%, 100%) -> (3ms, 17.71mb)  Time: O(n + (max(nums) - min(nums))) Space: O(n + (max(nums) - min(nums)))
    fast_nums: set[int] = set(nums)
    range_start: int = min(fast_nums)
    range_end: int = max(fast_nums)
    out: list[int] = []

    for val in range(range_start, range_end):
        if val in fast_nums:
            continue
        out.append(val)

    return out


# Time complexity: O(n)
# Always traversing the whole input array `nums` => O(n).
# Traversing every value of the range(max(nums) - min(nums)) => O(n + (max(nums) - min(nums))).
# --- --- --- ---
# Space complexity: O(n)
# `fast_nums` <- allocates space for each unique value of `nums` => O(n)
# `out` <- allocates space for each missing value of the range(min(nums), max(nums)) =>
# => O(n + (max(nums) - min(nums)))


test: list[int] = [1, 4, 2, 5]
test_out: list[int] = [3]
assert test_out == find_missing_elements(test)

test = [7, 8, 6, 9]
test_out = []
assert test_out == find_missing_elements(test)

test = [5, 1]
test_out = [2, 3, 4]
assert test_out == find_missing_elements(test)
