# You are given an array nums consisting of n prime integers.
# You need to construct an array ans of length n, such that, for each index i,
#  the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], i.e. ans[i] OR (ans[i] + 1) == nums[i].
# Additionally, you must minimize each value of ans[i] in the resulting array.
# If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1.
# ----------------------
# 1 <= nums.length <= 100
# 2 <= nums[i] <= 1000
# nums[i] is a prime number.


def min_bitwise_array(nums: list[int]) -> list[int]:
    # working_sol: (23.75%, 7.79%) -> (135ms, 17.2mb)  time: O(n) | space: O(n)
    out: list[int] = []
    # We can have duplicates in `nums` => cache it.
    checked: dict[int, int] = {}
    for num in nums:
        if num in checked:
            out.append(checked[num])
            continue
        check: int = 1
        while check < num:
            if (check | check + 1) == num:
                out.append(check)
                checked[num] = check
                break
            check += 1
        if num not in checked:
            out.append(-1)
            checked[num] = -1
    return out


# Time complexity: O(n) <- n - length of the input array `nums`.
# Always checking all the values in `nums` => O(n).
# ----------------------
# Auxiliary space: O(n)
# `checked` <- allocates space for each unique value in `nums` => O(n).


test: list[int] = [2, 3, 5, 7]
test_out: list[int] = [-1, 1, 4, 3]
assert test_out == min_bitwise_array(test)

test = [11, 13, 31]
test_out = [9, 12, 15]
assert test_out == min_bitwise_array(test)
