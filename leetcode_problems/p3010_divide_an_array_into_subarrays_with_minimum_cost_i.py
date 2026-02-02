# You are given an array of integers nums of length n.
# The cost of an array is the value of its first element.
# For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.
# You need to divide nums into 3 disjoint contiguous subarrays.
# Return the minimum possible sum of the cost of these subarrays
# --- --- --- ---
# 3 <= n <= 50
# 1 <= nums[i] <= 50


def minimum_cost(nums: list[int]) -> int:
    # working_solution: (100%, 33.68%) -> (0ms, 19.35mb)  Time: O(n * log n) Space: O(n)
    # No matter the order. 0 - index is always the first one to use.
    # And the other 2 values are always the smallest we could find in the array.
    out: int = nums[0]
    out += sum(
        sorted(nums[1:])[:2]
    )

    return out


# Time complexity: O(n * log n)
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [1, 2, 3, 12]
test_out: int = 6
assert test_out == minimum_cost(test)

tst = [5, 4, 3]
test_out = 12
assert test_out == minimum_cost(test)

test = [10, 3, 1, 1]
test_out = 12
assert test_out == minimum_cost(test)
