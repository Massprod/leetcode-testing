# An ant is on a boundary. It sometimes goes left and sometimes right.
# You are given an array of non-zero integers nums.
# The ant starts reading nums from the first element of it to its end.
# At each step, it moves according to the value of the current element:
#  - If nums[i] < 0, it moves left by -nums[i] units.
#  - If nums[i] > 0, it moves right by nums[i] units.
# Return the number of times the ant returns to the boundary.
# Notes:
#  - There is an infinite space on both sides of the boundary.
#  - We check whether the ant is on the boundary only after it has moved |nums[i]| units.
#    In other words, if the ant crosses the boundary during its movement, it does not count.
# -----------------------------
# 1 <= nums.length <= 100
# -10 <= nums[i] <= 10
# nums[i] != 0


def return_to_boundary_count(nums: list[int]) -> int:
    # working_sol (97.69%, 66.53%) -> (32ms, 16.48mb)  time: O(n) | space: O(1)
    out: int = 0
    cur_place: int = 0
    for num in nums:
        cur_place += num
        if 0 == cur_place:
            out += 1
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing whole input array `nums`, once => O(n).
# -----------------------------
# Auxiliary space: O(1).


test: list[int] = [2, 3, -5]
test_out: int = 1
assert test_out == return_to_boundary_count(test)

test = [3, 2, -3, -4]
test_out = 0
assert test_out == return_to_boundary_count(test)
