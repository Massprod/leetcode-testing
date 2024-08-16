# A bit flip of a number x is choosing a bit in the binary representation of x
#  and flipping it from either 0 to 1 or 1 to 0.
# For example, for x = 7, the binary representation is 111
#  and we may choose any bit (including any leading zeros not shown) and flip it.
# We can flip the first bit from the right to get 110,
#  flip the second bit from the right to get 101,
#  flip the fifth bit from the right (a leading zero) to get 10111, etc.
# Given two integers start and goal,
#  return the minimum number of bit flips to convert start to goal.
# --------------------------
# 0 <= start, goal <= 10 ** 9


def min_bit_flips(start: int, goal: int) -> int:
    # working_sol (67.64%, 65.62%) -> (34ms, 16.42mb)  time: O(max(start, goal)) | space: O(1)
    out: int = 0
    while max(start, goal):
        s_lsb_bit: int = start & 1
        g_lsb_bit: int = goal & 1
        if s_lsb_bit != g_lsb_bit:
            out += 1
        start >>= 1
        goal >>= 1
    return out


# Time complexity: O(max(start, goal))
# Always depleting the maximum value of the input to 0 => O(max(start, goal)).
# --------------------------
# Auxiliary space: O(1)
# Only 3 constant INTs used, none of them depends on input => O(1).


test_start: int = 10
test_goal: int = 7
test_out: int = 3
assert test_out == min_bit_flips(test_start, test_goal)

test_start = 3
test_goal = 4
test_out = 3
assert test_out == min_bit_flips(test_start, test_goal)
