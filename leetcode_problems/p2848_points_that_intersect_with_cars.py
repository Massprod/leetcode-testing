# You are given a 0-indexed 2D integer array nums representing
#  the coordinates of the cars parking on a number line.
# For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car
#  and endi is the ending point of the ith car.
# Return the number of integer points on the line that are covered with any part of a car.
# --------------------------
# 1 <= nums.length <= 100
# nums[i].length == 2
# 1 <= starti <= endi <= 100


def number_of_points(nums: list[list[int]]) -> int:
    # working_sol (75.95%, 53.16%) -> (71ms, 16.58mb)  time: O(n * log n) | space: O(n)
    out: int = 0
    nums.sort(
        key=lambda x: x[0]
    )
    cur_min = nums[0][0]
    cur_max = nums[0][1]
    # Extra 100% breakpoint if we're going to have all ranges in 1.
    nums.append([nums[-1][1] + 100, nums[-1][1] + 100])
    for index in range(len(nums)):
        if 0 < index and cur_max < nums[index][0]:
            out += 1 + (cur_max - cur_min)
            cur_min = nums[index][0]
            cur_max = nums[index][1]
            continue
        cur_min: int = min(cur_min, nums[index][0])
        cur_max: int = max(cur_max, nums[index][1])
    return out


# Time complexity: O(n * log n) <- n - length of the input array `nums`.
# Always sorting original input array `nums` => O(n * log n).
# Extra traversing every index of it, once => O(n + n * log n).
# --------------------------
# Auxiliary space: O(n).
# `sort` <- takes O(n).


test: list[list[int]] = [[3, 6], [1, 5], [4, 7]]
test_out: int = 7
assert test_out == number_of_points(test)

test = [[1, 3], [5, 8]]
test_out = 7
assert test_out == number_of_points(test)

test = [[2, 3], [3, 9], [5, 7], [4, 10], [9, 10]]
test_out = 9
assert test_out == number_of_points(test)

test = [[1, 9], [2, 10], [6, 7], [8, 9], [5, 8], [1, 3]]
test_out = 10
assert test_out == number_of_points(test)

test = [[6, 10], [6, 9], [1, 2], [6, 9], [5, 7], [6, 9], [1, 3], [5, 7], [5, 5]]
test_out = 9
assert test_out == number_of_points(test)
