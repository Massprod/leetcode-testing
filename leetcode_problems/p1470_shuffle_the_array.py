# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
# ----------------------
# 1 <= n <= 500
# nums.length == 2n
# 1 <= nums[i] <= 10 ** 3


def shuffle(nums: list[int], n: int) -> list[int]:
    # working_sol (99.34%, 10.98%) -> (41ms, 16.81mb)  time: O(m) | space: O(m)
    left: int = 0
    right: int = len(nums) // 2
    out: list[int] = []
    while right < len(nums):
        out.append(nums[left])
        out.append(nums[right])
        left += 1
        right += 1
    return out


# Time complexity: O(m) <- m - length of the input array `nums`.
# We're always using every index of the `nums`, once => O(m).
# ----------------------
# Auxiliary space: O(m)
# `out` <- always of the size `nums` => O(m).


test: list[int] = [2, 5, 1, 3, 4, 7]
test_n: int = 3
test_out: list[int] = [2, 3, 5, 4, 1, 7]
assert test_out == shuffle(test, test_n)

test = [1, 2, 3, 4, 4, 3, 2, 1]
test_n = 4
test_out = [1, 4, 2, 3, 3, 2, 4, 1]
assert test_out == shuffle(test, test_n)

test = [1, 1, 2, 2]
test_n = 2
test_out = [1, 2, 1, 2]
assert test_out == shuffle(test, test_n)
