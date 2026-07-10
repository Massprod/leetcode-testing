# You are given an integer array nums.
# The digit range of an integer is defined as the difference between
#  its largest digit and smallest digit.
# For example, the digit range of 5724 is 7 - 2 = 5.
# Return the sum of all integers in nums whose digit range is equal
#  to the maximum digit range among all integers in the array.
# --- --- --- ---
# 1 <= nums.length <= 100
# 10 <= nums[i] <= 10 ** 5


def max_digit_range(nums: list[int]) -> int:
    # working_solution: (90.54%, 9.73%) -> (6ms, 19.42mb)  Time: O(n * k) Space: O(n)
    d_ranges: list[int] = []
    for num in nums:
        min_d: int = 10
        max_d: int = -1
        while num:
            digit: int = num % 10
            min_d = min(min_d, digit)
            max_d = max(max_d, digit)
            num //= 10
        num_range: int = max_d - min_d
        d_ranges.append(num_range)
    max_range: int = max(d_ranges)
    out: int = 0
    for index, range in enumerate(d_ranges):
        if max_range != range:
            continue
        out += nums[index]
    
    return out


# Time complexity: O(n * k)
# n - length of the input array `nums`
# k - average digits in the `nums` numbers
# --- --- --- ---
# Space complexity: O(n)


test: list[int] = [5724, 111, 350]
test_out: int = 6074
assert test_out == max_digit_range(test)

test = [90, 900]
test_out = 990
assert test_out == max_digit_range(test)
