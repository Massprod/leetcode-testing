# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# -------------------
# n == height.length
# 2 <= n <= 10 ** 5
# 0 <= height[i] <= 10 ** 4


def max_area(height: list[int]) -> int:
    # working_sol (81.73%, 50.56%) -> (602ms, 29.39mb)  time: O(n) | space: O(1)
    volume: int = 0
    # Left|Right coordinates to get bot_side of rectangle.
    # max_x - min_x == bottom == distance between columns.
    min_x: int = 0
    max_x: int = len(height) - 1
    while max_x > min_x:
        # Right|Left sides of rectangle.
        right_col_height: int = height[max_x]
        left_col_height: int = height[min_x]
        # Current volume of the rectangle.
        cur_volume = min(right_col_height, left_col_height) * (max_x - min_x)
        # We search maximum ->
        volume = max(cur_volume, volume)
        # -> so we always need to stay with the highest side.
        if right_col_height > left_col_height:
            min_x += 1
        elif left_col_height > right_col_height:
            max_x -= 1
        elif left_col_height == right_col_height:
            max_x -= 1
    return volume


# Time complexity: O(n) -> standard 2 pointers, every index of input_array will be used once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> nothing extra used, only 5 constant INTs none of them depends on input => O(1).


test: list[int] = [1, 8, 6, 2, 5, 4, 8, 3, 7]
test_out: int = 49
assert test_out == max_area(test)

test = [1, 1]
test_out = 1
assert test_out == max_area(test)

test = [0, 0, 2, 1]
test_out = 1
assert test_out == max_area(test)

test = [1, 2, 1]
test_out = 2
assert test_out == max_area(test)
