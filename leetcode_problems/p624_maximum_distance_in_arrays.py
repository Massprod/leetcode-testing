# You are given m arrays, where each array is sorted in ascending order.
# You can pick up two integers from two different arrays (each array picks one)
#  and calculate the distance.
# We define the distance between two integers a and b to be their absolute difference |a - b|.
# Return the maximum distance.
# -----------------------
# m == arrays.length
# 2 <= m <= 10 ** 5
# 1 <= arrays[i].length <= 500
# -10 ** 4 <= arrays[i][j] <= 10 ** 4
# arrays[i] is sorted in ascending order.
# There will be at most 10 ** 5 integers in all the arrays.
from random import randint


def max_distance(arrays: list[list[int]]) -> int:
    # working_sol (32.18%, 63.79%) -> (1372ms, 42.43mb)  time: O(n) | space: O(1)
    # We need maximum distance of all.
    # The best option is to take minimum value from all the arrays.
    # With maximum value from all the arrays, and find their distance.
    # The Only concern is when the minimum and maximum values
    #  are going to be in the same array.
    # For this case, we're just calculating distance first.
    cur_min: int = arrays[0][0]
    cur_max: int = arrays[0][-1]
    out: int = 0
    for index in range(1, len(arrays)):
        out = max(out,
                  max(
                      abs(cur_min - arrays[index][-1]),
                      abs(cur_max - arrays[index][0]))
                  )
        cur_min = min(arrays[index][0], cur_min)
        cur_max = max(arrays[index][-1], cur_max)
    return out


# Time complexity: O(n) <- n - length of the input array `arrays`.
# Only using every `0` `-1` indexes of every array in `arrays`, once => O(n).
# -----------------------
# Auxiliary space: O(1)
# Only 3 constant INTs used, none of them depends on input => O(1).


test: list[list[int]] = [[1, 2, 3], [4, 5], [1, 2, 3]]
test_out: int = 4
assert test_out == max_distance(test)

test = [[1], [1]]
test_out = 0
assert test_out == max_distance(test)

test = [sorted([randint(-10 ** 4, 10 ** 4) for _ in range(500)]) for _ in range(100)]
print(test)
