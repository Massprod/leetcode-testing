# Given an integer array hours representing times in hours,
#  return an integer denoting the number of pairs i, j
#  where i < j and hours[i] + hours[j] forms a complete day.
# A complete day is defined as a time duration that is an exact multiple of 24 hours.
# For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.
# ----------------------
# 1 <= hours.length <= 100
# 1 <= hours[i] <= 10 ** 9


def count_complete_day_pairs(hours: list[int]) -> int:
    # working_sol (82.20%, 47.97%) -> (3ms, 16.65mb)  time: O(n) | space: O(1)
    out: int = 0
    fixed_hours: list[int] = [0 for _ in range(24)]
    for value in hours:
        fixed_hours[value % 24] += 1
    # We can only combine (1 - 11) with (12 - 23)
    for hour in range(1, 12):
        out += fixed_hours[hour] * fixed_hours[24 - hour]
    # Two edge cases:
    #  24 hours can be combined with itself == 48 <- divide to get pairs
    if 1 < fixed_hours[0]:
        out += fixed_hours[0] * (fixed_hours[0] - 1) // 2
    #  12 hours can be combined with itself == 24 <- divide to get pairs
    if 1 < fixed_hours[12]:
        out += fixed_hours[12] * (fixed_hours[12] - 1) // 2
    return out


# Time complexity: O(n) <- n - length of the input arrays `hours`.
# Always traversing whole input array `hours`, once => O(n).
# ----------------------
# Auxiliary space: O(1)
# `fixed_hours` <- allocates space for 24 hours => O(1).


test: list[int] = [12, 12, 30, 24, 24]
test_out: int = 2
assert test_out == count_complete_day_pairs(test)

test = [72, 48, 24, 3]
test_out = 3
assert test_out == count_complete_day_pairs(test)
