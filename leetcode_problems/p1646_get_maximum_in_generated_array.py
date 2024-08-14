# You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:
#  - nums[0] = 0
#  - nums[1] = 1
#  - nums[2 * i] = nums[i] when 2 <= 2 * i <= n
#  - nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
# Return the maximum integer in the array nums.
# -------------------
# 0 <= n <= 100


def get_maximum_generated(n: int) -> int:
    # working_sol (77.15, 33.42%) -> (32ms, 16.51mb)  time: O(n) | space: O(n)
    if 1 == n:
        return 1
    out: int = 0
    array: list[int] = [0, 1] + [0 for _ in range(n - 1)]
    for index in range(1, n + 1):
        mult: int = 2 * index
        if 2 <= mult <= n:
            array[mult] = array[index]
            out = max(out, array[mult])
        if 2 <= mult + 1 <= n:
            array[mult + 1] = array[index] + array[index + 1]
            out = max(out, array[mult + 1])
    return out


# Time complexity: O(n)
# Creating `array` of size `n + 2` => O(n + 2).
# Extra traversing indexes to get correct values => O(n + 2 + (n - 1)).
# -------------------
# Auxiliary space: O(n)
# `array` <- will be of size `n + 2` => O(n + 2).


test: int = 7
test_out: int = 3
assert test_out == get_maximum_generated(test)

test = 2
test_out = 1
assert test_out == get_maximum_generated(test)

test = 3
test_out = 2
assert test_out == get_maximum_generated(test)
