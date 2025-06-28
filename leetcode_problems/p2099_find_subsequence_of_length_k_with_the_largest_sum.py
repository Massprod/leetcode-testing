# You are given an integer array nums and an integer k.
# You want to find a subsequence of nums of length k that has the largest sum.
# Return any such subsequence as an integer array of length k.
# A subsequence is an array that can be derived from another array by deleting some
#  or no elements without changing the order of the remaining elements.
# -------------------------
# 1 <= nums.length <= 1000
# -10  5 <= nums[i] <= 10 ** 5
# 1 <= k <= nums.length


def max_subsequence(nums: list[int], k: int) -> list[int]:
    # working_sol (83.73%, 78.57%) -> (3ms, 17.96mb)  time: O(n * log n) | space: O(n)
    # The simplest way is to sort with indexes =>
    # => take `k` of the highest and sort them on indexes.
    # [(index, value)]
    index_sorted: list[tuple[int, int]] = sorted(
        enumerate(nums), key=lambda x: x[1], reverse=True
    )
    highest_slice: list[tuple[int, int]] = sorted(
        index_sorted[:k], key=lambda x: x[0]
    )

    return [pair[1] for pair in highest_slice]


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# In the worst case, we're going to have `n` == `k`.
# We're always sorting the input array `nums`, twice => O(n * log n).
# -------------------------
# Auxiliary space: O(n)
# `index_sorted`, `highest_slice` <- allocates space for each value from `nums` => O(n).


test: list[int] = [2, 1, 3, 3]
test_k: int = 2
test_out: list[int] = [3, 3]
assert test_out == max_subsequence(test, test_k)

test = [-1, -2, 3, 4]
test_k = 3
test_out = [-1, 3, 4]
assert test_out == max_subsequence(test, test_k)

test = [3 , 4, 3 ,3]
test_k = 2
test_out = [3, 4]
assert test_out == max_subsequence(test, test_k)
