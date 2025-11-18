# You are given an integer array nums.
# Choose three elements a, b, and c from nums at distinct indices such that
#  the value of the expression a + b - c is maximized.
# Return an integer denoting the maximum possible value of this expression.
# --- --- --- ---
# 3 <= nums.length <= 100
# -100 <= nums[i] <= 100


def maximize_expression_of_three(nums: list[int]) -> int:
    # working_solution: (42.47%, 89.84%) -> (1ms, 17.70mb)  Time: O(n) Space: O(1)
    max_val: int = -100
    second_to_max: int = -100
    minimum_val: int = 100
    for num in nums:
        if num > max_val:
            max_val, second_to_max, minimum_val = num, max_val, min(minimum_val, num)
        elif num >= second_to_max:
            second_to_max, minimum_val = num, min(minimum_val, num)
        else:
            minimum_val = min(minimum_val, num)

    out: int = max_val + second_to_max - minimum_val
    return out


# Time complexity: O(n)
# n - length of the ipnut array `nums`.
# Always traversing the whole input array `nums`, once => O(n).
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [1, 4, 2, 5]
test_out: int = 8
assert test_out == maximize_expression_of_three(test)

test = [-2, 0, 5, -2, 4]
test_out = 11
assert test_out == maximize_expression_of_three(test)
