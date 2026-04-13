# You are given an integer array nums and an integer digit.
# Return the total number of times digit appears in the decimal representation
#  of all elements in nums.
# --- --- --- ---
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 10 ** 6​​​​​​​
# 0 <= digit <= 9


def count_digit_occurrences(nums: list[int], digit: int) -> int:
    # working_solution: (100%, 100%) -> (29ms, 19.23mb)  Time: O(n) Space: O(1)
    out: int = 0
    for num in nums:
        while num:
            n_digit = num % 10
            if digit == n_digit:
                out += 1
            num //= 10

    return out


# Time complexity: O(n)
# --- --- --- ---
# Space complexity: O(1)


test: list[int] = [12, 54, 32, 22]
test_digit: int = 2
test_out: int = 4
assert test_out == count_digit_occurrences(test, test_digit)

test = [1, 34, 7]
test_digit = 9
test_out = 0
assert test_out == count_digit_occurrences(test, test_digit)
