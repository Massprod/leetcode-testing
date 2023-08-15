# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.
# ---------------------
# 1 <= nums.length <= 10 ** 5
# 1 <= nums[i] <= 10 ** 9
# 1 <= k <= 10 ** 9
from random import randint


def max_operations(nums: list[int], k: int) -> int:
    # working_sol (98.97%, 26.29%) -> (526ms, 29.6mb)  time: O(n) | space: O(n)
    values: dict[int, int] = {}
    # Count and store every number occurrences.
    for _ in nums:
        if _ in values:
            values[_] += 1
            continue
        values[_] = 1
    # Count all pairs.
    count: int = 0
    # Cull half calc in loop.
    half: int | None = None
    if k % 2 == 0:
        half = k // 2
    for num in values:
        # Store result, to cull extra calcs.
        value: int = k - num
        # If counterpart is present, and both nums can be used.
        if value in values and values[value] > 0 and values[num] > 0:
            # If counterpart is half of k -> value == num.
            # Then we need to extra check this value to have
            #  at least 2 free options.
            if half and value == half:
                if values[value] < 2:
                    continue
                # Instead of checking one by one, just take every
                # possible pair at once.
                pairs: int = values[value] // 2
                # We use same value for pair, so we need
                # to remove x2 used.
                values[value] -= pairs * 2
                count += pairs
                continue
            # We can make pair only for minimum value.
            # n1 == 5, n2 == 6, only 5 pairs possible.
            pairs = min(values[value], values[num])
            values[value] -= pairs
            values[num] -= pairs
            count += pairs
    return count


# Time complexity: O(n) -> traversing whole input array to count all nums => O(n) ->
# n - len of input_array^^| -> extra traverse to count all pairs possible, worst case all uniques => O(n).
# Auxiliary space: O(n) -> storing all unique values from nums into a dictionary, worst case == all uniques => O(n).
# ---------------------
# Ok. Brain-lag day, first I was thinking that we need to check only 2 half's for pairs.
# Then tried to use values as pairs, and didn't even consider to check if second num is present...


test: list[int] = [1, 2, 3, 4]
test_k: int = 5
test_out: int = 2
assert test_out == max_operations(test, test_k)

test = [3, 1, 3, 4, 3]
test_k = 6
test_out = 1
assert test_out == max_operations(test, test_k)

test = [2, 2, 2, 3, 1, 1, 4, 1]
test_k = 4
test_out = 2
assert test_out == max_operations(test, test_k)

test = [2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2]
test_k = 3
test_out = 4
assert test_out == max_operations(test, test_k)

test = []
for _ in range(10 ** 4):
    test.append(randint(1, 10 ** 9))
# print(test)
# print(randint(1, 10 ** 9))
