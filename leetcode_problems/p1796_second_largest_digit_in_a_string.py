# Given an alphanumeric string s,
#  return the second largest numerical digit that appears in s, or -1 if it does not exist.
# An alphanumeric string is a string consisting of lowercase English letters and digits.
# ----------------------
# 1 <= s.length <= 500
# s consists of only lowercase English letters and digits.


def second_highest(s: str) -> int:
    # working_sol (82.40%, 96.13%) -> (35ms, 16.36mb)  time: O(s) | space: O(1)
    first: int = -1
    second: int = -1
    for char in s:
        if char.isdigit():
            cur_int: int = int(char)
            if cur_int > first:
                first, second = max(first, cur_int), first
            elif cur_int != first and cur_int > second:
                second = cur_int
    return second


# Time complexity: O(s)
# Always traversing whole input string `s`, once => O(s).
# ----------------------
# Auxiliary space: O(1).


test: str = "dfa12321afd"
test_out: int = 2
assert test_out == second_highest(test)

test = "abc1111"
test_out = -1
assert test_out == second_highest(test)
