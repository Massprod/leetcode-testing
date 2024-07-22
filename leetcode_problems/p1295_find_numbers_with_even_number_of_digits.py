# Given an array nums of integers, return how many of them contain an even number of digits.
# ----------------------
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10 ** 5


def find_number(nums: list[int]) -> int:
    # working_sol (52.76%, 97.16%) -> (52ms, 16.45mb)  time: O(n) | space: O(1)
    out: int = 0
    for num in nums:
        count: int = 0
        while num:
            num //= 10
            count += 1
        if not count % 2:
            out += 1
    return out


# Time complexity: O(n) <- n - length of the input array `nums`, k - average number of digits in values of `nums`
# We're always traversing whole input array `nums`, once => O(n).
# And for each `num` in it, we exhaust it to 0 => O(n * k).
# ----------------------
# Auxiliary space: O(1)
# Only 2 constant INT's used, none of them depends on input => O(1).\


test: list[int] = [12, 345, 2, 6, 7896]
test_out: int = 2
assert test_out == find_number(test)

test = [555, 901, 482, 1771]
test_out = 1
assert test_out == find_number(test)
