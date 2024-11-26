# You are given an integer array nums.
# You replace each element in nums with the sum of its digits.
# Return the minimum element in nums after all replacements.
# -----------------
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 10 ** 4


def min_element(nums: list[int]) -> int:
    # working_sol (88.10%, 24.59%) -> (3ms, 16.78mb)  time: O(n) | space: O(1)
    out: int = 10 ** 4

    def sum_digits(value: int) -> int:
        _sum: int = 0
        while value:
            digit: int = value % 10
            _sum += digit
            value //= 10
        return _sum

    for num in nums:
        out = min(sum_digits(num), out)
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always traversing and checking all values in `nums` => O(n).
# -----------------
# Auxiliary space: O(1)


test: list[int] = [10, 12, 13, 14]
test_out: int = 1
assert test_out == min_element(test)

test = [1, 2, 3, 4]
test_out = 1
assert test_out == min_element(test)

test = [999, 19, 199]
test_out = 10
assert test_out == min_element(test)
