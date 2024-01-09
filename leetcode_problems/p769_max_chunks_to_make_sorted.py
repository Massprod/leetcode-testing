# You are given an integer array arr of length n that represents a permutation
#  of the integers in the range [0, n - 1].
# We split arr into some number of chunks (i.e., partitions),
#  and individually sort each chunk.
# After concatenating them, the result should equal the sorted array.
# Return the largest number of chunks we can make to sort the array.
# -----------------------
# n == arr.length
# 1 <= n <= 10
# 0 <= arr[i] < n
# All the elements of arr are unique.
from random import shuffle


def max_chunks_to_sorted(arr: list[int]) -> int:
    # working_sol (99.16%, 22.78%) -> (26ms, 17.21mb)  time: O(n) | space: O(1)
    out: int = 0
    highest: int = -1
    for index, value in enumerate(arr):
        highest = max(highest, value)
        if index == highest:
            out += 1
    return out


# Time complexity: O(n) <- n - length of input array `arr`.
# Single traverse of the whole input array `arr` => O(n).
# -----------------------
# Auxiliary space: O(1).
# -----------------------
# First we can't CHUNK randomly, we only can do this in left -> right order.
# Otherwise, why we can't slice [4, 3, 2, 1, 0] -> [4], [3], [2], [1], [0] in the first test_case.
# So, we can only slice and concatenate only left -> right chunks,
#  and we need to include everything from HIGHEST to current LOWEST.
# -----------------------
# Or, instead of checking all correct values we need to have in chunk.
# We can just check INDEXES. Because what we essentially care is that we should have
#  index == maximum value on the left side of it + itself.
# Like [4, 3, 2, 1, 0] -> because we're given 0 -> n - 1 all values in array.
# We can guarantee that there's 4 -> 0 values somewhere, and we didn't meet anything HIGHER than 4
#  by the time we reach index == 4, then we only have values lower than 4 AND there's 4 of them.
# Or [1, 0, 2, 3, 4] -> index == 2, so we have 2 values behind it, and none of them HIGHER than [2].
# Exactly what we need. So, there's no reason to bother with sets and sorting.


test: list[int] = [4, 3, 2, 1, 0]
test_out: int = 1
assert test_out == max_chunks_to_sorted(test)

test = [1, 0, 2, 3, 4]
test_out = 4
assert test_out == max_chunks_to_sorted(test)

test = [_ for _ in range(0, 10)]
shuffle(test)
print(test)
