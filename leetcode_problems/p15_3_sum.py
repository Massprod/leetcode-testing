# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
#  such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# ---------------
# 3 <= nums.length <= 3000
# -10 ** 5 <= nums[i] <= 10 ** 5


def three_sum(nums: list[int]) -> list[list[int]] | set[tuple[int, int, int]]:
    # working_sol (86.43%, 22.16%) -> (842ms, 20.9mb)  time: O(n) | space: O(n)
    # ! solution set must not contain duplicate triplets !
    # ! order of the triplets does not matter !
    # No matter the placement, we don't need same sums.
    sums: set[tuple[int, int, int]] = set()
    negative: dict[int, int] = {}
    positive: dict[int, int] = {}
    zeroes: int = 0
    # Count every option we can use for sums.
    for num in nums:
        if num > 0:
            if num in positive:
                positive[num] += 1
            else:
                positive[num] = 1
        elif num < 0:
            if num in negative:
                negative[num] += 1
            else:
                negative[num] = 1
        else:
            zeroes += 1
    # (neg, 0, pos)
    if zeroes:
        if zeroes > 2:
            sums.add((0, 0, 0))
        for pos in positive:
            if (pos * -1) in negative:
                sums.add(((pos * -1), 0, pos))
    # (neg, pos, pos)
    for value1 in positive:
        for value2 in positive:
            # Same value can be used, but only with different index.
            if value1 == value2 and positive[value1] < 2:
                continue
            value_sum: int = (value1 + value2) * -1
            if value_sum in negative:
                if value1 >= value2:
                    sums.add((value_sum, value2, value1))
                elif value1 < value2:
                    sums.add((value_sum, value1, value2))
    # (neg, neg, pos)
    for value1 in negative:
        for value2 in negative:
            if value1 == value2 and negative[value1] < 2:
                continue
            value_sum = (value1 + value2) * - 1
            if value_sum in positive:
                if value1 >= value2:
                    sums.add((value2, value1, value_sum))
                elif value1 < value2:
                    sums.add((value1, value2, value_sum))
    return sums


# Time complexity: O(n) -> traverse of whole input array to get all unique number and their occurrences => O(n) ->
# n - len of input array^^| -> traversing both dictionaries with negative and positive values, no matter the case ->
#                           -> assume worst case == everything is unique, then we will traverse dictionary for positive
#                           values twice, and negative once -> but no matter the case it's still same values from
#                           input array, and because all of them unique => O(n).
# Auxiliary space: O(n) -> worst case == every value is unique -> dictionaries will dominate sums,
#                          because they store every unique value => O(n).
# ---------------
# There's 3 options to get unique sum combinations:
# (neg, 0, pos)
# (neg, pos, pos)
# (neg, neg, pos)
# Just find everything we can use to build them.


test: list[int] = [-1, 0, 1, 2, -1, -4]
test_out: set[tuple[int, int, int]] = {(-1, -1, 2), (-1, 0, 1)}
assert test_out == three_sum(test)

test = [0, 1, 1]
test_out = set()
assert test_out == three_sum(test)

test = [0, 0, 0]
test_out = {(0, 0, 0)}
assert test_out == three_sum(test)
