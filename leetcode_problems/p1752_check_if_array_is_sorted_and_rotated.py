# Given an array nums, return true if the array was originally sorted in non-decreasing order,
#   then rotated some number of positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same length such that
#   A[i] == B[(i+x) % A.length], where % is the modulo operation.
# ---------------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100


def check(nums: list[int]) -> bool:
    # working_sol (97.71%, 92.39%) -> (35ms, 16.16mb)  time: O(n) | space: O(1)
    # 1val -> always True.
    if len(nums) == 1:
        return True
    # Min value we can have in right_part after pivot_point.
    min_left: int = nums[0]
    # We don't know if it's even Pivoted at start.
    pivoted: bool = False
    for x in range(1, len(nums)):
        if pivoted:
            # Ascending order and every value == lower|equal to min_left.
            if nums[x - 1] <= nums[x] <= min_left:
                continue
            # Otherwise it's not ascending, and there's something higher.
            # Which means we can't pivot array correctly,
            # cuz values higher than breakpoint can't be in a right_part.
            return False
        # Standard ascending order.
        elif nums[x] >= nums[x - 1]:
            continue
        # Breakpoint(pivot_point), everything after it
        # should be lower|equal = min_left and in ascending order.
        elif nums[x] < nums[x - 1]:
            if nums[x] > min_left:
                return False
            pivoted = True
    # Standard ascending array or correctly pivoted.
    return True


# Time complexity: O(n) -> the worst case it's correct array, pivoted or not, still traversing array, once => O(n).
# n - len of input_array^^|
# Auxiliary space: O(1) -> only 2 constants used => O(1).
# ---------------------
# No idea why would I need to use this formula -> A[i] == B[(i+x) % A.length].
# Just find breakpoint and check every value in it to be lower or equal(we can have duplicates) than nums[0],
# and if there's no breakpoint then it's just ascending array.


test: list[int] = [3, 4, 5, 1, 2]
test_out: bool = True
assert test_out == check(test)

test = [2, 1, 3, 4]
test_out = False
assert test_out == check(test)

test = [1, 2, 3]
test_out = True
assert test_out == check(test)

test = [2, 2, 2, 2, 2]
test_out = True
assert test_out == check(test)

# test -> Failed -> I was considering breaking on values == to min_left, and we can have duplicates.
#                   So it's just ! nums[x - 1] <= nums[x] <= min_left ! not < min_left.
test = [1, 2, 1, 1]
test_out = True
assert test_out == check(test)
