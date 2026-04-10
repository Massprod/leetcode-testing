# You are given an integer array nums.
# A tuple (i, j, k) of 3 distinct indices is good if nums[i] == nums[j] == nums[k].
# The distance of a good tuple is abs(i - j) + abs(j - k) + abs(k - i),
#  where abs(x) denotes the absolute value of x.
# Return an integer denoting the minimum possible distance of a good tuple.
# If no good tuples exist, return -1.
# --- --- --- ---
# 1 <= n == nums.length <= 100
# 1 <= nums[i] <= n


def minimum_distance(nums: list[int]) -> int:
    # working_solution: (100%, 48.66%) -> (0ms, 19.34mb)  Time: O(n * log n) Space: O(n)
    limit: int = 1_000
    out: int = limit
    vals: dict[int, list[int]] = {}
    for index, value in enumerate(nums):
        if value in vals:
            vals[value].append(index)
        else:
            vals[value] = [index]
    # We don't care about index order. But, we want to use the closest options possible.
    # So, take all of them in order and calc.
    for value, indexes in vals.items():
        ord_indexes: list[int] = sorted(indexes)
        end: int = 2
        while end < len(ord_indexes):
            start: int = end - 2
            middle: int = end - 1
            distance: int = (
                abs(ord_indexes[start] - ord_indexes[middle])
                + abs(ord_indexes[middle] - ord_indexes[end])
                + abs(ord_indexes[end] - ord_indexes[start])
            )
            out = min(out, distance)
            end += 1
    
    return out if limit != out else -1


# Time complexity: O(n * log n)
# n - length of the input array `nums`
# ---
# In the worst case, we're going to have all the same values in the `nums`.
# Traversing them => O(n)
# Sorting their indexes => O(n * log n).
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [1, 2, 1, 1, 3]
test_out: int = 6
assert test_out == minimum_distance(test)

test = [1, 1, 2, 3, 2, 1, 2]
test_out = 8
assert test_out == minimum_distance(test)

test = [1]
test_out = -1
assert test_out == minimum_distance(test)
