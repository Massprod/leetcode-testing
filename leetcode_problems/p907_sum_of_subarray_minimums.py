# Given an array of integers arr, find the sum of min(b),
#  where b ranges over every (contiguous) subarray of arr.
# Since the answer may be large, return the answer modulo 10 ** 9 + 7.
# ------------------
# 1 <= arr.length <= 3 * 10 ** 4
# 1 <= arr[i] <= 3 * 10 ** 4
from random import randint


def sum_subarray_mins(arr: list[int]) -> int:
    # working_sol (95.91%, 62.53%) -> (318ms, 21.41mb)  time: O(n) | space: O(n)
    # [sum of minimals of every (contiguous) subarray ending on this index]
    min_sums: list[int] = [0 for _ in arr]
    # [indexes of smaller values we have, before current index]
    stack: list[int] = []
    out: int = 0
    for index, value in enumerate(arr):
        while stack and arr[stack[-1]] >= value:
            stack.pop()
        # If we have something smaller before:
        # arr = [3, 1, 2, 4], index = 2, value = 2.
        # We can slice it like: [3, 1, 2], [1, 2] == min_sums[min_ind],
        #  and this 2 options are continuation of previously stored min_sums[1]: [3, 1], [1].
        # And extra to this we can have: [2] == value * (index - min_ind).
        # So, we include all previous contiguous subarrays with smaller value
        #  + subarrays we can build from this smaller value (not included) to our current value (index - min_ind).
        if stack:
            min_ind: int = stack[-1]
            min_sums[index] = min_sums[min_ind] + value * (index - min_ind)
        # If our current value is smallest (so far) then we need to include it,
        #  in every possible contiguous subarray we can build from 0 -> index (inclusive).
        else:
            min_sums[index] = value * (index + 1)
        out += min_sums[index]
        stack.append(index)
    return out % (10 ** 9 + 7)


# Time complexity: O(n) <- n - length of input array `arr`.
# Creating array to store sums of minimals for every index `min_sums` => O(n).
# Traversing original array `arr`, and in the worst case: we will have minimum value at the last index.
# So, we will use `n` elements + (`n` - 1) elements in `stack` => O(2n).
# Extra enumerate(), but I guess we can ignore it. Using because it's `recommended` to use.
# But, we can just use indexes, without extra creating enumerate() object.
# Because it's fast, but still takes time and space every (id(enumerate(arr)) is unique == space allocated.
# Still linear tho.
# ------------------
# Auxiliary space: O(n).
# Creating array to store sums of minimals for every index `min_sums` => O(n).
# In the worst case if every value is lower than previous, we will have `stack` with size of `n` => O(n).
# Extra O(n) for enumerate.


test: list[int] = [3, 1, 2, 4]
test_out: int = 17
assert test_out == sum_subarray_mins(test)

test = [11, 81, 94, 43, 3]
test_out = 444
assert test_out == sum_subarray_mins(test)

test = [randint(1, 3 * 10 ** 4) for _ in range(3 * 10 ** 4)]
print(test)
