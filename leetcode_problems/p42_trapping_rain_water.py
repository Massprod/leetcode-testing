# Given n non-negative integers representing an elevation map where the width of each bar is 1,
#  compute how much water it can trap after raining.
# ---------------------
# n == height.length
# 1 <= n <= 2 * 10 ** 4
# 0 <= height[i] <= 10 ** 5


def rain_water_trap(height: list[int]) -> int:
    # working_sol (82.59%, 99.38%) -> (107ms, 17.99mb)  time: O(n) | space: O(1)
    # 2 walls(pointers) on left and right sides.
    # Initially placed on [0], and [-1] indexes.
    volume: int = 0
    left: int = 0
    right: int = len(height) - 1
    # Initial height == 0.
    left_max: int = 0
    right_max: int = 0
    while left < right:
        # Water will be trapped only to the height of lower bound.
        # Otherwise, its overflow.
        if height[left] < height[right]:
            if height[left] > left_max:
                left_max = height[left]
            else:
                volume += left_max - height[left]
            left += 1
        else:
            if height[right] > right_max:
                right_max = height[right]
            else:
                volume += right_max - height[right]
            right -= 1
    return volume


# Time complexity: O(n) -> traverse of whole input array indexes => O(n).
# n - len of input array^^|
# Auxiliary space: O(1) -> only 5 extra constant INTs used, none of them depends on input => O(1).
# ---------------------
# We use 2 pointers to make correct steps from left and right sides. Because we always need to use LOWEST wall.
# Otherwise, water will overflow.
# Always maintain the highest walls on left and right sides.
# Because, we're making steps from left -> right and right -> left.
# And calc water assuming that there's wall on left == left_max and something higher on right side:
#                       (height[left] < height[right])
# But left_max is always updated only when its^^ satisfied, so it's equal or lower than height[right].
# Same goes for the right side.


test: list[int] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
test_out: int = 6
assert test_out == rain_water_trap(test)

test = [4, 2, 0, 3, 2, 5]
test_out = 9
assert test_out == rain_water_trap(test)
