# Given an array of integers nums, sort the array in increasing order
#  based on the frequency of the values.
# If multiple values have the same frequency, sort them in decreasing order.
# Return the sorted array.
# --------------------------
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100
from random import randint
from collections import Counter, defaultdict


def frequency_sort(nums: list[int]) -> list[int]:
    # working_sol (98.62%, 37.68%) -> (36ms, 16.50mb)  time: O(n * log n) | space: O(n)
    # {value: frequency}
    frequencies: dict[int, int] = Counter(nums)
    # Equal frequency => sort in descending, so we need to know these values.
    # {frequency: [values with that frequency]}
    equal_freq: dict[int, list[int]] = defaultdict(list)
    for val, freq in frequencies.items():
        equal_freq[freq] += [val] * freq
    # [correct order of values with different frequencies]
    order: list[int] = sorted(equal_freq.keys())
    out: list[int] = []
    # All that's left is to reverse the same frequency values.
    for seq in order:
        out += sorted(equal_freq[seq], reverse=True)
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# First traversing `nums`, once - to get all the unique values and their frequencies => O(n).
# In the worst case, all of them are unique, so we're traversing them again => O(2 * n).
# Sorting all the keys, which is all the unique values from `nums` => O(n * log n).
# For each unique frequency and values that have that frequency, we're sorting these values.
# And in our case, when everything is unique, we're going to have all values with frequency == 1,
#  means we're sorting `nums` itself => O(2 * n + 2 * (n * log n)).
# --------------------------
# Auxiliary space: O(n)
# In case with all values from `nums` being unique.
# `frequencies` <- will store all the values from `nums` => O(n).
# `equal_freq` <- can be of size `n` when there's only 1 value in `nums` => O(2 * n).
# `order` <- same size of an `equal_freq` => O(3 * n).
# `out` <- always a cpy of `nums` but with a correct ordering of the elements => O(4 * n)


test: list[int] = [1, 1, 2, 2, 2, 3]
test_out: list[int] = [3, 1, 1, 2, 2, 2]
assert test_out == frequency_sort(test)

test = [2, 3, 1, 3, 2]
test_out = [1, 3, 3, 2, 2]
assert test_out == frequency_sort(test)

test = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
test_out = [5, -1, 4, 4, -6, -6, 1, 1, 1]
assert test_out == frequency_sort(test)

test = [randint(-100, 100) for _ in range(100)]
print(test)
