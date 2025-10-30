# You are given an integer array target.
# You have an integer array initial of the same size
#  as target with all elements initially zeros.
# In one operation you can choose any subarray from initial
#  and increment each value by one.
# Return the minimum number of operations to form a target array from initial.
# The test cases are generated so that the answer fits in a 32-bit integer.
# --- --- --- ---
# 1 <= target.length <= 10 ** 5
# 1 <= target[i] <= 10 ** 5


def min_number_operations(target: list[int]) -> int:
    # working_solution: (29.57%, 76.07%) -> (78ms, 26.64mb)  Time: O(n) Space: O(1)
    # We need to make it equal at least to the first value.
    out: int = target[0]
    for index in range(1, len(target)):
        out += max(target[index] - target[index - 1], 0)

    return out


# Time complexity: O(n) <- n - length of the input array `target`
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, 2, 3, 2, 1]
test_out: int = 3
assert test_out == min_number_operations(test)

test = [3, 1, 1, 2]
test_out = 4
assert test_out == min_number_operations(test)

test = [3, 1, 5, 4, 2]
test_out = 7
assert test_out == min_number_operations(test)
